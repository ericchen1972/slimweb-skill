# External CSS and JavaScript

Use this when the user asks to add custom CSS, custom JavaScript, third-party widgets, pixels, analytics, chat plugins, embeds, fonts, animation libraries, or external assets to a SlimWeb site.

## Core Rules

- External CSS/JS must have a clear purpose and placement.
- Do not add third-party scripts without considering trust, performance, privacy, and page breakage.
- Do not use external CSS/JS to bypass SlimWeb settings when a supported MCP tool exists.
- Keep custom code scoped as narrowly as possible: page-level before global when the change is page-specific.
- Preserve existing custom code unless replacement is explicitly requested.

## Responsive and Visual Impact

Before adding CSS/JS that affects layout or visuals:

- Check mobile, tablet, and desktop behavior.
- Avoid fixed widths, fixed heights, and absolute positioning that breaks mobile.
- Avoid scripts that depend on hover-only interaction.
- Avoid layout shifts after load.
- Confirm external fonts do not cause severe flash or slow rendering.

## Safety Checks

Ask for confirmation when:

- The script collects user data.
- The script modifies checkout, payment, login, cart, or order flow.
- The source domain is unknown or untrusted.
- The code is minified and the intent is not clear.

Reject or warn when:

- The script attempts to steal credentials or tokens.
- The code hides required legal, price, payment, or order information.
- The CSS makes text unreadable or inaccessible.
- The code conflicts with SlimWeb's supported page or commerce workflows.

## Placement Guidance

- Global CSS/JS: only for site-wide behavior such as analytics, global chat, global typography, or shared tracking.
- Page CSS/JS: for a landing page, campaign page, or special visual effect.
- Component/section style: preferred when the MCP page tool supports scoped section styling.

