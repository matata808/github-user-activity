#!/usr/bin/env python3
import argparse
import json
import os
import urllib.error
import urllib.request
from pathlib import Path

GITHUB_EVENTS_URL = "https://api.github.com/users/{username}/events/public"


def fetch_user_activity(username: str):
    github_token = os.getenv("GITHUB_TOKEN")
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "github-user-activity-cli"}
    if github_token:
        headers["Authorization"] = f"Bearer {github_token}"

    request = urllib.request.Request(
        GITHUB_EVENTS_URL.format(username=username),
        headers=headers,
    )
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def save_json(data, output_path: Path):
    output_path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def load_json(input_path: Path):
    return json.loads(input_path.read_text(encoding="utf-8"))


def print_json(data):
    print(json.dumps(data, indent=2))


def build_parser():
    parser = argparse.ArgumentParser(description="Fetch and view GitHub user activity")
    subparsers = parser.add_subparsers(dest="command", required=True)

    fetch_parser = subparsers.add_parser("fetch", help="Fetch activity for a username and store it as JSON")
    fetch_parser.add_argument("username", help="GitHub username")
    fetch_parser.add_argument("-o", "--output", default="activity.json", help="Output JSON file path")
    fetch_parser.add_argument("--show", action="store_true", help="Print fetched JSON to stdout")

    show_parser = subparsers.add_parser("show", help="Display a stored JSON file")
    show_parser.add_argument("-i", "--input", default="activity.json", help="Input JSON file path")

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.command == "fetch":
        try:
            activity = fetch_user_activity(args.username)
        except urllib.error.HTTPError as error:
            if error.code == 403:
                parser.error("Failed to fetch activity: HTTP 403 (rate limited). Set GITHUB_TOKEN and try again.")
            parser.error(f"Failed to fetch activity: HTTP {error.code}")
        except urllib.error.URLError as error:
            parser.error(f"Failed to fetch activity: {error.reason}")

        output_path = Path(args.output)
        save_json(activity, output_path)
        print(f"Saved activity to {output_path}")

        if args.show:
            print_json(activity)
        return 0

    if args.command == "show":
        input_path = Path(args.input)
        if not input_path.exists():
            parser.error(f"JSON file not found: {input_path}")

        print_json(load_json(input_path))
        return 0

    parser.error("Unknown command")


if __name__ == "__main__":
    raise SystemExit(main())
