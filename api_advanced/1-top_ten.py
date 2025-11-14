#!/usr/bin/python3
"""Script that prints the titles of the first 10 hot posts."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a subreddit.
    If invalid, prints None.
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "MyAPI/0.0.1"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {}).get("children", [])

    if not data:
        print(None)
        return

    for post in data:
        print(post.get("data", {}).get("title"))

