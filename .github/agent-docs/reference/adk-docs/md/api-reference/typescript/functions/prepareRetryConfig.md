[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [prepareRetryConfig]()



# Function prepareRetryConfig

  * prepareRetryConfig(config: [RetryConfig](../interfaces/RetryConfig.html)): [PreparedRetryConfig](../interfaces/PreparedRetryConfig.html)

Validates and normalizes a [RetryConfig](../interfaces/RetryConfig.html) once, at config-acceptance time (i.e. when a node is constructed).

Throws if `exceptions` contains a malformed entry, surfacing the misconfiguration at construction rather than masking a node's real error from inside the retry path.

#### Parameters

    * config: [RetryConfig](../interfaces/RetryConfig.html)

#### Returns [PreparedRetryConfig](../interfaces/PreparedRetryConfig.html)

    * Defined in [core/src/workflow/retry_config.ts:113](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L113)




[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


