[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ReflectAndRetryToolPlugin]()



# Class ReflectAndRetryToolPlugin

Provides self-healing, concurrent-safe error recovery for tool failures.

This plugin intercepts tool failures, provides structured guidance to the LLM for reflection and correction, and retries the operation up to a configurable limit.

**Key Features:**

  * **Concurrency Safe:** Uses locking to safely handle parallel tool executions.
  * **Configurable Scope:** Tracks failures per-invocation (default) or globally using the [TrackingScope](../enums/TrackingScope.html) enum.
  * **Extensible Scoping:** The `getScopeKey` method can be overridden to implement custom tracking logic (e.g., per-user or per-session).
  * **Granular Tracking:** Failure counts are tracked per-tool within the defined scope. A success with one tool resets its counter without affecting others.
  * **Custom Error Extraction:** Supports detecting errors in normal tool responses that do not throw exceptions, by overriding `extractErrorFromResult`.



#### Example
    
    
    import {ReflectAndRetryToolPlugin, TrackingScope} from '@google/adk';  
      
    // Example 1: Track failures per invocation (default)  
    const errorPlugin = new ReflectAndRetryToolPlugin({maxRetries: 3});  
      
    // Example 2: Track failures globally across all turns  
    const globalPlugin = new ReflectAndRetryToolPlugin({  
      maxRetries: 5,  
      trackingScope: TrackingScope.GLOBAL,  
    });  
      
    // Example 3: Do not throw exception when retry limit is exceeded  
    const softFailPlugin = new ReflectAndRetryToolPlugin({  
      maxRetries: 3,  
      throwExceptionIfRetryExceeded: false,  
    });
    Copy

#### Hierarchy ([View Summary](../hierarchy.html#ReflectAndRetryToolPlugin))

  * [BasePlugin](BasePlugin.html)
    * ReflectAndRetryToolPlugin



  * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:86](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L86)



## Constructors

### constructor

  * new ReflectAndRetryToolPlugin(  
options?: [ReflectAndRetryToolPluginOptions](../interfaces/ReflectAndRetryToolPluginOptions.html),  
): [ReflectAndRetryToolPlugin]()

Initializes the ReflectAndRetryToolPlugin.

#### Parameters

    * options: [ReflectAndRetryToolPluginOptions](../interfaces/ReflectAndRetryToolPluginOptions.html) = {}

Configuration options for the plugin.

#### Returns [ReflectAndRetryToolPlugin]()

Overrides [BasePlugin](BasePlugin.html).[constructor](BasePlugin.html#constructor)

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:97](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L97)




## Properties

### `Readonly`maxRetries

maxRetries: number

  * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:87](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L87)



### `Readonly`name

name: string

Inherited from [BasePlugin](BasePlugin.html).[name](BasePlugin.html#name)

  * Defined in [core/src/plugins/base_plugin.ts:115](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L115)



### `Readonly`scope

scope: [TrackingScope](../enums/TrackingScope.html)

  * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:89](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L89)



### `Readonly`throwExceptionIfRetryExceeded

throwExceptionIfRetryExceeded: boolean

  * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:88](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L88)



## Methods

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
_params: { callbackContext: [Context](Context.html); llmResponse: [LlmResponse](../interfaces/LlmResponse.html) },  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed after a response is received from the model.

This is the ideal place to log model responses, collect metrics on token usage, or perform post-processing on the raw `LlmResponse`.

#### Parameters

    * _params: { callbackContext: [Context](Context.html); llmResponse: [LlmResponse](../interfaces/LlmResponse.html) }
      * ##### callbackContext: [Context](Context.html)

The context for the current agent call.

      * ##### llmResponse: [LlmResponse](../interfaces/LlmResponse.html)

The response object received from the model.

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional value. A non-`undefined` return may be used by the framework to modify or replace the response. Returning `undefined` allows the original response to be used.

Inherited from [BasePlugin](BasePlugin.html).[afterModelCallback](BasePlugin.html#aftermodelcallback)

    * Defined in [core/src/plugins/base_plugin.ts:311](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L311)




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
params: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Handles successful tool calls or extracts and processes errors.

#### Parameters

    * params: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
}

The tool callback parameters.

#### Returns Promise<Record<string, unknown> | undefined>

An optional record containing reflection guidance if an error is detected, or undefined if the tool call was successful or the response is already a reflection message.

Overrides [BasePlugin](BasePlugin.html).[afterToolCallback](BasePlugin.html#aftertoolcallback)

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:120](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L120)




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
_params: { callbackContext: [Context](Context.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) },  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed before a request is sent to the model.

This provides an opportunity to inspect, log, or modify the `LlmRequest` object. It can also be used to implement caching by returning a cached `LlmResponse`, which would skip the actual model call.

#### Parameters

    * _params: { callbackContext: [Context](Context.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }
      * ##### callbackContext: [Context](Context.html)

The context for the current agent call.

      * ##### llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The prepared request object to be sent to the model.

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional value. The interpretation of a non-`undefined` trigger an early exit and returns the response immediately. Returning `undefined` allows the LLM request to proceed normally.

Inherited from [BasePlugin](BasePlugin.html).[beforeModelCallback](BasePlugin.html#beforemodelcallback)

    * Defined in [core/src/plugins/base_plugin.ts:292](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L292)




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




### `Protected`createToolReflectionResponse

  * createToolReflectionResponse(  
tool: [BaseTool](BaseTool.html),  
toolArgs: Record<string, unknown>,  
error: unknown,  
retryCount: number,  
): Record<string, unknown>

Generates structured reflection guidance for tool failures.

#### Parameters

    * tool: [BaseTool](BaseTool.html)

The tool that failed.

    * toolArgs: Record<string, unknown>

The arguments supplied to the tool.

    * error: unknown

The error encountered.

    * retryCount: number

The current retry count.

#### Returns Record<string, unknown>

The structured tool failure response record.

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:297](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L297)




### `Protected`ensureException

  * ensureException(error: unknown): Error

Ensures the given error is an Error instance, wrapping if not.

#### Parameters

    * error: unknown

The error object.

#### Returns Error

An Error instance.

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:270](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L270)




### extractErrorFromResult

  * extractErrorFromResult(  
params: {  
result: unknown;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<unknown>

Extracts an error from a successful tool result and triggers retry logic.

This is useful when a tool call finishes without throwing an exception but the result contains an error payload like `{status: 'error', message: '...'}` that should be handled by the plugin.

#### Parameters

    * params: {  
result: unknown;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
}

Tool execution context and result.

#### Returns Promise<unknown>

The extracted error if any, or undefined if no error was detected.

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:166](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L166)




### `Protected`formatErrorDetails

  * formatErrorDetails(error: unknown): string

Formats error details for inclusion in the reflection message.

#### Parameters

    * error: unknown

The error object.

#### Returns string

Formatted error string.

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:280](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L280)




### `Protected`getScopeKey

  * getScopeKey(toolContext: [Context](Context.html)): string

Returns a unique key for the state tracker based on the configured scope.

This method can be overridden in a subclass to implement custom scoping logic, for example tracking failures on a per-user or per-session basis.

#### Parameters

    * toolContext: [Context](Context.html)

The tool context.

#### Returns string

The resolved scope key.

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:246](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L246)




### `Protected`getToolRetryExceedMsg

  * getToolRetryExceedMsg(  
tool: [BaseTool](BaseTool.html),  
toolArgs: Record<string, unknown>,  
error: unknown,  
): Record<string, unknown>

Generates guidance when the maximum retry limit is exceeded.

#### Parameters

    * tool: [BaseTool](BaseTool.html)

The tool that failed.

    * toolArgs: Record<string, unknown>

The arguments supplied to the tool.

    * error: unknown

The error encountered.

#### Returns Record<string, unknown>

The structured retry-exceeded failure response record.

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:350](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L350)




### `Protected`handleToolError

  * handleToolError(  
tool: [BaseTool](BaseTool.html),  
toolArgs: Record<string, unknown>,  
toolContext: [Context](Context.html),  
error: unknown,  
): Promise<Record<string, unknown> | undefined>

Central, thread-safe logic for processing tool errors.

#### Parameters

    * tool: [BaseTool](BaseTool.html)

The tool that was called.

    * toolArgs: Record<string, unknown>

The arguments passed to the tool.

    * toolContext: [Context](Context.html)

The context of the tool call.

    * error: unknown

The error to be handled.

#### Returns Promise<Record<string, unknown> | undefined>

An optional record containing reflection guidance for the error.

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:204](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L204)




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
params: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Handles tool exceptions by providing reflection guidance.

#### Parameters

    * params: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
}

The error callback parameters.

#### Returns Promise<Record<string, unknown> | undefined>

An optional record containing reflection guidance for the error.

Overrides [BasePlugin](BasePlugin.html).[onToolErrorCallback](BasePlugin.html#ontoolerrorcallback)

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:181](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L181)




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




### `Protected`resetFailuresForTool

  * resetFailuresForTool(toolContext: [Context](Context.html), toolName: string): Promise<void>

Atomically resets the failure count for a tool and cleans up state.

#### Parameters

    * toolContext: [Context](Context.html)

The tool context.

    * toolName: string

The name of the tool.

#### Returns Promise<void>

    * Defined in [core/src/plugins/reflect_retry_tool_plugin.ts:256](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/reflect_retry_tool_plugin.ts#L256)




Constructors

constructor

Properties

maxRetriesnamescopethrowExceptionIfRetryExceeded

Methods

afterAgentCallbackafterContextCompactionafterModelCallbackafterNodeCallbackafterRunCallbackafterToolCallbackbeforeAgentCallbackbeforeContextCompactionbeforeModelCallbackbeforeNodeCallbackbeforeRunCallbackbeforeToolCallbackbeforeToolSelectioncreateToolReflectionResponseensureExceptionextractErrorFromResultformatErrorDetailsgetScopeKeygetToolRetryExceedMsghandleToolErroronEventCallbackonModelErrorCallbackonToolErrorCallbackonUserMessageCallbackresetFailuresForTool

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


