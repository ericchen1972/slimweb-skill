# Marketing Campaigns and Promotions

Use this when the user asks for a campaign, sale, coupon, discount code, seasonal promotion, launch offer, membership offer, free shipping event, product bundle, or landing-page promotion.

## Planning Before Writing

Broad promotion requests should start with a plan, not immediate mutation. A good campaign plan includes:

- Goal: revenue, lead capture, clearance, new product launch, retention, membership growth.
- Audience: all visitors, members, returning customers, specific product/category buyers.
- Offer: percent off, fixed discount, threshold discount, discount code, coupon, free shipping, bundle, gift, or content-only promotion.
- Scope: whole site, category, product list, member segment, time window.
- Creative assets: banner, product image, social image, article, landing section, navigation entry.
- Execution tools: coupon/discount tools, product/category tools, page tools, media tools, navigation tools.
- Confirmation points: dates, budget, discount amount, eligible products, exclusions.

## Safe Defaults

Use safe defaults only when they will not create misleading or expensive data:

- If campaign dates are missing, create a draft plan or ask before enabling.
- If discount value is missing, ask.
- If applicable products/categories are missing, ask or make the campaign site-wide only if the user clearly implies it.
- If usage limits are missing, propose reasonable defaults but confirm before enabling.

## Tool Composition Pattern

1. Inspect current products, categories, pages, coupons, discount codes, and assets when tools exist.
2. Draft the campaign plan in plain language.
3. Ask for missing critical fields.
4. Create or update coupons/discount codes.
5. Create or update campaign page sections, banners, article content, navigation items, or product/category highlights.
6. Return the exact created items and how the user can review them.

## Useful Tool Families

- Homepage/page promotion: `slimweb_pages_get_home_content`, `slimweb_pages_update_home_content`, `slimweb_pages_upsert`.
- Coupons: `slimweb_coupon_templates_list`, `slimweb_coupon_templates_upsert`, `slimweb_members_coupons_issue`.
- Products/categories: product and category list/get/upsert tools.
- Articles: `slimweb_articles_list`, `slimweb_articles_upsert`.
- Navigation: `slimweb_nav_items_list`, `slimweb_nav_items_upsert`.
- Media: upload tools and asset tools.
- Preview: `slimweb_preview_get_page_url`.

## Campaign Building Blocks

- Homepage hero or promotion band.
- Landing page for the campaign.
- Product/category collection.
- Coupon template for member-issued coupons.
- Discount code for code-based offers.
- Article for content marketing or SEO.
- Navigation entry linking to the campaign.
- Uploaded images for banners, cards, and social-style visuals.

Match the building blocks to the user's goal; do not create every possible asset by default.

## Promotion Boundaries

- Do not invent unsupported promotion mechanics.
- Do not claim a discount is active unless the tool confirms it was created or enabled.
- Do not modify product prices directly when a coupon/discount-code tool is the better fit.
- Do not create a campaign that conflicts with user-stated exclusions.

## Example Interpretations

| User says | Agent should do |
| --- | --- |
| "Make a Mother's Day campaign" | Plan audience, offer, page/banner/coupon needs, then ask for discount/date if missing. |
| "Create 88% off code MOM88" | Create or update a discount code if supported; confirm scope/date if missing. |
| "Full-site anniversary sale next week" | Ask or infer exact date range from locale only when safe; define campaign assets and coupon rules. |
| "Promote men's clothing" | Inspect product category, create/update campaign content and optional coupon scoped to that category. |
