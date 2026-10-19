[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ReflectAndRetryModelPluginOptions]()



# Interface ReflectAndRetryModelPluginOptions

Options for configuring [ReflectAndRetryModelPlugin](../classes/ReflectAndRetryModelPlugin.html).

interface ReflectAndRetryModelPluginOptions {  
maxRetries?: number;  
name?: string;  
onModelErrors?: FinishReason[];  
throwExceptionIfRetryExceeded?: boolean;  
trackingScope?: [TrackingScope](../enums/TrackingScope.html);  
}

  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:27](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L27)



## Properties

### `Optional`maxRetries

maxRetries?: number

Maximum consecutive model failures before giving up (0 = no retries). Defaults to 3.

  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:31](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L31)



### `Optional`name

name?: string

Plugin instance identifier. Defaults to 'reflect_retry_model_plugin'.

  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:29](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L29)



### `Optional`onModelErrors

onModelErrors?: FinishReason[]

A list of FinishReasons that should be treated as model errors. Defaults to [FinishReason.MALFORMED_FUNCTION_CALL].

  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:37](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L37)



### `Optional`throwExceptionIfRetryExceeded

throwExceptionIfRetryExceeded?: boolean

If true, raises the exception when retry limit is reached. If false, returns response. Defaults to true.

  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:33](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L33)



### `Optional`trackingScope

trackingScope?: [TrackingScope](../enums/TrackingScope.html)

Determines the lifecycle of the error tracking state. Defaults to TrackingScope.INVOCATION.

  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:35](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L35)



Properties

maxRetriesnameonModelErrorsthrowExceptionIfRetryExceededtrackingScope

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


