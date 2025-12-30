JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../RunConfig.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [RunConfig](../RunConfig.html)



# Uses of Class  
com.google.adk.agents.RunConfig

Packages that use [RunConfig](../RunConfig.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.runner

 

  * ## Uses of [RunConfig](../RunConfig.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return [RunConfig](../RunConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[RunConfig](../RunConfig.html "class in com.google.adk.agents")`

RunConfig.Builder.`[build](../RunConfig.Builder.html#build\(\))()`

 

`[RunConfig](../RunConfig.html "class in com.google.adk.agents")`

InvocationContext.`[runConfig](../InvocationContext.html#runConfig\(\))()`

 

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [RunConfig](../RunConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [RunConfig.Builder](../RunConfig.Builder.html "class in com.google.adk.agents")`

RunConfig.`[builder](../RunConfig.html#builder\(com.google.adk.agents.RunConfig\))([RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`static [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`static [InvocationContext](../InvocationContext.html "class in com.google.adk.agents")`

InvocationContext.`[create](../InvocationContext.html#create\(com.google.adk.sessions.BaseSessionService,com.google.adk.artifacts.BaseArtifactService,java.lang.String,com.google.adk.agents.BaseAgent,com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](../BaseAgent.html "class in com.google.adk.agents") agent, [Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

 

  * ## Uses of [RunConfig](../RunConfig.html "class in com.google.adk.agents") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [RunConfig](../RunConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in the standard mode using a provided Session object.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in the standard mode.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in live mode, appending generated events to the session.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(java.lang.String,java.lang.String,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runWithSessionId](../../runner/Runner.html#runWithSessionId\(java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent asynchronously with a default user ID.




* * *

Copyright (C) 2025\. All rights reserved.
