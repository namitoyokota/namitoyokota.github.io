import requests
from requests.auth import HTTPBasicAuth
import json
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

email = os.getenv("EMAIL")
token = os.getenv("CONFLUENCE_TOKEN")
organization = os.getenv("ORGANIZATION")
username = os.getenv("CONFLUENCE_USERNAME")

if not all([email, token, organization, username]):
    raise ValueError("One or more required environment variables are missing")

confluence_url = f'https://{organization}.atlassian.net/wiki/rest/api/content'

auth = HTTPBasicAuth(email, token)
params = {
    'expand': 'body.storage',
    'type': 'page',
    'limit': 100,
}

def get_documents():
    all_documents = []
    start = 0

    while True:
        params['start'] = start
        response = requests.get(confluence_url, auth=auth, params=params)

        if response.status_code == 200:
            data = response.json()
            all_documents.extend(data['results'])

            if 'next' in data['_links']:
                start += 100
            else:
                break
        else:
            print(f"Error fetching data: {response.status_code} - {response.text}")
            break

    return all_documents

def check_if_created_and_get_date(document_id):
    history_url = f"{confluence_url}/{document_id}/history"
    response = requests.get(history_url, auth=auth)

    if response.status_code == 200:
        history = response.json()
        created_date = datetime.strptime(history["createdDate"], "%Y-%m-%dT%H:%M:%S.%f%z")
        if "Namito" in history["createdBy"]["displayName"]:
            return True, created_date

    return False, None

def display_documents(documents):
    created_count = 0
    stats_by_year = {}

    for doc in documents:
        title = doc['title']
        url = f"https://{organization}.atlassian.net/wiki{doc['_links']['webui']}"

        created, created_date = check_if_created_and_get_date(doc['id'])
        if created:
            created_count += 1
            year = created_date.year
            if year not in stats_by_year:
                stats_by_year[year] = {
                    "documents_created": 0,
                }
            stats_by_year[year]["documents_created"] += 1

        print(f"Title: {title}")
        print(f"URL: {url}")
        print(f"Created by me: {'Yes' if created else 'No'}")
        print("="*50)

    print(f"Total documents created: {created_count}")

    return created_count, stats_by_year

def save_results(created_count, stats_by_year):
    results = {
        "documents_created": created_count,
    }
    output_dir = os.path.join(os.path.dirname(__file__), "confluence")
    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "total.json"), "w") as f:
        json.dump(results, f, indent=4)

    for year, stats in stats_by_year.items():
        with open(os.path.join(output_dir, f"{year}.json"), "w") as f:
            json.dump(stats, f, indent=4)

if __name__ == "__main__":
    documents = get_documents()
    created_count, stats_by_year = display_documents(documents)
    save_results(created_count, stats_by_year)
