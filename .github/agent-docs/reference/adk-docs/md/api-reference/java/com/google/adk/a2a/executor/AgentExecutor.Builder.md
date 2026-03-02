JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AgentExecutor.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.executor](package-summary.html)
  2. [AgentExecutor](AgentExecutor.html)
  3. [Builder](AgentExecutor.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. agentExecutorConfig(AgentExecutorConfig)
     2. app(App)
     3. agent(BaseAgent)
     4. appName(String)
     5. artifactService(BaseArtifactService)
     6. sessionService(BaseSessionService)
     7. memoryService(BaseMemoryService)
     8. plugins(List)
     9. build()

Hide sidebar  Show sidebar

# Class AgentExecutor.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.executor.AgentExecutor.Builder

Enclosing class:
    `[AgentExecutor](AgentExecutor.html "class in com.google.adk.a2a.executor")`

* * *

public static class AgentExecutor.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`AgentExecutor`](AgentExecutor.html "class in com.google.adk.a2a.executor").

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

`[AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

`agent([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent)`

 

`[AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

`agentExecutorConfig([AgentExecutorConfig](AgentExecutorConfig.html "class in com.google.adk.a2a.executor") agentExecutorConfig)`

 

`[AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

`app([App](../../apps/App.html "class in com.google.adk.apps") app)`

 

`[AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

`appName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)`

 

`[AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

`artifactService([BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

 

`[AgentExecutor](AgentExecutor.html "class in com.google.adk.a2a.executor")`

`build()`

 

`[AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

`memoryService([BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

 

`[AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

`plugins([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

`[AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

`sessionService([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### agentExecutorConfig

@CanIgnoreReturnValue public [AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor") agentExecutorConfig([AgentExecutorConfig](AgentExecutorConfig.html "class in com.google.adk.a2a.executor") agentExecutorConfig)

    * ### app

@CanIgnoreReturnValue public [AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor") app([App](../../apps/App.html "class in com.google.adk.apps") app)

    * ### agent

@CanIgnoreReturnValue public [AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor") agent([BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents") agent)

    * ### appName

@CanIgnoreReturnValue public [AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor") appName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)

    * ### artifactService

@CanIgnoreReturnValue public [AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor") artifactService([BaseArtifactService](../../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)

    * ### sessionService

@CanIgnoreReturnValue public [AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor") sessionService([BaseSessionService](../../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)

    * ### memoryService

@CanIgnoreReturnValue public [AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor") memoryService([BaseMemoryService](../../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)

    * ### plugins

@CanIgnoreReturnValue public [AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor") plugins([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)

    * ### build

@CanIgnoreReturnValue public [AgentExecutor](AgentExecutor.html "class in com.google.adk.a2a.executor") build()




* * *

Copyright (C) 1980\. All rights reserved.
