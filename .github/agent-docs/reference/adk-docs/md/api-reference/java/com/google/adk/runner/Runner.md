JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Runner.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.runner](package-summary.html)
  2. [Runner](Runner.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Runner(BaseAgent, String, BaseArtifactService, BaseSessionService)
  5. Method Details
     1. agent()
     2. appName()
     3. artifactService()
     4. sessionService()
     5. runAsync(String, String, Content, RunConfig)
     6. runAsync(String, String, Content)
     7. runAsync(Session, Content, RunConfig)
     8. runLive(Session, LiveRequestQueue, RunConfig)
     9. runLive(String, String, LiveRequestQueue, RunConfig)
     10. runWithSessionId(String, Content, RunConfig)



# Class Runner

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.runner.Runner

Direct Known Subclasses:
    `[InMemoryRunner](InMemoryRunner.html "class in com.google.adk.runner")`

* * *

public class Runner extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

The main class for the GenAI Agents runner.

  * ## Constructor Summary

Constructors

Constructor

Description

`Runner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Creates a new `Runner`.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")`

`agent()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`appName()`

 

`[BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts")`

`artifactService()`

 

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in the standard mode using a provided Session object.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage)`

Asynchronously runs the agent for a given user and session, processing a new message and using a default [`RunConfig`](../agents/RunConfig.html "class in com.google.adk.agents").

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in the standard mode.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLive([Session](../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in live mode, appending generated events to the session.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLive([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runWithSessionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent asynchronously with a default user ID.

`[BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions")`

`sessionService()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Runner

public Runner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)

Creates a new `Runner`.

  * ## Method Details

    * ### agent

public [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent()

    * ### appName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName()

    * ### artifactService

public [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService()

    * ### sessionService

public [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService()

    * ### runAsync

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

Runs the agent in the standard mode.

Parameters:
    `userId` \- The ID of the user for the session.
    `sessionId` \- The ID of the session to run the agent in.
    `newMessage` \- The new message from the user to process.
    `runConfig` \- Configuration for the agent run.
Returns:
    A Flowable stream of [`Event`](../events/Event.html "class in com.google.adk.events") objects generated by the agent during execution.

    * ### runAsync

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage)

Asynchronously runs the agent for a given user and session, processing a new message and using a default [`RunConfig`](../agents/RunConfig.html "class in com.google.adk.agents"). 

This method initiates an agent execution within the specified session, appending the provided new message to the session's history. It utilizes a default `RunConfig` to control execution parameters. The method returns a stream of [`Event`](../events/Event.html "class in com.google.adk.events") objects representing the agent's activity during the run.

Parameters:
    `userId` \- The ID of the user initiating the session.
    `sessionId` \- The ID of the session in which the agent will run.
    `newMessage` \- The new `Content` message to be processed by the agent.
Returns:
    A `Flowable` emitting [`Event`](../events/Event.html "class in com.google.adk.events") objects generated by the agent.

    * ### runAsync

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

Runs the agent in the standard mode using a provided Session object.

Parameters:
    `session` \- The session to run the agent in.
    `newMessage` \- The new message from the user to process.
    `runConfig` \- Configuration for the agent run.
Returns:
    A Flowable stream of [`Event`](../events/Event.html "class in com.google.adk.events") objects generated by the agent during execution.

    * ### runLive

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLive([Session](../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

Runs the agent in live mode, appending generated events to the session.

Returns:
    stream of events from the agent.

    * ### runLive

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLive([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

Retrieves the session and runs the agent in live mode.

Returns:
    stream of events from the agent.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if the session is not found.

    * ### runWithSessionId

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runWithSessionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

Runs the agent asynchronously with a default user ID.

Returns:
    stream of generated events.




* * *

Copyright (C) 2025\. All rights reserved.
