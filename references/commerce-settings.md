# Commerce Settings: Payments and Logistics

Use this when the user asks about SlimWeb payment providers, logistics providers, provider setup, credentials, enablement, or what their SlimWeb site supports.

## Supported Providers

SlimWeb supported payment providers:

- ECPay.
- NewebPay.
- PayNow.
- LINE Pay.

SlimWeb supported logistics providers:

- ECPay logistics.
- NewebPay logistics.
- PayNow C2C logistics, including 7-ELEVEN frozen pickup and pay for eligible merchants.
- HCT logistics.

Do not invent other providers.

## Answering User Questions

When the user asks "What payment can my SlimWeb site use?", answer only from the SlimWeb supported provider list.

When the user asks "What payment should an ecommerce site use?" and they are using a generic AI client outside a SlimWeb site-setting context, explain that this is general ecommerce advice and not a SlimWeb site setting. If the conversation is inside SlimAI, answer from SlimWeb supported providers first.

## Setup Rules

- AI may fill provider credentials only for supported providers and fields exposed by MCP.
- AI may enable or disable supported providers.
- ECPay, NewebPay, and PayNow are mutually exclusive as the active online card provider. Pass `switch_primary_to` only when the merchant explicitly requests a switch.
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

## PayNow 7-ELEVEN Frozen Pickup and Pay

1. Select the correct shop in the merchant MCP and call `slimweb_payment_logistics_get`. Check the active provider, environment, PayNow credential presence, sender details, and store channels. Ask the merchant to confirm that the PayNow account for the intended environment has **7-ELEVEN frozen cash collection (冷凍取貨付款／代收)** enabled. If they are unsure, guide them to confirm in the PayNow merchant logistics dashboard or with PayNow support before turning on the SlimWeb option. An enabled frozen shipping channel alone does not confirm cash collection.
2. When the merchant requests activation and confirms cash collection, call `slimweb_payment_logistics_update` with a `payments` entry for `provider: paynow`, the intended `mode`, `is_enabled: true`, and `seven_frozen_cod_enabled: true`. Include `seven_frozen` in `store_types`, retaining the other selected channels. Reuse stored credentials and sender details. If a different provider is active, wait for the merchant's explicit request to switch before sending the activation update with `switch_primary_to: paynow`. An `activation_deferred` result means the new provider was saved for later activation.
3. Read the settings again to verify that PayNow, the intended environment, the frozen channel, and the cash collection option are active. Give the merchant the exact URL returned by `callback_urls.logistics.paynow.notify_url`. Guide them to paste and save it in the logistics status notification field (物流貨態回傳／物流 Notify URL) of the corresponding PayNow merchant environment. Ask them to confirm that PayNow saved it. The SlimWeb settings tool does not save settings inside PayNow.
4. Verify that the storefront checkout offers **7-ELEVEN 冷凍取貨付款** after activation. Report whether the PayNow URL was saved and whether a real shipment callback was verified. A visible checkout option alone does not establish that PayNow cash collection or status delivery works.

