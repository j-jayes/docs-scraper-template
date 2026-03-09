JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ReplayPlugin.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.plugins](package-summary.html)
  2. [ReplayPlugin](ReplayPlugin.html)



Contents 

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ReplayPlugin()
     2. ReplayPlugin(String)
  6. Method Details
     1. beforeRunCallback(InvocationContext)
     2. beforeModelCallback(CallbackContext, LlmRequest.Builder)
     3. beforeToolCallback(BaseTool, Map, ToolContext)
     4. afterRunCallback(InvocationContext)

Hide sidebar  Show sidebar

# Class ReplayPlugin

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.plugins.BasePlugin](BasePlugin.html "class in com.google.adk.plugins")

com.google.adk.plugins.ReplayPlugin

All Implemented Interfaces:
    `[Plugin](Plugin.html "interface in com.google.adk.plugins")`

* * *

public class ReplayPlugin extends [BasePlugin](BasePlugin.html "class in com.google.adk.plugins")

Plugin for replaying ADK agent interactions from recordings.

  * ## Field Summary

### Fields inherited from class [BasePlugin](BasePlugin.html#field-summary "class in com.google.adk.plugins")

`[name](BasePlugin.html#name)`

  * ## Constructor Summary

Constructors

Constructor

Description

`ReplayPlugin()`

 

`ReplayPlugin([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`afterRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed after an ADK runner run has completed.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`beforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Callback executed before a request is sent to the model.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`beforeRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed before the ADK runner runs.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`beforeToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Callback executed before a tool is called.

### Methods inherited from class [BasePlugin](BasePlugin.html#method-summary "class in com.google.adk.plugins")

`[getName](BasePlugin.html#getName\(\) "getName\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`

### Methods inherited from interface [Plugin](Plugin.html#method-summary "interface in com.google.adk.plugins")

`[afterAgentCallback](Plugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\) "afterAgentCallback\(BaseAgent, CallbackContext\)"), [afterModelCallback](Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\) "afterModelCallback\(CallbackContext, LlmResponse\)"), [afterToolCallback](Plugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\) "afterToolCallback\(BaseTool, Map, ToolContext, Map\)"), [beforeAgentCallback](Plugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\) "beforeAgentCallback\(BaseAgent, CallbackContext\)"), [onEventCallback](Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\) "onEventCallback\(InvocationContext, Event\)"), [onModelErrorCallback](Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\) "onModelErrorCallback\(CallbackContext, LlmRequest.Builder, Throwable\)"), [onToolErrorCallback](Plugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\) "onToolErrorCallback\(BaseTool, Map, ToolContext, Throwable\)"), [onUserMessageCallback](Plugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\) "onUserMessageCallback\(InvocationContext, Content\)")`




  * ## Constructor Details

    * ### ReplayPlugin

public ReplayPlugin()

    * ### ReplayPlugin

public ReplayPlugin([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

  * ## Method Details

    * ### beforeRunCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> beforeRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from interface: `[Plugin](Plugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\))`

Callback executed before the ADK runner runs.

Parameters:
    `invocationContext` \- The context for the entire invocation.
Returns:
    An optional Content to halt execution. Returning Empty to proceed normally.

    * ### beforeModelCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> beforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)

Description copied from interface: `[Plugin](Plugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))`

Callback executed before a request is sent to the model.

Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmRequest` \- The mutable request builder, allowing modification of the request before it is sent to the model.
Returns:
    An optional LlmResponse to trigger an early exit. Returning Empty to proceed normally.

    * ### beforeToolCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> beforeToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from interface: `[Plugin](Plugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))`

Callback executed before a tool is called.

Parameters:
    `tool` \- The tool instance that is about to be executed.
    `toolArgs` \- The dictionary of arguments to be used for invoking the tool.
    `toolContext` \- The context specific to the tool execution.
Returns:
    An optional Map to stop the tool execution and return this response immediately. Returning Empty to proceed normally.

    * ### afterRunCallback

public io.reactivex.rxjava3.core.Completable afterRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from interface: `[Plugin](Plugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))`

Callback executed after an ADK runner run has completed.

Parameters:
    `invocationContext` \- The context for the entire invocation.




* * *

Copyright (C) 1980\. All rights reserved.
