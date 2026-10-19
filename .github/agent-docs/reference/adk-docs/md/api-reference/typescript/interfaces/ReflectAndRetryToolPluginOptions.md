[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ReflectAndRetryToolPluginOptions]()



# Interface ReflectAndRetryToolPluginOptions

Options for configuring [ReflectAndRetryToolPlugin](../classes/ReflectAndRetryToolPlugin.html).

interface ReflectAndRetryToolPluginOptions {  
maxRetries?: number;  
name?: string;  
throwExceptionIfRetryExceeded?: boolean;  
trackingScope?: [TrackingScope](../enums/TrackingScope.html);  
}

  * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:21](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L21)



## Properties

### `Optional`maxRetries

maxRetries?: number

Maximum consecutive failures before giving up (0 = no retries). Defaults to 3.

  * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:32](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L32)



### `Optional`name

name?: string

Plugin instance identifier. Defaults to 'reflect_retry_tool_plugin'.

  * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:26](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L26)



### `Optional`throwExceptionIfRetryExceeded

throwExceptionIfRetryExceeded?: boolean

If true, raises the final exception when the retry limit is reached. If false, returns structured retry-exceeded guidance instead. Defaults to true.

  * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:39](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L39)



### `Optional`trackingScope

trackingScope?: [TrackingScope](../enums/TrackingScope.html)

Determines the lifecycle of the error tracking state. Defaults to `TrackingScope.INVOCATION` (tracking per-invocation).

  * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:45](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L45)



Properties

maxRetriesnamethrowExceptionIfRetryExceededtrackingScope

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


