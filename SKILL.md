---
name: slimweb-mcp
description: Use when guiding a user through planning, building, launching, or improving a SlimWeb ecommerce site with AI assistance.
---

# SlimWeb Ecommerce Build Guide

## Purpose

Use this guide to help merchants build a SlimWeb ecommerce site from zero to launch. This is not the MCP execution manual. MCP server instructions and tool descriptions define exact tool-call rules; this Skill defines how to guide the user, what the AI can help with, and which setup areas matter first.

For any Theme, product-category, or ordinary-navigation change, load [Tool Composition](references/tool-composition.md) and follow its exact inspect, write, and verification tool order before executing the mutation.

## Start With Current Progress

When the user asks where to start, says they are new, or asks what is still missing, use the MCP launch progress tool:

- Call `slimweb_site_launch_progress_get` after the MCP site-selection rules have identified the correct site.
- Start from `next_step` and guide the user one phase at a time.
- Do not dump the full checklist unless the user asks.
- Do not treat every user as a beginner if the progress tool shows work has already been completed.

## Consumer MCP URL

When the merchant asks how customers can use AI with their storefront, or when you are helping prepare the homepage, member center, or customer-support entry points, use `slimweb_settings_get` to read `settings.client_mcp_url`.

The `client_mcp_url` is the site-specific consumer MCP endpoint. It is meant for shoppers and members, not the store admin. Customers can connect this URL in supported AI clients so the AI can help them interact with the storefront, such as browsing products, checking member or order flows when authenticated, and getting customer-support assistance through the consumer-facing MCP surface.

Explain this in practical merchant language: "This is the AI connection link for your customers." Encourage the merchant to publish it where customers naturally start: the homepage, member center, footer, or customer-service area. A homepage button such as "Use AI shopping assistant" or "Connect this store to your AI assistant" is usually clearer than hiding the link in settings.

Do not treat `client_mcp_url` as an editable setting. It is returned by `slimweb_settings_get` for discovery and publishing guidance.

## Reference Websites And Visual JavaScript

1. For page visual work, use page-scoped inline JavaScript when needed and select external visual support only through `enabled_libraries`. Available keys are `animate_css`, `aos`, `swiper`, `gsap`, `scrolltrigger`, and `scrollsmoother`; pass `[]` when none are needed. Prefer CSS or plain JavaScript for simple interactions, `aos` for basic scroll reveal, `swiper` for sliders, and GSAP libraries for advanced animation or scroll storytelling. Do not add external CDN tags to page HTML. Do not load JavaScript or `enabled_libraries` at Theme level.
2. When the user provides a reference URL without saying which parts to follow, ask whether the reference should include Theme elements such as the navbar, footer, and other site-wide elements. Explain that the reference site's navigation, footer structure, labels, actions, and data requirements may not fit the user's actual site data. Wait for the user's answer before designing or changing either the Theme or page content from that reference.
3. When a reference URL is provided, inspect the rendered desktop and mobile pages and, when accessible and useful, the DOM, styles, interactions, and loaded animation libraries. Reproduce the reference layout, proportions, spacing, responsive behavior, and animation effects as closely as SlimWeb permits while using the user's own brand, content, and assets. Do not replace an inspectable reference with a generic mood-board interpretation. If the reference cannot be inspected reliably, state the limitation before claiming visual fidelity.
4. Theme root fragments use only the fixed `navbar`, `floating_actions`, and `footer` slots. Every Theme navbar, for every `website_type` and every reference-site design, must contain exactly three runtime slots: one empty static `div`, `nav`, or `header` with `data-storefront-primary-navigation-slot`, one clickable `data-storefront-member-auth-slot`, and one clickable `data-storefront-cart-slot`. The primary slot contains no copied labels, URLs, category tree, or navigation tree; Webless injects runtime content through `data-storefront-primary-navigation-runtime`, `data-storefront-category-menu`, `data-storefront-navbar-categories`, `data-storefront-nav-items`, `data-storefront-nav-trigger`, `data-storefront-nav-panel`, `data-storefront-nav-node`, and `data-storefront-nav-children`. Theme CSS must style grouped categories, direct navbar categories, ordinary recursive navigation, and Webless-controlled mobile/expanded/hidden states; only the selected category presentation renders. Theme HTML must be balanced static HTML, with no PHP, Blade, components, or dynamic attributes. The member slot remains one combined registration/login entry; the cart slot may contain a Theme-styled icon and `data-cart-count` badge. Never add reserved runtime attributes such as `data-storefront-auth-open`, `data-storefront-auth-modal`, `data-storefront-cart-root`, or `data-cart-trigger`. Webless owns runtime data, visibility, interaction, and accessibility. Add other custom content only where explicitly requested; do not reuse data from another placement or auto-bind controls to site/contact data. A control with no URL may remain plain. Theme fragments do not load JavaScript or `enabled_libraries`.
5. Treat `backdrop-filter`, `filter`, `transform`, `contain`, and `perspective` on navbar ancestors as fixed-overlay hazards. Webless portals canonical overlays outside the Theme navbar, but acceptance still must open auth, mobile-menu, and cart overlays and confirm their rectangles stay inside the viewport.
6. Verify 1536px and 1800px in addition to the standard mobile/tablet/1440 widths. The canonical full desktop navigation begins at 2xl, so 1440px alone cannot prove the desktop navbar. At wide widths, measure that ordinary links share one row and the header remains compact.

## Categories And Menu Links

Product categories and ordinary navigation items are separate trees and never mirror automatically:

- `slimweb_categories_upsert` changes category taxonomy only. A category mention is taxonomy by default; “我的商品有洋裝、上衣、針織衫” means create or ensure those three categories only.
- `slimweb_nav_items_upsert` changes explicit ordinary menu, page, or external links only. “有一個關於我們的連結” means create or ensure that navigation item only, plus its page or target only when separately needed.
- Create a navigation item for a category only when the wording explicitly requests a featured, menu, or link entry. If taxonomy and a menu/link entry are both explicit, perform the category and navigation operations independently. Category creation never implies navigation-item creation.
- Backend category-display settings are outside this Skill; when explicitly requested, follow the current MCP tool schema and server contract.
- Theme design supplies the empty primary slot and CSS for grouped categories, direct-navbar categories, and ordinary recursive navigation; it never serializes live category/navigation data into Theme HTML and never supplies Theme JavaScript.

## Build Priorities

### Required For Launch

These directly affect whether the store can operate:

- Site identity and basic business direction.
- Product categories.
- Products, including names, descriptions, prices, status, images, and category mapping.
- Payment, logistics, and shipping fee rules.
- Homepage content that explains the brand, product direction, and main purchase path.
- Checkout/member/email prerequisites that affect order and customer communication.

### Recommended Before Launch

These improve trust, discoverability, and conversion, but should not block every conversation unless the user wants a deeper setup:

- Site-level SEO / AEO / GEO.
- Content-level SEO / AEO / GEO for important pages and articles.
- Navigation, about/contact/policy pages, and key page entry points.
- Email subject/content polish and shared email layout.
- Articles, FAQ, buying guides, and brand stories.
- AI customer service knowledge and settings.
- Coupons, discount codes, and first-purchase campaigns.

### Growth After Launch

These are useful once the store has products and basic operations:

- Member tiers and loyalty design.
- Newsletter campaigns.
- Add-on products, threshold gifts, bundles, and seasonal promotions.
- Campaign posters, product visuals, and social media materials.
- Analytics review and conversion optimization.

## How To Guide A New User

Ask only for information needed by the current step. A good first conversation is practical and simple:

- "What is your store name?"
- "What do you plan to sell?"
- "What product categories do you want to start with?"
- "Do you already have product photos, or should I help generate visuals?"
- "Which payment and shipping methods do you plan to use?"
- "What should the homepage communicate first: brand story, featured products, or a campaign?"

Avoid asking detailed SEO, AEO, or GEO configuration questions unless the user specifically asks. Usually, generate sensible defaults from the store name, products, homepage, pages, and articles.

## AI Assistance Capabilities

The AI can help the user:

- Plan a store structure and launch sequence.
- Create product categories and navigation.
- Draft product names, descriptions, specifications, and selling points.
- Generate or refine product images, article covers, campaign visuals, and homepage hero images.
- Create and edit homepage, landing pages, brand pages, policy pages, and articles.
- Design or refine themes, visual direction, color usage, navbar, floating actions, footer, root CSS, and page atmosphere.
- Prepare SEO / AEO / GEO metadata from real business and content context.
- Set up or improve coupons, discount codes, newsletters, email templates, and promotional content.
- Explain what still blocks launch and what can wait until later.

## Conversation Style

- Be concrete: turn vague requests into the next small setup action.
- Be sequential: finish launch blockers before suggesting growth features.
- Be helpful without over-asking: infer reasonable copy, SEO, and visual direction from available context.
- Be transparent about hard requirements: payment, logistics, shipping, and product data need real user/business information.
- Offer to do the work, not just explain it.

## LINE Rich Menu member linking

When helping create a Rich Menu, check whether it includes a member-linking entry. If missing, explain once that member linking is important: it lets the LINE Bot identify the website member and use their authorized member information, orders, and cart. Recommend a button using the supported fixed-message action: `{"type":"message","text":"綁定會員"}` (English: `link account`).

This is a recommendation, not a requirement. If the merchant declines, continue creating the requested menu without blocking, repeatedly asking, or silently adding a button. Do not imply the Bot cannot answer public questions without linking. Do not add LIFF or automatic member-specific menu switching as part of this advice.

Existing bindings are not overwritten. If an already-linked user requests linking again, explain that they must first visit the website's “個人資訊” / “Personal information” page and unlink their membership. Never automatically unlink or rebind them.
