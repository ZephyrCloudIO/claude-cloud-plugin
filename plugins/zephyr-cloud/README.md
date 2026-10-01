# Zephyr Cloud

![Zephyr Cloud](assets/zephyr-cloud-icon.svg)

Create and publish small static websites, landing pages and HTML pages from Claude. Keep the same live address when you publish an update, inspect retained builds, roll back a release, and remember the organization used for deployments. Sign in with your own Zephyr Cloud account; its existing permissions and entitlements apply.

## Setup

Install this plugin from the `ZephyrCloudIO/claude-cloud-plugin` marketplace, or upload the plugin ZIP through **Customize > Plugins > Add > Upload plugin**. In the plugin's **Connectors** tab, connect **zephyr-cloud** and complete Zephyr OAuth sign-in. Team and Enterprise administrators may need to make the connector available before members connect with their own accounts.

The bundled remote connector is `https://mcp.zephyr-cloud.io/sites/content/mcp`. Claude Code loads it from `.mcp.json`. No API keys or tokens belong in the plugin files or chat.

## Try it

- “Make a simple coffee shop page and put it online with Zephyr Cloud.”
- “Use my selected organization and remember it for this chat.”
- “Add an autumn-special banner and publish the update at the same live address.”
- “Show the previous builds and roll back production to the version I select.”

Claude creates self-contained HTML or a built static bundle, chooses readable names, and generates the identifiers needed by the connector. With several organizations and no saved choice, it asks which organization owns the site. An unqualified request to remember the organization saves this chat's preference and verifies it; project and account preferences require an explicit scope. Updates reuse the configured site and retain its ownership.

“Publish” includes upload and promotion to the stable production URL. “Preview only” returns an immutable build URL. Publishing creates a public site, so include only content intended for public access. Rollback serves a retained build without rebuilding. Publishing and rollout may briefly require edge propagation.

## Limits and verification

The complete HTML or JSON bundle is limited to **256 KiB UTF-8**, including JSON/base64 overhead. Larger sites require the Zephyr CLI in an environment with shell access. Only built static assets are supported: source projects, SSR and Claude-only runtime APIs need a build/export or replacement before external hosting. No billing, purchases or subscription upgrades are exposed by these seven tools.

The skill checks the exact uploaded build before promotion and verifies the served page when fetching is available. A team's Claude network restrictions may prevent fetching `zephyrcloud.app`; in that case Claude reports the limitation and the link can be checked in a browser. This plugin does not change network or permission settings. Installation makes the skill available but does not guarantee automatic provider selection; respect explicit provider choices and existing hosting configurations.

## Data handling

The remote connector sends deployment content and requested site/organization identifiers to Zephyr Cloud using the connected user's OAuth authorization. The shared Zephyr publisher uses Zephyr's built-in Cloudflare infrastructure for static hosting. Published site assets are served publicly; account organization choices and generated conversation/project context keys must stay outside those assets.

Zephyr stores site configuration, requested organization defaults and publication/retry metadata for its publishing workflow. Builds are retained for inspection and rollback. Clearing a saved organization default removes that scoped preference; it does not remove a site or build. The plugin does not request Claude chat history or memories from the server and does not bundle local executables, hooks, credentials or account-test fixtures. Requests sent through Claude remain subject to Claude's own service terms and settings.

See [Zephyr's privacy policy](https://zephyr-cloud.io/privacy). For privacy, retention or account-support questions, contact [support@zephyr-cloud.io](mailto:support@zephyr-cloud.io).

## License

The plugin manifest declares a Proprietary license. Contact Zephyr Cloud for licensing questions.
