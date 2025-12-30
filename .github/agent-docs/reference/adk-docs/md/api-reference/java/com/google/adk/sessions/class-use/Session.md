JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Session.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.sessions](../package-summary.html)
  2. [Session](../Session.html)



# Uses of Class  
com.google.adk.sessions.Session

Packages that use [Session](../Session.html "class in com.google.adk.sessions")

Package

Description

com.google.adk.agents

 

com.google.adk.memory

 

com.google.adk.runner

 

com.google.adk.sessions

 

com.google.adk.web

 

  * ## Uses of [Session](../Session.html "class in com.google.adk.sessions") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return [Session](../Session.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`[Session](../Session.html "class in com.google.adk.sessions")`

InvocationContext.`[session](../../agents/InvocationContext.html#session\(\))()`

 

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [Session](../Session.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`static [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../../agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`static [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../../agents/InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([BaseSessionService](../BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Session](../Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

 

  * ## Uses of [Session](../Session.html "class in com.google.adk.sessions") in [com.google.adk.memory](../../memory/package-summary.html)

Methods in [com.google.adk.memory](../../memory/package-summary.html) with parameters of type [Session](../Session.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

BaseMemoryService.`[addSessionToMemory](../../memory/BaseMemoryService.html#addSessionToMemory\(com.google.adk.sessions.Session\))([Session](../Session.html "class in com.google.adk.sessions") session)`

Adds a session to the memory service.

`io.reactivex.rxjava3.core.Completable`

InMemoryMemoryService.`[addSessionToMemory](../../memory/InMemoryMemoryService.html#addSessionToMemory\(com.google.adk.sessions.Session\))([Session](../Session.html "class in com.google.adk.sessions") session)`

 

  * ## Uses of [Session](../Session.html "class in com.google.adk.sessions") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [Session](../Session.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([Session](../Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in the standard mode using a provided Session object.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([Session](../Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in live mode, appending generated events to the session.

  * ## Uses of [Session](../Session.html "class in com.google.adk.sessions") in [com.google.adk.sessions](../package-summary.html)

Methods in [com.google.adk.sessions](../package-summary.html) that return [Session](../Session.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`[Session](../Session.html "class in com.google.adk.sessions")`

Session.Builder.`[build](../Session.Builder.html#build\(\))()`

 

`static [Session](../Session.html "class in com.google.adk.sessions")`

Session.`[fromJson](../Session.html#fromJson\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") json)`

 

Methods in [com.google.adk.sessions](../package-summary.html) that return types with arguments of type [Session](../Session.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Single<[Session](../Session.html "class in com.google.adk.sessions")>`

BaseSessionService.`[createSession](../BaseSessionService.html#createSession\(java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)`

Creates a new session with the specified application name and user ID, using a default state (null) and allowing the service to generate a unique session ID.

`io.reactivex.rxjava3.core.Single<[Session](../Session.html "class in com.google.adk.sessions")>`

BaseSessionService.`[createSession](../BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.concurrent.ConcurrentMap,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Creates a new session with the specified parameters.

`io.reactivex.rxjava3.core.Single<[Session](../Session.html "class in com.google.adk.sessions")>`

InMemorySessionService.`[createSession](../InMemorySessionService.html#createSession\(java.lang.String,java.lang.String,java.util.concurrent.ConcurrentMap,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @Nullable [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

 

`io.reactivex.rxjava3.core.Single<[Session](../Session.html "class in com.google.adk.sessions")>`

VertexAiSessionService.`[createSession](../VertexAiSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.concurrent.ConcurrentMap,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

 

`io.reactivex.rxjava3.core.Maybe<[Session](../Session.html "class in com.google.adk.sessions")>`

BaseSessionService.`[getSession](../BaseSessionService.html#getSession\(java.lang.String,java.lang.String,java.lang.String,java.util.Optional\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[GetSessionConfig](../GetSessionConfig.html "class in com.google.adk.sessions")> config)`

Retrieves a specific session, optionally filtering the events included.

`io.reactivex.rxjava3.core.Maybe<[Session](../Session.html "class in com.google.adk.sessions")>`

InMemorySessionService.`[getSession](../InMemorySessionService.html#getSession\(java.lang.String,java.lang.String,java.lang.String,java.util.Optional\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[GetSessionConfig](../GetSessionConfig.html "class in com.google.adk.sessions")> configOpt)`

 

`io.reactivex.rxjava3.core.Maybe<[Session](../Session.html "class in com.google.adk.sessions")>`

VertexAiSessionService.`[getSession](../VertexAiSessionService.html#getSession\(java.lang.String,java.lang.String,java.lang.String,java.util.Optional\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[GetSessionConfig](../GetSessionConfig.html "class in com.google.adk.sessions")> config)`

 

`abstract com.google.common.collect.ImmutableList<[Session](../Session.html "class in com.google.adk.sessions")>`

ListSessionsResponse.`[sessions](../ListSessionsResponse.html#sessions\(\))()`

 

Methods in [com.google.adk.sessions](../package-summary.html) with parameters of type [Session](../Session.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Single<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseSessionService.`[appendEvent](../BaseSessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../Session.html "class in com.google.adk.sessions") session, [Event](../../events/Event.html "class in com.google.adk.events") event)`

Appends an event to an in-memory session object and updates the session's state based on the event's state delta, if applicable.

`io.reactivex.rxjava3.core.Single<[Event](../../events/Event.html "class in com.google.adk.events")>`

InMemorySessionService.`[appendEvent](../InMemorySessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../Session.html "class in com.google.adk.sessions") session, [Event](../../events/Event.html "class in com.google.adk.events") event)`

 

`io.reactivex.rxjava3.core.Single<[Event](../../events/Event.html "class in com.google.adk.events")>`

VertexAiSessionService.`[appendEvent](../VertexAiSessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))([Session](../Session.html "class in com.google.adk.sessions") session, [Event](../../events/Event.html "class in com.google.adk.events") event)`

 

`default io.reactivex.rxjava3.core.Completable`

BaseSessionService.`[closeSession](../BaseSessionService.html#closeSession\(com.google.adk.sessions.Session\))([Session](../Session.html "class in com.google.adk.sessions") session)`

Closes a session.

Method parameters in [com.google.adk.sessions](../package-summary.html) with type arguments of type [Session](../Session.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`abstract [ListSessionsResponse.Builder](../ListSessionsResponse.Builder.html "class in com.google.adk.sessions")`

ListSessionsResponse.Builder.`[sessions](../ListSessionsResponse.Builder.html#sessions\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Session](../Session.html "class in com.google.adk.sessions")> sessions)`

 

  * ## Uses of [Session](../Session.html "class in com.google.adk.sessions") in [com.google.adk.web](../../web/package-summary.html)

Methods in [com.google.adk.web](../../web/package-summary.html) that return [Session](../Session.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`[Session](../Session.html "class in com.google.adk.sessions")`

AdkWebServer.AgentController.`[createSession](../../web/AdkWebServer.AgentController.html#createSession\(java.lang.String,java.lang.String,java.util.Map\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)`

Creates a new session where the ID is generated by the service.

`[Session](../Session.html "class in com.google.adk.sessions")`

AdkWebServer.AgentController.`[createSessionWithId](../../web/AdkWebServer.AgentController.html#createSessionWithId\(java.lang.String,java.lang.String,java.lang.String,java.util.Map\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state)`

Creates a new session with a specific ID provided by the client.

`[Session](../Session.html "class in com.google.adk.sessions")`

AdkWebServer.AgentController.`[getSession](../../web/AdkWebServer.AgentController.html#getSession\(java.lang.String,java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Retrieves a specific session by its ID.

Methods in [com.google.adk.web](../../web/package-summary.html) that return types with arguments of type [Session](../Session.html "class in com.google.adk.sessions")

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Session](../Session.html "class in com.google.adk.sessions")>`

AdkWebServer.AgentController.`[listSessions](../../web/AdkWebServer.AgentController.html#listSessions\(java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)`

Lists all non-evaluation sessions for a given app and user.




* * *

Copyright (C) 2025\. All rights reserved.
