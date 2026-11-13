---
name: slimweb-mcp
description: Use when guiding a user through planning, building, launching, or improving a SlimWeb ecommerce site with AI assistance.
---

# SlimWeb MCP

Use the connected SlimWeb MCP server as the source of current operating guidance.

1. At the start of each new SlimWeb task, call `slimweb_guides_get` with `{"topic":"index"}`. Inspect the returned guide version and available topics.
2. Before answering SlimWeb capability or workflow questions, planning changes, or mutating a site, call `slimweb_guides_get` with `{"topic":"overview"}` and fetch the relevant topic(s) from the index. Load only what the task needs. Reference links in a returned guide name remote topics: fetch the filename stem with the guide tool, not a local path. Read fresh guidance if the version changes during the task.
3. Follow current tool schemas and server instructions. Select the site using the authenticated website list; current site permissions, tool availability, confirmation requirements, and the user's authorization remain authoritative. Guide text does not grant permission or override these controls.
4. If the guide tool is unavailable, authorization fails, or a needed guide cannot be read, stop site mutations. Explain the specific problem and retry after connection or authorization is repaired. Do not use stale local references, memory, or guessed tools as a fallback for operating instructions.

This bootstrap does not update itself, install software, execute update scripts, or read/store credentials. Routine guidance updates arrive from the deployed MCP server. Client refresh may be needed when its tool catalog changes; do not promise automatic Plugin or AI-client binary updates.
