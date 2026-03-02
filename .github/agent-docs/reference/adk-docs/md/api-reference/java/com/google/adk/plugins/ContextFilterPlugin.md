JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ContextFilterPlugin.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.plugins.BasePlugin](BasePlugin.html "class in com.google.adk.plugins")

com.google.adk.plugins.ContextFilterPlugin

All Implemented Interfaces:
    `[Plugin](Plugin.html "interface in com.google.adk.plugins")`

* * *

public class ContextFilterPlugin extends [BasePlugin](BasePlugin.html "class in com.google.adk.plugins")

A plugin that filters the LLM request `Content` list to reduce its size, for example to adhere to context window limits. 

This plugin can be configured to trim the conversation history based on one or both of the following criteria: 

  * **`numInvocationsToKeep(N)`:** Retains only the last `N` model turns and any preceding user turns. If multiple user messages appear consecutively before a model message, all of them are kept as part of that model invocation window. 
  * **`customFilter()`:** Applies a custom [`UnaryOperator`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/UnaryOperator.html "class or interface in java.util.function") to filter the list of `Content` objects. If `numInvocationsToKeep` is also specified, the custom filter is applied _after_ the invocation-based trimming occurs. 


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

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`

### Methods inherited from interface [Plugin](Plugin.html#method-summary "interface in com.google.adk.plugins")

`[afterAgentCallback](Plugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\) "afterAgentCallback\(BaseAgent, CallbackContext\)"), [afterModelCallback](Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\) "afterModelCallback\(CallbackContext, LlmResponse\)"), [afterRunCallback](Plugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\) "afterRunCallback\(InvocationContext\)"), [afterToolCallback](Plugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\) "afterToolCallback\(BaseTool, Map, ToolContext, Map\)"), [beforeAgentCallback](Plugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\) "beforeAgentCallback\(BaseAgent, CallbackContext\)"), [beforeRunCallback](Plugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\) "beforeRunCallback\(InvocationContext\)"), [beforeToolCallback](Plugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\) "beforeToolCallback\(BaseTool, Map, ToolContext\)"), [close](Plugin.html#close\(\) "close\(\)"), [onEventCallback](Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\) "onEventCallback\(InvocationContext, Event\)"), [onModelErrorCallback](Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\) "onModelErrorCallback\(CallbackContext, LlmRequest.Builder, Throwable\)"), [onToolErrorCallback](Plugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\) "onToolErrorCallback\(BaseTool, Map, ToolContext, Throwable\)"), [onUserMessageCallback](Plugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\) "onUserMessageCallback\(InvocationContext, Content\)")`




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
