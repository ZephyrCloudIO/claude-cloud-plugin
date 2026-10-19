# Zephyr Cloud

![Zephyr Cloud](assets/zephyr-cloud-icon.png)

Publish what Claude makes (HTML pages, React components, Markdown documents, SVG images and Mermaid diagrams) to Zephyr Cloud at a public, stable URL. In Claude Code, build and deploy a whole web app project as well. Keep the same live address when you publish an update, inspect retained builds, roll back a release, and remember the organization used for deployments. Sign in with your own Zephyr Cloud account; its existing permissions and entitlements apply.

## Setup

In Claude Code:

```sh
claude plugin marketplace add ZephyrCloudIO/claude-cloud-plugin
claude plugin install zephyr-cloud@zephyr-cloud
```

In Claude chat or Cowork, install this plugin from the `ZephyrCloudIO/claude-cloud-plugin` marketplace, or upload the plugin ZIP through **Customize > Plugins > Add > Upload plugin**. In the plugin's **Connectors** tab, connect **Zephyr Cloud** and complete Zephyr OAuth sign-in. Team and Enterprise administrators may need to make the connector available before members connect with their own accounts.

The bundled remote connector is `https://mcp.zephyr-cloud.io/sites/content/mcp`. Claude Code loads it from `.mcp.json`. No API keys or tokens belong in the plugin files or chat.

### Updating the connector name

Version 0.2.2 names the bundled connector **Zephyr Cloud**. The plugin and marketplace identifiers remain `zephyr-cloud`; the plugin's `displayName` does not set its connector's name.

An existing custom connector can retain the name saved when it was added. Updating the plugin does not rename that organization-level registration. If Claude offers to reuse an existing connection, its saved name may still appear. Once the separate connector directory listing is published with **Zephyr Cloud** branding, Claude can apply that branding to matching custom connector URLs. See [Claude's custom connector setup guide](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).

Claude Code namespaces the renamed bundled server as `plugin:zephyr-cloud:Zephyr Cloud` and normalizes its space in callable tool names to `_`. Existing permission rules or hook matchers that name `mcp__plugin_zephyr-cloud_zephyr-cloud__` need to use `mcp__plugin_zephyr-cloud_Zephyr_Cloud__` instead. See [plugin MCP server naming](https://code.claude.com/docs/en/mcp#use-mcp-servers-from-plugins).

## Try it

- “Make a simple coffee shop page and put it online with Zephyr Cloud.”
- “Publish this React dashboard artifact to Zephyr.”
- “Use my selected organization and remember it for this chat.”
- “Add an autumn-special banner and publish the update at the same live address.”
- “Show the previous builds and roll back production to the version I select.”
- In Claude Code: “Build this app and deploy it to Zephyr Cloud.”

Claude chooses readable names and generates the identifiers the connector needs. With several organizations and no saved choice, it asks which organization owns the site. An unqualified request to remember the organization saves this chat's preference and verifies it; project and account preferences require an explicit scope. Updates reuse the configured site and retain its ownership.

Claude can also share artifacts through its own artifact publishing. The plugin uses Zephyr when you ask for it, when you have made Zephyr your default host (“Make Zephyr my default host”), or when updating a site it already published. Installing the plugin does not change Claude's built-in behaviour by itself.

“Publish” includes upload and promotion to the stable production URL. “Preview only” returns an immutable build URL. Publishing creates a public site, so include only content intended for public access. Rollback serves a retained build without rebuilding. Publishing and rollout may briefly require edge propagation.

## What can be published

| Source | How | Notes |
| --- | --- | --- |
| HTML, React, Markdown, SVG or Mermaid artifact | `publish_artifact` (any Claude surface) | React artifacts use the libraries Claude's artifact runtime offers. Pages that call Claude-only APIs (`window.claude`, `window.storage`) are rejected until those calls are replaced |
| Hand-made multi-file static site | `publish_site_content` bundle | Up to 200 files, 25 MiB per file, within the 4 MiB MCP request |
| Web app project with a build | `deploy-app` skill (Claude Code only) | Runs the project's build and the pinned Zephyr CLI. Works for any size and stack |

Server-side rendering, APIs and databases are not hosted by these tools. No billing, purchases or subscription upgrades are exposed.

The skills check the exact uploaded build before promotion and verify the served page when fetching is available. A team's Claude network restrictions may prevent fetching `zephyrcloud.app`. In that case Claude reports the limitation, and the link can be checked in a browser. This plugin does not change network or permission settings. Installation makes the skills available but does not guarantee automatic provider selection. Explicit provider choices and existing hosting configurations take precedence.

## What the plugin runs

- **Remote connector:** the bundled connector runs no local code.
- **`deploy-app` (Claude Code only):** runs, in your shell and with your approval:
  - your project's own build script;
  - `zephyr-cli@1.7.0` (pinned), via `pnpm dlx` or `npx`, for `ze-cli doctor` and `ze-cli deploy`.

  The CLI uploads only the build output directory to Zephyr Cloud, using your Zephyr login, or in a non-interactive shell a personal token you export as `ZE_SECRET_TOKEN` (Zephyr **User settings → User tokens**). It reads your Git remote and `package.json` name to identify the app.
- **Published React and Mermaid pages:** these load pinned libraries from `esm.sh`, `cdn.tailwindcss.com` and `cdn.jsdelivr.net` in the visitor's browser.

## Data handling

The remote connector sends deployment content and requested site/organization identifiers to Zephyr Cloud using the connected user's OAuth authorization. The shared Zephyr publisher uses Zephyr's built-in Cloudflare infrastructure for static hosting. Published site assets are served publicly; account organization choices and generated conversation/project context keys must stay outside those assets.

Zephyr stores site configuration, requested organization defaults and publication/retry metadata for its publishing workflow. Builds are retained for inspection and rollback. Clearing a saved organization default removes that scoped preference; it does not remove a site or build. The plugin does not request Claude chat history or memories from the server and does not bundle local executables, hooks, credentials or account-test fixtures; `deploy-app` only invokes the pinned public Zephyr CLI from npm. Requests sent through Claude remain subject to Claude's own service terms and settings.

See [Zephyr Cloud's privacy policy](https://zephyr-cloud.io/privacy) and [terms of service](https://zephyr-cloud.io/terms), also linked in the main website's footer. For privacy, retention or account-support questions, contact [support@zephyr-cloud.io](mailto:support@zephyr-cloud.io).

## License

The plugin manifest declares a Proprietary license. Contact Zephyr Cloud for licensing questions.
