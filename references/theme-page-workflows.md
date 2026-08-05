# Theme, Page, and Homepage Workflows

Use this when the user asks for theme design, page design, homepage updates, landing pages, visual sections, navbar/footer/floating-action changes, preview URLs, or design-system style changes.

## Available Tool Families

- Site and target selection: `slimweb_auth_status`, `slimweb_sites_list`, `slimweb_site_select`.
- Theme shell: `slimweb_themes_list`, `slimweb_themes_create_from_default`, `slimweb_theme_shell_get_context`, `slimweb_themes_update_root_elements`.
- Style memory: `slimweb_theme_style_profile_get`, `slimweb_theme_style_profile_upsert`, `slimweb_theme_style_profile_append_request`.
- Homepage/page content: `slimweb_pages_get_home_content`, `slimweb_pages_update_home_content`, `slimweb_pages_upsert`, `slimweb_pages_delete`.
- Preview: `slimweb_preview_get_page_url`.
- Supporting content/assets: article, product, category, navigation, upload, and external asset tools as needed.

## Theme Design Pattern

1. Follow the MCP site-selection rules and identify the target site.
2. Read themes with `slimweb_themes_list`.
3. If creating a new visual direction, create a non-Default theme with `slimweb_themes_create_from_default`.
4. Read context with `slimweb_theme_shell_get_context` and style history with `slimweb_theme_style_profile_get`.
5. Plan the fixed `navbar`, `floating_actions`, and `footer` slots plus root CSS, colors, typography, spacing, and responsive behavior.
6. Update root elements with `slimweb_themes_update_root_elements`.
7. Save the design rationale and constraints with style profile tools.
8. Get a preview URL and report what to inspect.

Do not treat `Default` as a theme-shell editing target. Default page content and custom theme shell/root elements are separate concepts.

Theme root slots are fixed; arbitrary user-defined HTML is allowed inside each slot. Before writing `navbar`, inspect the returned `website_type` and storefront action requirements. Unless `website_type=brand`, preserve working cart, registration, and login entries. Their visual treatment and responsive placement may closely follow a reference site, but their functions cannot be omitted. Add custom content only to the slot where the user explicitly requested it. Do not move data supplied for one placement into another slot; footer contact or social URLs do not become `floating_actions` without a separate request. For `floating_actions`, use links and modal content exactly as the user supplies it. Do not bind custom controls to existing contact fields, invent or require missing URLs, or reject an unusual control merely because it has no predefined platform behavior. A missing URL remains a plain control without another clarification round. Theme JavaScript and Theme-level `enabled_libraries` are not supported.

## Page Design Pattern

1. Inspect the target page or homepage content.
2. Inspect related products, categories, articles, navigation, and assets if the design depends on them.
3. Plan desktop, tablet, and mobile behavior before writing.
4. Upload or reuse assets.
5. Update page/home content with the narrowest page tool.
6. Get a preview URL.
7. Summarize changed sections and responsive behavior.

Page content may use inline JavaScript and the supported page-level `enabled_libraries`: `animate_css`, `aos`, `swiper`, `gsap`, `scrolltrigger`, and `scrollsmoother`. Do not add CDN tags manually.

## Homepage Promotion Pattern

For homepage campaign sections, combine:

- `slimweb_pages_get_home_content`.
- Product/category tools for promoted items.
- Coupon/discount tools if the offer needs a real redeemable mechanism.
- Upload tools for campaign media.
- Navigation tools if the campaign needs a menu entry.
- `slimweb_pages_update_home_content` after planning the section.

Never advertise an active discount in page copy until the discount/coupon tool confirms it exists.

## Design Rules

- Every layout must include mobile, tablet, and desktop behavior.
- Prefer existing assets when appropriate; generate/upload new assets only when the task needs them.
- External CSS/JS should support, not replace, SlimWeb's supported content tools.
- Preview URLs are part of the workflow, not an afterthought.
