[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ReflectAndRetryModelPlugin]()



# Class ReflectAndRetryModelPlugin

Provides self-healing, concurrent-safe error recovery for model failures.

This plugin intercepts model failures (such as `MALFORMED_FUNCTION_CALL`), provides structured guidance to the LLM for reflection and correction, and retries the turn up to a configurable limit.

#### Example
    
    
    import {ReflectAndRetryModelPlugin, TrackingScope} from '@google/adk';  
      
    const modelRetryPlugin = new ReflectAndRetryModelPlugin({  
      maxRetries: 3,  
      trackingScope: TrackingScope.INVOCATION,  
    });
    Copy

#### Hierarchy ([View Summary](../hierarchy.html#ReflectAndRetryModelPlugin))

  * [BasePlugin](BasePlugin.html)
    * ReflectAndRetryModelPlugin



  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:57](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L57)



## Constructors

### constructor

  * new ReflectAndRetryModelPlugin(  
options?: [ReflectAndRetryModelPluginOptions](../interfaces/ReflectAndRetryModelPluginOptions.html),  
): [ReflectAndRetryModelPlugin]()

Initializes the ReflectAndRetryModelPlugin.

#### Parameters

    * options: [ReflectAndRetryModelPluginOptions](../interfaces/ReflectAndRetryModelPluginOptions.html) = {}

Configuration options for the plugin.

#### Returns [ReflectAndRetryModelPlugin]()

Overrides [BasePlugin](BasePlugin.html).[constructor](BasePlugin.html#constructor)

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:69](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L69)




## Properties

### `Readonly`maxRetries

maxRetries: number

  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:58](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L58)



### `Readonly`name

name: string

Inherited from [BasePlugin](BasePlugin.html).[name](BasePlugin.html#name)

  * Defined in [core/src/plugins/base_plugin.ts:115](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L115)



### `Readonly`onModelErrors

onModelErrors: FinishReason[]

  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:61](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L61)



### `Readonly`scope

scope: [TrackingScope](../enums/TrackingScope.html)

  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:60](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L60)



### `Readonly`throwExceptionIfRetryExceeded

throwExceptionIfRetryExceeded: boolean

  * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L59)



## Methods

### adkHandleModelError

  * adkHandleModelError(  
__namedParameters: {  
errorDetails?: string;  
errorType?: string;  
finishReason?: string;  
responseType?: string;  
retryCount?: number;  
},  
): { reflection_guidance: string }

Internal framework reflection tool handler.

#### Parameters

    * __namedParameters: {  
errorDetails?: string;  
errorType?: string;  
finishReason?: string;  
responseType?: string;  
retryCount?: number;  
}

#### Returns { reflection_guidance: string }

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:90](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L90)




### afterAgentCallback

  * afterAgentCallback(  
_params: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) },  
): Promise<Content | undefined>

Callback executed after an agent's primary logic has completed.

This callback can be used to inspect, log, or modify the agent's final result before it is returned.

#### Parameters

    * _params: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) }
      * ##### agent: [BaseAgent](BaseAgent.html)

The agent that has just run.

      * ##### callbackContext: [Context](Context.html)

The context for the agent invocation.

#### Returns Promise<Content | undefined>

An optional `Content` object. If a value is returned, it will replace the agent's original result. Returning `undefined` uses the original, unmodified result.

Inherited from [BasePlugin](BasePlugin.html).[afterAgentCallback](BasePlugin.html#afteragentcallback)

    * Defined in [core/src/plugins/base_plugin.ts:231](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L231)




### afterContextCompaction

  * afterContextCompaction(  
_params: {  
invocationContext: [InvocationContext](InvocationContext.html);  
trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html);  
},  
): Promise<void>

Callback executed after context compaction.

This callback provides an opportunity to inspect the context after it has been compacted.

#### Parameters

    * _params: { invocationContext: [InvocationContext](InvocationContext.html); trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html) }
      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation.

      * ##### trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html)

The trigger for the context compaction.

#### Returns Promise<void>

Inherited from [BasePlugin](BasePlugin.html).[afterContextCompaction](BasePlugin.html#aftercontextcompaction)

    * Defined in [core/src/plugins/base_plugin.ts:387](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L387)




### afterModelCallback

  * afterModelCallback(  
__namedParameters: {  
callbackContext: [Context](Context.html);  
llmResponse: [LlmResponse](../interfaces/LlmResponse.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Inspects LLM responses, intercepts model errors or reserved tool calls, and handles retries.

#### Parameters

    * __namedParameters: { callbackContext: [Context](Context.html); llmResponse: [LlmResponse](../interfaces/LlmResponse.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Overrides [BasePlugin](BasePlugin.html).[afterModelCallback](BasePlugin.html#aftermodelcallback)

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:152](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L152)




### afterNodeCallback

  * afterNodeCallback(  
params: { node: [BaseNode](BaseNode.html); nodeContext: [NodeContext](NodeContext.html); output: unknown },  
): Promise<unknown>

Callback executed after a workflow node has run.

Not called for a node whose body was skipped by `beforeNodeCallback`, and not called when the node throws.

#### Parameters

    * params: { node: [BaseNode](BaseNode.html); nodeContext: [NodeContext](NodeContext.html); output: unknown }
      * ##### node: [BaseNode](BaseNode.html)

The node that has just run.

      * ##### nodeContext: [NodeContext](NodeContext.html)

The node's execution context.

      * ##### output: unknown

The output the node produced.

#### Returns Promise<unknown>

An optional value replacing the node's output. Returning `undefined` keeps the original.

Inherited from [BasePlugin](BasePlugin.html).[afterNodeCallback](BasePlugin.html#afternodecallback)

    * Defined in [core/src/plugins/base_plugin.ts:271](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L271)




### afterRunCallback

  * afterRunCallback(  
_params: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<void>

Callback executed after an ADK runner run has completed.

This is the final callback in the ADK lifecycle, suitable for cleanup, final logging, or reporting tasks.

#### Parameters

    * _params: { invocationContext: [InvocationContext](InvocationContext.html) }
      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation.

#### Returns Promise<void>

undefined

Inherited from [BasePlugin](BasePlugin.html).[afterRunCallback](BasePlugin.html#afterruncallback)

    * Defined in [core/src/plugins/base_plugin.ts:194](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L194)




### afterToolCallback

  * afterToolCallback(  
_params: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Callback executed after a tool has been called.

This callback allows for inspecting, logging, or modifying the result returned by a tool.

#### Parameters

    * _params: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
}
      * ##### result: Record<string, unknown>

The dictionary returned by the tool invocation.

      * ##### tool: [BaseTool](BaseTool.html)

The tool instance that has just been executed.

      * ##### toolArgs: Record<string, unknown>

The original arguments that were passed to the tool.

      * ##### toolContext: [Context](Context.html)

The context specific to the tool execution.

#### Returns Promise<Record<string, unknown> | undefined>

An optional dictionary. If a dictionary is returned, it will **replace** the original result from the tool. This allows for post-processing or altering tool outputs. Returning `undefined` uses the original, unmodified result.

Inherited from [BasePlugin](BasePlugin.html).[afterToolCallback](BasePlugin.html#aftertoolcallback)

    * Defined in [core/src/plugins/base_plugin.ts:431](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L431)




### beforeAgentCallback

  * beforeAgentCallback(  
_params: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) },  
): Promise<Content | undefined>

Callback executed before an agent's primary logic is invoked.

This callback can be used for logging, setup, or to short-circuit the agent's execution by returning a value.

#### Parameters

    * _params: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) }
      * ##### agent: [BaseAgent](BaseAgent.html)

The agent that is about to run.

      * ##### callbackContext: [Context](Context.html)

The context for the agent invocation.

#### Returns Promise<Content | undefined>

An optional `Content` object. If a value is returned, it will bypass the agent's callbacks and its execution, and return this value directly. Returning `undefined` allows the agent to proceed normally.

Inherited from [BasePlugin](BasePlugin.html).[beforeAgentCallback](BasePlugin.html#beforeagentcallback)

    * Defined in [core/src/plugins/base_plugin.ts:212](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L212)




### beforeContextCompaction

  * beforeContextCompaction(  
_params: {  
invocationContext: [InvocationContext](InvocationContext.html);  
trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html);  
},  
): Promise<void>

Callback executed before context compaction.

This callback provides an opportunity to inspect or modify the context before it is compacted.

#### Parameters

    * _params: { invocationContext: [InvocationContext](InvocationContext.html); trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html) }
      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation.

      * ##### trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html)

The trigger for the context compaction.

#### Returns Promise<void>

Inherited from [BasePlugin](BasePlugin.html).[beforeContextCompaction](BasePlugin.html#beforecontextcompaction)

    * Defined in [core/src/plugins/base_plugin.ts:370](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L370)




### beforeModelCallback

  * beforeModelCallback(  
__namedParameters: { callbackContext: [Context](Context.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) },  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Prepares the LLM request by attaching the reflection tool.

#### Parameters

    * __namedParameters: { callbackContext: [Context](Context.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Overrides [BasePlugin](BasePlugin.html).[beforeModelCallback](BasePlugin.html#beforemodelcallback)

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:139](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L139)




### beforeNodeCallback

  * beforeNodeCallback(  
params: { input: unknown; node: [BaseNode](BaseNode.html); nodeContext: [NodeContext](NodeContext.html) },  
): Promise<unknown>

Callback executed before a workflow node runs.

#### Parameters

    * params: { input: unknown; node: [BaseNode](BaseNode.html); nodeContext: [NodeContext](NodeContext.html) }
      * ##### input: unknown

The input the node is about to receive.

      * ##### node: [BaseNode](BaseNode.html)

The node that is about to run.

      * ##### nodeContext: [NodeContext](NodeContext.html)

The node's execution context.

#### Returns Promise<unknown>

An optional value. If anything other than `undefined` is returned, the node's body is skipped and the returned value becomes its output, which is how a plugin implements a node-level cache or a stub. Returning `undefined` lets the node run normally.

Inherited from [BasePlugin](BasePlugin.html).[beforeNodeCallback](BasePlugin.html#beforenodecallback)

    * Defined in [core/src/plugins/base_plugin.ts:250](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L250)




### beforeRunCallback

  * beforeRunCallback(  
_params: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<Content | undefined>

Callback executed before the ADK runner runs.

This is the first callback to be called in the lifecycle, ideal for global setup or initialization tasks.

#### Parameters

    * _params: { invocationContext: [InvocationContext](InvocationContext.html) }
      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation, containing session information, the root agent, etc.

#### Returns Promise<Content | undefined>

An optional `Event` to be returned to the ADK. Returning a value to halt execution of the runner and ends the runner with that event. Return `undefined` to proceed normally.

Inherited from [BasePlugin](BasePlugin.html).[beforeRunCallback](BasePlugin.html#beforeruncallback)

    * Defined in [core/src/plugins/base_plugin.ts:158](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L158)




### beforeToolCallback

  * beforeToolCallback(  
_params: {  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Callback executed before a tool is called.

This callback is useful for logging tool usage, input validation, or modifying the arguments before they are passed to the tool.

#### Parameters

    * _params: { tool: [BaseTool](BaseTool.html); toolArgs: Record<string, unknown>; toolContext: [Context](Context.html) }
      * ##### tool: [BaseTool](BaseTool.html)

The tool instance that is about to be executed.

      * ##### toolArgs: Record<string, unknown>

The dictionary of arguments to be used for invoking the tool.

      * ##### toolContext: [Context](Context.html)

The context specific to the tool execution.

#### Returns Promise<Record<string, unknown> | undefined>

An optional dictionary. If a dictionary is returned, it will stop the tool execution and return this response immediately. Returning `undefined` uses the original, unmodified arguments.

Inherited from [BasePlugin](BasePlugin.html).[beforeToolCallback](BasePlugin.html#beforetoolcallback)

    * Defined in [core/src/plugins/base_plugin.ts:408](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L408)




### beforeToolSelection

  * beforeToolSelection(  
_params: {  
callbackContext: [Context](Context.html);  
tools: Readonly<Record<string, [BaseTool](BaseTool.html)>>;  
},  
): Promise<Readonly<Record<string, [BaseTool](BaseTool.html)>> | undefined>

Callback executed before a tool is selected.

This callback provides an opportunity to inspect, log, or modify the available tools before they are selected.

#### Parameters

    * _params: { callbackContext: [Context](Context.html); tools: Readonly<Record<string, [BaseTool](BaseTool.html)>> }
      * ##### callbackContext: [Context](Context.html)

The context for the current agent call.

      * ##### tools: Readonly<Record<string, [BaseTool](BaseTool.html)>>

The available tools.

#### Returns Promise<Readonly<Record<string, [BaseTool](BaseTool.html)>> | undefined>

An optional value. A non-`undefined` return may be used by the framework to modify or replace the available tools. Returning `undefined` allows the original tools to be used.

Inherited from [BasePlugin](BasePlugin.html).[beforeToolSelection](BasePlugin.html#beforetoolselection)

    * Defined in [core/src/plugins/base_plugin.ts:353](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L353)




### `Protected`checkForModelError

  * checkForModelError(llmResponse: [LlmResponse](../interfaces/LlmResponse.html)): boolean

Checks if the model response contains an error matching `onModelErrors`.

#### Parameters

    * llmResponse: [LlmResponse](../interfaces/LlmResponse.html)

#### Returns boolean

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:116](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L116)




### `Protected`generateModelRetryPart

  * generateModelRetryPart(  
retryCount: number,  
errorType?: string,  
errorDetails?: string,  
finishReason?: FinishReason,  
): Part

Generates a function call part for the model retry tool.

#### Parameters

    * retryCount: number
    * `Optional`errorType: string
    * `Optional`errorDetails: string
    * `Optional`finishReason: FinishReason

#### Returns Part

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:303](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L303)




### `Protected`getModelNameFromContext

  * getModelNameFromContext(callbackContext: [Context](Context.html)): string

Retrieves the model name from context.

#### Parameters

    * callbackContext: [Context](Context.html)

#### Returns string

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:132](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L132)




### `Protected`getModelRetryUuid

  * getModelRetryUuid(): string

Generates a unique ID for the model retry tool call.

#### Returns string

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:327](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L327)




### `Protected`getModelScopeKey

  * getModelScopeKey(callbackContext: [Context](Context.html)): string

Returns the scope key for model failure tracking.

#### Parameters

    * callbackContext: [Context](Context.html)

#### Returns string

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:334](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L334)




### `Protected`handleModelError

  * handleModelError(  
callbackContext: [Context](Context.html),  
llmResponse: [LlmResponse](../interfaces/LlmResponse.html),  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Handles detected model errors by initiating retry logic.

#### Parameters

    * callbackContext: [Context](Context.html)
    * llmResponse: [LlmResponse](../interfaces/LlmResponse.html)

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:241](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L241)




### `Protected`handleModelRetry

  * handleModelRetry(  
callbackContext: [Context](Context.html),  
errorType?: string,  
errorDetails?: string,  
finishReason?: FinishReason,  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Tracks retry count, generates retry response, and checks against limits.

#### Parameters

    * callbackContext: [Context](Context.html)
    * `Optional`errorType: string
    * `Optional`errorDetails: string
    * `Optional`finishReason: FinishReason

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:262](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L262)




### `Protected`handleReservedToolCall

  * handleReservedToolCall(  
callbackContext: [Context](Context.html),  
_llmResponse: [LlmResponse](../interfaces/LlmResponse.html),  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Handles direct calls to the reserved reflection tool.

#### Parameters

    * callbackContext: [Context](Context.html)
    * _llmResponse: [LlmResponse](../interfaces/LlmResponse.html)

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:216](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L216)




### `Protected`hasReservedToolCall

  * hasReservedToolCall(llmResponse: [LlmResponse](../interfaces/LlmResponse.html)): boolean

Checks if the model response calls the reserved reflection tool.

#### Parameters

    * llmResponse: [LlmResponse](../interfaces/LlmResponse.html)

#### Returns boolean

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:200](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L200)




### `Protected`incrementModelFailureCount

  * incrementModelFailureCount(scopeKey: string, itemName: string): Promise<number>

Increment the failure count for a model within a scope.

#### Parameters

    * scopeKey: string
    * itemName: string

#### Returns Promise<number>

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:341](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L341)




### onEventCallback

  * onEventCallback(  
_params: { event: [Event](../interfaces/Event.html); invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<[Event](../interfaces/Event.html) | undefined>

Callback executed after an event is yielded from runner.

This is the ideal place to make modification to the event before the event is handled by the underlying agent app.

#### Parameters

    * _params: { event: [Event](../interfaces/Event.html); invocationContext: [InvocationContext](InvocationContext.html) }
      * ##### event: [Event](../interfaces/Event.html)

The event raised by the runner.

      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation.

#### Returns Promise<[Event](../interfaces/Event.html) | undefined>

An optional value. A non-`undefined` return may be used by the framework to modify or replace the response. Copy the incoming `event` when constructing a replacement to preserve fields that are not being modified, such as event actions. Returning `undefined` allows the original response to be used.

Inherited from [BasePlugin](BasePlugin.html).[onEventCallback](BasePlugin.html#oneventcallback)

    * Defined in [core/src/plugins/base_plugin.ts:178](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L178)




### onModelErrorCallback

  * onModelErrorCallback(  
_params: {  
callbackContext: [Context](Context.html);  
error: Error;  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed when a model call encounters an error.

This callback provides an opportunity to handle model errors gracefully, potentially providing alternative responses or recovery mechanisms.

#### Parameters

    * _params: { callbackContext: [Context](Context.html); error: Error; llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }
      * ##### callbackContext: [Context](Context.html)

The context for the current agent call.

      * ##### error: Error

The exception that was raised during model execution.

      * ##### llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The request that was sent to the model when the error occurred.

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional LlmResponse. If an LlmResponse is returned, it will be used instead of propagating the error. Returning `undefined` allows the original error to be raised.

Inherited from [BasePlugin](BasePlugin.html).[onModelErrorCallback](BasePlugin.html#onmodelerrorcallback)

    * Defined in [core/src/plugins/base_plugin.ts:332](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L332)




### onToolErrorCallback

  * onToolErrorCallback(  
_params: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Callback executed when a tool call encounters an error. tool: BaseTool; toolArgs: Record<string, unknown>; toolContext: Context; result: Record<string, unknown>; }): Promise<Record<string, unknown> | undefined> { return; }

/** Callback executed when a tool call encounters an error.

This callback provides an opportunity to handle tool errors gracefully, potentially providing alternative responses or recovery mechanisms.

#### Parameters

    * _params: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
}
      * ##### error: Error

The exception that was raised during tool execution.

      * ##### tool: [BaseTool](BaseTool.html)

The tool instance that encountered an error.

      * ##### toolArgs: Record<string, unknown>

The arguments that were passed to the tool.

      * ##### toolContext: [Context](Context.html)

The context specific to the tool execution.

#### Returns Promise<Record<string, unknown> | undefined>

An optional dictionary. If a dictionary is returned, it will be used as the tool response instead of propagating the error. Returning `undefined` allows the original error to be raised.

Inherited from [BasePlugin](BasePlugin.html).[onToolErrorCallback](BasePlugin.html#ontoolerrorcallback)

    * Defined in [core/src/plugins/base_plugin.ts:464](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L464)




### onUserMessageCallback

  * onUserMessageCallback(  
_params: { invocationContext: [InvocationContext](InvocationContext.html); userMessage: Content },  
): Promise<Content | undefined>

Callback executed when a user message is received before an invocation starts.

This callback helps logging and modifying the user message before the runner starts the invocation.

#### Parameters

    * _params: { invocationContext: [InvocationContext](InvocationContext.html); userMessage: Content }
      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation.

      * ##### userMessage: Content

The message content input by user.

#### Returns Promise<Content | undefined>

An optional `Content` to be returned to the ADK. Returning a value to replace the user message. Returning `undefined` to proceed normally.

Inherited from [BasePlugin](BasePlugin.html).[onUserMessageCallback](BasePlugin.html#onusermessagecallback)

    * Defined in [core/src/plugins/base_plugin.ts:139](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L139)




### `Protected`provideReflectionTool

  * provideReflectionTool(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): void

Provides the adk_handle_model_error tool for reflection and retries.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

#### Returns void

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:176](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L176)




### `Protected`resetModelFailureCount

  * resetModelFailureCount(scopeKey: string, itemName: string): Promise<void>

Reset the failure count for a model within a scope.

#### Parameters

    * scopeKey: string
    * itemName: string

#### Returns Promise<void>

    * Defined in [core/src/plugins/reflect_retry_model_plugin.ts:351](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_model_plugin.ts#L351)




Constructors

constructor

Properties

maxRetriesnameonModelErrorsscopethrowExceptionIfRetryExceeded

Methods

adkHandleModelErrorafterAgentCallbackafterContextCompactionafterModelCallbackafterNodeCallbackafterRunCallbackafterToolCallbackbeforeAgentCallbackbeforeContextCompactionbeforeModelCallbackbeforeNodeCallbackbeforeRunCallbackbeforeToolCallbackbeforeToolSelectioncheckForModelErrorgenerateModelRetryPartgetModelNameFromContextgetModelRetryUuidgetModelScopeKeyhandleModelErrorhandleModelRetryhandleReservedToolCallhasReservedToolCallincrementModelFailureCountonEventCallbackonModelErrorCallbackonToolErrorCallbackonUserMessageCallbackprovideReflectionToolresetModelFailureCount

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


