JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Plugin.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.plugins](../package-summary.html)
  2. [Plugin](../Plugin.html)



# Uses of Interface  
com.google.adk.plugins.Plugin

Packages that use [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Package

Description

com.google.adk.a2a.executor

 

com.google.adk.agents

 

com.google.adk.apps

 

com.google.adk.plugins

 

com.google.adk.plugins.agentanalytics

 

com.google.adk.runner

 

  * ## Uses of [Plugin](../Plugin.html "interface in com.google.adk.plugins") in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html)

Method parameters in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html) with type arguments of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

`[AgentExecutor.Builder](../../a2a/executor/AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

AgentExecutor.Builder.`[plugins](../../a2a/executor/AgentExecutor.Builder.html#plugins\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

  * ## Uses of [Plugin](../Plugin.html "interface in com.google.adk.plugins") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

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

  * ## Uses of [Plugin](../Plugin.html "interface in com.google.adk.plugins") in [com.google.adk.apps](../../apps/package-summary.html)

Methods in [com.google.adk.apps](../../apps/package-summary.html) that return types with arguments of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../Plugin.html "interface in com.google.adk.plugins")>`

App.`[plugins](../../apps/App.html#plugins\(\))()`

 

Methods in [com.google.adk.apps](../../apps/package-summary.html) with parameters of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

`[App.Builder](../../apps/App.Builder.html "class in com.google.adk.apps")`

App.Builder.`[plugins](../../apps/App.Builder.html#plugins\(com.google.adk.plugins.Plugin...\))([Plugin](../Plugin.html "interface in com.google.adk.plugins")... plugins)`

 

Method parameters in [com.google.adk.apps](../../apps/package-summary.html) with type arguments of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

`[App.Builder](../../apps/App.Builder.html "class in com.google.adk.apps")`

App.Builder.`[plugins](../../apps/App.Builder.html#plugins\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

  * ## Uses of [Plugin](../Plugin.html "interface in com.google.adk.plugins") in [com.google.adk.plugins](../package-summary.html)

Classes in [com.google.adk.plugins](../package-summary.html) that implement [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Class

Description

`class `

`[BasePlugin](../BasePlugin.html "class in com.google.adk.plugins")`

Base class for creating plugins.

`class `

`[ContextFilterPlugin](../ContextFilterPlugin.html "class in com.google.adk.plugins")`

A plugin that filters the LLM request `Content` list to reduce its size, for example to adhere to context window limits.

`class `

`[GlobalInstructionPlugin](../GlobalInstructionPlugin.html "class in com.google.adk.plugins")`

Plugin that provides global instructions functionality at the App level.

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

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Plugin](../Plugin.html "interface in com.google.adk.plugins")>`

PluginManager.`[getPlugin](../PluginManager.html#getPlugin\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") pluginName)`

Retrieves a registered plugin by its name.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Plugin](../Plugin.html "interface in com.google.adk.plugins")>`

PluginManager.`[getPlugins](../PluginManager.html#getPlugins\(\))()`

Returns the list of registered plugins.

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

`[PluginManager](../PluginManager.html#%3Cinit%3E\(java.util.List\))(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

  * ## Uses of [Plugin](../Plugin.html "interface in com.google.adk.plugins") in [com.google.adk.plugins.agentanalytics](../agentanalytics/package-summary.html)

Classes in [com.google.adk.plugins.agentanalytics](../agentanalytics/package-summary.html) that implement [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Class

Description

`class `

`[BigQueryAgentAnalyticsPlugin](../agentanalytics/BigQueryAgentAnalyticsPlugin.html "class in com.google.adk.plugins.agentanalytics")`

BigQuery Agent Analytics Plugin for Java.

  * ## Uses of [Plugin](../Plugin.html "interface in com.google.adk.plugins") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

`[Runner.Builder](../../runner/Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[plugins](../../runner/Runner.Builder.html#plugins\(com.google.adk.plugins.Plugin...\))([Plugin](../Plugin.html "interface in com.google.adk.plugins")... plugins)`

 

Method parameters in [com.google.adk.runner](../../runner/package-summary.html) with type arguments of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier and Type

Method

Description

`[Runner.Builder](../../runner/Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[plugins](../../runner/Runner.Builder.html#plugins\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

Constructor parameters in [com.google.adk.runner](../../runner/package-summary.html) with type arguments of type [Plugin](../Plugin.html "interface in com.google.adk.plugins")

Modifier

Constructor

Description

` `

`[InMemoryRunner](../../runner/InMemoryRunner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,java.util.List\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../Plugin.html "interface in com.google.adk.plugins")> plugins)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../Plugin.html "interface in com.google.adk.plugins")> plugins, @Nullable [EventsCompactionConfig](../../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, @Nullable [ContextCacheConfig](../../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig,com.google.adk.apps.ResumabilityConfig\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../Plugin.html "interface in com.google.adk.plugins")> plugins, @Nullable [EventsCompactionConfig](../../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, @Nullable [ContextCacheConfig](../../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig, @Nullable [ResumabilityConfig](../../apps/ResumabilityConfig.html "class in com.google.adk.apps") resumabilityConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.




* * *

Copyright (C) 1980\. All rights reserved.
