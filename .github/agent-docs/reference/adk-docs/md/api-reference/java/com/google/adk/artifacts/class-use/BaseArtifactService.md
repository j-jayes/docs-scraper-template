JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseArtifactService.html)
  * Use
  * [Tree](../package-tree.html)
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

 

  * ## Uses of [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier and Type

Method

Description

`[BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")`

InvocationContext.`[artifactService](../../agents/InvocationContext.html#artifactService\(\))()`

 

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier and Type

Method

Description

`static [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../../agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`static [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../../agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

 

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

 

Constructors in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier

Constructor

Description

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Creates a new `Runner`.

  * ## Uses of [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") in [com.google.adk.web](../../web/package-summary.html)

Methods in [com.google.adk.web](../../web/package-summary.html) that return [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier and Type

Method

Description

`[BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")`

AdkWebServer.`[artifactService](../../web/AdkWebServer.html#artifactService\(\))()`

Provides the singleton instance of the ArtifactService (InMemory).

Constructors in [com.google.adk.web](../../web/package-summary.html) with parameters of type [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts")

Modifier

Constructor

Description

` `

`[AgentController](../../web/AdkWebServer.AgentController.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.util.Map,com.google.adk.web.AdkWebServer.ApiServerSpanExporter,com.google.adk.web.AdkWebServer.RunnerService\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")> agentRegistry, [AdkWebServer.ApiServerSpanExporter](../../web/AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web") apiServerSpanExporter, [AdkWebServer.RunnerService](../../web/AdkWebServer.RunnerService.html "class in com.google.adk.web") runnerService)`

Constructs the AgentController.

` `

`[RunnerService](../../web/AdkWebServer.RunnerService.html#%3Cinit%3E\(java.util.Map,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")> agentRegistry, [BaseArtifactService](../BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 




* * *

Copyright (C) 2025\. All rights reserved.
