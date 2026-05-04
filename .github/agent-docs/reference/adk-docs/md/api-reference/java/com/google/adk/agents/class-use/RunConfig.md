JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../RunConfig.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](../package-summary.html)
  2. [RunConfig](../RunConfig.html)



# Uses of Class  
com.google.adk.agents.RunConfig

Packages that use [RunConfig](../RunConfig.html "class in com.google.adk.agents")

Package

Description

com.google.adk.a2a.executor

 

com.google.adk.agents

 

com.google.adk.runner

 

  * ## Uses of [RunConfig](../RunConfig.html "class in com.google.adk.agents") in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html)

Methods in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html) that return [RunConfig](../RunConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`abstract [RunConfig](../RunConfig.html "class in com.google.adk.agents")`

AgentExecutorConfig.`[runConfig](../../a2a/executor/AgentExecutorConfig.html#runConfig\(\))()`

 

Methods in [com.google.adk.a2a.executor](../../a2a/executor/package-summary.html) with parameters of type [RunConfig](../RunConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`abstract [AgentExecutorConfig.Builder](../../a2a/executor/AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

AgentExecutorConfig.Builder.`[runConfig](../../a2a/executor/AgentExecutorConfig.Builder.html#runConfig\(com.google.adk.agents.RunConfig\))([RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

 

  * ## Uses of [RunConfig](../RunConfig.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return [RunConfig](../RunConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[RunConfig](../RunConfig.html "class in com.google.adk.agents")`

RunConfig.Builder.`[build](../RunConfig.Builder.html#build\(\))()`

 

`[RunConfig](../RunConfig.html "class in com.google.adk.agents")`

InvocationContext.`[runConfig](../InvocationContext.html#runConfig\(\))()`

Returns the configuration for the current agent run.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [RunConfig](../RunConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`static [RunConfig.Builder](../RunConfig.Builder.html "class in com.google.adk.agents")`

RunConfig.`[builder](../RunConfig.html#builder\(com.google.adk.agents.RunConfig\))([RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[runConfig](../InvocationContext.Builder.html#runConfig\(com.google.adk.agents.RunConfig\))([RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

Sets the configuration for the current agent run.

  * ## Uses of [RunConfig](../RunConfig.html "class in com.google.adk.agents") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [RunConfig](../RunConfig.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([SessionKey](../../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([SessionKey](../../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> stateDelta)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsync](../../runner/Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> stateDelta)`

Runs the agent with an invocation-based mode.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runAsyncImpl](../../runner/Runner.html#runAsyncImpl\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> stateDelta)`

Runs the agent asynchronously using a provided Session object.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(com.google.adk.sessions.SessionKey,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([SessionKey](../../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runLive](../../runner/Runner.html#runLive\(java.lang.String,java.lang.String,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

Runner.`[runLiveImpl](../../runner/Runner.html#runLiveImpl\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([Session](../../sessions/Session.html "class in com.google.adk.sessions") session, @Nullable [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in live mode, appending generated events to the session.




* * *

Copyright (C) 1980\. All rights reserved.
