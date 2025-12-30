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



  * Defined in [core/src/plugins/logging_plugin.ts:47](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L47)



## Constructors

### constructor

  * new LoggingPlugin(name?: string): [LoggingPlugin]()

Initialize the logging plugin.

#### Parameters

    * name: string = 'logging_plugin'

The name of the plugin instance.

#### Returns [LoggingPlugin]()

Overrides [BasePlugin](BasePlugin.html).[constructor](BasePlugin.html#constructor)

    * Defined in [core/src/plugins/logging_plugin.ts:53](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L53)




## Properties

### `Readonly`name

name: string

Inherited from [BasePlugin](BasePlugin.html).[name](BasePlugin.html#name)

  * Defined in [core/src/plugins/base_plugin.ts:102](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/base_plugin.ts#L102)



## Methods

### afterAgentCallback

  * afterAgentCallback(  
agent: { agent: [BaseAgent](BaseAgent.html); callbackContext: [CallbackContext](CallbackContext.html) },  
): Promise<Content | undefined>

Callback executed after an agent's primary logic has completed.

This callback can be used to inspect, log, or modify the agent's final result before it is returned.

#### Parameters

    * agent: { agent: [BaseAgent](BaseAgent.html); callbackContext: [CallbackContext](CallbackContext.html) }

The agent that has just run.

#### Returns Promise<Content | undefined>

An optional `Content` object. If a value is returned, it will replace the agent's original result. Returning `undefined` uses the original, unmodified result.

Overrides [BasePlugin](BasePlugin.html).[afterAgentCallback](BasePlugin.html#afteragentcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:132](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L132)




### afterModelCallback

  * afterModelCallback(  
callbackContext: {  
callbackContext: [CallbackContext](CallbackContext.html);  
llmResponse: [LlmResponse](../interfaces/LlmResponse.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed after a response is received from the model.

This is the ideal place to log model responses, collect metrics on token usage, or perform post-processing on the raw `LlmResponse`.

#### Parameters

    * callbackContext: { callbackContext: [CallbackContext](CallbackContext.html); llmResponse: [LlmResponse](../interfaces/LlmResponse.html) }

The context for the current agent call.

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional value. A non-`undefined` return may be used by the framework to modify or replace the response. Returning `undefined` allows the original response to be used.

Overrides [BasePlugin](BasePlugin.html).[afterModelCallback](BasePlugin.html#aftermodelcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:164](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L164)




### afterRunCallback

  * afterRunCallback(  
invocationContext: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<void>

Callback executed after an ADK runner run has completed.

This is the final callback in the ADK lifecycle, suitable for cleanup, final logging, or reporting tasks.

#### Parameters

    * invocationContext: { invocationContext: [InvocationContext](InvocationContext.html) }

The context for the entire invocation.

#### Returns Promise<void>

undefined

Overrides [BasePlugin](BasePlugin.html).[afterRunCallback](BasePlugin.html#afterruncallback)

    * Defined in [core/src/plugins/logging_plugin.ts:111](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L111)




### afterToolCallback

  * afterToolCallback(  
tool: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [ToolContext](ToolContext.html);  
},  
): Promise<Record<string, unknown> | undefined>

Callback executed after a tool has been called.

This callback allows for inspecting, logging, or modifying the result returned by a tool.

#### Parameters

    * tool: {  
result: Record<string, unknown>;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [ToolContext](ToolContext.html);  
}

The tool instance that has just been executed.

#### Returns Promise<Record<string, unknown> | undefined>

An optional dictionary. If a dictionary is returned, it will **replace** the original result from the tool. This allows for post-processing or altering tool outputs. Returning `undefined` uses the original, unmodified result.

Overrides [BasePlugin](BasePlugin.html).[afterToolCallback](BasePlugin.html#aftertoolcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:203](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L203)




### beforeAgentCallback

  * beforeAgentCallback(  
agent: { agent: [BaseAgent](BaseAgent.html); callbackContext: [CallbackContext](CallbackContext.html) },  
): Promise<Content | undefined>

Callback executed before an agent's primary logic is invoked.

This callback can be used for logging, setup, or to short-circuit the agent's execution by returning a value.

#### Parameters

    * agent: { agent: [BaseAgent](BaseAgent.html); callbackContext: [CallbackContext](CallbackContext.html) }

The agent that is about to run.

#### Returns Promise<Content | undefined>

An optional `Content` object. If a value is returned, it will bypass the agent's callbacks and its execution, and return this value directly. Returning `undefined` allows the agent to proceed normally.

Overrides [BasePlugin](BasePlugin.html).[beforeAgentCallback](BasePlugin.html#beforeagentcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:120](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L120)




### beforeModelCallback

  * beforeModelCallback(  
callbackContext: {  
callbackContext: [CallbackContext](CallbackContext.html);  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed before a request is sent to the model.

This provides an opportunity to inspect, log, or modify the `LlmRequest` object. It can also be used to implement caching by returning a cached `LlmResponse`, which would skip the actual model call.

#### Parameters

    * callbackContext: { callbackContext: [CallbackContext](CallbackContext.html); llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }

The context for the current agent call.

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional value. The interpretation of a non-`undefined` trigger an early exit and returns the response immediately. Returning `undefined` allows the LLM request to proceed normally.

Overrides [BasePlugin](BasePlugin.html).[beforeModelCallback](BasePlugin.html#beforemodelcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:141](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L141)




### beforeRunCallback

  * beforeRunCallback(  
invocationContext: { invocationContext: [InvocationContext](InvocationContext.html) },  
): Promise<Content | undefined>

Callback executed before the ADK runner runs.

This is the first callback to be called in the lifecycle, ideal for global setup or initialization tasks.

#### Parameters

    * invocationContext: { invocationContext: [InvocationContext](InvocationContext.html) }

The context for the entire invocation, containing session information, the root agent, etc.

#### Returns Promise<Content | undefined>

An optional `Event` to be returned to the ADK. Returning a value to halt execution of the runner and ends the runner with that event. Return `undefined` to proceed normally.

Overrides [BasePlugin](BasePlugin.html).[beforeRunCallback](BasePlugin.html#beforeruncallback)

    * Defined in [core/src/plugins/logging_plugin.ts:74](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L74)




### beforeToolCallback

  * beforeToolCallback(  
tool: {  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [ToolContext](ToolContext.html);  
},  
): Promise<Record<string, unknown> | undefined>

Callback executed before a tool is called.

This callback is useful for logging tool usage, input validation, or modifying the arguments before they are passed to the tool.

#### Parameters

    * tool: { tool: [BaseTool](BaseTool.html); toolArgs: Record<string, unknown>; toolContext: [ToolContext](ToolContext.html) }

The tool instance that is about to be executed.

#### Returns Promise<Record<string, unknown> | undefined>

An optional dictionary. If a dictionary is returned, it will stop the tool execution and return this response immediately. Returning `undefined` uses the original, unmodified arguments.

Overrides [BasePlugin](BasePlugin.html).[beforeToolCallback](BasePlugin.html#beforetoolcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:192](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L192)




### onEventCallback

  * onEventCallback(  
invocationContext: {  
event: [Event](../interfaces/Event.html);  
invocationContext: [InvocationContext](InvocationContext.html);  
},  
): Promise<[Event](../interfaces/Event.html) | undefined>

Callback executed after an event is yielded from runner.

This is the ideal place to make modification to the event before the event is handled by the underlying agent app.

#### Parameters

    * invocationContext: { event: [Event](../interfaces/Event.html); invocationContext: [InvocationContext](InvocationContext.html) }

The context for the entire invocation.

#### Returns Promise<[Event](../interfaces/Event.html) | undefined>

An optional value. A non-`undefined` return may be used by the framework to modify or replace the response. Returning `undefined` allows the original response to be used.

Overrides [BasePlugin](BasePlugin.html).[onEventCallback](BasePlugin.html#oneventcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:83](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L83)




### onModelErrorCallback

  * onModelErrorCallback(  
callbackContext: {  
callbackContext: [CallbackContext](CallbackContext.html);  
error: Error;  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html);  
},  
): Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

Callback executed when a model call encounters an error.

This callback provides an opportunity to handle model errors gracefully, potentially providing alternative responses or recovery mechanisms.

#### Parameters

    * callbackContext: { callbackContext: [CallbackContext](CallbackContext.html); error: Error; llmRequest: [LlmRequest](../interfaces/LlmRequest.html) }

The context for the current agent call.

#### Returns Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

An optional LlmResponse. If an LlmResponse is returned, it will be used instead of propagating the error. Returning `undefined` allows the original error to be raised.

Overrides [BasePlugin](BasePlugin.html).[onModelErrorCallback](BasePlugin.html#onmodelerrorcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:215](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L215)




### onToolErrorCallback

  * onToolErrorCallback(  
tool: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [ToolContext](ToolContext.html);  
},  
): Promise<Record<string, unknown> | undefined>

Callback executed when a tool call encounters an error.

This callback provides an opportunity to handle tool errors gracefully, potentially providing alternative responses or recovery mechanisms.

#### Parameters

    * tool: {  
error: Error;  
tool: [BaseTool](BaseTool.html);  
toolArgs: Record<string, unknown>;  
toolContext: [ToolContext](ToolContext.html);  
}

The tool instance that encountered an error.

#### Returns Promise<Record<string, unknown> | undefined>

An optional dictionary. If a dictionary is returned, it will be used as the tool response instead of propagating the error. Returning `undefined` allows the original error to be raised.

Overrides [BasePlugin](BasePlugin.html).[onToolErrorCallback](BasePlugin.html#ontoolerrorcallback)

    * Defined in [core/src/plugins/logging_plugin.ts:225](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L225)




### onUserMessageCallback

  * onUserMessageCallback(  
invocationContext: {  
invocationContext: [InvocationContext](InvocationContext.html);  
userMessage: Content;  
},  
): Promise<Content | undefined>

Callback executed when a user message is received before an invocation starts.

This callback helps logging and modifying the user message before the runner starts the invocation.

#### Parameters

    * invocationContext: { invocationContext: [InvocationContext](InvocationContext.html); userMessage: Content }

The context for the entire invocation.

#### Returns Promise<Content | undefined>

An optional `Content` to be returned to the ADK. Returning a value to replace the user message. Returning `undefined` to proceed normally.

Overrides [BasePlugin](BasePlugin.html).[onUserMessageCallback](BasePlugin.html#onusermessagecallback)

    * Defined in [core/src/plugins/logging_plugin.ts:57](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/plugins/logging_plugin.ts#L57)




Constructors

constructor

Properties

name

Methods

afterAgentCallbackafterModelCallbackafterRunCallbackafterToolCallbackbeforeAgentCallbackbeforeModelCallbackbeforeRunCallbackbeforeToolCallbackonEventCallbackonModelErrorCallbackonToolErrorCallbackonUserMessageCallback

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


