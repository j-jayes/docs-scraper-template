[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [RetryConfig]()



# Interface RetryConfig

Configuration for retrying a node.

Ported from `google/adk-python` `workflow/_retry_config.py`. Delays are expressed in **seconds** (fractions allowed) to match the Python semantics and keep configuration portable across runtimes. Unset fields fall back to the documented defaults inside the retry utilities.

interface RetryConfig {  
backoffFactor?: number;  
exceptions?: (string | [ErrorClass](../types/ErrorClass.html))[] | null;  
initialDelay?: number;  
jitter?: number;  
maxAttempts?: number;  
maxDelay?: number;  
}

  * Defined in [core/src/workflow/retry_config.ts:20](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L20)



## Properties

### `Optional`backoffFactor

backoffFactor?: number

Multiplier by which the delay increases after each attempt. If not specified, defaults to 2.0.

  * Defined in [core/src/workflow/retry_config.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L43)



### `Optional`exceptions

exceptions?: (string | [ErrorClass](../types/ErrorClass.html))[] | null

Exceptions to retry on. Accepts error class names as strings (e.g. `['TypeError']`) or error classes directly (e.g. `[TypeError]`). `undefined`/`null` means retry on all errors.

  * Defined in [core/src/workflow/retry_config.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L56)



### `Optional`initialDelay

initialDelay?: number

Initial delay before the first retry, in seconds. If not specified, defaults to 1.0 second.

  * Defined in [core/src/workflow/retry_config.ts:31](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L31)



### `Optional`jitter

jitter?: number

Randomness factor for the delay. If not specified, defaults to 1.0. Use 0.0 to remove randomness.

  * Defined in [core/src/workflow/retry_config.ts:49](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L49)



### `Optional`maxAttempts

maxAttempts?: number

Maximum number of attempts, including the original request. If 0 or 1, it means no retries. If not specified, defaults to 5.

  * Defined in [core/src/workflow/retry_config.ts:25](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L25)



### `Optional`maxDelay

maxDelay?: number

Maximum delay between retries, in seconds. If not specified, defaults to 60.0 seconds.

  * Defined in [core/src/workflow/retry_config.ts:37](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/retry_config.ts#L37)



Properties

backoffFactorexceptionsinitialDelayjittermaxAttemptsmaxDelay

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


