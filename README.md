# SlimWeb MCP Skill

This repository contains an agent skill for using SlimWeb MCP tools as higher-level website and commerce workflows.

The MCP server exposes concrete tools. This skill explains how an AI agent should combine those tools when a user asks for outcomes such as a marketing campaign, page redesign, responsive layout, product category update, payment setup, logistics setup, or external asset integration.

## Files

- `SKILL.md` - Skill entrypoint and compact workflow rules.
- `references/design-rwd.md` - Responsive page and visual design guardrails.
- `references/marketing-campaigns.md` - Promotion, coupon, discount-code, and campaign planning workflow.
- `references/commerce-settings.md` - Supported payment/logistics boundaries and setup rules.
- `references/external-assets.md` - External CSS/JS usage rules.
- `references/tool-composition.md` - How to compose low-level SlimWeb MCP tools into higher-level tasks.

## Installation

Install or copy this folder into the AI client's skill directory when that client supports skills. MCP clients that only connect to the SlimWeb MCP server will not automatically read this skill, so hard safety rules should also remain in MCP tool descriptions, schemas, and backend validation.

