JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../LiveRequestQueue.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](../package-summary.html)
  2. [LiveRequestQueue](../LiveRequestQueue.html)



# Uses of Class  
com.google.adk.agents.LiveRequestQueue

Packages that use [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.runner

 

  * ## Uses of [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`@Nullable [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents")`

ActiveStreamingTool.`[stream](../ActiveStreamingTool.html#stream\(\))()`

Returns the active stream of this streaming tool.

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents")>`

InvocationContext.`[liveRequestQueue](../InvocationContext.html#liveRequestQueue\(\))()`

Returns the queue for managing live requests, if available for this invocation.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`[InvocationContext.Builder](../InvocationContext.Builder.html "class in com.google.adk.agents")`

InvocationContext.Builder.`[liveRequestQueue](../InvocationContext.Builder.html#liveRequestQueue\(com.google.adk.agents.LiveRequestQueue\))(@Nullable [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue)`

Sets the queue for managing live requests.

`void`

ActiveStreamingTool.`[stream](../ActiveStreamingTool.html#stream\(com.google.adk.agents.LiveRequestQueue\))(@Nullable [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") stream)`

Sets the active stream of this streaming tool.

Constructors in [com.google.adk.agents](../package-summary.html) with parameters of type [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents")

Modifier

Constructor

Description

` `

`[ActiveStreamingTool](../ActiveStreamingTool.html#%3Cinit%3E\(com.google.adk.agents.LiveRequestQueue\))([LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") stream)`

 

` `

`[ActiveStreamingTool](../ActiveStreamingTool.html#%3Cinit%3E\(io.reactivex.rxjava3.disposables.Disposable,com.google.adk.agents.LiveRequestQueue\))(io.reactivex.rxjava3.disposables.Disposable task, [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") stream)`

 

  * ## Uses of [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents") in [com.google.adk.runner](../../runner/package-summary.html)

Methods in [com.google.adk.runner](../../runner/package-summary.html) with parameters of type [LiveRequestQueue](../LiveRequestQueue.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

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
