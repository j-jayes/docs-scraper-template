[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [PreparedRetryConfig]()



# Interface PreparedRetryConfig

A [RetryConfig](RetryConfig.html) whose `exceptions` filter has been normalized to error class-name strings once, up front.

Produced by [prepareRetryConfig](../functions/prepareRetryConfig.html) when a node accepts its config, so the retry hot path neither re-normalizes on every failure nor throws on a malformed config from inside the retry loop.

interface PreparedRetryConfig {  
backoffFactor?: number;  
exceptions?: readonly string[];  
initialDelay?: number;  
jitter?: number;  
maxAttempts?: number;  
maxDelay?: number;  
}

  * Defined in [core/src/workflow/retry_config.ts:95](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L95)



## Properties

### `Optional` `Readonly`backoffFactor

backoffFactor?: number

  * Defined in [core/src/workflow/retry_config.ts:99](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L99)



### `Optional` `Readonly`exceptions

exceptions?: readonly string[]

Normalized exception names; `undefined` means retry on all errors.

  * Defined in [core/src/workflow/retry_config.ts:102](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L102)



### `Optional` `Readonly`initialDelay

initialDelay?: number

  * Defined in [core/src/workflow/retry_config.ts:97](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L97)



### `Optional` `Readonly`jitter

jitter?: number

  * Defined in [core/src/workflow/retry_config.ts:100](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L100)



### `Optional` `Readonly`maxAttempts

maxAttempts?: number

  * Defined in [core/src/workflow/retry_config.ts:96](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L96)



### `Optional` `Readonly`maxDelay

maxDelay?: number

  * Defined in [core/src/workflow/retry_config.ts:98](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L98)



Properties

backoffFactorexceptionsinitialDelayjittermaxAttemptsmaxDelay

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


