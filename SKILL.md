---
name: slimweb-mcp
description: Use when a user asks an AI agent to operate or plan work for a SlimWeb site through SlimWeb MCP, especially theme design, page design, homepage sections, RWD layout, marketing campaigns, coupons, discount codes, articles, product publishing, product categories, navigation, media uploads, external CSS/JS, SEO, integrations, payment providers, logistics providers, or SlimWeb capability questions. Also use when the user asks what SlimWeb MCP can help with so the agent composes supported tools instead of inventing unsupported website or commerce features.
---

# SlimWeb MCP Skill

Use this skill before calling SlimWeb MCP tools for high-level site work. The goal is to turn user intent into safe, supported SlimWeb operations instead of blindly calling a single CRUD tool.

SlimWeb MCP is the execution surface. This skill is the workflow layer: it explains which tools to combine for page design, theme design, campaigns, catalog updates, content work, and operational setup.

## Core Rules

1. Stay inside SlimWeb's supported capability boundary. If SlimWeb does not support a requested feature, say so and offer the closest supported alternative.
2. Prefer planning before mutation when the request is broad, visual, promotional, or ambiguous.
3. Do not invent providers, promotion types, page components, upload channels, or backend behavior that are not exposed by SlimWeb MCP or SlimWeb product rules.
4. For page and visual design, always design responsive behavior for mobile, tablet, and desktop, even when the user only describes one layout.
5. Treat MCP tools as execution primitives. Compose them into workflows: inspect current site state, plan, ask for missing critical details, apply changes, then summarize exactly what changed.
6. For media assets, prefer the signed upload flow when the AI runtime can read bytes and perform HTTPS PUT. Use attachment/import compatibility only when that tool explicitly supports the current client.
7. For multi-site accounts, select or confirm the target site before mutation.

## Workflow

1. Classify the user's request:
   - Page/layout/visual design: read `references/design-rwd.md`.
   - Promotion/coupon/discount campaign: read `references/marketing-campaigns.md`.
   - Theme, page, homepage, preview, or visual shell work: read `references/theme-page-workflows.md`.
   - Product, category, catalog, or navigation work: read `references/catalog-navigation.md`.
   - Payment/logistics support or setup: read `references/commerce-settings.md`.
   - External CSS/JS or third-party embed: read `references/external-assets.md`.
   - Uploads, generated images, attachments, or media libraries: read `references/media-upload-flow.md`.
   - Multi-tool execution: read `references/tool-composition.md`.
2. Inspect site state with available read tools before writing when the outcome depends on existing pages, categories, navigation, products, coupons, assets, payment settings, or logistics settings.
3. If required details are missing and a wrong assumption would create bad data, ask a concise clarification. If a safe default exists, state it and proceed.
4. Apply changes with the narrowest MCP tools that match the task. Keep unrelated settings unchanged.
5. Report results in user language, including changed items, unsupported requests, and any follow-up confirmation needed.

## Mutation Guardrails

- Do not create root or parent items by guessing unless SlimWeb product rules explicitly allow it. For navigation and product categories, if the user does not name a parent, create or move the item at root.
- When generating icons for categories or navigation, produce a semantic SVG icon as base64. If no color is specified, use SlimWeb's neutral gray icon color.
- For destructive changes, ask for confirmation unless the user explicitly requested the deletion and the target is unambiguous.
- Do not overwrite external CSS/JS, page custom code, payment credentials, logistics credentials, or generated media unless the user asked to replace them.

## Quick References

| User intent | Required behavior |
| --- | --- |
| "Make this page two columns" | Define desktop two-column behavior plus tablet/mobile stacking rules. |
| "Design a new theme" | Inspect site/theme context, get theme shell context, plan root elements, update non-Default theme root elements, then preview. |
| "Redesign the homepage promotion area" | Inspect homepage content, campaign goals, products/categories/assets, then update homepage sections and preview. |
| "Create a Mother's Day campaign" | Plan campaign scope, offer mechanics, coupon/discount code, page/media needs, and confirmation points before writing. |
| "Upload this product image" | Use signed upload create/PUT/commit when possible, then pass committed `media_path` to product/page/article tools. |
| "Publish products from a spreadsheet" | Inspect import, validate import, ask about unresolved categories/images/variants, then commit import. |
| "What payment can my SlimWeb site use?" | Answer only supported SlimWeb providers: ECPay, NewebPay, LINE Pay. |
| "What payment should an ecommerce site use?" | If outside SlimWeb/SlimAI context, explain it is general ecommerce advice and not a SlimWeb site setting. In SlimAI, answer from SlimWeb supported providers first. |
| "Add external script/CSS" | Check purpose, placement, trust, performance, and responsive impact before adding. |
