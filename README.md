# GitHub User Activity Displayer

A Java CLI tool that fetches and displays a GitHub user's recent public activity in a clean, human-readable format.

## Example Output

```
- Pushed 5 commits to matata808/github-user-activity
- Pushed 9 commits to matata808/Task-Tracker
- Pull Request closed in matata808/github-user-activity
- Deleted branch 'copilot/create-cli-tool-branch' in matata808/github-user-activity
- Created a new branch in matata808/Task-Tracker
- Starred matata808/github-user-activity
```

## Features

- Fetches recent public events via the GitHub API
- Aggregates push events per repository (e.g. "Pushed 5 commits to ...")
- Displays pull requests, branch creations, deletions, stars, and more
- No external frameworks. Just Java and the GitHub REST API

## Requirements

- Java 17+
- [`json-20251224.jar`](https://mvnrepository.com/artifact/org.json/json) (org.json)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/matata808/github-user-activity.git
   cd github-user-activity
   git checkout dev
   ```

2. Download the `org.json` dependency and add it to your classpath:
   ```
   json-20251224.jar
   ```

3. Compile:
   ```bash
   javac -cp .:json-20251224.jar src/Main.java -d out/
   ```

4. Run:
   ```bash
   java -cp out:json-20251224.jar Main <github-username>
   ```

   Example:
   ```bash
   java -cp out:json-20251224.jar Main matata808
   ```

## How It Works

1. Calls `https://api.github.com/users/{username}/events`
2. Parses the JSON response using `org.json`
3. Groups and counts push events per repository using a `HashMap<String, Integer>`
4. Translates each event type into a readable sentence

## Supported Event Types

| Event | Output |
|---|---|
| `PushEvent` | Pushed N commits to repo |
| `PullRequestEvent` | Pull Request opened/closed in repo |
| `CreateEvent` | Created a new branch/repo |
| `DeleteEvent` | Deleted branch in repo |
| `WatchEvent` | Starred repo |
| `IssuesEvent` | Opened a new issue in repo |

## Project Structure

```
GitHub-User-Activity-Displayer/
└── src/
    └── untitled/
        └── src/
            ├── ArgsParser.java
            ├── GitFetcher.java
            ├── JSONDisplayer.java
            └── Main.java
```

## Classes

| Class | Responsibility |
|---|---|
| `Main` | Entry point, wires everything together |
| `ArgsParser` | Validates and parses the CLI argument (username) |
| `GitFetcher` | Calls the GitHub API and retrieves the raw JSON |
| `JSONDisplayer` | Parses and prints the activity in human-readable format |

## Inspiration

This project is based on the [GitHub User Activity](https://roadmap.sh/projects/github-user-activity) challenge from [roadmap.sh](https://roadmap.sh).
