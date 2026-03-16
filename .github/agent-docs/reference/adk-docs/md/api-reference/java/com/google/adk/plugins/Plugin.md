JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Plugin.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.plugins](package-summary.html)
  2. [Plugin](Plugin.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. getName()
     2. onUserMessageCallback(InvocationContext, Content)
     3. beforeRunCallback(InvocationContext)
     4. onEventCallback(InvocationContext, Event)
     5. afterRunCallback(InvocationContext)
     6. close()
     7. beforeAgentCallback(BaseAgent, CallbackContext)
     8. afterAgentCallback(BaseAgent, CallbackContext)
     9. beforeModelCallback(CallbackContext, LlmRequest.Builder)
     10. afterModelCallback(CallbackContext, LlmResponse)
     11. onModelErrorCallback(CallbackContext, LlmRequest.Builder, Throwable)
     12. beforeToolCallback(BaseTool, Map, ToolContext)
     13. afterToolCallback(BaseTool, Map, ToolContext, Map)
     14. onToolErrorCallback(BaseTool, Map, ToolContext, Throwable)

Hide sidebar  Show sidebar

# Interface Plugin

All Known Implementing Classes:
    `[BasePlugin](BasePlugin.html "class in com.google.adk.plugins"), [ContextFilterPlugin](ContextFilterPlugin.html "class in com.google.adk.plugins"), [GlobalInstructionPlugin](GlobalInstructionPlugin.html "class in com.google.adk.plugins"), [LoggingPlugin](LoggingPlugin.html "class in com.google.adk.plugins"), [PluginManager](PluginManager.html "class in com.google.adk.plugins"), [ReplayPlugin](ReplayPlugin.html "class in com.google.adk.plugins")`

* * *

public interface Plugin

Interface for creating plugins. 

Plugins provide a structured way to intercept and modify agent, tool, and LLM behaviors at critical execution points in a callback manner. While agent callbacks apply to a particular agent, plugins applies globally to all agents added in the runner. Plugins are best used for adding custom behaviors like logging, monitoring, caching, or modifying requests and responses at key stages. 

A plugin can implement one or more methods of callbacks, but should not implement the same method of callback for multiple times.

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsDefault Methods

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`afterAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed after an agent's primary logic has completed.

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`afterModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Callback executed after a response is received from the model.

`default io.reactivex.rxjava3.core.Completable`

`afterRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed after an ADK runner run has completed.

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`afterToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> result)`

Callback executed after a tool has been called.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`beforeAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed before an agent's primary logic is invoked.

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`beforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Callback executed before a request is sent to the model.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`beforeRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed before the ADK runner runs.

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`beforeToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Callback executed before a tool is called.

`default io.reactivex.rxjava3.core.Completable`

`close()`

Method executed when the runner is closed.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`getName()`

 

`default io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")>`

`onEventCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../events/Event.html "class in com.google.adk.events") event)`

Callback executed after an event is yielded from runner.

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`onModelErrorCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

Callback executed when a model call encounters an error.

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`onToolErrorCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

Callback executed when a tool call encounters an error.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`onUserMessageCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

Callback executed when a user message is received before an invocation starts.




  * ## Method Details

    * ### getName

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getName()

    * ### onUserMessageCallback

default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> onUserMessageCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)

Callback executed when a user message is received before an invocation starts.

Parameters:
    `invocationContext` \- The context for the entire invocation.
    `userMessage` \- The message content input by user.
Returns:
    An optional Content to replace the user message. Returning Empty to proceed normally.

    * ### beforeRunCallback

default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> beforeRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Callback executed before the ADK runner runs.

Parameters:
    `invocationContext` \- The context for the entire invocation.
Returns:
    An optional Content to halt execution. Returning Empty to proceed normally.

    * ### onEventCallback

default io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")> onEventCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../events/Event.html "class in com.google.adk.events") event)

Callback executed after an event is yielded from runner.

Parameters:
    `invocationContext` \- The context for the entire invocation.
    `event` \- The event raised by the runner.
Returns:
    An optional Event to modify or replace the response. Returning Empty to proceed normally.

    * ### afterRunCallback

default io.reactivex.rxjava3.core.Completable afterRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Callback executed after an ADK runner run has completed.

Parameters:
    `invocationContext` \- The context for the entire invocation.

    * ### close

default io.reactivex.rxjava3.core.Completable close()

Method executed when the runner is closed. 

This method is used for cleanup tasks such as closing network connections or releasing resources.

    * ### beforeAgentCallback

default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> beforeAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)

Callback executed before an agent's primary logic is invoked.

Parameters:
    `agent` \- The agent that is about to run.
    `callbackContext` \- The context for the agent invocation.
Returns:
    An optional Content object to bypass the agent's execution. Returning Empty to proceed normally.

    * ### afterAgentCallback

default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> afterAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)

Callback executed after an agent's primary logic has completed.

Parameters:
    `agent` \- The agent that has just run.
    `callbackContext` \- The context for the agent invocation.
Returns:
    An optional Content object to replace the agent's original result. Returning Empty to use the original result.

    * ### beforeModelCallback

default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> beforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)

Callback executed before a request is sent to the model.

Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmRequest` \- The mutable request builder, allowing modification of the request before it is sent to the model.
Returns:
    An optional LlmResponse to trigger an early exit. Returning Empty to proceed normally.

    * ### afterModelCallback

default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> afterModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../models/LlmResponse.html "class in com.google.adk.models") llmResponse)

Callback executed after a response is received from the model.

Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmResponse` \- The response object received from the model.
Returns:
    An optional LlmResponse to modify or replace the response. Returning Empty to use the original response.

    * ### onModelErrorCallback

default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> onModelErrorCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)

Callback executed when a model call encounters an error.

Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmRequest` \- The mutable request builder for the request that failed.
    `error` \- The exception that was raised.
Returns:
    An optional LlmResponse to use instead of propagating the error. Returning Empty to allow the original error to be raised.

    * ### beforeToolCallback

default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> beforeToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)

Callback executed before a tool is called.

Parameters:
    `tool` \- The tool instance that is about to be executed.
    `toolArgs` \- The dictionary of arguments to be used for invoking the tool.
    `toolContext` \- The context specific to the tool execution.
Returns:
    An optional Map to stop the tool execution and return this response immediately. Returning Empty to proceed normally.

    * ### afterToolCallback

default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> afterToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> result)

Callback executed after a tool has been called.

Parameters:
    `tool` \- The tool instance that has just been executed.
    `toolArgs` \- The original arguments that were passed to the tool.
    `toolContext` \- The context specific to the tool execution.
    `result` \- The dictionary returned by the tool invocation.
Returns:
    An optional Map to replace the original result from the tool. Returning Empty to use the original result.

    * ### onToolErrorCallback

default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> onToolErrorCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)

Callback executed when a tool call encounters an error.

Parameters:
    `tool` \- The tool instance that encountered an error.
    `toolArgs` \- The arguments that were passed to the tool.
    `toolContext` \- The context specific to the tool execution.
    `error` \- The exception that was raised during tool execution.
Returns:
    An optional Map to be used as the tool response instead of propagating the error. Returning Empty to allow the original error to be raised.




* * *

Copyright (C) 1980\. All rights reserved.
