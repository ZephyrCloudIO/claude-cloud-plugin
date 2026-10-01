# Claude launch

Checked 2026-10-01. This repository distributes the plugin; it does not contain or deploy the MCP backend.

## Submission details

| Field | Value |
| --- | --- |
| Repository | `https://github.com/ZephyrCloudIO/claude-cloud-plugin` |
| Plugin folder | `plugins/zephyr-cloud` |
| Plugin name / version | `zephyr-cloud` / `0.2.1` |
| Marketplace | `zephyr-cloud` |
| Connector URL | `https://mcp.zephyr-cloud.io/sites/content/mcp` |
| Public setup documentation after publishing source | `https://github.com/ZephyrCloudIO/claude-cloud-plugin/blob/main/plugins/zephyr-cloud/README.md` |
| Privacy policy | `https://zephyr-cloud.io/privacy` |
| Support | `support@zephyr-cloud.io` |
| Icon | `plugins/zephyr-cloud/assets/zephyr-cloud-icon.png` |
| License metadata | `Proprietary` in the plugin manifest |

Submit from the Zephyr Cloud Claude organization that should own both listings. Team/Enterprise submissions require an Owner or the applicable directory permission. Submit the remote server as an MCP connector and the plugin bundle separately, using the same connector URL.

## Verified

- Native Claude plugin and marketplace structure validate locally.
- The deployment skill and portable connector installed in Claude chat; existing Zephyr OAuth worked.
- A fresh coffee-shop prompt automatically loaded the skill and generated a page. Claude still asked public Zephyr versus private artifact, so installation alone does not guarantee provider routing.
- An organization answer containing “remember this organization for this chat” saved the preference and read it back in the same turn.
- Claude published the generated page and promoted its exact build to a stable production URL. A short update reused that site and URL without another host or organization question.
- The updated immutable and production pages both returned HTTP 200, identical 9,303-byte HTML and the requested autumn-special banner. Chrome rendered the live page. The original build remained available.
- These tests used the shared production MCP service, which reported v0.5.1 for the update verification. Its backend suite passed 85 tests, type checking, lint, workerd upload checks and a deployment dry-run; those checks belong to the separate backend repository.
- Signed-in Claude Code also completed six real MCP calls through a local Worker with fake downstream APIs. That is account/tool integration evidence, not a production Claude Code or Cowork publishing test.

The deployment skill copied into this repository is the tested v0.2.0 skill. Version 0.2.1 adds the portal-required 512px PNG icon and explicit privacy-policy metadata. These packaging changes do not change its deployment workflow.

## Remaining launch steps

1. Source publication uses this repository's `main` branch with **Public** visibility, authorized on 2026-10-01. The repository was empty and Internal when preparation started. Publishing the source and marketplace does not submit or publish either Claude directory listing; the backend repository remains separate.
2. Run the directory portal's Validate against the committed plugin folder. Local `claude plugin validate` checks syntax and schema, not every directory requirement or name availability.
3. Review the shared server's write-tool annotations against Claude's connector checklist. In v0.5.1, `configure_site`, `set_organization_default` and `publish_site_content` declare `destructiveHint: false`; the checklist requests `true` for modifying tools. `promote_build` already declares `true`. This is a backend metadata follow-up, not a publisher rewrite; this repository cannot change the hosted tools.
4. Prepare a dedicated populated reviewer account and setup instructions. Do not use production operator credentials or commit reviewer credentials. Provide them only through the submission portal after authorization.
5. Confirm the privacy-policy answers cover deployment content, OAuth, persisted defaults/configuration, retained builds, and Cloudflare hosting. Use the README as the public setup documentation; confirm the listing icon is accepted by the portal.
6. Complete portal data-handling/contact fields, directory terms and policy acknowledgements, then submit both listings for review. Terms acceptance and final public publication require the appropriate account owner's approval.
7. Publish the passing/approved plugin version in the portal. Choose the tracked release branch/tag and update settings intentionally; directory review timing is not fixed.

Recommended final smoke tests: a fresh user's install/sign-in, default reuse for a second new site, rollback, and every advertised Claude surface. Cowork and production Claude Code publishing have not been verified. Claude chat's team sandbox could not fetch the public hosting domain during testing; independent browser/HTTP checks verified it without changing team network policy.

## Primary references

- [Plugin structure and testing](https://claude.com/docs/plugins/build)
- [Plugin pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist)
- [Plugin submission and public-source requirement](https://claude.com/docs/plugins/submit)
- [Connector review criteria](https://claude.com/docs/connectors/building/review-criteria)
- [Connector submission materials](https://claude.com/docs/connectors/building/submission)
- [Directory submissions](https://claude.com/docs/directory/publish)
- [Marketplace structure](https://code.claude.com/docs/en/plugin-marketplaces)
