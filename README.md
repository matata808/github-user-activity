# github-user-activity

Minimal CLI tool to fetch GitHub user activity and save/show it as JSON.

## Usage

Fetch activity for a username and save it to JSON:

```bash
python github_user_activity.py fetch <github-username> --output activity.json
```

Show a previously saved JSON file:

```bash
python github_user_activity.py show --input activity.json
```

Optional: print fetched JSON immediately:

```bash
python github_user_activity.py fetch <github-username> --show
```

If GitHub API rate limits anonymous requests, set a token:

```bash
export GITHUB_TOKEN=<your-token>
```
