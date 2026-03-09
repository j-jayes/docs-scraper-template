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

com.google.adk.agents

 

com.google.adk.artifacts

 

com.google.adk.runner

 

com.google.adk.web

 

com.google.adk.web.controller

 

com.google.adk.web.service

 

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

`static [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../../agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.builder()`](../../agents/InvocationContext.html#builder\(\)) instead.

`static [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../../agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.builder()`](../../agents/InvocationContext.html#builder\(\)) instead.

Constructors in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier

Constructor

Description

` `

`[InvocationContext](../../agents/InvocationContext.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.memory.BaseMemoryService,com.google.adk.plugins.Plugin,java.util.Optional,java.util.Optional,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,java.util.Optional,com.google.adk.agents.RunConfig,boolean\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins") pluginManager, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, boolean endInvocation)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.builder()`](../../agents/InvocationContext.html#builder\(\)) instead.

` `

`[InvocationContext](../../agents/InvocationContext.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.memory.BaseMemoryService,java.util.Optional,java.util.Optional,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,java.util.Optional,com.google.adk.agents.RunConfig,boolean\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, boolean endInvocation)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.builder()`](../../agents/InvocationContext.html#builder\(\)) instead.

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

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../../plugins/BasePlugin.html "class in com.google.adk.plugins")> plugins)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.flows.llmflows.ResumabilityConfig\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../../plugins/BasePlugin.html "class in com.google.adk.plugins")> plugins, [ResumabilityConfig](../../flows/llmflows/ResumabilityConfig.html "class in com.google.adk.flows.llmflows") resumabilityConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.flows.llmflows.ResumabilityConfig,com.google.adk.summarizer.EventsCompactionConfig\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../../plugins/BasePlugin.html "class in com.google.adk.plugins")> plugins, [ResumabilityConfig](../../flows/llmflows/ResumabilityConfig.html "class in com.google.adk.flows.llmflows") resumabilityConfig, [EventsCompactionConfig](../../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig)`

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
