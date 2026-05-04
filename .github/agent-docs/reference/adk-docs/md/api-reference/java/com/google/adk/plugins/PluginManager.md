JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/PluginManager.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.plugins](package-summary.html)
  2. [PluginManager](PluginManager.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
     1. Methods inherited from class BasePlugin
     2. Methods inherited from class Object
  5. Constructor Details
     1. PluginManager(List)
     2. PluginManager()
  6. Method Details
     1. registerPlugin(Plugin)
     2. getPlugin(String)
     3. getPlugins()
     4. runOnUserMessageCallback(InvocationContext, Content)
     5. onUserMessageCallback(InvocationContext, Content)
     6. runBeforeRunCallback(InvocationContext)
     7. beforeRunCallback(InvocationContext)
     8. afterRunCallback(InvocationContext)
     9. close()
     10. onEventCallback(InvocationContext, Event)
     11. beforeAgentCallback(BaseAgent, CallbackContext)
     12. afterAgentCallback(BaseAgent, CallbackContext)
     13. beforeModelCallback(CallbackContext, LlmRequest.Builder)
     14. afterModelCallback(CallbackContext, LlmResponse)
     15. onModelErrorCallback(CallbackContext, LlmRequest.Builder, Throwable)
     16. beforeToolCallback(BaseTool, Map, ToolContext)
     17. afterToolCallback(BaseTool, Map, ToolContext, Map)
     18. onToolErrorCallback(BaseTool, Map, ToolContext, Throwable)

Hide sidebar  Show sidebar

# Class PluginManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.plugins.BasePlugin](BasePlugin.html "class in com.google.adk.plugins")

com.google.adk.plugins.PluginManager

All Implemented Interfaces:
    `[Plugin](Plugin.html "interface in com.google.adk.plugins")`

* * *

public class PluginManager extends [BasePlugin](BasePlugin.html "class in com.google.adk.plugins")

Manages the registration and execution of plugins. 

The PluginManager is an internal class that orchestrates the invocation of plugin callbacks at key points in the SDK's execution lifecycle.

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

Constructor

Description

`PluginManager()`

 

`PluginManager(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`afterAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed after an agent's primary logic has completed.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`afterModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Callback executed after a response is received from the model.

`io.reactivex.rxjava3.core.Completable`

`afterRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed after an ADK runner run has completed.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`afterToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> result)`

Callback executed after a tool has been called.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`beforeAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Callback executed before an agent's primary logic is invoked.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`beforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Callback executed before a request is sent to the model.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`beforeRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Callback executed before the ADK runner runs.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`beforeToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Callback executed before a tool is called.

`io.reactivex.rxjava3.core.Completable`

`close()`

Method executed when the runner is closed.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Plugin](Plugin.html "interface in com.google.adk.plugins")>`

`getPlugin([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") pluginName)`

Retrieves a registered plugin by its name.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Plugin](Plugin.html "interface in com.google.adk.plugins")>`

`getPlugins()`

Returns the list of registered plugins.

`io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")>`

`onEventCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../events/Event.html "class in com.google.adk.events") event)`

Callback executed after an event is yielded from runner.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`onModelErrorCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Callback executed when a model call encounters an error.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`onToolErrorCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Callback executed when a tool call encounters an error.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`onUserMessageCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

Callback executed when a user message is received before an invocation starts.

`void`

`registerPlugin([Plugin](Plugin.html "interface in com.google.adk.plugins") plugin)`

Registers a new plugin.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`runBeforeRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`runOnUserMessageCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

 

### Methods inherited from class [BasePlugin](BasePlugin.html#method-summary "class in com.google.adk.plugins")

`[getName](BasePlugin.html#getName\(\) "getName\(\)")`

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[getName](BasePlugin.html#getName\(\))()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### PluginManager

public PluginManager(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](Plugin.html "interface in com.google.adk.plugins")> plugins)

    * ### PluginManager

public PluginManager()

  * ## Method Details

    * ### registerPlugin

public void registerPlugin([Plugin](Plugin.html "interface in com.google.adk.plugins") plugin)

Registers a new plugin.

Parameters:
    `plugin` \- The plugin instance to register.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- If a plugin with the same name is already registered.

    * ### getPlugin

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Plugin](Plugin.html "interface in com.google.adk.plugins")> getPlugin([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") pluginName)

Retrieves a registered plugin by its name.

Parameters:
    `pluginName` \- The name of the plugin to retrieve.
Returns:
    The plugin instance if found, otherwise [`Optional.empty()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html#empty\(\)).

    * ### getPlugins

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Plugin](Plugin.html "interface in com.google.adk.plugins")> getPlugins()

Returns the list of registered plugins. 

This method is intended for testing purposes only. 

Note that it returns a copy of the plugins list to prevent modification of the original list.

Returns:
    The list of registered plugins.

    * ### runOnUserMessageCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> runOnUserMessageCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)

    * ### onUserMessageCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> onUserMessageCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)

Description copied from interface: `[Plugin](Plugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\))`

Callback executed when a user message is received before an invocation starts.

Parameters:
    `invocationContext` \- The context for the entire invocation.
    `userMessage` \- The message content input by user.
Returns:
    An optional Content to replace the user message. Returning Empty to proceed normally.

    * ### runBeforeRunCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> runBeforeRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

    * ### beforeRunCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> beforeRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from interface: `[Plugin](Plugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\))`

Callback executed before the ADK runner runs.

Parameters:
    `invocationContext` \- The context for the entire invocation.
Returns:
    An optional Content to halt execution. Returning Empty to proceed normally.

    * ### afterRunCallback

public io.reactivex.rxjava3.core.Completable afterRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from interface: `[Plugin](Plugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))`

Callback executed after an ADK runner run has completed.

Parameters:
    `invocationContext` \- The context for the entire invocation.

    * ### close

public io.reactivex.rxjava3.core.Completable close()

Description copied from interface: `[Plugin](Plugin.html#close\(\))`

Method executed when the runner is closed. 

This method is used for cleanup tasks such as closing network connections or releasing resources.

    * ### onEventCallback

public io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")> onEventCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../events/Event.html "class in com.google.adk.events") event)

Description copied from interface: `[Plugin](Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))`

Callback executed after an event is yielded from runner.

Parameters:
    `invocationContext` \- The context for the entire invocation.
    `event` \- The event raised by the runner.
Returns:
    An optional Event to modify or replace the response. Returning Empty to proceed normally.

    * ### beforeAgentCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> beforeAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)

Description copied from interface: `[Plugin](Plugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))`

Callback executed before an agent's primary logic is invoked.

Parameters:
    `agent` \- The agent that is about to run.
    `callbackContext` \- The context for the agent invocation.
Returns:
    An optional Content object to bypass the agent's execution. Returning Empty to proceed normally.

    * ### afterAgentCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> afterAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)

Description copied from interface: `[Plugin](Plugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))`

Callback executed after an agent's primary logic has completed.

Parameters:
    `agent` \- The agent that has just run.
    `callbackContext` \- The context for the agent invocation.
Returns:
    An optional Content object to replace the agent's original result. Returning Empty to use the original result.

    * ### beforeModelCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> beforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)

Description copied from interface: `[Plugin](Plugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))`

Callback executed before a request is sent to the model.

Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmRequest` \- The mutable request builder, allowing modification of the request before it is sent to the model.
Returns:
    An optional LlmResponse to trigger an early exit. Returning Empty to proceed normally.

    * ### afterModelCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> afterModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../models/LlmResponse.html "class in com.google.adk.models") llmResponse)

Description copied from interface: `[Plugin](Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))`

Callback executed after a response is received from the model.

Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmResponse` \- The response object received from the model.
Returns:
    An optional LlmResponse to modify or replace the response. Returning Empty to use the original response.

    * ### onModelErrorCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> onModelErrorCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)

Description copied from interface: `[Plugin](Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))`

Callback executed when a model call encounters an error.

Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmRequest` \- The mutable request builder for the request that failed.
    `error` \- The exception that was raised.
Returns:
    An optional LlmResponse to use instead of propagating the error. Returning Empty to allow the original error to be raised.

    * ### beforeToolCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> beforeToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from interface: `[Plugin](Plugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))`

Callback executed before a tool is called.

Parameters:
    `tool` \- The tool instance that is about to be executed.
    `toolArgs` \- The dictionary of arguments to be used for invoking the tool.
    `toolContext` \- The context specific to the tool execution.
Returns:
    An optional Map to stop the tool execution and return this response immediately. Returning Empty to proceed normally.

    * ### afterToolCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> afterToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> result)

Description copied from interface: `[Plugin](Plugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))`

Callback executed after a tool has been called.

Parameters:
    `tool` \- The tool instance that has just been executed.
    `toolArgs` \- The original arguments that were passed to the tool.
    `toolContext` \- The context specific to the tool execution.
    `result` \- The dictionary returned by the tool invocation.
Returns:
    An optional Map to replace the original result from the tool. Returning Empty to use the original result.

    * ### onToolErrorCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> onToolErrorCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)

Description copied from interface: `[Plugin](Plugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))`

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
