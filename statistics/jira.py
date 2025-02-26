# This script retrieves and outputs statistics on Jira stories that I've completed.

import base64
import json
from datetime import datetime
import aiohttp
import asyncio
import time
import os
from dotenv import load_dotenv
from tqdm import tqdm
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Load environment variables from .env file
load_dotenv()

# Required
email = os.getenv("EMAIL")
token = os.getenv("JIRA_TOKEN")
organization = os.getenv("JIRA_ORGANIZATION")
user_id = os.getenv("JIRA_USER_ID")

# Check if all required environment variables are set
if not all([email, token, organization, user_id]):
    raise ValueError(Fore.RED + "One or more required environment variables are missing")

# Settings
take = 100

# Constants
base64_auth_info = base64.b64encode(f"{email}:{token}".encode("ascii")).decode("ascii")
headers = {"Authorization": f"Basic {base64_auth_info}"}

async def fetch(session, url):
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def get_total_stories(session, organization, user_id):
    jql = f"assignee={user_id} AND status=Released AND (type=Story OR type=Bug)"
    endpoint = f"https://{organization}.atlassian.net/rest/api/3/search?jql={jql}&maxResults=0"
    response = await fetch(session, endpoint)
    return response.get("total", 0)

async def get_next_stories(session, organization, user_id, start_at):
    jql = f"assignee={user_id} AND status=Released AND (type=Story OR type=Bug)"
    endpoint = f"https://{organization}.atlassian.net/rest/api/3/search?jql={jql}&startAt={start_at}&maxResults={take}"
    response = await fetch(session, endpoint)
    return response.get("issues", [])

async def get_issue_history(session, organization, issue_id):
    endpoint = f"https://{organization}.atlassian.net/rest/api/3/issue/{issue_id}/changelog"
    response = await fetch(session, endpoint)
    return response.get("values", [])

def parse_datetime(date_str):
    if date_str:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f%z")
    return None

async def process_stories(session, organization, user_id, progress_bar):
    story_stats_by_year = {}

    start_at = 0
    while True:
        stories = await get_next_stories(session, organization, user_id, start_at)
        start_at += take

        if not stories:
            break

        for story in stories:
            fields = story["fields"]
            created_time = parse_datetime(fields["created"])
            completed_time = parse_datetime(fields.get("resolutiondate") or fields.get("updated"))  # Check for alternative field names
            issue_id = story["id"]
            history = await get_issue_history(session, organization, issue_id)
            assigned_time = None
            code_review_time = None
            for change in history:
                for item in change["items"]:
                    if item["field"] == "assignee" and item["to"] == user_id:
                        assigned_time = parse_datetime(change["created"])
                    if item["field"] == "status" and item["toString"] == "Code Review":
                        code_review_time = parse_datetime(change["created"])
                        break
                if assigned_time and code_review_time:
                    break

            if not assigned_time or not completed_time:
                continue

            if not code_review_time:
                for change in history:
                    for item in change["items"]:
                        if item["field"] == "status" and item["from"] == user_id:
                            code_review_time = parse_datetime(change["created"])
                            break
                    if code_review_time:
                        break

            if not code_review_time:
                code_review_time = completed_time

            year = assigned_time.year
            if year not in story_stats_by_year:
                story_stats_by_year[year] = {
                    "stories": {
                        "completed": 0,
                        "written": 0,
                        "total_turnaround_hours": 0,
                        "total_development_hours": 0,
                    },
                    "bugs": {
                        "completed": 0,
                        "written": 0,
                        "total_turnaround_hours": 0,
                        "total_development_hours": 0,
                    }
                }

            if fields["issuetype"]["name"] == "Story":
                story_stats_by_year[year]["stories"]["completed"] += 1
                if fields["creator"]["accountId"] == user_id:
                    story_stats_by_year[year]["stories"]["written"] += 1
                turnaround_time = (completed_time - assigned_time).total_seconds() / 3600
                development_time = (code_review_time - assigned_time).total_seconds() / 3600
                story_stats_by_year[year]["stories"]["total_turnaround_hours"] += turnaround_time
                story_stats_by_year[year]["stories"]["total_development_hours"] += development_time
            elif fields["issuetype"]["name"] == "Bug":
                story_stats_by_year[year]["bugs"]["completed"] += 1
                if fields["creator"]["accountId"] == user_id:
                    story_stats_by_year[year]["bugs"]["written"] += 1
                turnaround_time = (completed_time - assigned_time).total_seconds() / 3600
                development_time = (code_review_time - assigned_time).total_seconds() / 3600
                story_stats_by_year[year]["bugs"]["total_turnaround_hours"] += turnaround_time
                story_stats_by_year[year]["bugs"]["total_development_hours"] += development_time

            progress_bar.update(1)

    return {year: stats for year, stats in story_stats_by_year.items() if stats["stories"]["completed"] > 0 or stats["bugs"]["completed"] > 0}

async def main():
    start_time = time.time()
    print(Fore.GREEN + "Starting script...")
    async with aiohttp.ClientSession() as session:
        total_stories = await get_total_stories(session, organization, user_id)

        story_stats_by_year_list = []
        with tqdm(total=total_stories, desc="Processing stories") as progress_bar:
            story_stats_by_year_list.append(await process_stories(session, organization, user_id, progress_bar))

        total_stats_by_year = {}
        overall_total_stats = {
            "stories": {
                "completed": 0,
                "written": 0,
                "total_turnaround_hours": 0,
                "total_development_hours": 0,
            },
            "bugs": {
                "completed": 0,
                "written": 0,
                "total_turnaround_hours": 0,
                "total_development_hours": 0,
            }
        }

        for story_stats_by_year in story_stats_by_year_list:
            for year, story_stats in story_stats_by_year.items():
                if year not in total_stats_by_year:
                    total_stats_by_year[year] = {
                        "stories": {
                            "completed": 0,
                            "written": 0,
                            "total_turnaround_hours": 0,
                            "total_development_hours": 0,
                        },
                        "bugs": {
                            "completed": 0,
                            "written": 0,
                            "total_turnaround_hours": 0,
                            "total_development_hours": 0,
                        }
                    }

                for key in total_stats_by_year[year]["stories"].keys():
                    total_stats_by_year[year]["stories"][key] += story_stats["stories"][key]
                    overall_total_stats["stories"][key] += story_stats["stories"][key]

                for key in total_stats_by_year[year]["bugs"].keys():
                    total_stats_by_year[year]["bugs"][key] += story_stats["bugs"][key]
                    overall_total_stats["bugs"][key] += story_stats["bugs"][key]

        # Export JSON files
        output_dir = os.path.join(os.path.dirname(__file__), "jira")
        os.makedirs(output_dir, exist_ok=True)

        for year, total_stats in total_stats_by_year.items():
            if total_stats["stories"]["completed"] > 0:
                total_stats["stories"]["average_turnaround_hours"] = total_stats["stories"]["total_turnaround_hours"] / total_stats["stories"]["completed"]
                total_stats["stories"]["average_development_hours"] = total_stats["stories"]["total_development_hours"] / total_stats["stories"]["completed"]
            else:
                total_stats["stories"]["average_turnaround_hours"] = 0
                total_stats["stories"]["average_development_hours"] = 0

            if total_stats["bugs"]["completed"] > 0:
                total_stats["bugs"]["average_turnaround_hours"] = total_stats["bugs"]["total_turnaround_hours"] / total_stats["bugs"]["completed"]
                total_stats["bugs"]["average_development_hours"] = total_stats["bugs"]["total_development_hours"] / total_stats["bugs"]["completed"]
            else:
                total_stats["bugs"]["average_turnaround_hours"] = 0
                total_stats["bugs"]["average_development_hours"] = 0

            with open(os.path.join(output_dir, f"{year}.json"), "w") as f:
                json.dump(total_stats, f, indent=4)

        if overall_total_stats["stories"]["completed"] > 0:
            overall_total_stats["stories"]["average_turnaround_hours"] = overall_total_stats["stories"]["total_turnaround_hours"] / overall_total_stats["stories"]["completed"]
            overall_total_stats["stories"]["average_development_hours"] = overall_total_stats["stories"]["total_development_hours"] / overall_total_stats["stories"]["completed"]
        else:
            overall_total_stats["stories"]["average_turnaround_hours"] = 0
            overall_total_stats["stories"]["average_development_hours"] = 0

        if overall_total_stats["bugs"]["completed"] > 0:
            overall_total_stats["bugs"]["average_turnaround_hours"] = overall_total_stats["bugs"]["total_turnaround_hours"] / overall_total_stats["bugs"]["completed"]
            overall_total_stats["bugs"]["average_development_hours"] = overall_total_stats["bugs"]["total_development_hours"] / overall_total_stats["bugs"]["completed"]
        else:
            overall_total_stats["bugs"]["average_turnaround_hours"] = 0
            overall_total_stats["bugs"]["average_development_hours"] = 0

        with open(os.path.join(output_dir, "total.json"), "w") as f:
            json.dump(overall_total_stats, f, indent=4)

    end_time = time.time()
    print(Fore.GREEN + f"Script finished in {end_time - start_time:.2f} seconds")

asyncio.run(main())
