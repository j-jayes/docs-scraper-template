JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AgentExecutorConfig.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.a2a.executor](package-summary.html)
  2. [AgentExecutorConfig](AgentExecutorConfig.html)
  3. [Builder](AgentExecutorConfig.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. runConfig(RunConfig)
     2. outputMode(AgentExecutorConfig.OutputMode)
     3. beforeExecuteCallback(Callbacks.BeforeExecuteCallback)
     4. afterExecuteCallback(Callbacks.AfterExecuteCallback)
     5. afterEventCallback(Callbacks.AfterEventCallback)
     6. build()

Hide sidebar  Show sidebar

# Class AgentExecutorConfig.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.a2a.executor.AgentExecutorConfig.Builder

Enclosing class:
    `[AgentExecutorConfig](AgentExecutorConfig.html "class in com.google.adk.a2a.executor")`

* * *

public abstract static class AgentExecutorConfig.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`AgentExecutorConfig`](AgentExecutorConfig.html "class in com.google.adk.a2a.executor").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

`afterEventCallback([Callbacks.AfterEventCallback](Callbacks.AfterEventCallback.html "interface in com.google.adk.a2a.executor") afterEventCallback)`

 

`abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

`afterExecuteCallback([Callbacks.AfterExecuteCallback](Callbacks.AfterExecuteCallback.html "interface in com.google.adk.a2a.executor") afterExecuteCallback)`

 

`abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

`beforeExecuteCallback([Callbacks.BeforeExecuteCallback](Callbacks.BeforeExecuteCallback.html "interface in com.google.adk.a2a.executor") beforeExecuteCallback)`

 

`[AgentExecutorConfig](AgentExecutorConfig.html "class in com.google.adk.a2a.executor")`

`build()`

 

`abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

`outputMode([AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor") outputMode)`

 

`abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor")`

`runConfig([RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### runConfig

@CanIgnoreReturnValue public abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor") runConfig([RunConfig](../../agents/RunConfig.html "class in com.google.adk.agents") runConfig)

    * ### outputMode

@CanIgnoreReturnValue public abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor") outputMode([AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor") outputMode)

    * ### beforeExecuteCallback

@CanIgnoreReturnValue public abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor") beforeExecuteCallback([Callbacks.BeforeExecuteCallback](Callbacks.BeforeExecuteCallback.html "interface in com.google.adk.a2a.executor") beforeExecuteCallback)

    * ### afterExecuteCallback

@CanIgnoreReturnValue public abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor") afterExecuteCallback([Callbacks.AfterExecuteCallback](Callbacks.AfterExecuteCallback.html "interface in com.google.adk.a2a.executor") afterExecuteCallback)

    * ### afterEventCallback

@CanIgnoreReturnValue public abstract [AgentExecutorConfig.Builder](AgentExecutorConfig.Builder.html "class in com.google.adk.a2a.executor") afterEventCallback([Callbacks.AfterEventCallback](Callbacks.AfterEventCallback.html "interface in com.google.adk.a2a.executor") afterEventCallback)

    * ### build

public [AgentExecutorConfig](AgentExecutorConfig.html "class in com.google.adk.a2a.executor") build()




* * *

Copyright (C) 1980\. All rights reserved.
