[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LoggingPlugin]()



# Class LoggingPlugin

A plugin that logs important information at each callback point.

This plugin helps printing all critical events in the console. It is not a replacement of existing logging in ADK. It rather helps terminal based debugging by showing all logs in the console, and serves as a simple demo for everyone to leverage when developing new plugins.

This plugin helps users track the invocation status by logging:

  * User messages and invocation context
  * Agent execution flow
  * LLM requests and responses
  * Tool calls with arguments and results
  * Events and final responses
  * Errors during model and tool execution



Example:
    
    
    const loggingPlugin = new LoggingPlugin();  
    const runner = new Runner({  
      agents: [myAgent],  
      // ...  
      plugins: [loggingPlugin],  
    });
    Copy

#### Hierarchy ([View Summary](../hierarchy.html#LoggingPlugin))

  * [BasePlugin](BasePlugin.html)
    * LoggingPlugin



  * Defined in [core/src/plugins/logging_plugin.ts:51](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L51)



## Constructors

### constructor

  * new LoggingPlugin(name?: string): [LoggingPlugin]()

Initialize the logging plugin.

#### Parameters

    * name: string = 'logging_plugin'

The name of the plugin instance.

#### Returns [LoggingPlugin]()

Overrides [BasePlugin](BasePlugin.html).[constructor](BasePlugin.html#constructor)

    * Defined in [core/src/plugins/logging_plugin.ts:57](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L57)




## Properties

### `Readonly`name

name: string

Inherited from [BasePlugin](BasePlugin.html).[name](BasePlugin.html#name)

  * Defined in [core/src/plugins/base_plugin.ts:111](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/base_plugin.ts#L111)



## Methods

### afterAgentCallback

  * afterAgentCallback(  
__namedParameters: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) },  
): Promise<Content | undefined>

Callback executed after an agent's primary logic has completed.

This callback can be used to inspect, log, or modify the agent's final result before it is returned.

#### Parameters

    * __namedParameters: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) }

#### Returns Promise<Content | undefined>

An optional `Content` object. If a value is returned, it will replace the agent's original result. Returning `undefined` uses the original, unmodified result.

Overrides [BasePlugin](BasePlugin.html).[afterAgentCallback](BasePlugin.html#afteragentcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:149](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L149)




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
__namedParameters: {  
callbackContext: [Context](Context.html);  
llmResponse: [LlmResponse](../interfaces/LlmResponse.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed after a response is received from the model.

This is the ideal place to log model responses, collect metrics on token usage, or perform post-processing on the raw `LlmResponse`.

#### Parameters

    * __namedParameters: { callbackContext: [Context](Context.html); llmResponse: [LlmResponse](../interfaces/LlmResponse.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional value. A non-`undefined` return may be used by the framework to modify or replace the response. Returning `undefined` allows the original response to be used.

Overrides [BasePlugin](BasePlugin.html).[afterModelCallback](BasePlugin.html#aftermodelcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:188](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L188)




### afterRunCallback

  * afterRunCallback(  
__namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<void>

Callback executed after an ADK runner run has completed.

This is the final callback in the ADK lifecycle, suitable for cleanup, final logging, or reporting tasks.

#### Parameters

    * __namedParameters: { invocationContext: [InvocationContext](InvocationContext.html) }

#### Returns Promise<void>

undefined

Overrides [BasePlugin](BasePlugin.html).[afterRunCallback](BasePlugin.html#afterruncallback)

    * Defined in [core/src/plugins/logging_plugin.ts:123](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L123)




### afterToolCallback

  * afterToolCallback(  
__namedParameters: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
},  
): Promise<Record<string, unknown> | undefined>

Callback executed after a tool has been called.

This callback allows for inspecting, logging, or modifying the result returned by a tool.

#### Parameters

    * __namedParameters: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
}

#### Returns Promise<Record<string, unknown> | undefined>

An optional dictionary. If a dictionary is returned, it will **replace** the original result from the tool. This allows for post-processing or altering tool outputs. Returning `undefined` uses the original, unmodified result.

Overrides [BasePlugin](BasePlugin.html).[afterToolCallback](BasePlugin.html#aftertoolcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:237](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L237)




### beforeAgentCallback

  * beforeAgentCallback(  
__namedParameters: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) },  
): Promise<Content | undefined>

Callback executed before an agent's primary logic is invoked.

This callback can be used for logging, setup, or to short-circuit the agent's execution by returning a value.

#### Parameters

    * __namedParameters: { agent: [BaseAgent](BaseAgent.html); callbackContext: [Context](Context.html) }

#### Returns Promise<Content | undefined>

An optional `Content` object. If a value is returned, it will bypass the agent's callbacks and its execution, and return this value directly. Returning `undefined` allows the agent to proceed normally.

Overrides [BasePlugin](BasePlugin.html).[beforeAgentCallback](BasePlugin.html#beforeagentcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:134](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L134)




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
__namedParameters: { callbackContext: [Context](Context.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) },  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed before a request is sent to the model.

This provides an opportunity to inspect, log, or modify the `LlmRequest` object. It can also be used to implement caching by returning a cached `LlmResponse`, which would skip the actual model call.

#### Parameters

    * __namedParameters: { callbackContext: [Context](Context.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional value. The interpretation of a non-`undefined` trigger an early exit and returns the response immediately. Returning `undefined` allows the LLM request to proceed normally.

Overrides [BasePlugin](BasePlugin.html).[beforeModelCallback](BasePlugin.html#beforemodelcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:161](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L161)




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

    * Defined in [core/src/plugins/logging_plugin.ts:81](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L81)




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

    * Defined in [core/src/plugins/logging_plugin.ts:220](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L220)




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

An optional value. A non-`undefined` return may be used by the framework to modify or replace the response. Returning `undefined` allows the original response to be used.

Overrides [BasePlugin](BasePlugin.html).[onEventCallback](BasePlugin.html#oneventcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:92](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L92)




### onModelErrorCallback

  * onModelErrorCallback(  
__namedParameters: {  
callbackContext: [Context](Context.html);  
error: Error;  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed when a model call encounters an error.

This callback provides an opportunity to handle model errors gracefully, potentially providing alternative responses or recovery mechanisms.

#### Parameters

    * __namedParameters: { callbackContext: [Context](Context.html); error: Error; llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional LlmResponse. If an LlmResponse is returned, it will be used instead of propagating the error. Returning `undefined` allows the original error to be raised.

Overrides [BasePlugin](BasePlugin.html).[onModelErrorCallback](BasePlugin.html#onmodelerrorcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:255](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L255)




### onToolErrorCallback

  * onToolErrorCallback(  
__namedParameters: {  
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

    * __namedParameters: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [Context](Context.html);  
}

#### Returns Promise<Record<string, unknown> | undefined>

An optional dictionary. If a dictionary is returned, it will be used as the tool response instead of propagating the error. Returning `undefined` allows the original error to be raised.

Overrides [BasePlugin](BasePlugin.html).[onToolErrorCallback](BasePlugin.html#ontoolerrorcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:270](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L270)




### onUserMessageCallback

  * onUserMessageCallback(  
__namedParameters: {  
invocationContext: [InvocationContext](InvocationContext.html);  
userMessage: Content;  
},  
): Promise<Content | undefined>

Callback executed when a user message is received before an invocation starts.

This callback helps logging and modifying the user message before the runner starts the invocation.

#### Parameters

    * __namedParameters: { invocationContext: [InvocationContext](InvocationContext.html); userMessage: Content }

#### Returns Promise<Content | undefined>

An optional `Content` to be returned to the ADK. Returning a value to replace the user message. Returning `undefined` to proceed normally.

Overrides [BasePlugin](BasePlugin.html).[onUserMessageCallback](BasePlugin.html#onusermessagecallback)

    * Defined in [core/src/plugins/logging_plugin.ts:61](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/plugins/logging_plugin.ts#L61)




Constructors

constructor

Properties

name

Methods

afterAgentCallbackafterContextCompactionafterModelCallbackafterRunCallbackafterToolCallbackbeforeAgentCallbackbeforeContextCompactionbeforeModelCallbackbeforeRunCallbackbeforeToolCallbackbeforeToolSelectiononEventCallbackonModelErrorCallbackonToolErrorCallbackonUserMessageCallback

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


