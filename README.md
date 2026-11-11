# SlimWeb AI Skill and Knowledge Pack

This repository teaches AI agents how to use SlimWeb MCP as a higher-level website and ecommerce operating surface.

SlimWeb MCP exposes concrete tools. This pack explains how an AI should combine those tools when a user asks for outcomes such as theme design, page design, marketing campaigns, coupons, discount codes, product publishing, navigation, product categories, external CSS/JS, articles, and media uploads.

## Who This Is For

- ChatGPT / Custom GPT builders: upload the Markdown files under `chatgpt-knowledge/` as Knowledge or Project files.
- Codex and other skill-capable agents: install this repository or copy the skill folder so `SKILL.md` is available to the agent.
- MCP implementers: keep the hard safety rules in MCP tool descriptions and backend validation; this repo is workflow guidance, not a substitute for server-side validation.

## Repository Layout

- `SKILL.md` - Codex skill entrypoint and compact routing rules.
- `references/` - Focused workflow references loaded only when the task needs them.
- `chatgpt-knowledge/` - Consolidated files intended for Custom GPT Knowledge or ChatGPT Project files.

## What This Pack Adds Beyond MCP Tool Descriptions

MCP tool descriptions explain individual tools. This pack explains task composition:

- For theme/page design: which read tools to call first, how to plan responsive behavior, when to use theme shell tools, page tools, preview URLs, uploads, and external CSS/JS.
- For marketing campaigns: how to combine homepage sections, landing pages, articles, coupons, discount codes, product/category highlights, navigation, and media assets.
- For catalog work: how to combine product, category, navigation, image upload, and preview tools.
- For operational setup: how to use payment, logistics, SEO, integration, settings, and admin tools without inventing unsupported providers or fields.

## ChatGPT Knowledge Usage

For a Custom GPT, upload:

- `chatgpt-knowledge/slimweb-mcp-ai-guide.md`
- Any individual files from `references/` that you want the GPT to search directly.

Recommended Custom GPT instruction:

```text
You are a SlimWeb assistant. Use SlimWeb MCP tools when available. Before making broad site, page, catalog, or marketing changes, consult the uploaded SlimWeb MCP knowledge and plan the workflow. Do not invent tools, providers, promotion types, upload paths, or internal storage behavior. When a task requires changes, inspect current SlimWeb state first, then apply the narrowest supported MCP tools.
```

Knowledge files help ChatGPT reason about SlimWeb. They do not by themselves connect ChatGPT to SlimWeb MCP; the GPT still needs an Action/App/MCP connection or the user must use a client where SlimWeb MCP is connected.

## Codex Skill Usage

Install this repo as a Codex skill, or copy the folder into:

```text
~/.codex/skills/slimweb-mcp/
```

Codex will use `SKILL.md` when the task matches SlimWeb MCP operations.

## Maintenance Rule

When SlimWeb MCP adds or removes tools, update this pack at the workflow level. Keep single-tool schema details in the MCP repo; keep multi-tool task guidance here.

## Capability discovery and maintenance

`references/capability-map.md` is the maintained capability map, merchant-language routing, pre-refusal checklist and full Merchant MCP tool index. `references/marketing-campaigns.md` describes promotion composition, including quantity discounts, add-on products and threshold gifts. Current tools/list, schemas, site permissions and deployment readiness remain authoritative.

The ChatGPT Knowledge file and embedded website Skill include these references inline so uploaded/downloaded copies are self-contained. The shared MCP Core packages the same capability map as `src/merchant-capabilities.md`, exposes it at `slimweb://guides/merchant-capabilities`, and includes compact discovery rules in initialize, server/discover and service instructions.

After editing the canonical references, run (pass only consumer directories available on your machine):

```sh
node scripts/sync-capability-guide.mjs --core-root ../SlimWeb-MCP-Core --webless-root ../webless --standalone-root ../SlimWeb-Standalone --installed-root ~/.codex/skills/slimweb-mcp
node scripts/sync-capability-guide.mjs --check --core-root ../SlimWeb-MCP-Core --webless-root ../webless --standalone-root ../SlimWeb-Standalone --installed-root ~/.codex/skills/slimweb-mcp
```

Keep the complete index aligned with Core tools/list and run Core protocol tests plus merchant scenarios. Source synchronization does not publish GitHub updates or deploy running MCP services; consumers pinned to a Core release need an updated release/deployment to serve the new handshake instructions.
