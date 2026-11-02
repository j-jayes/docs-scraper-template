JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Runner.Builder.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.runner](../package-summary.html)
  2. [Runner](../Runner.html)
  3. [Builder](../Runner.Builder.html)



# Uses of Class  
com.google.adk.runner.Runner.Builder

Packages that use [Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")

Package

Description

com.google.adk.runner

 

  * ## Uses of [Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner") in [com.google.adk.runner](../package-summary.html)

Methods in [com.google.adk.runner](../package-summary.html) that return [Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")

Modifier and Type

Method

Description

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[agent](../Runner.Builder.html#agent\(com.google.adk.agents.BaseAgent\))([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent)`

 

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[app](../Runner.Builder.html#app\(com.google.adk.apps.App\))([App](../../apps/App.html "class in com.google.adk.apps") app)`

 

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[appName](../Runner.Builder.html#appName\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName)`

 

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[artifactService](../Runner.Builder.html#artifactService\(com.google.adk.artifacts.BaseArtifactService\))([BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

 

`static [Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.`[builder](../Runner.html#builder\(\))()`

 

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[instantSource](../Runner.Builder.html#instantSource\(java.time.InstantSource\))(@Nullable [InstantSource](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html "interface in java.time") instantSource)`

Sets the [`InstantSource`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/InstantSource.html "interface in java.time") that supplies every timestamp this runner generates: event timestamps, and the `lastUpdateTime` of sessions created by the default in-memory session service, which is created on the first `build()`.

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[memoryService](../Runner.Builder.html#memoryService\(com.google.adk.memory.BaseMemoryService\))([BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

 

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[plugins](../Runner.Builder.html#plugins\(com.google.adk.plugins.Plugin...\))([Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")... plugins)`

 

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[plugins](../Runner.Builder.html#plugins\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[scheduler](../Runner.Builder.html#scheduler\(io.reactivex.rxjava3.core.Scheduler\))(@Nullable io.reactivex.rxjava3.core.Scheduler scheduler)`

Sets the `Scheduler` for the work ADK hands off to worker threads in this runner's invocations: the sub-agents of a `ParallelAgent`, tool calls in [`RunConfig.ToolExecutionMode.PARALLEL_SUBSCRIBE`](../../agents/RunConfig.ToolExecutionMode.html#PARALLEL_SUBSCRIBE) mode, and the hop that starts the live send loop.

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[sessionService](../Runner.Builder.html#sessionService\(com.google.adk.sessions.BaseSessionService\))([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 

`[Runner.Builder](../Runner.Builder.html "class in com.google.adk.runner")`

Runner.Builder.`[uuidProvider](../Runner.Builder.html#uuidProvider\(com.google.adk.platform.UuidProvider\))(@Nullable [UuidProvider](../../platform/UuidProvider.html "interface in com.google.adk.platform") uuidProvider)`

Sets the [`UuidProvider`](../../platform/UuidProvider.html "interface in com.google.adk.platform") that supplies every identifier this runner generates: event, invocation, and client function-call ids, and the ids of sessions created by the default in-memory session service, which is created on the first `build()`.




* * *

Copyright (C) 1980\. All rights reserved.
