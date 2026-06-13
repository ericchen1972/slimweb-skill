---
name: slimweb-mcp
description: Use when operating a SlimWeb site through SlimWeb MCP.
---

# SlimWeb MCP Skill

## Required Common Rules

1. Before calling any MCP tool, call `SlimWeb.slimweb_sites_list` to obtain `site_id`.
2. If more than one `site_id` is returned, stop the task and list the available `site_id` values for the user to choose from.
3. Never use a `site_id` that does not appear in the `SlimWeb.slimweb_sites_list` result.

## Common Image Rules

1. If a task needs image assets, obtain usable image URLs or media paths before creating or editing pages or articles.
2. If an image is already a publicly reachable URL, use that URL directly.
3. If the client can access local files and upload bytes, use `slimweb_uploads_create` and `slimweb_uploads_commit` to upload the image to the server and obtain a usable media path or URL.
4. If the client cannot upload bytes directly but the user pasted an image attachment in the conversation, use `slimweb_images_import_chatgpt_attachment` to import the attachment and obtain a usable image URL or media path.
5. If the client cannot upload bytes directly and the user has not provided an attachment or image URL, stop the task and ask the user to paste or upload the image first.
6. If the image is AI-generated, generate it according to the color scheme and design direction from `slimweb_design_context_get` so it fits the active theme.
7. If the image is AI-generated and the client cannot access local files or upload bytes, stop the task and ask the user to paste the generated image back into the conversation.

## Page Create Flow

1. Require a `title` before creating a page; ask the user if it is missing.
2. Use `slimweb_pages_check_title` to check for duplicate titles. If `exists` is true, stop immediately and tell the user.
3. Use `slimweb_design_context_get` to obtain the current site design summary, color scheme, and framework.
4. If the page needs images, follow the Common Image Rules.
5. Design from the site design summary, color scheme, and framework.
6. HTML may include custom CSS and JavaScript needed for visual design.
7. Use `slimweb_pages_create` to create the page.
8. Return the page URL after creation. Use `slimweb_preview_get_page_url` for preview verification when useful.

## Page Edit Flow

1. Require `page_name` before editing a page; ask the user if it is missing.
2. Use `slimweb_pages_get_content` to read the current page content.
3. If the page is not found, stop immediately and tell the user.
4. If adding or replacing images, follow the Common Image Rules.
5. Modify HTML using the current content and the design summary from `slimweb_design_context_get`.
6. Use `slimweb_pages_update` to save the page.
7. Return the page URL after editing. Use `slimweb_preview_get_page_url` for preview verification when useful.

## Article Create Flow

1. Require a `title` before creating an article; ask the user if it is missing.
2. Use `slimweb_articles_check_title` to check for duplicate titles. If `exists` is true, stop immediately and tell the user.
3. Use `slimweb_design_context_get` to obtain the current site design summary, color scheme, and framework.
4. A new article must always have a 16:9 cover image. Follow the Common Image Rules.
5. If the user does not provide a cover image and does not describe one, generate the cover from the article title or content.
6. If the article needs content images, follow the Common Image Rules.
7. Do not repeat the article title as an `h1` in `content_html`.
8. Use `slimweb_articles_create` to create the article.
9. Return the article URL after creation.

## Article Edit Flow

1. Require article identification before editing; the user may provide `article_id` or an article title. Ask the user if both are missing.
2. If the user provides an article title, use `slimweb_articles_list` to list articles, match the title, and obtain `article_id`. If no match or multiple similar matches are found, stop immediately and ask the user to confirm.
3. Use `slimweb_articles_get_content` to read the current article content.
4. If the article is not found, stop immediately and tell the user.
5. Use `slimweb_design_context_get` to obtain the current site design summary, color scheme, and framework.
6. If adding or replacing the cover image or content images, follow the Common Image Rules.
7. Modify `content_html` using the current article content and the design summary from `slimweb_design_context_get`.
8. If changing the article title, first use `slimweb_articles_check_title` to check for duplicates. If `exists` is true, stop immediately and tell the user.
9. Do not repeat the article title as an `h1` in `content_html`, because SlimWeb renders the title separately.
10. Use `slimweb_articles_update` to save the article.
11. Return the article URL after editing.

## Article Delete Flow

- No SlimWeb MCP article deletion tool is currently available.
- Do not invent a deletion tool or use another tool to delete an article.
- Stop and tell the user that article deletion is not supported by the current MCP.

## Theme Create Flow

1. Require a `name` before creating a theme; ask the user if it is missing.
2. Use `slimweb_themes_list` to check for duplicate or similar custom themes. If an exact duplicate exists, stop immediately and tell the user.
3. If the user requests dark, fluorescent, neon, high-contrast, or another style that depends on light/dark mode, use `slimweb_site_theme_mode_get` first. Use `slimweb_site_theme_mode_update` to switch light/dark mode when needed.
4. Use `slimweb_themes_create_from_default` to create a new custom theme from Default.
5. Use `slimweb_theme_shell_get_context` to read real shell reference data such as navbar, footer, categories, login, and cart.
6. Use `slimweb_design_context_get` to read the current site design summary, color scheme, and framework.
7. Design the theme base from the user request, site colors, shell reference, and framework. Include navbar, footer, root CSS, body background, and overall visual atmosphere.
8. Use `slimweb_themes_update_root_elements` to write the new theme navbar, footer, and root CSS. Do not use this tool to modify single-page body content.
9. Use `slimweb_theme_style_profile_upsert` to save the theme style profile, including colors, typography, layout, illustration direction, avoid notes, and user intent.
10. Return the theme name and `theme_id`. Only use `slimweb_themes_activate` when the user explicitly asks to activate the new theme.

## Theme Edit Flow

1. Require `theme_id` or a theme name before editing a theme; ask the user if both are missing.
2. Use `slimweb_themes_list` to find the target custom theme. If no target or multiple possible targets are found, stop immediately and ask the user to confirm.
3. Use `slimweb_theme_style_profile_get` to read the current theme style profile and request history.
4. Use `slimweb_theme_shell_get_context` to read real shell reference data such as navbar, footer, categories, login, and cart.
5. Use `slimweb_design_context_get` to read the current site design summary, color scheme, and framework.
6. If the user requests dark, fluorescent, neon, high-contrast, or another style that depends on light/dark mode, use `slimweb_site_theme_mode_get` first. Use `slimweb_site_theme_mode_update` to switch light/dark mode when needed.
7. Modify the theme base from the user request, existing style profile, site colors, shell reference, and framework. Include navbar, footer, root CSS, body background, and overall visual atmosphere.
8. Use `slimweb_themes_update_root_elements` to save navbar, footer, and root CSS. Do not use this tool to modify single-page body content.
9. Use `slimweb_theme_style_profile_upsert` to update the theme style profile.
10. Use `slimweb_theme_style_profile_append_request` to append this user change request and AI design notes.
11. Return the theme name and `theme_id`. Only use `slimweb_themes_activate` when the user explicitly asks to activate the theme.

## Shared Email Layout Edit Flow

1. The shared email layout has edit flow only; there is no create flow.
2. Use `slimweb_mail_layout_get` to read the current shared layout, default layout HTML, and available placeholders.
3. The shared email layout is the wrapper used by every event email: background, logo, site name, frame, footer, container, and global button styling.
4. Modify the current or default HTML returned by `slimweb_mail_layout_get`. Do not rewrite the entire HTML from scratch.
5. Preserve the `{content}` placeholder because event email content is inserted there.
6. Always preserve existing placeholders such as `{site_name}`, `{site_url}`, and `{logo_url}`.
7. Use email-client-safe HTML: simple structure, inline styles, fixed-width containers, and conservative CSS. Avoid JavaScript, external CSS, complex interactions, and normal web layout assumptions.
8. If the shared layout needs images, follow the Common Image Rules and use stable publicly reachable image URLs.
9. Use `slimweb_mail_layout_update` to save the full HTML and set `is_active`.
10. Tell the user that the shared email layout applies to all event emails.

## Event Email Content Edit Flow

1. Before editing event email content, identify which event email the user wants to change. Ask the user if it is not clear.
2. Use `slimweb_mail_templates_get` to read all current event email templates.
3. Identify the target event from user intent only. Do not guess from history.
4. Editable fields include the email subject, content HTML, internal content layout, content images, and enabled state.
5. If adding or replacing images, follow the Common Image Rules.
6. When editing content HTML, change only that event email content. Do not modify the shared email layout wrapper here.
7. Use email-client-safe HTML: inline styles, simple tables or blocks, and conservative CSS. Avoid JavaScript, external CSS, and complex interactions.
8. To change only the subject, use `slimweb_mail_templates_update` with the matching `trigger_event` and `subject`.
9. To change content or internal content layout, use `slimweb_mail_templates_update` with the matching `trigger_event` and `content`.
10. To enable or disable an event email, use `slimweb_mail_templates_update` with the matching `trigger_event` and `is_active`.
11. Return the changed event email type, subject, and update result.
