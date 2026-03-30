JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BasePlugin.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.plugins](../package-summary.html)
  2. [BasePlugin](../BasePlugin.html)



# Uses of Class  
com.google.adk.plugins.BasePlugin

Packages that use [BasePlugin](../BasePlugin.html "class in com.google.adk.plugins")

Package

Description

com.google.adk.plugins

 

com.google.adk.plugins.agentanalytics

 

com.google.adk.runner

 

com.google.adk.web.service

 

  * ## Uses of [BasePlugin](../BasePlugin.html "class in com.google.adk.plugins") in [com.google.adk.plugins](../package-summary.html)

Subclasses of [BasePlugin](../BasePlugin.html "class in com.google.adk.plugins") in [com.google.adk.plugins](../package-summary.html)

Modifier and Type

Class

Description

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

  * ## Uses of [BasePlugin](../BasePlugin.html "class in com.google.adk.plugins") in [com.google.adk.plugins.agentanalytics](../agentanalytics/package-summary.html)

Subclasses of [BasePlugin](../BasePlugin.html "class in com.google.adk.plugins") in [com.google.adk.plugins.agentanalytics](../agentanalytics/package-summary.html)

Modifier and Type

Class

Description

`class `

`[BigQueryAgentAnalyticsPlugin](../agentanalytics/BigQueryAgentAnalyticsPlugin.html "class in com.google.adk.plugins.agentanalytics")`

BigQuery Agent Analytics Plugin for Java.

  * ## Uses of [BasePlugin](../BasePlugin.html "class in com.google.adk.plugins") in [com.google.adk.runner](../../runner/package-summary.html)

Constructor parameters in [com.google.adk.runner](../../runner/package-summary.html) with type arguments of type [BasePlugin](../BasePlugin.html "class in com.google.adk.plugins")

Modifier

Constructor

Description

` `

`[FirestoreDatabaseRunner](../../runner/FirestoreDatabaseRunner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,java.util.List,com.google.cloud.firestore.Firestore\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") baseAgent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../BasePlugin.html "class in com.google.adk.plugins")> plugins, com.google.cloud.firestore.Firestore firestore)`

Constructor for FirestoreDatabaseRunner with parent runners

  * ## Uses of [BasePlugin](../BasePlugin.html "class in com.google.adk.plugins") in [com.google.adk.web.service](../../web/service/package-summary.html)

Constructor parameters in [com.google.adk.web.service](../../web/service/package-summary.html) with type arguments of type [BasePlugin](../BasePlugin.html "class in com.google.adk.plugins")

Modifier

Constructor

Description

` `

`[RunnerService](../../web/service/RunnerService.html#%3Cinit%3E\(com.google.adk.web.AgentLoader,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([AgentLoader](../../web/AgentLoader.html "interface in com.google.adk.web") agentProvider, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../BasePlugin.html "class in com.google.adk.plugins")> extraPlugins)`

 




* * *

Copyright (C) 1980\. All rights reserved.
