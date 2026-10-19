JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Runner.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.runner](package-summary.html)
  2. [Runner](Runner.html)
  3. [Builder](Runner.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. app(App)
     2. agent(BaseAgent)
     3. appName(String)
     4. artifactService(BaseArtifactService)
     5. sessionService(BaseSessionService)
     6. memoryService(BaseMemoryService)
     7. plugins(List)
     8. plugins(Plugin...)
     9. scheduler(Scheduler)
     10. instantSource(InstantSource)
     11. uuidProvider(UuidProvider)
     12. build()

Hide sidebar  Show sidebar

# Class Runner.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.runner.Runner.Builder

Enclosing class:
    `[Runner](Runner.html "class in com.google.adk.runner")`

* * *

public static class Runner.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`Runner`](Runner.html "class in com.google.adk.runner").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`agent([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`app([App](../apps/App.html "class in com.google.adk.apps") app)`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`appName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName)`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`artifactService([BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

 

`[Runner](Runner.html "class in com.google.adk.runner")`

`build()`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`instantSource(@Nullable [InstantSource](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html "interface in java.time") instantSource)`

Sets the [`InstantSource`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html "interface in java.time") that supplies every timestamp this runner generates: event timestamps, and the `lastUpdateTime` of sessions created by the default in-memory session service, which is created on the first `build()`.

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`memoryService([BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`plugins([Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")... plugins)`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`plugins([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`scheduler(@Nullable io.reactivex.rxjava3.core.Scheduler scheduler)`

Sets the `Scheduler` for the work ADK hands off to worker threads in this runner's invocations: the sub-agents of a `ParallelAgent`, tool calls in [`RunConfig.ToolExecutionMode.PARALLEL_SUBSCRIBE`](../agents/RunConfig.ToolExecutionMode.html#PARALLEL_SUBSCRIBE) mode, and the hop that starts the live send loop.

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`sessionService([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`uuidProvider(@Nullable [UuidProvider](../platform/UuidProvider.html "interface in com.google.adk.platform") uuidProvider)`

Sets the [`UuidProvider`](../platform/UuidProvider.html "interface in com.google.adk.platform") that supplies every identifier this runner generates: event, invocation, and client function-call ids, and the ids of sessions created by the default in-memory session service, which is created on the first `build()`.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### app

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") app([App](../apps/App.html "class in com.google.adk.apps") app)

    * ### agent

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") agent([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)

    * ### appName

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") appName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName)

    * ### artifactService

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") artifactService([BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)

    * ### sessionService

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") sessionService([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)

    * ### memoryService

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") memoryService([BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)

    * ### plugins

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") plugins([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)

    * ### plugins

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") plugins([Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")... plugins)

    * ### scheduler

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") scheduler(@Nullable io.reactivex.rxjava3.core.Scheduler scheduler)

Sets the `Scheduler` for the work ADK hands off to worker threads in this runner's invocations: the sub-agents of a `ParallelAgent`, tool calls in [`RunConfig.ToolExecutionMode.PARALLEL_SUBSCRIBE`](../agents/RunConfig.ToolExecutionMode.html#PARALLEL_SUBSCRIBE) mode, and the hop that starts the live send loop. The runs that an `AgentTool` nests inherit it. An agent-level ` ParallelAgent.Builder#scheduler` or `LlmAgent.Builder#executor` takes precedence. `null` (the default) selects `Schedulers.io()`. 

Only these hand-offs are affected; work that completes asynchronously elsewhere (model clients, session services, MCP, plugins) stays on its own threads. ` Schedulers.trampoline()` runs the hand-offs inline, so sub-agents and tools are subscribed sequentially, but anything they start asynchronously can still overlap.

    * ### instantSource

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") instantSource(@Nullable [InstantSource](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html "interface in java.time") instantSource)

Sets the [`InstantSource`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html "interface in java.time") that supplies every timestamp this runner generates: event timestamps, and the `lastUpdateTime` of sessions created by the default in-memory session service, which is created on the first `build()`. `null` (the default) selects [`InstantSource.system()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html#system\(\)).

    * ### uuidProvider

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") uuidProvider(@Nullable [UuidProvider](../platform/UuidProvider.html "interface in com.google.adk.platform") uuidProvider)

Sets the [`UuidProvider`](../platform/UuidProvider.html "interface in com.google.adk.platform") that supplies every identifier this runner generates: event, invocation, and client function-call ids, and the ids of sessions created by the default in-memory session service, which is created on the first `build()`. `null` (the default) selects [`UuidProvider.SYSTEM`](../platform/UuidProvider.html#SYSTEM).

    * ### build

public [Runner](Runner.html "class in com.google.adk.runner") build()




* * *

Copyright (C) 1980\. All rights reserved.
