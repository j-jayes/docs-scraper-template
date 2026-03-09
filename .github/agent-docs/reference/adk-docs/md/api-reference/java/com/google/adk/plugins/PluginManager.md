JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/PluginManager.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.plugins](package-summary.html)
  2. [PluginManager](PluginManager.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. PluginManager(List)
     2. PluginManager()
  5. Method Details
     1. getName()
     2. registerPlugin(Plugin)
     3. getPlugin(String)
     4. runOnUserMessageCallback(InvocationContext, Content)
     5. onUserMessageCallback(InvocationContext, Content)
     6. runBeforeRunCallback(InvocationContext)
     7. beforeRunCallback(InvocationContext)
     8. runAfterRunCallback(InvocationContext)
     9. afterRunCallback(InvocationContext)
     10. runOnEventCallback(InvocationContext, Event)
     11. onEventCallback(InvocationContext, Event)
     12. runBeforeAgentCallback(BaseAgent, CallbackContext)
     13. beforeAgentCallback(BaseAgent, CallbackContext)
     14. runAfterAgentCallback(BaseAgent, CallbackContext)
     15. afterAgentCallback(BaseAgent, CallbackContext)
     16. runBeforeModelCallback(CallbackContext, LlmRequest.Builder)
     17. beforeModelCallback(CallbackContext, LlmRequest.Builder)
     18. runAfterModelCallback(CallbackContext, LlmResponse)
     19. afterModelCallback(CallbackContext, LlmResponse)
     20. runOnModelErrorCallback(CallbackContext, LlmRequest.Builder, Throwable)
     21. onModelErrorCallback(CallbackContext, LlmRequest.Builder, Throwable)
     22. runBeforeToolCallback(BaseTool, Map, ToolContext)
     23. beforeToolCallback(BaseTool, Map, ToolContext)
     24. runAfterToolCallback(BaseTool, Map, ToolContext, Map)
     25. afterToolCallback(BaseTool, Map, ToolContext, Map)
     26. runOnToolErrorCallback(BaseTool, Map, ToolContext, Throwable)
     27. onToolErrorCallback(BaseTool, Map, ToolContext, Throwable)

Hide sidebar  Show sidebar

# Class PluginManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.plugins.PluginManager

All Implemented Interfaces:
    `[Plugin](Plugin.html "interface in com.google.adk.plugins")`

Direct Known Subclasses:
    `[CallbackPlugin](../agents/CallbackPlugin.html "class in com.google.adk.agents")`

* * *

public class PluginManager extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [Plugin](Plugin.html "interface in com.google.adk.plugins")

Manages the registration and execution of plugins. 

The PluginManager is an internal class that orchestrates the invocation of plugin callbacks at key points in the SDK's execution lifecycle.

  * ## Constructor Summary

Constructors

Constructor

Description

`PluginManager()`

 

`PluginManager([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

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

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`afterToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> result)`

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

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`beforeToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Callback executed before a tool is called.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`getName()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Plugin](Plugin.html "interface in com.google.adk.plugins")>`

`getPlugin([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") pluginName)`

Retrieves a registered plugin by its name.

`io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")>`

`onEventCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../events/Event.html "class in com.google.adk.events") event)`

Callback executed after an event is yielded from runner.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`onModelErrorCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

Callback executed when a model call encounters an error.

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`onToolErrorCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

Callback executed when a tool call encounters an error.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`onUserMessageCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

Callback executed when a user message is received before an invocation starts.

`void`

`registerPlugin([Plugin](Plugin.html "interface in com.google.adk.plugins") plugin)`

Registers a new plugin.

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`runAfterAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`runAfterModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`io.reactivex.rxjava3.core.Completable`

`runAfterRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runAfterToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> result)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`runBeforeAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`runBeforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`runBeforeRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runBeforeToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")>`

`runOnEventCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../events/Event.html "class in com.google.adk.events") event)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`runOnModelErrorCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runOnToolErrorCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`runOnUserMessageCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### PluginManager

public PluginManager([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](Plugin.html "interface in com.google.adk.plugins")> plugins)

    * ### PluginManager

public PluginManager()

  * ## Method Details

    * ### getName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getName()

Specified by:
    `[getName](Plugin.html#getName\(\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`

    * ### registerPlugin

public void registerPlugin([Plugin](Plugin.html "interface in com.google.adk.plugins") plugin)

Registers a new plugin.

Parameters:
    `plugin` \- The plugin instance to register.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- If a plugin with the same name is already registered.

    * ### getPlugin

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Plugin](Plugin.html "interface in com.google.adk.plugins")> getPlugin([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") pluginName)

Retrieves a registered plugin by its name.

Parameters:
    `pluginName` \- The name of the plugin to retrieve.
Returns:
    The plugin instance if found, otherwise [`Optional.empty()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html#empty\(\) "class or interface in java.util").

    * ### runOnUserMessageCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> runOnUserMessageCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)

    * ### onUserMessageCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> onUserMessageCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, com.google.genai.types.Content userMessage)

Description copied from interface: `[Plugin](Plugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\))`

Callback executed when a user message is received before an invocation starts.

Specified by:
    `[onUserMessageCallback](Plugin.html#onUserMessageCallback\(com.google.adk.agents.InvocationContext,com.google.genai.types.Content\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
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

Specified by:
    `[beforeRunCallback](Plugin.html#beforeRunCallback\(com.google.adk.agents.InvocationContext\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `invocationContext` \- The context for the entire invocation.
Returns:
    An optional Content to halt execution. Returning Empty to proceed normally.

    * ### runAfterRunCallback

public io.reactivex.rxjava3.core.Completable runAfterRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

    * ### afterRunCallback

public io.reactivex.rxjava3.core.Completable afterRunCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from interface: `[Plugin](Plugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))`

Callback executed after an ADK runner run has completed.

Specified by:
    `[afterRunCallback](Plugin.html#afterRunCallback\(com.google.adk.agents.InvocationContext\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `invocationContext` \- The context for the entire invocation.

    * ### runOnEventCallback

public io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")> runOnEventCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../events/Event.html "class in com.google.adk.events") event)

    * ### onEventCallback

public io.reactivex.rxjava3.core.Maybe<[Event](../events/Event.html "class in com.google.adk.events")> onEventCallback([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../events/Event.html "class in com.google.adk.events") event)

Description copied from interface: `[Plugin](Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))`

Callback executed after an event is yielded from runner.

Specified by:
    `[onEventCallback](Plugin.html#onEventCallback\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `invocationContext` \- The context for the entire invocation.
    `event` \- The event raised by the runner.
Returns:
    An optional Event to modify or replace the response. Returning Empty to proceed normally.

    * ### runBeforeAgentCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> runBeforeAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)

    * ### beforeAgentCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> beforeAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)

Description copied from interface: `[Plugin](Plugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))`

Callback executed before an agent's primary logic is invoked.

Specified by:
    `[beforeAgentCallback](Plugin.html#beforeAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `agent` \- The agent that is about to run.
    `callbackContext` \- The context for the agent invocation.
Returns:
    An optional Content object to bypass the agent's execution. Returning Empty to proceed normally.

    * ### runAfterAgentCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> runAfterAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)

    * ### afterAgentCallback

public io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> afterAgentCallback([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext)

Description copied from interface: `[Plugin](Plugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))`

Callback executed after an agent's primary logic has completed.

Specified by:
    `[afterAgentCallback](Plugin.html#afterAgentCallback\(com.google.adk.agents.BaseAgent,com.google.adk.agents.CallbackContext\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `agent` \- The agent that has just run.
    `callbackContext` \- The context for the agent invocation.
Returns:
    An optional Content object to replace the agent's original result. Returning Empty to use the original result.

    * ### runBeforeModelCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> runBeforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)

    * ### beforeModelCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> beforeModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)

Description copied from interface: `[Plugin](Plugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))`

Callback executed before a request is sent to the model.

Specified by:
    `[beforeModelCallback](Plugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmRequest` \- The mutable request builder, allowing modification of the request before it is sent to the model.
Returns:
    An optional LlmResponse to trigger an early exit. Returning Empty to proceed normally.

    * ### runAfterModelCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> runAfterModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../models/LlmResponse.html "class in com.google.adk.models") llmResponse)

    * ### afterModelCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> afterModelCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../models/LlmResponse.html "class in com.google.adk.models") llmResponse)

Description copied from interface: `[Plugin](Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))`

Callback executed after a response is received from the model.

Specified by:
    `[afterModelCallback](Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmResponse` \- The response object received from the model.
Returns:
    An optional LlmResponse to modify or replace the response. Returning Empty to use the original response.

    * ### runOnModelErrorCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> runOnModelErrorCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)

    * ### onModelErrorCallback

public io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> onModelErrorCallback([CallbackContext](../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)

Description copied from interface: `[Plugin](Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))`

Callback executed when a model call encounters an error.

Specified by:
    `[onModelErrorCallback](Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `callbackContext` \- The context for the current agent call.
    `llmRequest` \- The mutable request builder for the request that failed.
    `error` \- The exception that was raised.
Returns:
    An optional LlmResponse to use instead of propagating the error. Returning Empty to allow the original error to be raised.

    * ### runBeforeToolCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runBeforeToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)

    * ### beforeToolCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> beforeToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from interface: `[Plugin](Plugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))`

Callback executed before a tool is called.

Specified by:
    `[beforeToolCallback](Plugin.html#beforeToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `tool` \- The tool instance that is about to be executed.
    `toolArgs` \- The dictionary of arguments to be used for invoking the tool.
    `toolContext` \- The context specific to the tool execution.
Returns:
    An optional Map to stop the tool execution and return this response immediately. Returning Empty to proceed normally.

    * ### runAfterToolCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runAfterToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> result)

    * ### afterToolCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> afterToolCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> result)

Description copied from interface: `[Plugin](Plugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))`

Callback executed after a tool has been called.

Specified by:
    `[afterToolCallback](Plugin.html#afterToolCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.util.Map\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `tool` \- The tool instance that has just been executed.
    `toolArgs` \- The original arguments that were passed to the tool.
    `toolContext` \- The context specific to the tool execution.
    `result` \- The dictionary returned by the tool invocation.
Returns:
    An optional Map to replace the original result from the tool. Returning Empty to use the original result.

    * ### runOnToolErrorCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runOnToolErrorCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)

    * ### onToolErrorCallback

public io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> onToolErrorCallback([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolArgs, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)

Description copied from interface: `[Plugin](Plugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))`

Callback executed when a tool call encounters an error.

Specified by:
    `[onToolErrorCallback](Plugin.html#onToolErrorCallback\(com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Throwable\))` in interface `[Plugin](Plugin.html "interface in com.google.adk.plugins")`
Parameters:
    `tool` \- The tool instance that encountered an error.
    `toolArgs` \- The arguments that were passed to the tool.
    `toolContext` \- The context specific to the tool execution.
    `error` \- The exception that was raised during tool execution.
Returns:
    An optional Map to be used as the tool response instead of propagating the error. Returning Empty to allow the original error to be raised.




* * *

Copyright (C) 1980\. All rights reserved.
