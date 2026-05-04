JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BigQueryAgentAnalyticsPlugin.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.plugins.agentanalytics](package-summary.html)
  2. [BigQueryAgentAnalyticsPlugin](BigQueryAgentAnalyticsPlugin.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
     1. Methods inherited from class BasePlugin
     2. Methods inherited from class Object
  5. Constructor Details
     1. BigQueryAgentAnalyticsPlugin(BigQueryLoggerConfig)
     2. BigQueryAgentAnalyticsPlugin(BigQueryLoggerConfig, BigQuery)
  6. Method Details
     1. close()
     2. onUserMessageCallback(InvocationContext, Content)
     3. onEventCallback(InvocationContext, Event)
     4. beforeRunCallback(InvocationContext)
     5. afterRunCallback(InvocationContext)
     6. beforeAgentCallback(BaseAgent, CallbackContext)
     7. afterAgentCallback(BaseAgent, CallbackContext)
     8. beforeModelCallback(CallbackContext, LlmRequest.Builder)
     9. afterModelCallback(CallbackContext, LlmResponse)
     10. onModelErrorCallback(CallbackContext, LlmRequest.Builder, Throwable)
     11. beforeToolCallback(BaseTool, Map, ToolContext)
     12. afterToolCallback(BaseTool, Map, ToolContext, Map)
     13. onToolErrorCallback(BaseTool, Map, ToolContext, Throwable)

Hide sidebar  Show sidebar

# Class BigQueryAgentAnalyticsPlugin

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.plugins.BasePlugin](../BasePlugin.html "class in com.google.adk.plugins")

com.google.adk.plugins.agentanalytics.BigQueryAgentAnalyticsPlugin

All Implemented Interfaces:
    `[Plugin](../Plugin.html "interface in com.google.adk.plugins")`

* * *

public class BigQueryAgentAnalyticsPlugin extends [BasePlugin](../BasePlugin.html "class in com.google.adk.plugins")

BigQuery Agent Analytics Plugin for Java. 

Logs agent execution events directly to a BigQuery table using the Storage Write API.

  * ## Field Summary

### Fields inherited from class [BasePlugin](../BasePlugin.html#field-summary "class in com.google.adk.plugins")

`[name](../BasePlugin.html#name)`

Modifier and Type

Field

Description

`protected final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](../BasePlugin.html#name)`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`BigQueryAgentAnalyticsPlugin([BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics") config)`

 

`BigQueryAgentAnalyticsPlugin([BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics") config, com.google.cloud.bigquery.BigQuery bigQuery)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`afterAgentCallback([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed after an agent's primary logic has completed.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

`afterModelCallback([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Callback executed after a response is received from the model.

`io.reactivex.rxjava3.core.Completable`

`afterRunCallback([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed after an ADK runner run has completed.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`afterToolCallback([BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> result)`

Callback executed after a tool has been called.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`beforeAgentCallback([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed before an agent's primary logic is invoked.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

`beforeModelCallback([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Callback before LLM call.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`beforeRunCallback([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed before the ADK runner runs.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`beforeToolCallback([BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Callback executed before a tool is called.

`io.reactivex.rxjava3.core.Completable`

`close()`

Method executed when the runner is closed.

`io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

`onEventCallback([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") event)`

Callback executed after an event is yielded from runner.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

`onModelErrorCallback([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Callback executed when a model call encounters an error.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`onToolErrorCallback([BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Callback executed when a tool call encounters an error.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`onUserMessageCallback([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

Callback executed when a user message is received before an invocation starts.

### Methods inherited from class [BasePlugin](../BasePlugin.html#method-summary "class in com.google.adk.plugins")

`[getName](../BasePlugin.html#getName\(\) "getName\(\)")`

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[getName](../BasePlugin.html#getName\(\))()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### BigQueryAgentAnalyticsPlugin

public BigQueryAgentAnalyticsPlugin([BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics") config) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")`

    * ### BigQueryAgentAnalyticsPlugin

public BigQueryAgentAnalyticsPlugin([BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics") config, com.google.cloud.bigquery.BigQuery bigQuery) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")

Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class in java.io")`

  * ## Method Details

    * ### close

public io.reactivex.rxjava3.core.Completable close()

Description copied from interface: `[Plugin](../Plugin.html#close\(\))`

Method executed when the runner is closed. 

This method is used for cleanup tasks such as closing network connections or releasing resources.

    * ### onUserMessageCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> onUserMessageCallback([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)

Description copied from interface: `[Plugin](../Plugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\))`

Callback executed when a user message is received before an invocation starts.

Parameters:
    `invocationContext` \- The context for the entire invocation.
    `userMessage` \- The message content input by user.
Returns:
    An optional Content to replace the user message. Returning Empty to proceed normally.

    * ### onEventCallback

public io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")> onEventCallback([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") event)

Description copied from interface: `[Plugin](../Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))`

Callback executed after an event is yielded from runner.

Parameters:
    `invocationContext` \- The context for the entire invocation.
    `event` \- The event raised by the runner.
Returns:
    An optional Event to modify or replace the response. Returning Empty to proceed normally.

    * ### beforeRunCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> beforeRunCallback([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from interface: `[Plugin](../Plugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\))`

Callback executed before the ADK runner runs.

Parameters:
    `invocationContext` \- The context for the entire invocation.
Returns:
    An optional Content to halt execution. Returning Empty to proceed normally.

    * ### afterRunCallback

public io.reactivex.rxjava3.core.Completable afterRunCallback([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from interface: `[Plugin](../Plugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))`

Callback executed after an ADK runner run has completed.

Parameters:
    `invocationContext` \- The context for the entire invocation.

    * ### beforeAgentCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> beforeAgentCallback([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)

Description copied from interface: `[Plugin](../Plugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))`

Callback executed before an agent's primary logic is invoked.

Parameters:
    `agent` \- The agent that is about to run.
    `callbackContext` \- The context for the agent invocation.
Returns:
    An optional Content object to bypass the agent's execution. Returning Empty to proceed normally.

    * ### afterAgentCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> afterAgentCallback([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)

Description copied from interface: `[Plugin](../Plugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))`

Callback executed after an agent's primary logic has completed.

Parameters:
    `agent` \- The agent that has just run.
    `callbackContext` \- The context for the agent invocation.
Returns:
    An optional Content object to replace the agent's original result. Returning Empty to use the original result.

    * ### beforeModelCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")> beforeModelCallback([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)

Callback before LLM call. 

Logs the LLM request details including: 1. Prompt content 2. System instruction (if available) 

The content is formatted as 'Prompt: {prompt} | System Prompt: {system_prompt}'.

Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmRequest` \- The mutable request builder, allowing modification of the request before it is sent to the model.
Returns:
    An optional LlmResponse to trigger an early exit. Returning Empty to proceed normally.

    * ### afterModelCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")> afterModelCallback([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)

Description copied from interface: `[Plugin](../Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))`

Callback executed after a response is received from the model.

Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmResponse` \- The response object received from the model.
Returns:
    An optional LlmResponse to modify or replace the response. Returning Empty to use the original response.

    * ### onModelErrorCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")> onModelErrorCallback([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)

Description copied from interface: `[Plugin](../Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))`

Callback executed when a model call encounters an error.

Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmRequest` \- The mutable request builder for the request that failed.
    `error` \- The exception that was raised.
Returns:
    An optional LlmResponse to use instead of propagating the error. Returning Empty to allow the original error to be raised.

    * ### beforeToolCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> beforeToolCallback([BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from interface: `[Plugin](../Plugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))`

Callback executed before a tool is called.

Parameters:
    `tool` \- The tool instance that is about to be executed.
    `toolArgs` \- The dictionary of arguments to be used for invoking the tool.
    `toolContext` \- The context specific to the tool execution.
Returns:
    An optional Map to stop the tool execution and return this response immediately. Returning Empty to proceed normally.

    * ### afterToolCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> afterToolCallback([BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> result)

Description copied from interface: `[Plugin](../Plugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))`

Callback executed after a tool has been called.

Parameters:
    `tool` \- The tool instance that has just been executed.
    `toolArgs` \- The original arguments that were passed to the tool.
    `toolContext` \- The context specific to the tool execution.
    `result` \- The dictionary returned by the tool invocation.
Returns:
    An optional Map to replace the original result from the tool. Returning Empty to use the original result.

    * ### onToolErrorCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> onToolErrorCallback([BaseTool](../../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)

Description copied from interface: `[Plugin](../Plugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))`

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
