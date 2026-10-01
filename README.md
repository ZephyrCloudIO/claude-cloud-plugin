# Zephyr Cloud for Claude

Create, publish, update and roll back static sites from Claude using your own Zephyr Cloud account. This repository distributes the native Claude plugin and its marketplace; the hosted MCP service is maintained separately.

See the [plugin's setup and usage guide](plugins/zephyr-cloud/README.md) for installation, examples, content limits and data handling. The [launch checklist](docs/launch.md) records verification and the remaining public directory steps.

## Install from this repository

In Claude chat or Cowork, open **Customize > Plugins > Add > Add marketplace**, enter `https://github.com/ZephyrCloudIO/claude-cloud-plugin`, and install **Zephyr Cloud**. Connect its bundled connector separately with your Zephyr login. A repository that is still Internal requires repository access; public availability begins after it is made Public.

In Claude Code:

```sh
claude plugin marketplace add ZephyrCloudIO/claude-cloud-plugin
claude plugin install zephyr-cloud@zephyr-cloud
```

For development without changing your installed plugins:

```sh
claude --plugin-dir ./plugins/zephyr-cloud
```

## Validate and package

```sh
claude plugin validate plugins/zephyr-cloud
claude plugin validate .claude-plugin/marketplace.json
python3 scripts/package-plugin.py
```

The ZIP at `dist/zephyr-cloud-claude.zip` contains only the plugin manifest, connector declaration, deployment skill, README and icon. Upload it through **Customize > Plugins > Add > Upload plugin** for private testing. The ZIP is not a public directory submission; that submission uses this GitHub repository and plugin path `plugins/zephyr-cloud`.
