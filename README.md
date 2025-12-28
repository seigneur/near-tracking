# Release Tracker

Automated tracking of new releases for blockchain and Web3 projects.

## Tracked Projects

This repository monitors releases for the following projects:

- **Aztec CLI** ([AztecProtocol/aztec-packages](https://github.com/AztecProtocol/aztec-packages)) - Privacy-focused application development tools
- **NEAR Protocol** ([near/nearcore](https://github.com/near/nearcore)) - NEAR Protocol node implementation
- **Nethermind** ([NethermindEth/nethermind](https://github.com/NethermindEth/nethermind)) - Ethereum client implementation

## How It Works

This repository uses GitHub Actions to automatically check for new releases:

1. **Daily Checks**: A scheduled workflow runs daily at 00:00 UTC
2. **Release Detection**: The script queries GitHub API for the latest release of each tracked project
3. **Comparison**: New releases are compared against previously tracked versions
4. **Updates**: When new releases are detected:
   - The `releases.json` file is updated with the latest release information
   - A `RELEASES_SUMMARY.md` file is generated with release details
   - Changes are automatically committed to the repository
   - Notifications are sent to Telegram (if configured)

## Telegram Integration

This repository can send notifications to a Telegram channel or chat whenever new releases are detected.

### Setup Instructions

1. **Create a Telegram Bot:**
   - Open Telegram and search for [@BotFather](https://t.me/BotFather)
   - Send `/newbot` and follow the instructions
   - Save the bot token (looks like `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

2. **Get Your Chat ID:**
   - Add your bot to a channel/group or start a private chat
   - Send a message to the bot
   - Visit `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
   - Look for `"chat":{"id":` in the response (the number is your chat ID)
   - For channels, the chat ID will be negative (e.g., `-1001234567890`)

3. **Configure GitHub Secrets:**
   - Go to your repository Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Add two secrets:
     - Name: `TELEGRAM_BOT_TOKEN`, Value: Your bot token from step 1
     - Name: `TELEGRAM_CHAT_ID`, Value: Your chat ID from step 2

4. **Test the Integration:**
   - Go to Actions tab and manually trigger the workflow
   - Check your Telegram chat for notifications

### Message Format

Telegram notifications include:
- Project name and release version
- Publication date
- Direct link to the release
- Release notes (truncated to 500 characters)

Messages are formatted with HTML for better readability.

## Files

- `config.yaml` - Configuration file listing all tracked projects
- `releases.json` - Current state of tracked releases (auto-generated)
- `RELEASES_SUMMARY.md` - Human-readable summary of latest releases (auto-generated)
- `scripts/check_releases.py` - Python script that checks for new releases

## Manual Execution

You can manually trigger a release check:

1. Go to the [Actions tab](../../actions)
2. Select "Check for New Releases" workflow
3. Click "Run workflow"

## Local Development

To run the release checker locally:

```bash
# Install dependencies
pip install pyyaml requests

# Run the script (without Telegram notifications)
python scripts/check_releases.py

# Or with Telegram notifications (optional)
export TELEGRAM_BOT_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"
python scripts/check_releases.py
```

## Adding New Projects

To track additional projects, edit `config.yaml` and add a new entry:

```yaml
projects:
  - name: "Project Name"
    repo: "owner/repository"
    description: "Project description"
```

## License

See [LICENSE](LICENSE) file for details.