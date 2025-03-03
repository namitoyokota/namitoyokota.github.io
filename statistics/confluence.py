import aiohttp
import asyncio
import json
import os
from datetime import datetime
from dotenv import load_dotenv
import base64

load_dotenv()

email = os.getenv("EMAIL")
token = os.getenv("CONFLUENCE_TOKEN")
organization = os.getenv("ORGANIZATION")
username = os.getenv("CONFLUENCE_USERNAME")

if not all([email, token, organization, username]):
    raise ValueError("One or more required environment variables are missing")

confluence_url = f'https://{organization}.atlassian.net/wiki/rest/api/content'
auth_header = {"Authorization": f"Basic {base64.b64encode(f'{email}:{token}'.encode()).decode()}"}
params = {
    'expand': 'body.storage',
    'type': 'page',
    'limit': 100,
}

async def fetch_documents(session, url):
    async with session.get(url, headers=auth_header, params=params) as response:
        return await response.json()

async def fetch_document(session, url):
    async with session.get(url, headers=auth_header) as response:
        return await response.json()

async def get_documents(session):
    all_documents = []
    start = 0

    while True:
        params['start'] = start
        response = await fetch_documents(session, confluence_url)

        if response:
            all_documents.extend(response['results'])

            if 'next' in response['_links']:
                start += 100
                print(f"Fetching documents {start} to {start+100}")
            else:
                break
        else:
            print(f"Error fetching data: {response}")
            break

    return all_documents

async def check_if_created_and_get_date(session, doc_id):
    history_url = f"{confluence_url}/{doc_id}/history"
    response = await fetch_document(session, history_url)

    created_date = None
    created = False
    edited = False

    if response:
        created_date = datetime.strptime(response["createdDate"], "%Y-%m-%dT%H:%M:%S.%f%z")
        created = "Namito" in response["createdBy"]["displayName"]
        edited = "Namito" in response["lastUpdated"]["by"]["displayName"]

    return created, edited, created_date

async def process_documents(session, documents):
    created_count = 0
    edited_count = 0
    stats_by_year = {}

    tasks = []
    for doc in documents:
        tasks.append(check_if_created_and_get_date(session, doc['id']))

    results = await asyncio.gather(*tasks)

    for doc, (created, edited, created_date) in zip(documents, results):
        if created or edited:
            year = created_date.year
            if year not in stats_by_year:
                stats_by_year[year] = {
                    "documents_created": 0,
                    "documents_edited": 0,
                }

            if created:
                created_count += 1
                stats_by_year[year]["documents_created"] += 1

            if edited:
                edited_count += 1
                stats_by_year[year]["documents_edited"] += 1

    print(f"Total documents created: {created_count}")
    print(f"Total documents edited: {edited_count}")

    return created_count, edited_count, stats_by_year

def save_results(created_count, edited_count, stats_by_year):
    results = {
        "documents_created": created_count,
        "documents_edited": edited_count,
    }
    output_dir = os.path.join(os.path.dirname(__file__), "confluence")
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "total.json"), "w") as f:
        json.dump(results, f, indent=4)

    for year, stats in stats_by_year.items():
        with open(os.path.join(output_dir, f"{year}.json"), "w") as f:
            json.dump(stats, f, indent=4)

async def main():
    async with aiohttp.ClientSession() as session:
        print('Getting documents...')
        documents = await get_documents(session)
        print(f"{len(documents)} documents found.")
        print('Parsing documents...')
        created_count, edited_count, stats_by_year = await process_documents(session, documents)
        save_results(created_count, edited_count, stats_by_year)

if __name__ == "__main__":
    asyncio.run(main())
