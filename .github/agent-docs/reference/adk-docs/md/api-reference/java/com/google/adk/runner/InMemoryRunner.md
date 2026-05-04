JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InMemoryRunner.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.runner](package-summary.html)
  2. [InMemoryRunner](InMemoryRunner.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. InMemoryRunner(BaseAgent)
     2. InMemoryRunner(BaseAgent, String)
     3. InMemoryRunner(BaseAgent, String, List)

Hide sidebar  Show sidebar

# Class InMemoryRunner

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.runner.Runner](Runner.html "class in com.google.adk.runner")

com.google.adk.runner.InMemoryRunner

* * *

public class InMemoryRunner extends [Runner](Runner.html "class in com.google.adk.runner")

The class for the in-memory GenAi runner, using in-memory artifact and session services.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [Runner](Runner.html#nested-class-summary "class in com.google.adk.runner")

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

Modifier and Type

Class

Description

`static class `

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

Builder for [`Runner`](Runner.html "class in com.google.adk.runner").

  * ## Constructor Summary

Constructors

Constructor

Description

`InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)`

 

`InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName)`

 

`InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

  * ## Method Summary

### Methods inherited from class [Runner](Runner.html#method-summary "class in com.google.adk.runner")

`[agent](Runner.html#agent\(\) "agent\(\)"), [appName](Runner.html#appName\(\) "appName\(\)"), [artifactService](Runner.html#artifactService\(\) "artifactService\(\)"), [builder](Runner.html#builder\(\) "builder\(\)"), [close](Runner.html#close\(\) "close\(\)"), [memoryService](Runner.html#memoryService\(\) "memoryService\(\)"), [pluginManager](Runner.html#pluginManager\(\) "pluginManager\(\)"), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content\) "runAsync\(SessionKey, Content\)"), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig\) "runAsync\(SessionKey, Content, RunConfig\)"), [runAsync](Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\) "runAsync\(SessionKey, Content, RunConfig, Map\)"), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content\) "runAsync\(String, String, Content\)"), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\) "runAsync\(String, String, Content, RunConfig\)"), [runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\) "runAsync\(String, String, Content, RunConfig, Map\)"), [runAsyncImpl](Runner.html#runAsyncImpl\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\) "runAsyncImpl\(Session, Content, RunConfig, Map\)"), [runLive](Runner.html#runLive\(com.google.adk.sessions.SessionKey,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\) "runLive\(SessionKey, LiveRequestQueue, RunConfig\)"), [runLive](Runner.html#runLive\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\) "runLive\(Session, LiveRequestQueue, RunConfig\)"), [runLive](Runner.html#runLive\(java.lang.String,java.lang.String,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\) "runLive\(String, String, LiveRequestQueue, RunConfig\)"), [runLiveImpl](Runner.html#runLiveImpl\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\) "runLiveImpl\(Session, LiveRequestQueue, RunConfig\)"), [sessionService](Runner.html#sessionService\(\) "sessionService\(\)")`

Modifier and Type

Method

Description

`[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")`

`[agent](Runner.html#agent\(\))()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[appName](Runner.html#appName\(\))()`

 

`[BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts")`

`[artifactService](Runner.html#artifactService\(\))()`

 

`static [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`[builder](Runner.html#builder\(\))()`

 

`io.reactivex.rxjava3.core.Completable`

`[close](Runner.html#close\(\))()`

Closes all plugins, code executors, and releases any resources.

`@Nullable [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory")`

`[memoryService](Runner.html#memoryService\(\))()`

 

`[PluginManager](../plugins/PluginManager.html "class in com.google.adk.plugins")`

`[pluginManager](Runner.html#pluginManager\(\))()`

 

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runAsync](Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runAsync](Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runAsync](Runner.html#runAsync\(com.google.adk.sessions.SessionKey,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> stateDelta)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, com.google.genai.types.Content newMessage)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

See [`Runner.runAsync(String, String, Content, RunConfig, Map)`](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\)).

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runAsync](Runner.html#runAsync\(java.lang.String,java.lang.String,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> stateDelta)`

Runs the agent with an invocation-based mode.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runAsyncImpl](Runner.html#runAsyncImpl\(com.google.adk.sessions.Session,com.google.genai.types.Content,com.google.adk.agents.RunConfig,java.util.Map\))([Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> stateDelta)`

Runs the agent asynchronously using a provided Session object.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runLive](Runner.html#runLive\(com.google.adk.sessions.SessionKey,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runLive](Runner.html#runLive\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([Session](../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runLive](Runner.html#runLive\(java.lang.String,java.lang.String,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`[runLiveImpl](Runner.html#runLiveImpl\(com.google.adk.sessions.Session,com.google.adk.agents.LiveRequestQueue,com.google.adk.agents.RunConfig\))([Session](../sessions/Session.html "class in com.google.adk.sessions") session, @Nullable [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in live mode, appending generated events to the session.

`[BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions")`

`[sessionService](Runner.html#sessionService\(\))()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### InMemoryRunner

public InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)

    * ### InMemoryRunner

public InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName)

    * ### InMemoryRunner

public InMemoryRunner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)




* * *

Copyright (C) 1980\. All rights reserved.
