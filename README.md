# SlimWeb AI Skill and Knowledge Pack

This repository maintains a thin client bootstrap and server-delivered operating guides for SlimWeb MCP.

**Install MCP + Skill together:** [Unified Plugin installation guide](INSTALL.md). It includes copy-paste AI instructions, target-matched packages, a generator for a supplied complete MCP URL, and the original separate MCP + Skill fallback. Select a package by matching its manifest URL exactly to the website-provided URL; do not infer a target from a website name or default endpoint. These are self-managed plugin packages, not a claim of publication in an official public marketplace.

SlimWeb MCP exposes concrete tools. The deployed guides explain how an AI should combine those tools when a user asks for outcomes such as theme design, page design, marketing campaigns, coupons, discount codes, product publishing, navigation, product categories, external CSS/JS, articles, and media uploads.

## Who This Is For

- ChatGPT / Custom GPT builders: upload the Markdown files under `chatgpt-knowledge/` as Knowledge or Project files.
- Codex and other skill-capable agents: install this repository or copy the skill folder so `SKILL.md` is available to the agent.
- MCP implementers: keep the hard safety rules in MCP tool descriptions and backend validation; this repo is workflow guidance, not a substitute for server-side validation.

## Repository Layout

- `SKILL.md` - Stable thin bootstrap: read the deployed guide index, overview and relevant topics.
- `guides/overview.md` - Full operating overview, maintained as server guidance.
- `references/` - Canonical topic guides exported to the MCP service.
- `scripts/export-guides.py` - Deterministic Markdown + manifest export for server deployment.
- `chatgpt-knowledge/` - Consolidated files intended for Custom GPT Knowledge or ChatGPT Project files.

## What This Pack Adds Beyond MCP Tool Descriptions

MCP tool descriptions explain individual tools. This pack explains task composition:

- For theme/page design: which read tools to call first, how to plan responsive behavior, when to use theme shell tools, page tools, preview URLs, uploads, and external CSS/JS.
- For marketing campaigns: how to combine homepage sections, landing pages, articles, coupons, discount codes, product/category highlights, navigation, and media assets.
- For catalog work: how to combine product, category, navigation, image upload, and preview tools.
- For operational setup: how to use payment, logistics, SEO, integration, settings, and admin tools without inventing unsupported providers or fields.

## Thin Plugin and Current Guidance

Upgrade older full-Skill packages once to **1.1.0**. New Plugins contain only `skills/slimweb-mcp/SKILL.md`, not bundled reference documents. At each new task, the bootstrap calls `slimweb_guides_get` for `index`, then reads `overview` and relevant topics from the deployed service. Routine guide updates take effect after an MCP service deployment without reinstalling the Plugin. Bootstrap changes still require an ordinary package upgrade.

This does not automatically update an AI client or Plugin binary. New tools may require a client catalog refresh, reconnection or restart. If a required guide cannot be read, the AI stops site mutations, explains the failure and retries after the connection is repaired; it does not fall back to stale local guidance. Current tool schemas, site authentication, permissions, site selection and user confirmation remain authoritative.

## Legacy ChatGPT Knowledge Usage

These static Knowledge files are retained for existing integrations and are not the thin Plugin operating path. They do not update themselves or replace live guidance. For a Custom GPT that needs static Knowledge, upload:

- `chatgpt-knowledge/slimweb-mcp-ai-guide.md`
- Any individual files from `references/` that you want the GPT to search directly.

Recommended Custom GPT instruction:

```text
You are a SlimWeb assistant. Use SlimWeb MCP tools when available. Before making broad site, page, catalog, or marketing changes, consult the uploaded SlimWeb MCP knowledge and plan the workflow. Do not invent tools, providers, promotion types, upload paths, or internal storage behavior. When a task requires changes, inspect current SlimWeb state first, then apply the narrowest supported MCP tools.
```

Knowledge files help ChatGPT reason about SlimWeb. They do not by themselves connect ChatGPT to SlimWeb MCP; the GPT still needs an Action/App/MCP connection or the user must use a client where SlimWeb MCP is connected.

## Codex Plugin Compatibility

Use package **1.1.0 or later** for the thin architecture. Its portable `mcp.json` contains `type: streamable-http` and the exact MCP URL; OAuth uses host-managed discovery and DCR. Version 1.0.0's per-server `extensions` field is rejected by the observed Codex 0.167 parser and prevented its bundled MCP from loading, even though the Plugin and Skill appeared installed. See [installation and update steps](INSTALL.md#codex-安裝與更新).

ChatGPT users should enter Codex mode and grant full access before giving the automatic installation instructions to AI. Sign in and grant Google consent yourself. Verify by successfully calling `slimweb_sites_list`; an installed Plugin or Skill alone is insufficient. Manual **Settings → Plugins → Add → Add MCP server**, with **SlimWeb**, **Streamable HTTP**, and the exact website MCP URL, connects MCP only. Complete Skill installation separately if you use that route.

## Codex Skill Usage

For a separate Skill installation, copy only `SKILL.md` into a `slimweb-mcp/` directory (do not install the full source repository as an operating fallback), for example:

```text
~/.codex/skills/slimweb-mcp/
```

Codex will use `SKILL.md` when the task matches SlimWeb MCP operations.

## Maintenance Rule

When SlimWeb MCP adds or removes tools, update `guides/overview.md` and the relevant `references/` at the workflow level. Keep single-tool schema details in the MCP repo; keep multi-tool task guidance here.

## Capability discovery and maintenance

`references/capability-map.md` is the maintained capability map, merchant-language routing, pre-refusal checklist and full Merchant MCP tool index. `references/marketing-campaigns.md` describes promotion composition, including quantity discounts, add-on products and threshold gifts. Current tools/list, schemas, site permissions and deployment readiness remain authoritative.

The embedded website AI retains full overview guidance; changing the thin client bootstrap must not strip its operating instructions. The legacy capability resource and static Knowledge remain available for existing consumers, while the guide tool serves the new canonical topic bundle.

Export and deploy current guidance:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/export-guides.py --output /absolute/path/to/new-guide-export
```

The output path must not exist. The exporter reads only `guides/overview.md` and `references/*.md`, rejects symlink sources and invalid topic paths, and writes Markdown files plus `manifest.json`. Its schema is `{schema_version: 1, guide_version: "sha256:<hash>", topics: [{topic, file, sha256, bytes}]}`. Topics are sorted; guide version hashes their canonical JSON metadata, and each content hash covers exact UTF-8 bytes. Copy the export into the MCP service's guide bundle and publish the service; source synchronization alone does not update running clients.

For explicitly selected legacy consumers, the existing sync command is still available:

```sh
node scripts/sync-capability-guide.mjs --core-root /path/to/core --webless-root /path/to/web --standalone-root /path/to/standalone
```

It uses `guides/overview.md` for embedded website AI. `--installed-root /path/to/skill` now updates only the thin `SKILL.md`; it neither copies old reference/Knowledge files nor deletes user files. Generated Plugin refresh removes only unchanged canonical reference copies from old full packages and refuses to discard modified or unknown reference files. Verify server deployment and a real guide-tool call after synchronization.
