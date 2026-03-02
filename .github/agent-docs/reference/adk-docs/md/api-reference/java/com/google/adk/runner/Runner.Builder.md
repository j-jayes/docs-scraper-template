JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Runner.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



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
     8. build()

Hide sidebar  Show sidebar

# Class Runner.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.runner.Runner.Builder

Enclosing class:
    `[Runner](Runner.html "class in com.google.adk.runner")`

* * *

public static class Runner.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`appName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`artifactService([BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)`

 

`[Runner](Runner.html "class in com.google.adk.runner")`

`build()`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`memoryService([BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`plugins([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)`

 

`[Runner.Builder](Runner.Builder.html "class in com.google.adk.runner")`

`sessionService([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### app

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") app([App](../apps/App.html "class in com.google.adk.apps") app)

    * ### agent

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") agent([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent)

    * ### appName

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") appName([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)

    * ### artifactService

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") artifactService([BaseArtifactService](../artifacts/BaseArtifactService.html "interface in com.google.adk.artifacts") artifactService)

    * ### sessionService

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") sessionService([BaseSessionService](../sessions/BaseSessionService.html "interface in com.google.adk.sessions") sessionService)

    * ### memoryService

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") memoryService([BaseMemoryService](../memory/BaseMemoryService.html "interface in com.google.adk.memory") memoryService)

    * ### plugins

@CanIgnoreReturnValue public [Runner.Builder](Runner.Builder.html "class in com.google.adk.runner") plugins([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<? extends [Plugin](../plugins/Plugin.html "interface in com.google.adk.plugins")> plugins)

    * ### build

public [Runner](Runner.html "class in com.google.adk.runner") build()




* * *

Copyright (C) 1980\. All rights reserved.
