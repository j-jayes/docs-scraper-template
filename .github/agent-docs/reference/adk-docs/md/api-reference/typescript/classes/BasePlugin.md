[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BasePlugin]()



# Class BasePlugin`Abstract`

Base class for creating plugins.

Plugins provide a structured way to intercept and modify agent, tool, and LLM behaviors at critical execution points in a callback manner. While agent callbacks apply to a particular agent, plugins applies globally to all agents added in the runner. Plugins are best used for adding custom behaviors like logging, monitoring, caching, or modifying requests and responses at key stages.

A plugin can implement one or more methods of callbacks, but should not implement the same method of callback for multiple times.

Relation with [Agent callbacks](https://google.github.io/adk-docs/callbacks/):

**Execution Order** Similar to Agent callbacks, Plugins are executed in the order they are registered. However, Plugin and Agent Callbacks are executed sequentially, with Plugins takes precedence over agent callbacks. When the callback in a plugin returns a value, it will short circuit all remaining plugins and agent callbacks, causing all remaining plugins and agent callbacks to be skipped.

**Change Propagation** Plugins and agent callbacks can both modify the value of the input parameters, including agent input, tool input, and LLM request/response, etc. They work in the exactly same way. The modifications will be visible and passed to the next callback in the chain. For example, if a plugin modifies the tool input with before_tool_callback, the modified tool input will be passed to the before_tool_callback of the next plugin, and further passed to the agent callbacks if not short circuited.

To use a plugin, implement the desired callback methods and pass an instance of your custom plugin class to the ADK Runner.

Example: A simple plugin that logs every tool call.
    
    
    class ToolLoggerPlugin extends BasePlugin {  
      constructor() {  
        super('tool_logger');  
      }  
      
      override async beforeToolCallback(  
        {tool, toolArgs, toolContext}: {  
          tool: BaseTool,  
          toolArgs: Record<string, unknown>,  
          toolContext: Context,  
        },  
      ): Promise<Record<string, unknown> | undefined> {  
        this.logger.info(  
          `[${this.name}] Calling tool '${tool.name}' with args:  
    ${JSON.stringify( toolArgs,  
          )}`,  
        );  
        return;  
      }  
      
      override async afterToolCallback(  
        {tool, toolArgs, toolContext, result}: {  
          tool: BaseTool,  
          toolArgs: Record<string, unknown>,  
          toolContext: Context,  
          result: Record<string, unknown>,  
        },  
      ): Promise<Record<string, unknown> | undefined> {  
        this.logger.info(  
          `[${this.name}] Tool '${tool.name}' finished with result:  
    ${JSON.stringify( result,  
          )}`,  
        );  
        return;  
      }  
    }  
      
    // Add the plugin to ADK Runner  
    // runner = new Runner({  
    //   ...  
    //   plugins: [new ToolLoggerPlugin(), new AgentPolicyPlugin()],  
    // });
    Copy

#### Hierarchy ([View Summary](../hierarchy.html#BasePlugin))

  * BasePlugin
    * [LoggingPlugin](LoggingPlugin.html)
    * [SecurityPlugin](SecurityPlugin.html)



  * Defined in [plugins/base_plugin.ts:100](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L100)



## Constructors

### constructor

  * new BasePlugin(name: string): [BasePlugin]()

Initializes the plugin.

#### Parameters

    * name: string

A unique identifier for this plugin instance.

#### Returns [BasePlugin]()

    * Defined in [plugins/base_plugin.ts:108](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L108)




## Properties

### `Readonly`name

name: string

  * Defined in [plugins/base_plugin.ts:101](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L101)



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

    * Defined in [plugins/base_plugin.ts:221](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L221)




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

    * Defined in [plugins/base_plugin.ts:262](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L262)




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

    * Defined in [plugins/base_plugin.ts:182](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L182)




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

    * Defined in [plugins/base_plugin.ts:331](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L331)




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

    * Defined in [plugins/base_plugin.ts:201](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L201)




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

    * Defined in [plugins/base_plugin.ts:242](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L242)




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

    * Defined in [plugins/base_plugin.ts:146](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L146)




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

    * Defined in [plugins/base_plugin.ts:307](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L307)




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

    * Defined in [plugins/base_plugin.ts:165](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L165)




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

    * Defined in [plugins/base_plugin.ts:284](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L284)




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

    * Defined in [plugins/base_plugin.ts:365](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L365)




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

    * Defined in [plugins/base_plugin.ts:126](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/plugins/base_plugin.ts#L126)




Constructors

constructor

Properties

name

Methods

afterAgentCallbackafterModelCallbackafterRunCallbackafterToolCallbackbeforeAgentCallbackbeforeModelCallbackbeforeRunCallbackbeforeToolCallbackonEventCallbackonModelErrorCallbackonToolErrorCallbackonUserMessageCallback

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


