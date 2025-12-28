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

# Run the script
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