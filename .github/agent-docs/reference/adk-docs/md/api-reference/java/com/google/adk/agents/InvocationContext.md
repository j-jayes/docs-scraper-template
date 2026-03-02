JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InvocationContext.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [InvocationContext](InvocationContext.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. InvocationContext(InvocationContext.Builder)
     2. InvocationContext(BaseSessionService, BaseArtifactService, BaseMemoryService, Plugin, Optional, Optional, String, BaseAgent, Session, Optional, RunConfig, boolean)
     3. InvocationContext(BaseSessionService, BaseArtifactService, BaseMemoryService, Optional, Optional, String, BaseAgent, Session, Optional, RunConfig, boolean)
  6. Method Details
     1. create(BaseSessionService, BaseArtifactService, String, BaseAgent, Session, Content, RunConfig)
     2. create(BaseSessionService, BaseArtifactService, BaseAgent, Session, LiveRequestQueue, RunConfig)
     3. builder()
     4. toBuilder()
     5. copyOf(InvocationContext)
     6. sessionService()
     7. artifactService()
     8. memoryService()
     9. pluginManager()
     10. activeStreamingTools()
     11. liveRequestQueue()
     12. invocationId()
     13. branch(String)
     14. branch()
     15. agent()
     16. agent(BaseAgent)
     17. session()
     18. userContent()
     19. runConfig()
     20. callbackContextData()
     21. endInvocation()
     22. setEndInvocation(boolean)
     23. appName()
     24. userId()
     25. newInvocationContextId()
     26. incrementLlmCallsCount()
     27. eventsCompactionConfig()
     28. contextCacheConfig()
     29. equals(Object)
     30. hashCode()

Hide sidebar  Show sidebar

# Class InvocationContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.InvocationContext

* * *

public class InvocationContext extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

The context for an agent invocation.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

Builder for [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents").

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`InvocationContext([InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") builder)`

 

` `

`InvocationContext([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins") pluginManager, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig, boolean endInvocation)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use `builder()` instead.

` `

`InvocationContext([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig, boolean endInvocation)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use `builder()` instead.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ActiveStreamingTool](ActiveStreamingTool.html "class in com.google.adk.agents")>`

`activeStreamingTools()`

Returns a map of tool call IDs to active streaming tools for the current invocation.

`[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`

`agent()`

Returns the agent being invoked.

`void`

`agent([BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use `toBuilder()` and [`InvocationContext.Builder.agent(BaseAgent)`](InvocationContext.Builder.html#agent\(com.google.adk.agents.BaseAgent\)) instead.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`appName()`

Returns the application name associated with the session.

`[BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts")`

`artifactService()`

Returns the artifact service for persisting artifacts.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`branch()`

Returns the branch ID for the current invocation, if one is set.

`void`

`branch([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)`

Sets the [branch] ID for the current invocation.

`static [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`builder()`

Returns a new [`InvocationContext.Builder`](InvocationContext.Builder.html "class in com.google.adk.agents") for creating [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents") instances.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`callbackContextData()`

Returns a map for storing temporary context data that can be shared between different parts of the invocation (e.g., before/on/after model callbacks).

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ContextCacheConfig](ContextCacheConfig.html "class in com.google.adk.agents")>`

`contextCacheConfig()`

Returns the context cache configuration for the current agent run.

`static [InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`copyOf([InvocationContext](InvocationContext.html "class in com.google.adk.agents") other)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use `other.toBuilder().build()` instead.

`static [InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`create([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use `builder()` instead.

`static [InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`create([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)`

Deprecated, for removal: This API element is subject to removal in a future version.

Use `builder()` instead.

`boolean`

`endInvocation()`

Returns whether this invocation should be ended, e.g., due to reaching a terminal state or error.

`boolean`

`equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer")>`

`eventsCompactionConfig()`

Returns the events compaction configuration for the current agent run.

`int`

`hashCode()`

 

`void`

`incrementLlmCallsCount()`

Increments the count of LLM calls made during this invocation and throws an exception if the limit defined in [`RunConfig`](RunConfig.html "class in com.google.adk.agents") is exceeded.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`invocationId()`

Returns the unique ID for this invocation.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")>`

`liveRequestQueue()`

Returns the queue for managing live requests, if available for this invocation.

`[BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory")`

`memoryService()`

Returns the memory service for accessing agent memory.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`newInvocationContextId()`

Generates a new unique ID for an invocation context.

`[Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")`

`pluginManager()`

Returns the plugin manager for accessing tools and plugins.

`[RunConfig](RunConfig.html "class in com.google.adk.agents")`

`runConfig()`

Returns the configuration for the current agent run.

`[Session](../sessions/Session.html "class in com.google.adk.sessions")`

`session()`

Returns the session associated with this invocation.

`[BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions")`

`sessionService()`

Returns the session service for managing session state.

`void`

`setEndInvocation(boolean endInvocation)`

Sets whether this invocation should be ended.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`toBuilder()`

Returns a [`InvocationContext.Builder`](InvocationContext.Builder.html "class in com.google.adk.agents") initialized with the values of this instance.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

`userContent()`

Returns the user content that triggered this invocation, if any.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`userId()`

Returns the user ID associated with the session.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### InvocationContext

protected InvocationContext([InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") builder)

    * ### InvocationContext

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang")([forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval\(\) "class or interface in java.lang")=true) public InvocationContext([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins") pluginManager, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig, boolean endInvocation)

Deprecated, for removal: This API element is subject to removal in a future version.

Use `builder()` instead.

    * ### InvocationContext

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang")([forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval\(\) "class or interface in java.lang")=true) public InvocationContext([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig, boolean endInvocation)

Deprecated, for removal: This API element is subject to removal in a future version.

Use `builder()` instead.

  * ## Method Details

    * ### create

@InlineMe(replacement="InvocationContext.builder().sessionService(sessionService).artifactService(artifactService).invocationId(invocationId).agent(agent).session(session).userContent(Optional.ofNullable(userContent)).runConfig(runConfig).build()", imports={"com.google.adk.agents.InvocationContext","java.util.Optional"}) [@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang")([forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval\(\) "class or interface in java.lang")=true) public static [InvocationContext](InvocationContext.html "class in com.google.adk.agents") create([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, com.google.genai.types.Content userContent, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)

Deprecated, for removal: This API element is subject to removal in a future version.

Use `builder()` instead.

    * ### create

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang")([forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval\(\) "class or interface in java.lang")=true) public static [InvocationContext](InvocationContext.html "class in com.google.adk.agents") create([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService, [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService, [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent, [Session](../sessions/Session.html "class in com.google.adk.sessions") session, [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue, [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)

Deprecated, for removal: This API element is subject to removal in a future version.

Use `builder()` instead.

    * ### builder

public static [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") builder()

Returns a new [`InvocationContext.Builder`](InvocationContext.Builder.html "class in com.google.adk.agents") for creating [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents") instances.

    * ### toBuilder

public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") toBuilder()

Returns a [`InvocationContext.Builder`](InvocationContext.Builder.html "class in com.google.adk.agents") initialized with the values of this instance.

    * ### copyOf

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang")([forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval\(\) "class or interface in java.lang")=true) public static [InvocationContext](InvocationContext.html "class in com.google.adk.agents") copyOf([InvocationContext](InvocationContext.html "class in com.google.adk.agents") other)

Deprecated, for removal: This API element is subject to removal in a future version.

Use `other.toBuilder().build()` instead.

Creates a shallow copy of the given [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents").

    * ### sessionService

public [BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService()

Returns the session service for managing session state.

    * ### artifactService

public [BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService()

Returns the artifact service for persisting artifacts.

    * ### memoryService

public [BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService()

Returns the memory service for accessing agent memory.

    * ### pluginManager

public [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins") pluginManager()

Returns the plugin manager for accessing tools and plugins.

    * ### activeStreamingTools

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ActiveStreamingTool](ActiveStreamingTool.html "class in com.google.adk.agents")> activeStreamingTools()

Returns a map of tool call IDs to active streaming tools for the current invocation.

    * ### liveRequestQueue

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents")> liveRequestQueue()

Returns the queue for managing live requests, if available for this invocation.

    * ### invocationId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId()

Returns the unique ID for this invocation.

    * ### branch

public void branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)

Sets the [branch] ID for the current invocation. A branch represents a fork in the conversation history.

    * ### branch

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> branch()

Returns the branch ID for the current invocation, if one is set. A branch represents a fork in the conversation history.

    * ### agent

public [BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent()

Returns the agent being invoked.

    * ### agent

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang")([forRemoval](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html#forRemoval\(\) "class or interface in java.lang")=true) public void agent([BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent)

Deprecated, for removal: This API element is subject to removal in a future version.

Use `toBuilder()` and [`InvocationContext.Builder.agent(BaseAgent)`](InvocationContext.Builder.html#agent\(com.google.adk.agents.BaseAgent\)) instead.

Sets the [agent] being invoked. This is useful when delegating to a sub-agent.

    * ### session

public [Session](../sessions/Session.html "class in com.google.adk.sessions") session()

Returns the session associated with this invocation.

    * ### userContent

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content> userContent()

Returns the user content that triggered this invocation, if any.

    * ### runConfig

public [RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig()

Returns the configuration for the current agent run.

    * ### callbackContextData

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> callbackContextData()

Returns a map for storing temporary context data that can be shared between different parts of the invocation (e.g., before/on/after model callbacks).

    * ### endInvocation

public boolean endInvocation()

Returns whether this invocation should be ended, e.g., due to reaching a terminal state or error.

    * ### setEndInvocation

public void setEndInvocation(boolean endInvocation)

Sets whether this invocation should be ended.

    * ### appName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName()

Returns the application name associated with the session.

    * ### userId

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId()

Returns the user ID associated with the session.

    * ### newInvocationContextId

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") newInvocationContextId()

Generates a new unique ID for an invocation context.

    * ### incrementLlmCallsCount

public void incrementLlmCallsCount() throws [LlmCallsLimitExceededException](../models/LlmCallsLimitExceededException.html "class in com.google.adk.models")

Increments the count of LLM calls made during this invocation and throws an exception if the limit defined in [`RunConfig`](RunConfig.html "class in com.google.adk.agents") is exceeded.

Throws:
    `[LlmCallsLimitExceededException](../models/LlmCallsLimitExceededException.html "class in com.google.adk.models")` \- if the call limit is exceeded

    * ### eventsCompactionConfig

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer")> eventsCompactionConfig()

Returns the events compaction configuration for the current agent run.

    * ### contextCacheConfig

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ContextCacheConfig](ContextCacheConfig.html "class in com.google.adk.agents")> contextCacheConfig()

Returns the context cache configuration for the current agent run.

    * ### equals

public boolean equals([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") o)

Overrides:
    `[equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`

    * ### hashCode

public int hashCode()

Overrides:
    `[hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`




* * *

Copyright (C) 1980\. All rights reserved.
