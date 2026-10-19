[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolCallIntegrityPlugin]()



# Class ToolCallIntegrityPlugin

Stamps function calls and verifies them before runs and tool calls.

`onEventCallback` adds `"v1:" + HMAC-SHA256(key, payload)` for each function call to `event.customMetadata["__adk_internal_fc_hmac"]`, and throws [ToolCallIntegrityError](ToolCallIntegrityError.html) for a response that repeats a call ID before it is stored. `beforeRunCallback` recomputes the HMAC for every function call with an ID in the session history, answered or not, and throws when a stamp is wrong, malformed, repeated or left over from a call that no longer matches. `beforeToolCallback` lets a tool run only when every stored copy of its call verifies and the tool's name and arguments match one of them; it always refuses a call with no ID. Unstamped calls are rejected unless `allowUnstampedCalls` is set, in which case they are logged.

Events without function calls are ignored. Events marked as restored are not verified, and their function calls are never executed. ADK marks events restored by `adk run --replay`, and prepareRestoredEvent marks events that your code copies. Anyone who can write to the session store can also set the marker, but `beforeToolCallback` still refuses those events' calls.

`PluginManager` re-throws plugin errors as a generic `Error`; the [ToolCallIntegrityError](ToolCallIntegrityError.html) is its `cause`.

Register this plugin before other plugins. `PluginManager` stops at the first `onEventCallback` that returns an event, and a later plugin must not change function calls or replace `customMetadata`.

Requires the Web Crypto API (`globalThis.crypto.subtle`), available in browsers and in Node.js 19 and later.

Example:
    
    
    const plugin = new ToolCallIntegrityPlugin({secretKey: keyBytes});  
    const app = {name: 'my_app', rootAgent: agent, plugins: [plugin]};  
      
    // Key rotation: stamp with the new key, accept both.  
    new ToolCallIntegrityPlugin({secretKey: [newKeyBytes, oldKeyBytes]});
    Copy

#### Hierarchy ([View Summary](../hierarchy.html#ToolCallIntegrityPlugin))

  * [BasePlugin](BasePlugin.html)
    * ToolCallIntegrityPlugin



  * Defined in [core/src/plugins/tool_call_integrity_plugin.ts:221](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/tool_call_integrity_plugin.ts#L221)



## Constructors

### constructor

  * new ToolCallIntegrityPlugin(  
options: [ToolCallIntegrityPluginOptions](../interfaces/ToolCallIntegrityPluginOptions.html),  
): [ToolCallIntegrityPlugin]()

#### Parameters

    * options: [ToolCallIntegrityPluginOptions](../interfaces/ToolCallIntegrityPluginOptions.html)

#### Returns [ToolCallIntegrityPlugin]()

#### Throws

If `secretKey` is empty or contains a key that is not non-empty bytes.

Overrides [BasePlugin](BasePlugin.html).[constructor](BasePlugin.html#constructor)

    * Defined in [core/src/plugins/tool_call_integrity_plugin.ts:230](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/tool_call_integrity_plugin.ts#L230)




## Properties

### `Readonly`name

name: string

Inherited from [BasePlugin](BasePlugin.html).[name](BasePlugin.html#name)

  * Defined in [core/src/plugins/base_plugin.ts:115](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/base_plugin.ts#L115)



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
__namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<Content | undefined>

Callback executed before the ADK runner runs.

This is the first callback to be called in the lifecycle, ideal for global setup or initialization tasks.

#### Parameters

    * __namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) }

#### Returns Promise<Content | undefined>

An optional `Event` to be returned to the ADK. Returning a value to halt execution of the runner and ends the runner with that event. Return `undefined` to proceed normally.

Overrides [BasePlugin](BasePlugin.html).[beforeRunCallback](BasePlugin.html#beforeruncallback)

    * Defined in [core/src/plugins/tool_call_integrity_plugin.ts:355](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/tool_call_integrity_plugin.ts#L355)




### beforeToolCallback

  * beforeToolCallback(  
__namedParameters: {  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Callback executed before a tool is called.

This callback is useful for logging tool usage, input validation, or modifying the arguments before they are passed to the tool.

#### Parameters

    * __namedParameters: { tool: [BaseTool](BaseTool.html); toolArgs: Record<string, unknown>; toolContext: [Context](Context.html) }

#### Returns Promise<Record<string, unknown> | undefined>

An optional dictionary. If a dictionary is returned, it will stop the tool execution and return this response immediately. Returning `undefined` uses the original, unmodified arguments.

Overrides [BasePlugin](BasePlugin.html).[beforeToolCallback](BasePlugin.html#beforetoolcallback)

    * Defined in [core/src/plugins/tool_call_integrity_plugin.ts:410](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/tool_call_integrity_plugin.ts#L410)




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




### onEventCallback

  * onEventCallback(  
__namedParameters: {  
event: [Event](../interfaces/Event.html);  
invocationContext: [InvocationContext](InvocationContext.html);  
},  
): Promise<[Event](../interfaces/Event.html) | undefined>

Callback executed after an event is yielded from runner.

This is the ideal place to make modification to the event before the event is handled by the underlying agent app.

#### Parameters

    * __namedParameters: { event: [Event](../interfaces/Event.html); invocationContext: [InvocationContext](InvocationContext.html) }

#### Returns Promise<[Event](../interfaces/Event.html) | undefined>

An optional value. A non-`undefined` return may be used by the framework to modify or replace the response. Copy the incoming `event` when constructing a replacement to preserve fields that are not being modified, such as event actions. Returning `undefined` allows the original response to be used.

Overrides [BasePlugin](BasePlugin.html).[onEventCallback](BasePlugin.html#oneventcallback)

    * Defined in [core/src/plugins/tool_call_integrity_plugin.ts:316](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/tool_call_integrity_plugin.ts#L316)




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




### `Static`prepareRestoredEvent

  * prepareRestoredEvent(event: [Event](../interfaces/Event.html)): [Event](../interfaces/Event.html)

Returns a copy with internal metadata removed and marked as restored.

Use it on events that your code copies into another session, so that the history passes the integrity check. The copy only keeps the history: its function calls are never executed.

#### Parameters

    * event: [Event](../interfaces/Event.html)

The event to copy. It is not modified.

#### Returns [Event](../interfaces/Event.html)

The marked copy, ready to append to the new session.

    * Defined in [core/src/plugins/tool_call_integrity_plugin.ts:262](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/plugins/tool_call_integrity_plugin.ts#L262)




Constructors

constructor

Properties

name

Methods

afterAgentCallbackafterContextCompactionafterModelCallbackafterNodeCallbackafterRunCallbackafterToolCallbackbeforeAgentCallbackbeforeContextCompactionbeforeModelCallbackbeforeNodeCallbackbeforeRunCallbackbeforeToolCallbackbeforeToolSelectiononEventCallbackonModelErrorCallbackonToolErrorCallbackonUserMessageCallbackprepareRestoredEvent

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


