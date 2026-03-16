JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InvocationContext.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [InvocationContext](InvocationContext.html)
  3. [Builder](InvocationContext.Builder.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. sessionService(BaseSessionService)
     2. artifactService(BaseArtifactService)
     3. memoryService(BaseMemoryService)
     4. pluginManager(Plugin)
     5. liveRequestQueue(LiveRequestQueue)
     6. branch(String)
     7. invocationId(String)
     8. agent(BaseAgent)
     9. session(Session)
     10. userContent(Content)
     11. runConfig(RunConfig)
     12. endInvocation(boolean)
     13. eventsCompactionConfig(EventsCompactionConfig)
     14. contextCacheConfig(ContextCacheConfig)
     15. callbackContextData(Map)
     16. build()

Hide sidebar  Show sidebar

# Class InvocationContext.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.agents.InvocationContext.Builder

Enclosing class:
    `[InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

* * *

public static class InvocationContext.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents").

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`agent([BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent)`

Sets the agent being invoked.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`artifactService([BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

Sets the artifact service for persisting artifacts.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`branch([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)`

Sets the branch ID for the invocation.

`[InvocationContext](InvocationContext.html "class in com.google.adk.agents")`

`build()`

Builds the [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents") instance.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`callbackContextData([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> callbackContextData)`

Sets the callback context data for the invocation.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`contextCacheConfig([ContextCacheConfig](ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)`

Sets the context cache configuration for the current agent run.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`endInvocation(boolean endInvocation)`

Sets whether this invocation should be ended.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`eventsCompactionConfig([EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig)`

Sets the events compaction configuration for the current agent run.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`invocationId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)`

Sets the unique ID for the invocation.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`liveRequestQueue([LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue)`

Sets the queue for managing live requests.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`memoryService([BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

Sets the memory service for accessing agent memory.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`pluginManager([Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins") pluginManager)`

Sets the plugin manager for accessing tools and plugins.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`runConfig([RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)`

Sets the configuration for the current agent run.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`session([Session](../sessions/Session.html "class in com.google.adk.sessions") session)`

Sets the session associated with this invocation.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`sessionService([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

Sets the session service for managing session state.

`[InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents")`

`userContent(com.google.genai.types.Content userContent)`

Sets the user content that triggered this invocation.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### sessionService

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") sessionService([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)

Sets the session service for managing session state.

Parameters:
    `sessionService` \- the session service to use; required.
Returns:
    this builder instance for chaining.

    * ### artifactService

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") artifactService([BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)

Sets the artifact service for persisting artifacts.

Parameters:
    `artifactService` \- the artifact service to use; required.
Returns:
    this builder instance for chaining.

    * ### memoryService

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") memoryService([BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)

Sets the memory service for accessing agent memory.

Parameters:
    `memoryService` \- the memory service to use.
Returns:
    this builder instance for chaining.

    * ### pluginManager

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") pluginManager([Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins") pluginManager)

Sets the plugin manager for accessing tools and plugins.

Parameters:
    `pluginManager` \- the plugin manager to use.
Returns:
    this builder instance for chaining.

    * ### liveRequestQueue

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") liveRequestQueue(@Nullable [LiveRequestQueue](LiveRequestQueue.html "class in com.google.adk.agents") liveRequestQueue)

Sets the queue for managing live requests.

Parameters:
    `liveRequestQueue` \- the queue for managing live requests.
Returns:
    this builder instance for chaining.

    * ### branch

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") branch(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") branch)

Sets the branch ID for the invocation.

Parameters:
    `branch` \- the branch ID for the invocation.
Returns:
    this builder instance for chaining.

    * ### invocationId

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") invocationId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)

Sets the unique ID for the invocation.

Parameters:
    `invocationId` \- the unique ID for the invocation.
Returns:
    this builder instance for chaining.

    * ### agent

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") agent([BaseAgent](BaseAgent.html "class in com.google.adk.agents") agent)

Sets the agent being invoked.

Parameters:
    `agent` \- the agent being invoked; required.
Returns:
    this builder instance for chaining.

    * ### session

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") session([Session](../sessions/Session.html "class in com.google.adk.sessions") session)

Sets the session associated with this invocation.

Parameters:
    `session` \- the session associated with this invocation; required.
Returns:
    this builder instance for chaining.

    * ### userContent

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") userContent(@Nullable com.google.genai.types.Content userContent)

Sets the user content that triggered this invocation.

Parameters:
    `userContent` \- the user content that triggered this invocation.
Returns:
    this builder instance for chaining.

    * ### runConfig

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") runConfig([RunConfig](RunConfig.html "class in com.google.adk.agents") runConfig)

Sets the configuration for the current agent run.

Parameters:
    `runConfig` \- the configuration for the current agent run.
Returns:
    this builder instance for chaining.

    * ### endInvocation

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") endInvocation(boolean endInvocation)

Sets whether this invocation should be ended.

Parameters:
    `endInvocation` \- whether this invocation should be ended.
Returns:
    this builder instance for chaining.

    * ### eventsCompactionConfig

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") eventsCompactionConfig(@Nullable [EventsCompactionConfig](../summarizer/EventsCompactionConfig.html "class in com.google.adk.summarizer") eventsCompactionConfig)

Sets the events compaction configuration for the current agent run.

Parameters:
    `eventsCompactionConfig` \- the events compaction configuration.
Returns:
    this builder instance for chaining.

    * ### contextCacheConfig

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") contextCacheConfig(@Nullable [ContextCacheConfig](ContextCacheConfig.html "class in com.google.adk.agents") contextCacheConfig)

Sets the context cache configuration for the current agent run.

Parameters:
    `contextCacheConfig` \- the context cache configuration.
Returns:
    this builder instance for chaining.

    * ### callbackContextData

@CanIgnoreReturnValue public [InvocationContext.Builder](InvocationContext.Builder.html "class in com.google.adk.agents") callbackContextData([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> callbackContextData)

Sets the callback context data for the invocation.

Parameters:
    `callbackContextData` \- the callback context data.
Returns:
    this builder instance for chaining.

    * ### build

public [InvocationContext](InvocationContext.html "class in com.google.adk.agents") build()

Builds the [`InvocationContext`](InvocationContext.html "class in com.google.adk.agents") instance.

Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class or interface in java.lang")` \- if any required parameters are missing.




* * *

Copyright (C) 1980\. All rights reserved.
