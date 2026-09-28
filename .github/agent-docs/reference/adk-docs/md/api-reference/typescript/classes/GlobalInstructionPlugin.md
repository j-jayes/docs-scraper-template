[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [GlobalInstructionPlugin]()



# Class GlobalInstructionPlugin

Plugin that provides global instructions functionality at the App level.

This plugin replaces the deprecated globalInstruction field on LlmAgent. Global instructions are applied to all agents in the application, providing a consistent way to set application-wide instructions, identity, or personality.

The plugin operates through the beforeModelCallback, allowing it to modify LLM requests before they are sent to the model.

#### Hierarchy ([View Summary](../hierarchy.html#GlobalInstructionPlugin))

  * [BasePlugin](BasePlugin.html)
    * GlobalInstructionPlugin



  * Defined in [core/src/plugins/global_instruction_plugin.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/global_instruction_plugin.ts#L26)



## Constructors

### constructor

  * new GlobalInstructionPlugin(  
globalInstruction?: string | [InstructionProvider](../types/InstructionProvider.html),  
name?: string,  
): [GlobalInstructionPlugin]()

Initializes the GlobalInstructionPlugin.

#### Parameters

    * `Optional`globalInstruction: string | [InstructionProvider](../types/InstructionProvider.html)

The instruction to apply globally. Can be a string or an InstructionProvider function that takes ReadonlyContext and returns a string (sync or async).

    * name: string = 'global_instruction'

The name of the plugin (defaults to 'global_instruction').

#### Returns [GlobalInstructionPlugin]()

Overrides [BasePlugin](BasePlugin.html).[constructor](BasePlugin.html#constructor)

    * Defined in [core/src/plugins/global_instruction_plugin.ts:37](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/global_instruction_plugin.ts#L37)




## Properties

### `Readonly`name

name: string

Inherited from [BasePlugin](BasePlugin.html).[name](BasePlugin.html#name)

  * Defined in [core/src/plugins/base_plugin.ts:111](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L111)



## Methods

### afterAgentCallback

  * afterAgentCallback(  
params: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) },  
): Promise<Content | undefined>

Callback executed after an agent's primary logic has completed.

This callback can be used to inspect, log, or modify the agent's final result before it is returned.

#### Parameters

    * params: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) }
      * ##### agent: [BaseAgent](BaseAgent.html)

The agent that has just run.

      * ##### callbackContext: [Context](Context.html)

The context for the agent invocation.

#### Returns Promise<Content | undefined>

An optional `Content` object. If a value is returned, it will replace the agent's original result. Returning `undefined` uses the original, unmodified result.

Inherited from [BasePlugin](BasePlugin.html).[afterAgentCallback](BasePlugin.html#afteragentcallback)

    * Defined in [core/src/plugins/base_plugin.ts:231](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L231)




### afterContextCompaction

  * afterContextCompaction(  
params: {  
invocationContext: [InvocationContext](InvocationContext.html);  
trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html);  
},  
): Promise<void>

Callback executed after context compaction.

This callback provides an opportunity to inspect the context after it has been compacted.

#### Parameters

    * params: { invocationContext: [InvocationContext](InvocationContext.html); trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html) }
      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation.

      * ##### trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html)

The trigger for the context compaction.

#### Returns Promise<void>

Inherited from [BasePlugin](BasePlugin.html).[afterContextCompaction](BasePlugin.html#aftercontextcompaction)

    * Defined in [core/src/plugins/base_plugin.ts:352](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L352)




### afterModelCallback

  * afterModelCallback(  
params: { callbackContext: [Context](Context.html); llmResponse: [LlmResponse](../interfaces/LlmResponse.html) },  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed after a response is received from the model.

This is the ideal place to log model responses, collect metrics on token usage, or perform post-processing on the raw `LlmResponse`.

#### Parameters

    * params: { callbackContext: [Context](Context.html); llmResponse: [LlmResponse](../interfaces/LlmResponse.html) }
      * ##### callbackContext: [Context](Context.html)

The context for the current agent call.

      * ##### llmResponse: [LlmResponse](../interfaces/LlmResponse.html)

The response object received from the model.

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional value. A non-`undefined` return may be used by the framework to modify or replace the response. Returning `undefined` allows the original response to be used.

Inherited from [BasePlugin](BasePlugin.html).[afterModelCallback](BasePlugin.html#aftermodelcallback)

    * Defined in [core/src/plugins/base_plugin.ts:272](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L272)




### afterRunCallback

  * afterRunCallback(  
params: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<void>

Callback executed after an ADK runner run has completed.

This is the final callback in the ADK lifecycle, suitable for cleanup, final logging, or reporting tasks.

#### Parameters

    * params: { invocationContext: [InvocationContext](InvocationContext.html) }
      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation.

#### Returns Promise<void>

undefined

Inherited from [BasePlugin](BasePlugin.html).[afterRunCallback](BasePlugin.html#afterruncallback)

    * Defined in [core/src/plugins/base_plugin.ts:192](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L192)




### afterToolCallback

  * afterToolCallback(  
params: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Callback executed after a tool has been called.

This callback allows for inspecting, logging, or modifying the result returned by a tool.

#### Parameters

    * params: {  
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

    * Defined in [core/src/plugins/base_plugin.ts:398](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L398)




### beforeAgentCallback

  * beforeAgentCallback(  
params: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) },  
): Promise<Content | undefined>

Callback executed before an agent's primary logic is invoked.

This callback can be used for logging, setup, or to short-circuit the agent's execution by returning a value.

#### Parameters

    * params: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) }
      * ##### agent: [BaseAgent](BaseAgent.html)

The agent that is about to run.

      * ##### callbackContext: [Context](Context.html)

The context for the agent invocation.

#### Returns Promise<Content | undefined>

An optional `Content` object. If a value is returned, it will bypass the agent's callbacks and its execution, and return this value directly. Returning `undefined` allows the agent to proceed normally.

Inherited from [BasePlugin](BasePlugin.html).[beforeAgentCallback](BasePlugin.html#beforeagentcallback)

    * Defined in [core/src/plugins/base_plugin.ts:211](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L211)




### beforeContextCompaction

  * beforeContextCompaction(  
params: {  
invocationContext: [InvocationContext](InvocationContext.html);  
trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html);  
},  
): Promise<void>

Callback executed before context compaction.

This callback provides an opportunity to inspect or modify the context before it is compacted.

#### Parameters

    * params: { invocationContext: [InvocationContext](InvocationContext.html); trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html) }
      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation.

      * ##### trigger: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html)

The trigger for the context compaction.

#### Returns Promise<void>

Inherited from [BasePlugin](BasePlugin.html).[beforeContextCompaction](BasePlugin.html#beforecontextcompaction)

    * Defined in [core/src/plugins/base_plugin.ts:334](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L334)




### beforeModelCallback

  * beforeModelCallback(  
params: { callbackContext: [Context](Context.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) },  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed before a request is sent to the model.

This provides an opportunity to inspect, log, or modify the `LlmRequest` object. It can also be used to implement caching by returning a cached `LlmResponse`, which would skip the actual model call.

#### Parameters

    * params: { callbackContext: [Context](Context.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }
      * ##### callbackContext: [Context](Context.html)

The context for the current agent call.

      * ##### llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The prepared request object to be sent to the model.

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional value. The interpretation of a non-`undefined` trigger an early exit and returns the response immediately. Returning `undefined` allows the LLM request to proceed normally.

Overrides [BasePlugin](BasePlugin.html).[beforeModelCallback](BasePlugin.html#beforemodelcallback)

    * Defined in [core/src/plugins/global_instruction_plugin.ts:45](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/global_instruction_plugin.ts#L45)




### beforeRunCallback

  * beforeRunCallback(  
params: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<Content | undefined>

Callback executed before the ADK runner runs.

This is the first callback to be called in the lifecycle, ideal for global setup or initialization tasks.

#### Parameters

    * params: { invocationContext: [InvocationContext](InvocationContext.html) }
      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation, containing session information, the root agent, etc.

#### Returns Promise<Content | undefined>

An optional `Event` to be returned to the ADK. Returning a value to halt execution of the runner and ends the runner with that event. Return `undefined` to proceed normally.

Inherited from [BasePlugin](BasePlugin.html).[beforeRunCallback](BasePlugin.html#beforeruncallback)

    * Defined in [core/src/plugins/base_plugin.ts:156](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L156)




### beforeToolCallback

  * beforeToolCallback(  
params: {  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Callback executed before a tool is called.

This callback is useful for logging tool usage, input validation, or modifying the arguments before they are passed to the tool.

#### Parameters

    * params: { tool: [BaseTool](BaseTool.html); toolArgs: Record<string, unknown>; toolContext: [Context](Context.html) }
      * ##### tool: [BaseTool](BaseTool.html)

The tool instance that is about to be executed.

      * ##### toolArgs: Record<string, unknown>

The dictionary of arguments to be used for invoking the tool.

      * ##### toolContext: [Context](Context.html)

The context specific to the tool execution.

#### Returns Promise<Record<string, unknown> | undefined>

An optional dictionary. If a dictionary is returned, it will stop the tool execution and return this response immediately. Returning `undefined` uses the original, unmodified arguments.

Inherited from [BasePlugin](BasePlugin.html).[beforeToolCallback](BasePlugin.html#beforetoolcallback)

    * Defined in [core/src/plugins/base_plugin.ts:374](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L374)




### beforeToolSelection

  * beforeToolSelection(  
params: {  
callbackContext: [Context](Context.html);  
tools: Readonly<Record<string, [BaseTool](BaseTool.html)>>;  
},  
): Promise<Readonly<Record<string, [BaseTool](BaseTool.html)>> | undefined>

Callback executed before a tool is selected.

This callback provides an opportunity to inspect, log, or modify the available tools before they are selected.

#### Parameters

    * params: { callbackContext: [Context](Context.html); tools: Readonly<Record<string, [BaseTool](BaseTool.html)>> }
      * ##### callbackContext: [Context](Context.html)

The context for the current agent call.

      * ##### tools: Readonly<Record<string, [BaseTool](BaseTool.html)>>

The available tools.

#### Returns Promise<Readonly<Record<string, [BaseTool](BaseTool.html)>> | undefined>

An optional value. A non-`undefined` return may be used by the framework to modify or replace the available tools. Returning `undefined` allows the original tools to be used.

Inherited from [BasePlugin](BasePlugin.html).[beforeToolSelection](BasePlugin.html#beforetoolselection)

    * Defined in [core/src/plugins/base_plugin.ts:316](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L316)




### onEventCallback

  * onEventCallback(  
params: { event: [Event](../interfaces/Event.html); invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<[Event](../interfaces/Event.html) | undefined>

Callback executed after an event is yielded from runner.

This is the ideal place to make modification to the event before the event is handled by the underlying agent app.

#### Parameters

    * params: { event: [Event](../interfaces/Event.html); invocationContext: [InvocationContext](InvocationContext.html) }
      * ##### event: [Event](../interfaces/Event.html)

The event raised by the runner.

      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation.

#### Returns Promise<[Event](../interfaces/Event.html) | undefined>

An optional value. A non-`undefined` return may be used by the framework to modify or replace the response. Returning `undefined` allows the original response to be used.

Inherited from [BasePlugin](BasePlugin.html).[onEventCallback](BasePlugin.html#oneventcallback)

    * Defined in [core/src/plugins/base_plugin.ts:175](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L175)




### onModelErrorCallback

  * onModelErrorCallback(  
params: {  
callbackContext: [Context](Context.html);  
error: Error;  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed when a model call encounters an error.

This callback provides an opportunity to handle model errors gracefully, potentially providing alternative responses or recovery mechanisms.

#### Parameters

    * params: { callbackContext: [Context](Context.html); error: Error; llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }
      * ##### callbackContext: [Context](Context.html)

The context for the current agent call.

      * ##### error: Error

The exception that was raised during model execution.

      * ##### llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The request that was sent to the model when the error occurred.

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional LlmResponse. If an LlmResponse is returned, it will be used instead of propagating the error. Returning `undefined` allows the original error to be raised.

Inherited from [BasePlugin](BasePlugin.html).[onModelErrorCallback](BasePlugin.html#onmodelerrorcallback)

    * Defined in [core/src/plugins/base_plugin.ts:294](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L294)




### onToolErrorCallback

  * onToolErrorCallback(  
params: {  
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

    * params: {  
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

    * Defined in [core/src/plugins/base_plugin.ts:432](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L432)




### onUserMessageCallback

  * onUserMessageCallback(  
params: { invocationContext: [InvocationContext](InvocationContext.html); userMessage: Content },  
): Promise<Content | undefined>

Callback executed when a user message is received before an invocation starts.

This callback helps logging and modifying the user message before the runner starts the invocation.

#### Parameters

    * params: { invocationContext: [InvocationContext](InvocationContext.html); userMessage: Content }
      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The context for the entire invocation.

      * ##### userMessage: Content

The message content input by user.

#### Returns Promise<Content | undefined>

An optional `Content` to be returned to the ADK. Returning a value to replace the user message. Returning `undefined` to proceed normally.

Inherited from [BasePlugin](BasePlugin.html).[onUserMessageCallback](BasePlugin.html#onusermessagecallback)

    * Defined in [core/src/plugins/base_plugin.ts:136](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L136)




Constructors

constructor

Properties

name

Methods

afterAgentCallbackafterContextCompactionafterModelCallbackafterRunCallbackafterToolCallbackbeforeAgentCallbackbeforeContextCompactionbeforeModelCallbackbeforeRunCallbackbeforeToolCallbackbeforeToolSelectiononEventCallbackonModelErrorCallbackonToolErrorCallbackonUserMessageCallback

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


