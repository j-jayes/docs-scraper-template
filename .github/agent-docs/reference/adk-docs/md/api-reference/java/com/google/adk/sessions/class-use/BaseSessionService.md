JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseSessionService.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.sessions](../package-summary.html)
  2. [BaseSessionService](../BaseSessionService.html)



# Uses of Interface  
com.google.adk.sessions.BaseSessionService

Packages that use [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Package

Description

com.google.adk.a2a.executor

 

com.google.adk.agents

 

com.google.adk.runner

 

com.google.adk.sessions

 

com.google.adk.summarizer

 

com.google.adk.web

 

com.google.adk.web.controller

 

com.google.adk.web.service

 

com.google.adk.web.websocket

 

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html)

Methods in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`[AgentExecutor.Builder](../../a2a/executor/AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

AgentExecutor.Builder.`[sessionService](../../a2a/executor/AgentExecutor.Builder.html#sessionService\(com.google.adk.sessions.BaseSessionService\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`[BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")`

InvocationContext.`[sessionService](../../agents/InvocationContext.html#sessionService\(\))()`

Returns the session service for managing session state.

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`static [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../../agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.builder()`](../../agents/InvocationContext.html#builder\(\)) instead.

`static [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../../agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.builder()`](../../agents/InvocationContext.html#builder\(\)) instead.

`[InvocationContext.Builder](../../agents/InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[sessionService](../../agents/InvocationContext.Builder.html#sessionService\(com.google.adk.sessions.BaseSessionService\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Sets the session service for managing session state.

Constructors in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier

Constructor

Description

` `

`[InvocationContext](../../agents/InvocationContext.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.memory.BaseMemoryService,com.google.adk.plugins.Plugin,java.util.Optional,java.util.Optional,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,java.util.Optional,com.google.adk.agents.RunConfig,boolean\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins") pluginManager, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../Session.html "class in com.google.adk.sessions") session, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, boolean endInvocation)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.builder()`](../../agents/InvocationContext.html#builder\(\)) instead.

` `

`[InvocationContext](../../agents/InvocationContext.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.memory.BaseMemoryService,java.util.Optional,java.util.Optional,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,java.util.Optional,com.google.adk.agents.RunConfig,boolean\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../Session.html "class in com.google.adk.sessions") session, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig, boolean endInvocation)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use [`InvocationContext.builder()`](../../agents/InvocationContext.html#builder\(\)) instead.

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) that return [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`[BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")`

Runner.`[sessionService](../../runner/Runner.html#sessionService\(\))()`

 

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`[Runner.Builder](../../runner/Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[sessionService](../../runner/Runner.Builder.html#sessionService\(com.google.adk.sessions.BaseSessionService\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 

Constructors in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier

Constructor

Description

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

`protected `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List,com.google.adk.summarizer.EventsCompactionConfig,com.google.adk.agents.ContextCacheConfig\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins, [EventsCompactionConfig](../../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, [ContextCacheConfig](../../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

Deprecated.

Use [`Runner.Builder`](../../runner/Runner.Builder.html "class in com.google.adk.runner") instead.

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.sessions](../package-summary.html)

Classes in [com.google.adk.sessions](../package-summary.html) that implement [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Class

Description

`class `

`[FirestoreSessionService](../FirestoreSessionService.html "class in com.google.adk.sessions")`

FirestoreSessionService implements session management using Google Firestore as the backend storage.

`final class `

`[InMemorySessionService](../InMemorySessionService.html "class in com.google.adk.sessions")`

An in-memory implementation of [`BaseSessionService`](../BaseSessionService.html "interface in com.google.adk.sessions") assuming [`Session`](../Session.html "class in com.google.adk.sessions") objects are mutable regarding their state map, events list, and last update time.

`final class `

`[VertexAiSessionService](../VertexAiSessionService.html "class in com.google.adk.sessions")`

Connects to the managed Vertex AI Session Service.

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.summarizer](../../summarizer/package-summary.html)

Methods in [com.google.adk.summarizer](../../summarizer/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

EventCompactor.`[compact](../../summarizer/EventCompactor.html#compact\(com.google.adk.sessions.Session,com.google.adk.sessions.BaseSessionService\))([Session](../Session.html "class in com.google.adk.sessions") session, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Compacts events in the given session.

`io.reactivex.rxjava3.core.Completable`

SlidingWindowEventCompactor.`[compact](../../summarizer/SlidingWindowEventCompactor.html#compact\(com.google.adk.sessions.Session,com.google.adk.sessions.BaseSessionService\))([Session](../Session.html "class in com.google.adk.sessions") session, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Runs compaction for SlidingWindowCompactor.

`io.reactivex.rxjava3.core.Completable`

TailRetentionEventCompactor.`[compact](../../summarizer/TailRetentionEventCompactor.html#compact\(com.google.adk.sessions.Session,com.google.adk.sessions.BaseSessionService\))([Session](../Session.html "class in com.google.adk.sessions") session, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.web](../../web/package-summary.html)

Methods in [com.google.adk.web](../../web/package-summary.html) that return [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`[BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")`

AdkWebServer.`[sessionService](../../web/AdkWebServer.html#sessionService\(\))()`

 

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.web.controller](../../web/controller/package-summary.html)

Constructors in [com.google.adk.web.controller](../../web/controller/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier

Constructor

Description

` `

`[GraphController](../../web/controller/GraphController.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.web.AgentLoader\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [AgentLoader](../../web/AgentLoader.html "interface in com.google.adk.web") agentProvider)`

 

` `

`[SessionController](../../web/controller/SessionController.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.web.service](../../web/service/package-summary.html)

Constructors in [com.google.adk.web.service](../../web/service/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier

Constructor

Description

` `

`[RunnerService](../../web/service/RunnerService.html#%3Cinit%3E\(com.google.adk.web.AgentLoader,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService,com.google.adk.memory.BaseMemoryService,java.util.List\))([AgentLoader](../../web/AgentLoader.html "interface in com.google.adk.web") agentProvider, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BasePlugin](../../plugins/BasePlugin.html "class in com.google.adk.plugins")> extraPlugins)`

 

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.web.websocket](../../web/websocket/package-summary.html)

Constructors in [com.google.adk.web.websocket](../../web/websocket/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier

Constructor

Description

` `

`[LiveWebSocketHandler](../../web/websocket/LiveWebSocketHandler.html#%3Cinit%3E\(com.fasterxml.jackson.databind.ObjectMapper,com.google.adk.sessions.BaseSessionService,com.google.adk.web.service.RunnerService\))(com.fasterxml.jackson.databind.ObjectMapper objectMapper, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [RunnerService](../../web/service/RunnerService.html "class in com.google.adk.web.service") runnerService)`

 




* * *

Copyright (C) 1980\. All rights reserved.
