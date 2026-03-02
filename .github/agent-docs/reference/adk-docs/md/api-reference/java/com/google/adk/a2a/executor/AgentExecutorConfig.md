JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AgentExecutorConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.executor](package-summary.html)
  2. [AgentExecutorConfig](AgentExecutorConfig.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. AgentExecutorConfig()
  6. Method Details
     1. runConfig()
     2. beforeExecuteCallback()
     3. afterExecuteCallback()
     4. afterEventCallback()
     5. toBuilder()
     6. builder()

Hide sidebar  Show sidebar

# Class AgentExecutorConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.executor.AgentExecutorConfig

* * *

public abstract class AgentExecutorConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Configuration for the [`AgentExecutor`](AgentExecutor.html "class in com.google.adk.a2a.executor").

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

Builder for [`AgentExecutorConfig`](AgentExecutorConfig.html "class in com.google.adk.a2a.executor").

  * ## Constructor Summary

Constructors

Constructor

Description

`AgentExecutorConfig()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract @Nullable [Callbacks.AfterEventCallback](Callbacks.AfterEventCallback.html "interface in com.google.adk.a2a.executor")`

`afterEventCallback()`

 

`abstract @Nullable [Callbacks.AfterExecuteCallback](Callbacks.AfterExecuteCallback.html "interface in com.google.adk.a2a.executor")`

`afterExecuteCallback()`

 

`abstract @Nullable [Callbacks.BeforeExecuteCallback](Callbacks.BeforeExecuteCallback.html "interface in com.google.adk.a2a.executor")`

`beforeExecuteCallback()`

 

`static [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

`builder()`

 

`abstract [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents")`

`runConfig()`

 

`abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

`toBuilder()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### AgentExecutorConfig

public AgentExecutorConfig()

  * ## Method Details

    * ### runConfig

public abstract [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig()

    * ### beforeExecuteCallback

public abstract @Nullable [Callbacks.BeforeExecuteCallback](Callbacks.BeforeExecuteCallback.html "interface in com.google.adk.a2a.executor") beforeExecuteCallback()

    * ### afterExecuteCallback

public abstract @Nullable [Callbacks.AfterExecuteCallback](Callbacks.AfterExecuteCallback.html "interface in com.google.adk.a2a.executor") afterExecuteCallback()

    * ### afterEventCallback

public abstract @Nullable [Callbacks.AfterEventCallback](Callbacks.AfterEventCallback.html "interface in com.google.adk.a2a.executor") afterEventCallback()

    * ### toBuilder

public abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor") toBuilder()

    * ### builder

public static [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor") builder()




* * *

Copyright (C) 1980\. All rights reserved.
