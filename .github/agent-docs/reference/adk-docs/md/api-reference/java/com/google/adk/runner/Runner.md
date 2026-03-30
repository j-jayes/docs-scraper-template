JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Runner.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.runner](package-summary.html)
  2. [Runner](Runner.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService)
     2. Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService, List)
     3. Runner(BaseAgent, String, BaseArtifactService, BaseSessionService, BaseMemoryService, List, EventsCompactionConfig, ContextCacheConfig)
     4. Runner(BaseAgent, String, BaseArtifactService, BaseSessionService)
  6. Method Details
     1. builder()
     2. agent()
     3. appName()
     4. artifactService()
     5. sessionService()
     6. memoryService()
     7. pluginManager()
     8. close()
     9. runAsync(String, String, Content, RunConfig)
     10. runAsync(String, String, Content, RunConfig, Map)
     11. runAsync(SessionKey, Content, RunConfig, Map)
     12. runAsync(SessionKey, Content, RunConfig)
     13. runAsync(SessionKey, Content)
     14. runAsync(String, String, Content)
     15. runAsync(Session, Content, RunConfig)
     16. runAsync(Session, Content, RunConfig, Map)
     17. runAsyncImpl(Session, Content, RunConfig, Map)
     18. runLive(Session, LiveRequestQueue, RunConfig)
     19. runLive(String, String, LiveRequestQueue, RunConfig)
     20. runLive(SessionKey, LiveRequestQueue, RunConfig)
     21. runLiveImpl(Session, LiveRequestQueue, RunConfig)
     22. runWithSessionId(String, Content, RunConfig)

Hide sidebar  Show sidebar

# Class Runner

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.runner.Runner

Direct Known Subclasses:
    `[FirestoreDatabaseRunner](FirestoreDatabaseRunner.html "class in com.google.adk.runner"), [InMemoryRunner](InMemoryRunner.html "class in com.google.adk.runner")`

* * *

public class Runner extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

The main class for the GenAI Agents runner.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

Builder for [`Runner`](Runner.html "class in com.google.adk.runner").

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

` `

`Runner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Deprecated.

Use [`Runner.Builder`](Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`Runner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

Deprecated.

Use [`Runner.Builder`](Runner.Builder.html "class in com.google.adk.runner") instead.

` `

`Runner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

Deprecated.

Use [`Runner.Builder`](Runner.Builder.html "class in com.google.adk.runner") instead.

`protected `

`Runner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins, [EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, [ContextCacheConfig](../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

Deprecated.

Use [`Runner.Builder`](Runner.Builder.html "class in com.google.adk.runner") instead.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")`

`agent()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`appName()`

 

`[BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts")`

`artifactService()`

 

`static [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`builder()`

 

`io.reactivex.rxjava3.core.Completable`

`close()`

Closes all plugins, code executors, and releases any resources.

`[BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory")`

`memoryService()`

 

`[PluginManager](../plugins/PluginManager.html "class in com.google.adk.plugins")`

`pluginManager()`

 

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage)`

See `runAsync(String, String, Content, RunConfig, Map)`.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

See `runAsync(String, String, Content, RunConfig, Map)`.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)`

See `runAsync(String, String, Content, RunConfig, Map)`.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use runAsync with sessionId.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use runAsync with sessionId.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage)`

See `runAsync(String, String, Content, RunConfig, Map)`.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

See `runAsync(String, String, Content, RunConfig, Map)`.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsync([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)`

Runs the agent with an invocation-based mode.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsyncImpl([Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)`

Runs the agent asynchronously using a provided Session object.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLive([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLive([Session](../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

 

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLive([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Retrieves the session and runs the agent in live mode.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLiveImpl([Session](../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Runs the agent in live mode, appending generated events to the session.

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runWithSessionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

Deprecated, for removal: This API element is subject to removal in a future version.

`[BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions")`

`sessionService()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Runner

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public Runner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)

Deprecated.

Use [`Runner.Builder`](Runner.Builder.html "class in com.google.adk.runner") instead.

Creates a new `Runner`.

    * ### Runner

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public Runner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)

Deprecated.

Use [`Runner.Builder`](Runner.Builder.html "class in com.google.adk.runner") instead.

Creates a new `Runner` with a list of plugins.

    * ### Runner

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") protected Runner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, @Nullable [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins, @Nullable [EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig, @Nullable [ContextCacheConfig](../agents/ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)

Deprecated.

Use [`Runner.Builder`](Runner.Builder.html "class in com.google.adk.runner") instead.

Creates a new `Runner` with a list of plugins.

    * ### Runner

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public Runner([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)

Deprecated.

Use [`Runner.Builder`](Runner.Builder.html "class in com.google.adk.runner") instead.

Creates a new `Runner`.

  * ## Method Details

    * ### builder

public static [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") builder()

    * ### agent

public [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent()

    * ### appName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName()

    * ### artifactService

public [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService()

    * ### sessionService

public [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService()

    * ### memoryService

@Nullable public [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService()

    * ### pluginManager

public [PluginManager](../plugins/PluginManager.html "class in com.google.adk.plugins") pluginManager()

    * ### close

public io.reactivex.rxjava3.core.Completable close()

Closes all plugins, code executors, and releases any resources.

    * ### runAsync

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

See `runAsync(String, String, Content, RunConfig, Map)`.

    * ### runAsync

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)

Runs the agent with an invocation-based mode. 

TODO: make this the main implementation.

Parameters:
    `userId` \- The ID of the user for the session.
    `sessionId` \- The ID of the session to run the agent in.
    `newMessage` \- The new message from the user to process.
    `runConfig` \- Configuration for the agent run.
    `stateDelta` \- Optional map of state updates to merge into the session for this run.
Returns:
    A Flowable stream of [`Event`](../events/Event.html "class in com.google.adk.events") objects generated by the agent during execution.

    * ### runAsync

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)

See `runAsync(String, String, Content, RunConfig, Map)`.

    * ### runAsync

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

See `runAsync(String, String, Content, RunConfig, Map)`.

    * ### runAsync

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, com.google.genai.types.Content newMessage)

See `runAsync(String, String, Content, RunConfig, Map)`.

    * ### runAsync

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage)

See `runAsync(String, String, Content, RunConfig, Map)`.

    * ### runAsync

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang")([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since\(\) "class or interface in java.lang")="0.4.0", [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval\(\) "class or interface in java.lang")=true) public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

Deprecated, for removal: This API element is subject to removal in a future version.

Use runAsync with sessionId.

See `runAsync(Session, Content, RunConfig, Map)`.

    * ### runAsync

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang")([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since\(\) "class or interface in java.lang")="0.4.0", [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval\(\) "class or interface in java.lang")=true) public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsync([Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)

Deprecated, for removal: This API element is subject to removal in a future version.

Use runAsync with sessionId.

Runs the agent asynchronously using a provided Session object.

Parameters:
    `session` \- The session to run the agent in.
    `newMessage` \- The new message from the user to process.
    `runConfig` \- Configuration for the agent run.
    `stateDelta` \- Optional map of state updates to merge into the session for this run.
Returns:
    A Flowable stream of [`Event`](../events/Event.html "class in com.google.adk.events") objects generated by the agent during execution.

    * ### runAsyncImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsyncImpl([Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> stateDelta)

Runs the agent asynchronously using a provided Session object.

Parameters:
    `session` \- The session to run the agent in.
    `newMessage` \- The new message from the user to process.
    `runConfig` \- Configuration for the agent run.
    `stateDelta` \- Optional map of state updates to merge into the session for this run.
Returns:
    A Flowable stream of [`Event`](../events/Event.html "class in com.google.adk.events") objects generated by the agent during execution.

    * ### runLive

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLive([Session](../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

    * ### runLive

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLive([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

Retrieves the session and runs the agent in live mode.

Returns:
    stream of events from the agent.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if the session is not found.

    * ### runLive

public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLive([SessionKey](../sessions/SessionKey.html "class in com.google.adk.sessions") sessionKey, [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

Retrieves the session and runs the agent in live mode.

Returns:
    stream of events from the agent.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if the session is not found.

    * ### runLiveImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLiveImpl([Session](../sessions/Session.html "class in com.google.adk.sessions") session, @Nullable [LiveRequestQueue](../agents/LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

Runs the agent in live mode, appending generated events to the session.

Returns:
    stream of events from the agent.

    * ### runWithSessionId

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang")([since](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#since\(\) "class or interface in java.lang")="0.5.0", [forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval\(\) "class or interface in java.lang")=true) public io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runWithSessionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content newMessage, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

Deprecated, for removal: This API element is subject to removal in a future version.

Runs the agent asynchronously with a default user ID.

Returns:
    stream of generated events.




* * *

Copyright (C) 1980\. All rights reserved.
