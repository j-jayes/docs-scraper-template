JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseMemoryService.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.memory](../package-summary.html)
  2. [BaseMemoryService](../BaseMemoryService.html)



# Uses of Interface  
com.google.adk.memory.BaseMemoryService

Packages that use [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")

Package

Description

com.google.adk.a2a.executor

 

com.google.adk.agents

 

com.google.adk.memory

 

com.google.adk.runner

 

com.google.adk.web

 

com.google.adk.web.service

 

  * ## Uses of [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html)

Methods in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html) with parameters of type [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")

Modifier and Type

Method

Description

`[AgentExecutor.Builder](../../a2a/executor/AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

AgentExecutor.Builder.`[memoryService](../../a2a/executor/AgentExecutor.Builder.html#memoryService\(com.google.adk.memory.BaseMemoryService\))([BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

 

  * ## Uses of [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")

Modifier and Type

Method

Description

`[BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")`

InvocationContext.`[memoryService](../../agents/InvocationContext.html#memoryService\(\))()`

Returns the memory service for accessing agent memory.

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")

Modifier and Type

Method

Description

`[InvocationContext.Builder](../../agents/InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[memoryService](../../agents/InvocationContext.Builder.html#memoryService\(com.google.adk.memory.BaseMemoryService\))([BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

Sets the memory service for accessing agent memory.

  * ## Uses of [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") in [com.google.adk.memory](../package-summary.html)

Classes in [com.google.adk.memory](../package-summary.html) that implement [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")

Modifier and Type

Class

Description

`class `

`[FirestoreMemoryService](../FirestoreMemoryService.html "class in com.google.adk.memory")`

FirestoreMemoryService is an implementation of BaseMemoryService that uses Firestore to store and retrieve session memory entries.

`final class `

`[InMemoryMemoryService](../InMemoryMemoryService.html "class in com.google.adk.memory")`

An in-memory memory service for prototyping purposes only.

  * ## Uses of [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) that return [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")

Modifier and Type

Method

Description

`@Nullable [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")`

Runner.`[memoryService](../../runner/Runner.html#memoryService\(\))()`

 

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")

Modifier and Type

Method

Description

`[Runner.Builder](../../runner/Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[memoryService](../../runner/Runner.Builder.html#memoryService\(com.google.adk.memory.BaseMemoryService\))([BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

 

Constructors in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")

Modifier

Constructor

Description

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins, @Nullable [EventsCompactionConfig](../../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, @Nullable [ContextCacheConfig](../../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig,com.google.adk.apps.ResumabilityConfig\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins, @Nullable [EventsCompactionConfig](../../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, @Nullable [ContextCacheConfig](../../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig, @Nullable [ResumabilityConfig](../../apps/ResumabilityConfig.html "class in com.google.adk.apps") resumabilityConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

  * ## Uses of [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") in [com.google.adk.web](../../web/package-summary.html)

Methods in [com.google.adk.web](../../web/package-summary.html) that return [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")

Modifier and Type

Method

Description

`[BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")`

AdkWebServer.`[memoryService](../../web/AdkWebServer.html#memoryService\(\))()`

Provides the singleton instance of the MemoryService (InMemory).

  * ## Uses of [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") in [com.google.adk.web.service](../../web/service/package-summary.html)

Constructors in [com.google.adk.web.service](../../web/service/package-summary.html) with parameters of type [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory")

Modifier

Constructor

Description

` `

`[RunnerService](../../web/service/RunnerService.html#%3Cinit%3E\(com.google.adk.web.AgentLoader,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([AgentLoader](../../web/AgentLoader.html "interface in com.google.adk.web") agentProvider, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[BasePlugin](../../plugins/BasePlugin.html "class in com.google.adk.plugins")> extraPlugins)`

 




* * *

Copyright (C) 1980\. All rights reserved.
