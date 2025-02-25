# This script retrieves and outputs statistics on Azure DevOps pull requests that I've created and completed.

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
token = os.getenv("TOKEN")
organization = os.getenv("ORGANIZATION")
creator_id = os.getenv("CREATOR_ID")

# Check if all required environment variables are set
if not all([email, token, organization, creator_id]):
    raise ValueError(Fore.RED + "One or more required environment variables are missing")

# Settings
take = 1000

# Constants
base64_auth_info = base64.b64encode(f"{email}:{token}".encode("ascii")).decode("ascii")
headers = {"Authorization": f"Basic {base64_auth_info}"}

async def fetch(session, url):
    async with session.get(url, headers=headers) as response:
        return await response.json()

async def get_user_object(session, email):
    user_endpoint = f"https://vssps.dev.azure.com/{organization}/_apis/graph/users?api-version=6.0-preview.1"
    response = await fetch(session, user_endpoint)
    users = response.get("value", [])
    for user in users:
        if user.get("mailAddress") == email:
            return user
    raise ValueError(Fore.RED + f"User with email {email} not found")

async def get_repositories(session, organization):
    repo_endpoint = f"https://dev.azure.com/{organization}/_apis/git/repositories?api-version=6.1-preview.1"
    response = await fetch(session, repo_endpoint)
    return response.get("value", [])

async def get_total_pull_requests(session, organization, repository_id, creator_id):
    endpoint = f"https://dev.azure.com/{organization}/_apis/git/repositories/{repository_id}/pullrequests?api-version=7.0&searchCriteria.status=completed&searchCriteria.creatorId={creator_id}&$top=1"
    response = await fetch(session, endpoint)
    return response.get("count", 0)

async def get_next_pull_requests(session, organization, repository_id, creator_id, skip):
    endpoint = f"https://dev.azure.com/{organization}/_apis/git/repositories/{repository_id}/pullrequests?api-version=7.0&searchCriteria.status=completed&searchCriteria.creatorId={creator_id}&$top={take}&$skip={skip}"
    response = await fetch(session, endpoint)
    return response.get("value", [])

async def get_threads(session, organization, repository_id, pull_request_id):
    endpoint = f"https://dev.azure.com/{organization}/_apis/git/repositories/{repository_id}/pullrequests/{pull_request_id}/threads?api-version=7.0"
    response = await fetch(session, endpoint)
    return response.get("value", [])

async def get_next_commits(session, organization, repository_id, author, skip):
    endpoint = f"https://dev.azure.com/{organization}/_apis/git/repositories/{repository_id}/commits?api-version=7.0&searchCriteria.author={author}&$top={take}&$skip={skip}"
    response = await fetch(session, endpoint)
    return response.get("value", [])

def parse_datetime(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        try:
            return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
        except ValueError:
            return datetime.strptime(date_str[:19], "%Y-%m-%dT%H:%M:%S")

async def process_repository(session, repo, creator_id, author, progress_bar):
    repo_stats_by_year = {}

    skip = 0
    while True:
        pull_requests = await get_next_pull_requests(session, organization, repo["id"], creator_id, skip)
        skip += take

        if not pull_requests:
            break

        for pr in pull_requests:
            year = parse_datetime(pr["creationDate"]).year
            if year not in repo_stats_by_year:
                repo_stats_by_year[year] = {
                    "repository": repo["name"],
                    "pull_requests_completed": 0,
                    "threads_received": 0,
                    "comments_received": 0,
                    "total_commits": 0,
                    "total_turnaround_hours": 0,
                }

            repo_stats_by_year[year]["pull_requests_completed"] += 1
            threads = await get_threads(session, organization, repo["id"], pr["pullRequestId"])
            repo_stats_by_year[year]["threads_received"] += len(threads)
            for thread in threads:
                repo_stats_by_year[year]["comments_received"] += len(thread["comments"])

            created_time = parse_datetime(pr["creationDate"])
            completed_time = parse_datetime(pr["closedDate"])
            turnaround_time = (completed_time - created_time).total_seconds() / 3600
            repo_stats_by_year[year]["total_turnaround_hours"] += turnaround_time

            progress_bar.update(1)

    skip = 0
    while True:
        commits = await get_next_commits(session, organization, repo["id"], author, skip)
        skip += take

        if not commits:
            break

        for commit in commits:
            year = parse_datetime(commit["author"]["date"]).year
            if year not in repo_stats_by_year:
                repo_stats_by_year[year] = {
                    "repository": repo["name"],
                    "pull_requests_completed": 0,
                    "threads_received": 0,
                    "comments_received": 0,
                    "total_commits": 0,
                    "total_turnaround_hours": 0,
                }

            repo_stats_by_year[year]["total_commits"] += 1

    return {year: stats for year, stats in repo_stats_by_year.items() if stats["pull_requests_completed"] > 0}

async def main():
    start_time = time.time()
    print(Fore.GREEN + "Starting script...")
    async with aiohttp.ClientSession() as session:
        user_object = await get_user_object(session, email)
        author = user_object["displayName"]
        repos = await get_repositories(session, organization)
        total_pull_requests = 0
        for repo in repos:
            total_pull_requests += await get_total_pull_requests(session, organization, repo["id"], creator_id)

        repo_stats_by_year_list = []
        with tqdm(total=total_pull_requests, desc="Processing pull requests") as progress_bar:
            tasks = [process_repository(session, repo, creator_id, author, progress_bar) for repo in repos]
            for task in asyncio.as_completed(tasks):
                repo_stats_by_year_list.append(await task)

        total_stats_by_year = {}
        total_stats_overall = {}

        for repo_stats_by_year in repo_stats_by_year_list:
            for year, repo_stats in repo_stats_by_year.items():
                if year not in total_stats_by_year:
                    total_stats_by_year[year] = {
                        "repository": "Total",
                        "pull_requests_completed": 0,
                        "threads_received": 0,
                        "comments_received": 0,
                        "total_commits": 0,
                        "total_turnaround_hours": 0,
                    }

                for key in total_stats_by_year[year].keys():
                    if key != "repository":
                        total_stats_by_year[year][key] += repo_stats[key]

                repo_name = repo_stats["repository"]
                if repo_name not in total_stats_overall:
                    total_stats_overall[repo_name] = {
                        "repository": repo_name,
                        "pull_requests_completed": 0,
                        "threads_received": 0,
                        "comments_received": 0,
                        "total_commits": 0,
                        "total_turnaround_hours": 0,
                    }

                for key in total_stats_overall[repo_name].keys():
                    if key != "repository":
                        total_stats_overall[repo_name][key] += repo_stats[key]

        # Export JSON files
        output_dir = os.path.join(os.path.dirname(__file__), "completed_prs")
        os.makedirs(output_dir, exist_ok=True)

        for repo_stats_by_year in repo_stats_by_year_list:
            for year, repo_stats in repo_stats_by_year.items():
                year_dir = os.path.join(output_dir, str(year))
                os.makedirs(year_dir, exist_ok=True)

                if repo_stats["pull_requests_completed"] > 0:
                    repo_stats["average_threads_received"] = repo_stats["threads_received"] / repo_stats["pull_requests_completed"]
                    repo_stats["average_comments_received"] = repo_stats["comments_received"] / repo_stats["pull_requests_completed"]
                    repo_stats["average_commits"] = repo_stats["total_commits"] / repo_stats["pull_requests_completed"]
                    repo_stats["average_turnaround_hours"] = repo_stats["total_turnaround_hours"] / repo_stats["pull_requests_completed"]
                else:
                    repo_stats["average_threads_received"] = 0
                    repo_stats["average_comments_received"] = 0
                    repo_stats["average_commits"] = 0
                    repo_stats["average_turnaround_hours"] = 0

                repo_name = repo_stats["repository"].replace(" ", "-").lower()
                with open(os.path.join(year_dir, f"{repo_name}.json"), "w") as f:
                    json.dump(repo_stats, f, indent=4)

        for year, total_stats in total_stats_by_year.items():
            year_dir = os.path.join(output_dir, str(year))
            if total_stats["pull_requests_completed"] > 0:
                total_stats["average_threads_received"] = total_stats["threads_received"] / total_stats["pull_requests_completed"]
                total_stats["average_comments_received"] = total_stats["comments_received"] / total_stats["pull_requests_completed"]
                total_stats["average_commits"] = total_stats["total_commits"] / total_stats["pull_requests_completed"]
                total_stats["average_turnaround_hours"] = total_stats["total_turnaround_hours"] / total_stats["pull_requests_completed"]
            else:
                total_stats["average_threads_received"] = 0
                total_stats["average_comments_received"] = 0
                total_stats["average_commits"] = 0
                total_stats["average_turnaround_hours"] = 0

            with open(os.path.join(year_dir, "total.json"), "w") as f:
                json.dump(total_stats, f, indent=4)

        overall_total_stats = {
            "repository": "Total",
            "pull_requests_completed": 0,
            "threads_received": 0,
            "comments_received": 0,
            "total_commits": 0,
            "total_turnaround_hours": 0,
        }

        for repo_name, stats in total_stats_overall.items():
            if stats["pull_requests_completed"] > 0:
                stats["average_threads_received"] = stats["threads_received"] / stats["pull_requests_completed"]
                stats["average_comments_received"] = stats["comments_received"] / stats["pull_requests_completed"]
                stats["average_commits"] = stats["total_commits"] / stats["pull_requests_completed"]
                stats["average_turnaround_hours"] = stats["total_turnaround_hours"] / stats["pull_requests_completed"]
            else:
                stats["average_threads_received"] = 0
                stats["average_comments_received"] = 0
                stats["average_commits"] = 0
                stats["average_turnaround_hours"] = 0

            for key in overall_total_stats.keys():
                if key != "repository":
                    overall_total_stats[key] += stats[key]

            repo_name = stats["repository"].replace(" ", "-").lower()
            with open(os.path.join(output_dir, f"{repo_name}.json"), "w") as f:
                json.dump(stats, f, indent=4)

        if overall_total_stats["pull_requests_completed"] > 0:
            overall_total_stats["average_threads_received"] = overall_total_stats["threads_received"] / overall_total_stats["pull_requests_completed"]
            overall_total_stats["average_comments_received"] = overall_total_stats["comments_received"] / overall_total_stats["pull_requests_completed"]
            overall_total_stats["average_commits"] = overall_total_stats["total_commits"] / overall_total_stats["pull_requests_completed"]
            overall_total_stats["average_turnaround_hours"] = overall_total_stats["total_turnaround_hours"] / overall_total_stats["pull_requests_completed"]
        else:
            overall_total_stats["average_threads_received"] = 0
            overall_total_stats["average_comments_received"] = 0
            overall_total_stats["average_commits"] = 0
            overall_total_stats["average_turnaround_hours"] = 0

        with open(os.path.join(output_dir, "total.json"), "w") as f:
            json.dump(overall_total_stats, f, indent=4)

    end_time = time.time()
    print(Fore.GREEN + f"Script finished in {end_time - start_time:.2f} seconds")

asyncio.run(main())