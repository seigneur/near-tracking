# NEAR DAppNode Release Tracker

A Cloudflare Worker that monitors the [dappnode/DAppNodePackage-NEAR](https://github.com/dappnode/DAppNodePackage-NEAR) repository for new releases and sends Telegram notifications.

## Features

- 🕐 **Automatic checks every 6 hours** via cron trigger
- 💾 **KV storage** to track the last checked release
- 📱 **Telegram notifications** for new releases
- 🚀 **TypeScript** with proper type definitions
- 🔧 **Manual trigger** endpoint for testing

## Setup

### Prerequisites

- [Node.js](https://nodejs.org/) (v16 or higher)
- [Wrangler CLI](https://developers.cloudflare.com/workers/wrangler/)
- A Cloudflare account
- A Telegram Bot (create one via [@BotFather](https://t.me/botfather))

### Installation

1. Clone the repository:
```bash
git clone https://github.com/seigneur/near-tracking.git
cd near-tracking
```

2. Install dependencies:
```bash
npm install
```

3. Create a KV namespace:
```bash
wrangler kv:namespace create RELEASE_TRACKER
wrangler kv:namespace create RELEASE_TRACKER --preview
```

4. Update `wrangler.toml` with your KV namespace IDs from the previous step.

5. Set up secrets:
```bash
wrangler secret put TG_BOT_TOKEN
# Enter your Telegram Bot Token when prompted

wrangler secret put TG_CHAT_ID
# Enter your Telegram Chat ID when prompted
```

### Getting Telegram Credentials

1. **Bot Token**: Create a bot via [@BotFather](https://t.me/botfather) and copy the token
2. **Chat ID**: 
   - Start a conversation with your bot
   - Send a message to [@userinfobot](https://t.me/userinfobot) to get your chat ID
   - Or use `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates` after sending a message to your bot

### Deployment

Deploy to Cloudflare Workers:
```bash
npm run deploy
```

## Usage

### Automatic Checks

The worker automatically runs every 6 hours (at 00:00, 06:00, 12:00, and 18:00 UTC) via the cron trigger.

### Manual Trigger

You can manually trigger a check by visiting:
```
https://near-tracking.<your-subdomain>.workers.dev/trigger
```

Or using curl:
```bash
curl https://near-tracking.<your-subdomain>.workers.dev/trigger
```

### Health Check

Check if the worker is running:
```bash
curl https://near-tracking.<your-subdomain>.workers.dev/health
```

## Development

Run the worker locally:
```bash
npm run dev
```

## How It Works

1. **Scheduled Trigger**: Every 6 hours, Cloudflare triggers the worker
2. **GitHub API Call**: Fetches the latest release from `dappnode/DAppNodePackage-NEAR`
3. **Compare**: Checks the release tag against the stored value in KV
4. **Notify**: If new, sends a formatted Telegram message with release details
5. **Update**: Stores the new release tag in KV storage

## Configuration

### wrangler.toml

- **Cron schedule**: `0 */6 * * *` (every 6 hours)
- **KV namespace**: `RELEASE_TRACKER`
- **Secrets**: `TG_BOT_TOKEN`, `TG_CHAT_ID`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.