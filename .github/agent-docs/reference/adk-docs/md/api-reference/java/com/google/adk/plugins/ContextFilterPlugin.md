JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ContextFilterPlugin.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.plugins](package-summary.html)
  2. [ContextFilterPlugin](ContextFilterPlugin.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Constructor Summary
  5. Method Summary
  6. Constructor Details
     1. ContextFilterPlugin(ContextFilterPlugin.Builder)
  7. Method Details
     1. builder()
     2. beforeModelCallback(CallbackContext, LlmRequest.Builder)

Hide sidebar  Show sidebar

# Class ContextFilterPlugin

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.plugins.BasePlugin](BasePlugin.html "class in com.google.adk.plugins")

com.google.adk.plugins.ContextFilterPlugin

All Implemented Interfaces:
    `[Plugin](Plugin.html "interface in com.google.adk.plugins")`

* * *

public class ContextFilterPlugin extends [BasePlugin](BasePlugin.html "class in com.google.adk.plugins")

A plugin that filters the LLM request `Content` list to reduce its size, for example to adhere to context window limits. 

This plugin can be configured to trim the conversation history based on one or both of the following criteria: 

  * **`numInvocationsToKeep(N)`:** Retains only the last `N` model turns and any preceding user turns. If multiple user messages appear consecutively before a model message, all of them are kept as part of that model invocation window. 
  * **`customFilter()`:** Applies a custom [`UnaryOperator`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/UnaryOperator.html "interface in java.util.function") to filter the list of `Content` objects. If `numInvocationsToKeep` is also specified, the custom filter is applied _after_ the invocation-based trimming occurs. 


**Function Call Handling:** The plugin ensures that if a `FunctionResponse` is included in the filtered list, its corresponding `FunctionCall` is also included. If filtering would otherwise exclude the `FunctionCall`, the window is automatically expanded to include it, preventing orphaned function responses. 

If no filtering options are provided, this plugin has no effect. If the `customFilter` throws an exception during execution, filtering is aborted, and the [`LlmRequest`](../models/LlmRequest.html "class in com.google.adk.models") is not modified.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins")`

Builder for [`ContextFilterPlugin`](ContextFilterPlugin.html "class in com.google.adk.plugins").

  * ## Field Summary

### Fields inherited from class [BasePlugin](BasePlugin.html#field-summary "class in com.google.adk.plugins")

`[name](BasePlugin.html#name)`

Modifier and Type

Field

Description

`protected final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](BasePlugin.html#name)`

 

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`ContextFilterPlugin([ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins") builder)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`beforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Filters the LLM request context by trimming recent turns and applying any custom filter.

`static [ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins")`

`builder()`

 

### Methods inherited from class [BasePlugin](BasePlugin.html#method-summary "class in com.google.adk.plugins")

`[getName](BasePlugin.html#getName\(\) "getName\(\)")`

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[getName](BasePlugin.html#getName\(\))()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [Plugin](Plugin.html#method-summary "interface in com.google.adk.plugins")

`[afterAgentCallback](Plugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\) "afterAgentCallback\(BaseAgent, CallbackContext\)"), [afterModelCallback](Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\) "afterModelCallback\(CallbackContext, LlmResponse\)"), [afterRunCallback](Plugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\) "afterRunCallback\(InvocationContext\)"), [afterToolCallback](Plugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\) "afterToolCallback\(BaseTool, Map, ToolContext, Map\)"), [beforeAgentCallback](Plugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\) "beforeAgentCallback\(BaseAgent, CallbackContext\)"), [beforeRunCallback](Plugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\) "beforeRunCallback\(InvocationContext\)"), [beforeToolCallback](Plugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\) "beforeToolCallback\(BaseTool, Map, ToolContext\)"), [close](Plugin.html#close\(\) "close\(\)"), [onEventCallback](Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\) "onEventCallback\(InvocationContext, Event\)"), [onModelErrorCallback](Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\) "onModelErrorCallback\(CallbackContext, LlmRequest.Builder, Throwable\)"), [onToolErrorCallback](Plugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\) "onToolErrorCallback\(BaseTool, Map, ToolContext, Throwable\)"), [onUserMessageCallback](Plugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\) "onUserMessageCallback\(InvocationContext, Content\)")`

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`[afterAgentCallback](Plugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed after an agent's primary logic has completed.

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`[afterModelCallback](Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Callback executed after a response is received from the model.

`default io.reactivex.rxjava3.core.Completable`

`[afterRunCallback](Plugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed after an ADK runner run has completed.

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[afterToolCallback](Plugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> result)`

Callback executed after a tool has been called.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`[beforeAgentCallback](Plugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed before an agent's primary logic is invoked.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`[beforeRunCallback](Plugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\))([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed before the ADK runner runs.

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[beforeToolCallback](Plugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Callback executed before a tool is called.

`default io.reactivex.rxjava3.core.Completable`

`[close](Plugin.html#close\(\))()`

Method executed when the runner is closed.

`default io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")>`

`[onEventCallback](Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../events/Event.html "class in com.google.adk.events") event)`

Callback executed after an event is yielded from runner.

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`[onModelErrorCallback](Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Callback executed when a model call encounters an error.

`default io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[onToolErrorCallback](Plugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Callback executed when a tool call encounters an error.

`default io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`[onUserMessageCallback](Plugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\))([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

Callback executed when a user message is received before an invocation starts.




  * ## Constructor Details

    * ### ContextFilterPlugin

protected ContextFilterPlugin([ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins") builder)

  * ## Method Details

    * ### builder

public static [ContextFilterPlugin.Builder](ContextFilterPlugin.Builder.html "class in com.google.adk.plugins") builder()

    * ### beforeModelCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> beforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)

Filters the LLM request context by trimming recent turns and applying any custom filter. 

If `numInvocationsToKeep` is set, this method retains only the most recent model turns and their preceding user turns. It ensures that function calls and responses remain paired. If a `customFilter` is provided, it is applied to the list after trimming.

Parameters:
    `callbackContext` \- The context of the callback.
    `llmRequest` \- The request builder whose contents will be updated in place.
Returns:
    `Maybe.empty()` as this plugin only modifies the request builder.




* * *

Copyright (C) 1980\. All rights reserved.
