JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Plugin.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.plugins](../package-summary.html)
  2. [Plugin](../Plugin.html)



# Uses of Interface  
com.google.adk.plugins.Plugin

Packages that use [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Package

Description

com.google.adk.agents

 

com.google.adk.plugins

 

  * ## Uses of [Plugin](../Plugin.html "interface in com.google.adk.plugins") in [com.google.adk.agents](../../agents/package-summary.html)

Classes in [com.google.adk.agents](../../agents/package-summary.html) that implement [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Class

Description

`class `

`[CallbackPlugin](../../agents/CallbackPlugin.html "class in com.google.adk.agents")`

A plugin that wraps callbacks and exposes them as a plugin.

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

`[Plugin](../Plugin.html "interface in com.google.adk.plugins")`

BaseAgent.`[getPlugin](../../agents/BaseAgent.html#getPlugin\(\))()`

 

`[Plugin](../Plugin.html "interface in com.google.adk.plugins")`

InvocationContext.`[pluginManager](../../agents/InvocationContext.html#pluginManager\(\))()`

Returns the plugin manager for accessing tools and plugins.

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

`[InvocationContext.Builder](../../agents/InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[pluginManager](../../agents/InvocationContext.Builder.html#pluginManager\(com.google.adk.plugins.Plugin\))([Plugin](../Plugin.html "interface in com.google.adk.plugins") pluginManager)`

Sets the plugin manager for accessing tools and plugins.

Constructors in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier

Constructor

Description

` `

`[InvocationContext](../../agents/InvocationContext.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.memory.BaseMemoryService,com.google.adk.plugins.Plugin,java.util.Optional,java.util.Optional,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,java.util.Optional,com.google.adk.agents.RunConfig,boolean\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [Plugin](../Plugin.html "interface in com.google.adk.plugins") pluginManager, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, boolean endInvocation)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.builder()`](../../agents/InvocationContext.html#builder\(\)) instead.

  * ## Uses of [Plugin](../Plugin.html "interface in com.google.adk.plugins") in [com.google.adk.plugins](../package-summary.html)

Classes in [com.google.adk.plugins](../package-summary.html) that implement [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Class

Description

`class `

`[BasePlugin](../BasePlugin.html "class in com.google.adk.plugins")`

Base class for creating plugins.

`class `

`[LoggingPlugin](../LoggingPlugin.html "class in com.google.adk.plugins")`

A plugin that logs important information at each callback point.

`class `

`[PluginManager](../PluginManager.html "class in com.google.adk.plugins")`

Manages the registration and execution of plugins.

`class `

`[ReplayPlugin](../ReplayPlugin.html "class in com.google.adk.plugins")`

Plugin for replaying ADK agent interactions from recordings.

Methods in [com.google.adk.plugins](../package-summary.html) that return types with arguments of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Plugin](../Plugin.html "interface in com.google.adk.plugins")>`

PluginManager.`[getPlugin](../PluginManager.html#getPlugin\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") pluginName)`

Retrieves a registered plugin by its name.

Methods in [com.google.adk.plugins](../package-summary.html) with parameters of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

`void`

PluginManager.`[registerPlugin](../PluginManager.html#registerPlugin\(com.google.adk.plugins.Plugin\))([Plugin](../Plugin.html "interface in com.google.adk.plugins") plugin)`

Registers a new plugin.

Constructor parameters in [com.google.adk.plugins](../package-summary.html) with type arguments of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier

Constructor

Description

` `

`[PluginManager](../PluginManager.html#%3Cinit%3E\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../Plugin.html "interface in com.google.adk.plugins")> plugins)`

 




* * *

Copyright (C) 1980\. All rights reserved.
