# Tool Composition for SlimWeb MCP

Use this reference when a user asks for an outcome that spans multiple SlimWeb MCP tools.

## Composition Principle

SlimWeb MCP tools are execution primitives. High-level user requests should be decomposed into inspect, plan, apply, and report steps.

## General Pattern

1. Inspect: read current site state with available list/get tools.
2. Plan: map the request to supported SlimWeb operations.
3. Clarify: ask only for missing details that would change the data materially.
4. Execute: call write tools in a safe order.
5. Verify: re-read important state when tools are available.
6. Report: summarize created/updated items and unsupported parts.

## Common High-Level Requests

### Theme/page/homepage work

- Read theme/page state first.
- Use style profile tools to preserve high-level visual direction and avoid repeating the same user preference discovery.
- Use upload tools before referencing new media in page/theme content.
- Get preview URLs after page/theme mutations.

### Product/category/navigation work

- Inspect categories and navigation first.
- If no parent is specified for a new category or navigation item, create it at root.
- Generate semantic SVG icons as base64 when creating or updating category/navigation icons.
- Use the neutral gray icon color when the user does not specify a color.

### Page/visual design work

- Inspect existing page/theme/asset state where available.
- Plan desktop, tablet, and mobile behavior.
- Use existing assets before generating or uploading new assets unless the user asks for new visuals.
- Keep external CSS/JS scoped and responsive.

### Campaign work

- Plan campaign mechanics before creating coupons, pages, assets, or navigation entries.
- Confirm discount value, validity period, and scope when missing.
- Apply coupon/discount changes before updating page or navigation copy that advertises the offer.
- Prefer a coherent small set of campaign assets over updating unrelated site areas.

### Payment/logistics work

- Read current provider state first.
- Only use supported providers.
- Enforce online card exclusivity between ECPay and NewebPay; LINE Pay is exempt.
- Mask credentials in responses.

## Reporting Pattern

End with:

- What was created.
- What was updated.
- What was left unchanged.
- What still needs user confirmation.
- Any unsupported request that was not executed.
