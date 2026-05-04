JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AgentExecutorConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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
     2. outputMode()
     3. beforeExecuteCallback()
     4. afterExecuteCallback()
     5. afterEventCallback()
     6. toBuilder()
     7. builder()

Hide sidebar  Show sidebar

# Class AgentExecutorConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.a2a.executor.AgentExecutorConfig

* * *

public abstract class AgentExecutorConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Configuration for the [`AgentExecutor`](AgentExecutor.html "class in com.google.adk.a2a.executor").

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

Builder for [`AgentExecutorConfig`](AgentExecutorConfig.html "class in com.google.adk.a2a.executor").

`static enum `

`[AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor")`

Output mode for the agent executor.

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

 

`abstract [AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor")`

`outputMode()`

 

`abstract [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents")`

`runConfig()`

 

`abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

`toBuilder()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### AgentExecutorConfig

public AgentExecutorConfig()

  * ## Method Details

    * ### runConfig

public abstract [RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig()

    * ### outputMode

public abstract [AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor") outputMode()

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
