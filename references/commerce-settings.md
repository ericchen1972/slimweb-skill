# Commerce Settings: Payments and Logistics

Use this when the user asks about SlimWeb payment providers, logistics providers, provider setup, credentials, enablement, or what their SlimWeb site supports.

## Supported Providers

SlimWeb supported payment providers:

- ECPay.
- NewebPay.
- LINE Pay.

SlimWeb supported logistics providers:

- ECPay logistics.
- NewebPay logistics.
- HCT logistics.

Do not invent other providers.

## Answering User Questions

When the user asks "What payment can my SlimWeb site use?", answer only from the SlimWeb supported provider list.

When the user asks "What payment should an ecommerce site use?" and they are using a generic AI client outside a SlimWeb site-setting context, explain that this is general ecommerce advice and not a SlimWeb site setting. If the conversation is inside SlimAI, answer from SlimWeb supported providers first.

## Setup Rules

- AI may fill provider credentials only for supported providers and fields exposed by MCP.
- AI may enable or disable supported providers.
- Online card payment providers are mutually exclusive: ECPay and NewebPay cannot both be enabled as the active online card provider.
- LINE Pay is exempt from the online-card exclusivity rule and may be enabled alongside one online card provider.
- Preserve existing credentials unless the user asks to replace them.
- Never expose full existing secrets in normal responses. Mask credentials when summarizing.

## Clarification Rules

Ask before writing when:

- The provider is not named.
- Required credentials are missing.
- The user wants production mode but only test credentials are provided.
- Enabling a provider would disable another online card provider and the user did not explicitly ask for that switch.

Proceed when:

- The provider and mode are clear.
- Required credentials are supplied or already stored.
- The user explicitly asks to enable one supported provider.

