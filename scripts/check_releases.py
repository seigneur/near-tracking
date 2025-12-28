#!/usr/bin/env python3
"""
Script to check for new releases of tracked projects.
"""

import os
import json
import yaml
import requests
from datetime import datetime
from pathlib import Path


def load_config():
    """Load the configuration file."""
    with open('config.yaml', 'r') as f:
        return yaml.safe_load(f)


def load_releases():
    """Load previously tracked releases."""
    releases_file = Path('releases.json')
    if releases_file.exists():
        with open(releases_file, 'r') as f:
            return json.load(f)
    return {}


def save_releases(releases):
    """Save tracked releases to file."""
    with open('releases.json', 'w') as f:
        json.dump(releases, f, indent=2)


def get_latest_release(repo, token=None):
    """Fetch the latest release from GitHub API."""
    url = f"https://api.github.com/repos/{repo}/releases/latest"
    headers = {}
    if token:
        headers['Authorization'] = f'token {token}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return {
            'tag_name': data['tag_name'],
            'name': data.get('name', data['tag_name']),
            'published_at': data['published_at'],
            'html_url': data['html_url'],
            'body': data.get('body', '')
        }
    elif response.status_code == 404:
        # No releases found, try tags instead
        url = f"https://api.github.com/repos/{repo}/tags"
        response = requests.get(url, headers=headers)
        if response.status_code == 200 and response.json():
            data = response.json()[0]
            return {
                'tag_name': data['name'],
                'name': data['name'],
                'published_at': None,
                'html_url': f"https://github.com/{repo}/releases/tag/{data['name']}",
                'body': ''
            }

    return None


def create_issue(repo_name, release_info, token=None):
    """Create a GitHub issue for a new release (optional)."""
    # This would create an issue in the current repository
    # You can implement this if you want automatic issue creation
    pass


def main():
    """Main function to check for new releases."""
    config = load_config()
    releases = load_releases()
    token = os.getenv('GITHUB_TOKEN')

    new_releases_found = []

    for project in config['projects']:
        name = project['name']
        repo = project['repo']

        print(f"Checking {name} ({repo})...")

        latest_release = get_latest_release(repo, token)

        if not latest_release:
            print(f"  No releases found for {name}")
            continue

        current_tag = latest_release['tag_name']
        previous_tag = releases.get(repo, {}).get('tag_name')

        if previous_tag != current_tag:
            print(f"  New release found: {current_tag}")
            new_releases_found.append({
                'project': name,
                'repo': repo,
                'release': latest_release
            })
        else:
            print(f"  No new release (current: {current_tag})")

        # Update tracked releases
        releases[repo] = latest_release

    # Save updated releases
    save_releases(releases)

    # Generate summary report
    if new_releases_found:
        print("\n" + "=" * 60)
        print("NEW RELEASES DETECTED:")
        print("=" * 60)
        for item in new_releases_found:
            print(f"\n{item['project']}:")
            print(f"  Version: {item['release']['tag_name']}")
            print(f"  URL: {item['release']['html_url']}")
            if item['release']['published_at']:
                print(f"  Published: {item['release']['published_at']}")
        print("\n" + "=" * 60)

        # Update summary file
        summary_file = Path('RELEASES_SUMMARY.md')
        with open(summary_file, 'w') as f:
            f.write("# Latest Releases\n\n")
            f.write(f"*Last updated: {datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')} UTC*\n\n")

            for project in config['projects']:
                repo = project['repo']
                if repo in releases:
                    rel = releases[repo]
                    f.write(f"## {project['name']}\n\n")
                    f.write(f"**Latest Version:** {rel['tag_name']}\n\n")
                    if rel['published_at']:
                        f.write(f"**Published:** {rel['published_at']}\n\n")
                    f.write(f"**URL:** {rel['html_url']}\n\n")
                    if rel['body']:
                        f.write(f"**Release Notes:**\n\n{rel['body'][:500]}\n\n")
                    f.write("---\n\n")
    else:
        print("\nNo new releases detected.")


if __name__ == '__main__':
    main()
