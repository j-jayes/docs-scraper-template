JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseSessionService.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.sessions](../package-summary.html)
  2. [BaseSessionService](../BaseSessionService.html)



# Uses of Interface  
com.google.adk.sessions.BaseSessionService

Packages that use [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Package

Description

com.google.adk.agents

 

com.google.adk.runner

 

com.google.adk.sessions

 

com.google.adk.web

 

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`[BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")`

InvocationContext.`[sessionService](../../agents/InvocationContext.html#sessionService\(\))()`

 

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`static [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../../agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`static [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../../agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

 

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) that return [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`[BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")`

Runner.`[sessionService](../../runner/Runner.html#sessionService\(\))()`

 

Constructors in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier

Constructor

Description

` `

`[Runner](../../runner/Runner.html#%3Cinit%3E\(com.google.adk.agents.BaseAgent,java.lang.String,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Creates a new `Runner`.

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.sessions](../package-summary.html)

Classes in [com.google.adk.sessions](../package-summary.html) that implement [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Class

Description

`final class `

`[InMemorySessionService](../InMemorySessionService.html "class in com.google.adk.sessions")`

An in-memory implementation of [`BaseSessionService`](../BaseSessionService.html "interface in com.google.adk.sessions") assuming [`Session`](../Session.html "class in com.google.adk.sessions") objects are mutable regarding their state map, events list, and last update time.

`final class `

`[VertexAiSessionService](../VertexAiSessionService.html "class in com.google.adk.sessions")`

TODO: Use the genai HttpApiClient and ApiResponse methods once they are public.

  * ## Uses of [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") in [com.google.adk.web](../../web/package-summary.html)

Methods in [com.google.adk.web](../../web/package-summary.html) that return [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier and Type

Method

Description

`[BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")`

AdkWebServer.`[sessionService](../../web/AdkWebServer.html#sessionService\(\))()`

 

Constructors in [com.google.adk.web](../../web/package-summary.html) with parameters of type [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions")

Modifier

Constructor

Description

` `

`[AgentController](../../web/AdkWebServer.AgentController.html#%3Cinit%3E\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.util.Map,com.google.adk.web.AdkWebServer.ApiServerSpanExporter,com.google.adk.web.AdkWebServer.RunnerService\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")> agentRegistry, [AdkWebServer.ApiServerSpanExporter](../../web/AdkWebServer.ApiServerSpanExporter.html "class in com.google.adk.web") apiServerSpanExporter, [AdkWebServer.RunnerService](../../web/AdkWebServer.RunnerService.html "class in com.google.adk.web") runnerService)`

Constructs the AgentController.

` `

`[LiveWebSocketHandler](../../web/AdkWebServer.LiveWebSocketHandler.html#%3Cinit%3E\(com.fasterxml.jackson.databind.ObjectMapper,com.google.adk.sessions.BaseSessionService,com.google.adk.web.AdkWebServer.RunnerService\))(com.fasterxml.jackson.databind.ObjectMapper objectMapper, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [AdkWebServer.RunnerService](../../web/AdkWebServer.RunnerService.html "class in com.google.adk.web") runnerService)`

 

` `

`[RunnerService](../../web/AdkWebServer.RunnerService.html#%3Cinit%3E\(java.util.Map,com.google.adk.artifacts.BaseArtifactService,com.google.adk.sessions.BaseSessionService\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")> agentRegistry, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 




* * *

Copyright (C) 2025\. All rights reserved.
