# SlimWeb Ecommerce Build Guide

## Purpose

Use this guide to help merchants build a SlimWeb ecommerce site from zero to launch. This is not the MCP execution manual. MCP server instructions and tool descriptions define exact tool-call rules; this guide defines how to guide the user, what the AI can help with, and which setup areas matter first.

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
4. Theme root fragments use only the fixed `navbar`, `floating_actions`, and `footer` areas. Every Theme navbar needs one empty primary-navigation position, one clickable combined registration/login position, and one clickable cart position. The Theme designs these positions and all category/menu layouts, but does not copy current category names, menu labels, or links into its HTML. SlimWeb fills those in and controls mobile opening, keyboard/accessibility behavior, signed-in member state, and cart behavior. The Theme HTML stays static and balanced; it contains no PHP, Blade, components, dynamic attributes, or Theme JavaScript. Continue to preserve the current member/cart reserved-attribute rules. Add custom content only in the area the merchant requested, and do not reuse footer/page data as floating actions without a separate request.
5. Navbar effects such as `backdrop-filter`, `filter`, `transform`, `contain`, and `perspective` can change how fixed descendants are positioned. Open the actual member-login, mobile-menu, and cart overlays after Theme changes and confirm they remain bounded to the browser viewport.
6. Test 1536px and 1800px as well as mobile, tablet, 1024px, and 1440px. SlimWeb's full desktop navigation begins at the 2xl breakpoint; at those wide widths confirm the main links stay on one row and the header does not become unusually tall.

## 商品分類與選單連結

商品分類和一般選單連結是兩份不同的網站資料，不會自動互相複製：

- 商品分類用來整理商品。`slimweb_categories_upsert` 只調整分類；例如「我的商品有洋裝、上衣、針織衫」只建立或確認這三個分類。
- 一般選單用來放頁面或外部連結。`slimweb_nav_items_upsert` 只調整一般選單；例如「有一個關於我們的連結」只建立或確認該選單項目，頁面或連結目標則在另外有需要時處理。
- 只提到某個分類時，預設是處理商品分類。只有明確說要「精選入口」、「選單項目」或「連結」時，才另外建立一般選單項目；兩者都明確要求時，分開完成，絕不推定兩邊要同步。
- 若商家明確要求變更後台的分類顯示設定，依當下 MCP 工具提供的欄位與規則處理；這份指南不定義設定值或分類放置方式。

設計 Theme 導覽列時，要保留空的主要導覽位置，並同時設計「分類收合選單」、「分類直接顯示」及「一般多層選單」三種畫面。實際分類、標籤、網址和階層由 SlimWeb 即時提供，不寫死在 Theme 裡；一次只會顯示所選的分類方式。

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

## LINE Bot setup

Start by asking whether the merchant already has a LINE Official Account (LINE 官方帳號) they can administer, unless they already told you. If they have one, confirm which account and whether Messaging API is already enabled. Confirm the target SlimWeb site before reading or changing its settings. For a standalone site, use its merchant MCP connection with the correct `domain` and confirm the selected site. If available, call `slimweb_line_bot_settings_get` to see what is already configured. Otherwise, use the site's Web admin. Give the next unfinished step and wait for the merchant's result before moving on.

1. **Create the official account if needed.** Guide the merchant to [LINE Official Account Manager](https://manager.line.biz/) to sign in or register a Business ID using a LINE account or email, then create the LINE Official Account. If they already have the official account, use it. [LINE account and Messaging API setup](https://developers.line.biz/en/docs/messaging-api/getting-started/).
2. **Enable Messaging API.** In that official account's LINE Official Account Manager, open Settings → Messaging API and enable it. If LINE prompts for developer registration, have the merchant enter their developer name and email. Have them select or create the provider for their business. LINE creates the Messaging API channel during this process, and the provider cannot be changed afterward. If Messaging API is already enabled, open the existing channel in the [LINE Developers Console](https://developers.line.biz/console/) using the same login.
3. **Get both credentials from that channel.** Find **Channel secret** under **Basic settings**. In **Messaging API**, use the existing long-lived **Channel access token**, or select **Issue** if one has not been issued. If an existing token is unavailable, check who uses it before reissuing, since replacement can interrupt an existing integration. Confirm both values belong to the same Messaging API channel. Direct the merchant to enter them in SlimWeb's credential fields. Never ask them to paste the values into chat or include them in screenshots. [Channel secret](https://developers.line.biz/en/docs/messaging-api/verify-webhook-signature/#get-channel-secret) and [channel access token](https://developers.line.biz/en/docs/basics/channel-access-token/#long-lived-channel-access-token).
4. **Enable and save in SlimWeb.** If `ai_ready` is false or SlimWeb asks to configure AI first, guide the merchant to **AI 管理 → AI 串接** (AI Integration) on the same site to save their AI provider, API key, and required model settings. Reload the LINE Bot status after saving. Then go to **系統管理 → 串接設定 → LINE Bot** (Integration Settings → LINE Bot), check **啟用 LINE Bot**, enter the LINE credentials in the two fields and save. Confirm SlimWeb reports the access token verified and shows the expected bot. If the token check fails, check the channel and token before moving on. Copy the **Webhook URL** shown by SlimWeb.
5. **Verify the webhook in LINE.** In the same channel's **Messaging API** tab, paste the exact SlimWeb HTTPS URL into **Webhook URL**, save, click **Verify**, and look for **Success**. Then turn on **Use webhook**. If a different Webhook URL is already configured, confirm the merchant intends to switch it before replacing it, since LINE sends events to one endpoint. If verification fails, check the copied URL, HTTPS accessibility, and that the saved Channel Secret and verified access token are from the same channel. [LINE webhook setup](https://developers.line.biz/en/docs/messaging-api/building-bot/#set-webhook-url).
6. **Confirm a real reply.** Reload SlimWeb's LINE Bot panel or call `slimweb_line_bot_settings_get` again. Confirm the bot is enabled, the AI is ready, and both token and webhook show verification timestamps. Ask the merchant to add the official account as a friend and send a simple test message to check the Bot's actual reply. If LINE's built-in auto-reply duplicates the Bot's reply, guide the merchant to disable that auto-reply in LINE Official Account Manager if they want SlimWeb to handle replies. Report the verified stages separately. A saved credential or a successful webhook check alone does not confirm an AI reply.

## LINE Rich Menu member linking

When helping create a Rich Menu, check whether it includes a member-linking entry. If missing, explain once that member linking is important: it lets the LINE Bot identify the website member and use their authorized member information, orders, and cart. Recommend a button using the supported fixed-message action: `{"type":"message","text":"綁定會員"}` (English: `link account`).

This is a recommendation, not a requirement. If the merchant declines, continue creating the requested menu without blocking, repeatedly asking, or silently adding a button. Do not imply the Bot cannot answer public questions without linking. Do not add LIFF or automatic member-specific menu switching as part of this advice.

Existing bindings are not overwritten. If an already-linked user requests linking again, explain that they must first visit the website's “個人資訊” / “Personal information” page and unlink their membership. Never automatically unlink or rebind them.
