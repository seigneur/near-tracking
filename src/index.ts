/**
 * Cloudflare Worker to track NEAR DAppNode package releases
 * Checks GitHub API every 6 hours and sends Telegram notifications for new releases
 */

// Environment interface with KV namespace and secrets
export interface Env {
	RELEASE_TRACKER: KVNamespace;
	TG_BOT_TOKEN: string;
	TG_CHAT_ID: string;
}

// GitHub Release interface
interface GitHubRelease {
	tag_name: string;
	name: string;
	html_url: string;
	published_at: string;
}

// Storage key for last checked release
const LAST_RELEASE_KEY = 'last_release_tag';

/**
 * Fetch the latest release from GitHub API
 */
async function fetchLatestRelease(): Promise<GitHubRelease | null> {
	const owner = 'dappnode';
	const repo = 'DAppNodePackage-NEAR';
	const url = `https://api.github.com/repos/${owner}/${repo}/releases/latest`;

	try {
		const response = await fetch(url, {
			headers: {
				'User-Agent': 'Cloudflare-Worker-NEAR-Tracker',
				'Accept': 'application/vnd.github.v3+json',
			},
		});

		if (!response.ok) {
			console.error(`GitHub API error: ${response.status} ${response.statusText}`);
			return null;
		}

		const release: GitHubRelease = await response.json();
		return release;
	} catch (error) {
		console.error('Error fetching latest release:', error);
		return null;
	}
}

/**
 * Send Telegram notification
 */
async function sendTelegramNotification(
	botToken: string,
	chatId: string,
	message: string
): Promise<boolean> {
	const url = `https://api.telegram.org/bot${botToken}/sendMessage`;

	try {
		const response = await fetch(url, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({
				chat_id: chatId,
				text: message,
				parse_mode: 'Markdown',
			}),
		});

		if (!response.ok) {
			const errorData = await response.text();
			console.error(`Telegram API error: ${response.status} ${response.statusText}`, errorData);
			return false;
		}

		return true;
	} catch (error) {
		console.error('Error sending Telegram notification:', error);
		return false;
	}
}

/**
 * Main handler function
 */
async function handleScheduled(env: Env): Promise<void> {
	console.log('Checking for new NEAR DAppNode package releases...');

	// Fetch the latest release from GitHub
	const latestRelease = await fetchLatestRelease();
	if (!latestRelease) {
		console.error('Failed to fetch latest release');
		return;
	}

	console.log(`Latest release: ${latestRelease.tag_name}`);

	// Get the last checked release from KV storage
	const lastRelease = await env.RELEASE_TRACKER.get(LAST_RELEASE_KEY);
	console.log(`Last checked release: ${lastRelease || 'none'}`);

	// Check if this is a new release
	if (lastRelease !== latestRelease.tag_name) {
		console.log('New release detected!');

		// Compose the notification message
		const message = `🚀 *New NEAR DAppNode Package Release*\n\n` +
			`*Version:* ${latestRelease.tag_name}\n` +
			`*Name:* ${latestRelease.name || latestRelease.tag_name}\n` +
			`*Published:* ${new Date(latestRelease.published_at).toLocaleString()}\n\n` +
			`🔗 [View Release](${latestRelease.html_url})`;

		// Send Telegram notification
		const sent = await sendTelegramNotification(
			env.TG_BOT_TOKEN,
			env.TG_CHAT_ID,
			message
		);

		if (sent) {
			console.log('Telegram notification sent successfully');
			// Update the last checked release in KV storage
			await env.RELEASE_TRACKER.put(LAST_RELEASE_KEY, latestRelease.tag_name);
			console.log('Updated last release in KV storage');
		} else {
			console.error('Failed to send Telegram notification');
		}
	} else {
		console.log('No new release detected');
	}
}

/**
 * Worker export with scheduled and fetch handlers
 */
export default {
	// Scheduled handler for cron triggers
	async scheduled(event: ScheduledEvent, env: Env, ctx: ExecutionContext): Promise<void> {
		ctx.waitUntil(handleScheduled(env));
	},

	// Fetch handler for manual testing/triggering
	async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
		const url = new URL(request.url);

		// Manual trigger endpoint
		if (url.pathname === '/trigger' || url.pathname === '/') {
			try {
				await handleScheduled(env);
				return new Response('Release check completed. Check logs for details.', {
					status: 200,
					headers: { 'Content-Type': 'text/plain' },
				});
			} catch (error) {
				console.error('Error in fetch handler:', error);
				return new Response(`Error: ${error}`, {
					status: 500,
					headers: { 'Content-Type': 'text/plain' },
				});
			}
		}

		// Health check endpoint
		if (url.pathname === '/health') {
			return new Response('OK', {
				status: 200,
				headers: { 'Content-Type': 'text/plain' },
			});
		}

		return new Response('NEAR DAppNode Release Tracker\n\nEndpoints:\n- / or /trigger - Manually trigger release check\n- /health - Health check', {
			status: 200,
			headers: { 'Content-Type': 'text/plain' },
		});
	},
};
