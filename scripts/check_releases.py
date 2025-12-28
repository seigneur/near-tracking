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


def send_telegram_notification(message, bot_token=None, chat_id=None):
    """Send notification to Telegram."""
    if not bot_token or not chat_id:
        print("  Telegram credentials not configured, skipping notification")
        return False

    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'HTML',
        'disable_web_page_preview': False
    }

    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            print("  Telegram notification sent successfully")
            return True
        else:
            print(f"  Failed to send Telegram notification: {response.status_code}")
            print(f"  Response: {response.text}")
            return False
    except Exception as e:
        print(f"  Error sending Telegram notification: {e}")
        return False


def main():
    """Main function to check for new releases."""
    config = load_config()
    releases = load_releases()
    token = os.getenv('GITHUB_TOKEN')

    # Get Telegram credentials
    telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')

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

        # Send Telegram notifications for each new release
        # Wrapped in try-except to ensure pipeline continues even if notifications fail
        if telegram_bot_token and telegram_chat_id:
            print("\nSending Telegram notifications...")
            try:
                for item in new_releases_found:
                    try:
                        release = item['release']

                        # Truncate release notes if too long
                        body = release.get('body', '')
                        if len(body) > 500:
                            body = body[:500] + "..."

                        # Format message with HTML
                        message = f"🚀 <b>New Release: {item['project']}</b>\n\n"
                        message += f"<b>Version:</b> {release['tag_name']}\n"

                        if release.get('published_at'):
                            message += f"<b>Published:</b> {release['published_at']}\n"

                        message += f"\n<a href=\"{release['html_url']}\">View Release</a>\n"

                        if body:
                            message += f"\n<b>Release Notes:</b>\n{body}"

                        send_telegram_notification(message, telegram_bot_token, telegram_chat_id)
                    except Exception as e:
                        # Log error but continue with other notifications
                        print(f"  Error processing Telegram notification for {item['project']}: {e}")
                        continue
            except Exception as e:
                # Catch any unexpected errors in the Telegram section
                print(f"  Telegram notification section failed: {e}")
                print("  Continuing with workflow...")

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
