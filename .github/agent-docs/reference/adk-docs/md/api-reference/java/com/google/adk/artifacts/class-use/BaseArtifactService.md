JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseArtifactService.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.artifacts](../package-summary.html)
  2. [BaseArtifactService](../BaseArtifactService.html)



# Uses of Interface  
com.google.adk.artifacts.BaseArtifactService

Packages that use [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Package

Description

com.google.adk.a2a.executor

 

com.google.adk.agents

 

com.google.adk.artifacts

 

com.google.adk.runner

 

com.google.adk.web

 

com.google.adk.web.controller

 

com.google.adk.web.service

 

  * ## Uses of [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html)

Methods in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html) with parameters of type [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier and Type

Method

Description

`[AgentExecutor.Builder](../../a2a/executor/AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

AgentExecutor.Builder.`[artifactService](../../a2a/executor/AgentExecutor.Builder.html#artifactService\(com.google.adk.artifacts.BaseArtifactService\))([BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

 

  * ## Uses of [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier and Type

Method

Description

`[BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")`

InvocationContext.`[artifactService](../../agents/InvocationContext.html#artifactService\(\))()`

Returns the artifact service for persisting artifacts.

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier and Type

Method

Description

`[InvocationContext.Builder](../../agents/InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[artifactService](../../agents/InvocationContext.Builder.html#artifactService\(com.google.adk.artifacts.BaseArtifactService\))([BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

Sets the artifact service for persisting artifacts.

  * ## Uses of [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") in [com.google.adk.artifacts](../package-summary.html)

Classes in [com.google.adk.artifacts](../package-summary.html) that implement [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier and Type

Class

Description

`final class `

`[GcsArtifactService](../GcsArtifactService.html "class in com.google.adk.artifacts")`

An artifact service implementation using Google Cloud Storage (GCS).

`final class `

`[InMemoryArtifactService](../InMemoryArtifactService.html "class in com.google.adk.artifacts")`

An in-memory implementation of the [`BaseArtifactService`](../BaseArtifactService.html "interface in com.google.adk.artifacts").

  * ## Uses of [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) that return [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier and Type

Method

Description

`[BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")`

Runner.`[artifactService](../../runner/Runner.html#artifactService\(\))()`

 

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier and Type

Method

Description

`[Runner.Builder](../../runner/Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[artifactService](../../runner/Runner.Builder.html#artifactService\(com.google.adk.artifacts.BaseArtifactService\))([BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

 

Constructors in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier

Constructor

Description

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins, @Nullable [EventsCompactionConfig](../../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, @Nullable [ContextCacheConfig](../../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

  * ## Uses of [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") in [com.google.adk.web](../../web/package-summary.html)

Methods in [com.google.adk.web](../../web/package-summary.html) that return [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier and Type

Method

Description

`[BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")`

AdkWebServer.`[artifactService](../../web/AdkWebServer.html#artifactService\(\))()`

Provides the singleton instance of the ArtifactService (InMemory).

  * ## Uses of [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") in [com.google.adk.web.controller](../../web/controller/package-summary.html)

Constructors in [com.google.adk.web.controller](../../web/controller/package-summary.html) with parameters of type [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier

Constructor

Description

` `

`[ArtifactController](../../web/controller/ArtifactController.html#%3Cinit%3E\(com.google.adk.artifacts.BaseArtifactService\))([BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

 

  * ## Uses of [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") in [com.google.adk.web.service](../../web/service/package-summary.html)

Constructors in [com.google.adk.web.service](../../web/service/package-summary.html) with parameters of type [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier

Constructor

Description

` `

`[RunnerService](../../web/service/RunnerService.html#%3Cinit%3E\(com.google.adk.web.AgentLoader,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([AgentLoader](../../web/AgentLoader.html "interface in com.google.adk.web") agentProvider, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../../plugins/BasePlugin.html "class in com.google.adk.plugins")> extraPlugins)`

 




* * *

Copyright (C) 1980\. All rights reserved.
