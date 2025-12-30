JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/SequentialAgent.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [SequentialAgent](SequentialAgent.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. builder()
     2. runAsyncImpl(InvocationContext)
     3. runLiveImpl(InvocationContext)



# Class SequentialAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.agents.BaseAgent](BaseAgent.html "class in com.google.adk.agents")

com.google.adk.agents.SequentialAgent

* * *

public class SequentialAgent extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")

An agent that runs its sub-agents sequentially.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

Builder for [`SequentialAgent`](SequentialAgent.html "class in com.google.adk.agents").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents")`

`builder()`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents sequentially.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Runs sub-agents sequentially in live mode.

### Methods inherited from class com.google.adk.agents.[BaseAgent](BaseAgent.html "class in com.google.adk.agents")

`[afterAgentCallback](BaseAgent.html#afterAgentCallback\(\)), [beforeAgentCallback](BaseAgent.html#beforeAgentCallback\(\)), [description](BaseAgent.html#description\(\)), [findAgent](BaseAgent.html#findAgent\(java.lang.String\)), [findSubAgent](BaseAgent.html#findSubAgent\(java.lang.String\)), [name](BaseAgent.html#name\(\)), [parentAgent](BaseAgent.html#parentAgent\(\)), [parentAgent](BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\)), [rootAgent](BaseAgent.html#rootAgent\(\)), [runAsync](BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\)), [runLive](BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\)), [subAgents](BaseAgent.html#subAgents\(\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### builder

public static [SequentialAgent.Builder](SequentialAgent.Builder.html "class in com.google.adk.agents") builder()

    * ### runAsyncImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Runs sub-agents sequentially.

Specified by:
    `[runAsyncImpl](BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Invocation context.
Returns:
    Flowable emitting events from sub-agents.

    * ### runLiveImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Runs sub-agents sequentially in live mode.

Specified by:
    `[runLiveImpl](BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Invocation context.
Returns:
    Flowable emitting events from sub-agents in live mode.




* * *

Copyright (C) 2025\. All rights reserved.
