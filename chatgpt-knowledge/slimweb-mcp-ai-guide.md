# SlimWeb MCP AI Guide

This guide helps ChatGPT and other AI agents use SlimWeb MCP as a high-level website and ecommerce operating surface.

SlimWeb MCP tools perform concrete operations. This guide explains how to combine them safely for real user tasks.

## Core Principle

Use SlimWeb MCP as the source of truth for actions. Do not invent tools, storage paths, payment providers, promotion mechanics, or backend behavior. For broad requests, inspect current site state, plan the workflow, ask only for critical missing details, execute supported tools, verify, and summarize.

## Start Every Site Task

1. Check auth and available sites with SlimWeb MCP.
2. Select or confirm the target site when there is ambiguity.
3. Inspect current state before making changes that depend on existing pages, products, categories, navigation, coupons, articles, assets, payment/logistics settings, or themes.

## High-Level Workflows

### Theme and Page Design

Use theme tools for navbar, footer, online support, root CSS, style profile, and theme shell work.

Use page tools for homepage sections, landing pages, page bodies, and page-specific content.

Always include mobile, tablet, and desktop behavior. For page work, upload or reuse assets, update the page, then get a preview URL.

### Marketing Campaigns

A campaign may combine:

- Homepage promotion sections.
- Landing pages.
- Coupons or discount codes.
- Product/category highlights.
- Navigation entries.
- Articles.
- Uploaded campaign images.
- SEO copy.

Plan the offer, audience, dates, scope, and creative assets before writing. Do not advertise a coupon or discount as active until SlimWeb confirms it exists.

### Product and Catalog Work

For product publishing, inspect categories and existing products first. Upload images before product upsert. Assign categories intentionally. For batch import, inspect, validate, resolve errors, then commit.

For categories and navigation, read the existing tree before writing. If no parent is specified, root is the safe default. Generate semantic SVG icons when requested.

### Media Uploads

Prefer signed upload:

1. Create upload.
2. PUT bytes to the upload URL.
3. Commit upload.
4. Use the returned `media_path`.

Do not use fake URLs, local sandbox paths, or unresolved ChatGPT attachment paths as final content.

### External CSS and JavaScript

Use external CSS/JS only when the goal cannot be handled by normal SlimWeb tools or when the user explicitly wants a third-party integration. Check trust, privacy, performance, and responsive impact. Page-level code is safer than global code for page-specific effects.

### Commerce Settings

SlimWeb supported payment providers are ECPay, NewebPay, and LINE Pay.

SlimWeb supported logistics providers are ECPay logistics, NewebPay logistics, and HCT logistics.

Do not invent other providers. ECPay and NewebPay online card payments are mutually exclusive; LINE Pay can coexist with one online card provider.

## What To Report After Changes

End with:

- What was created.
- What was updated.
- What was left unchanged.
- What needs user confirmation.
- Preview or review links when available.
- Any unsupported request that was not executed.

## Knowledge File Map

For deeper guidance, use:

- `references/theme-page-workflows.md`
- `references/design-rwd.md`
- `references/marketing-campaigns.md`
- `references/catalog-navigation.md`
- `references/media-upload-flow.md`
- `references/external-assets.md`
- `references/commerce-settings.md`
- `references/tool-composition.md`
