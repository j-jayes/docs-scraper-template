JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LoopAgent.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [LoopAgent](LoopAgent.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. builder()
     2. runAsyncImpl(InvocationContext)
     3. runLiveImpl(InvocationContext)



# Class LoopAgent

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.agents.BaseAgent](BaseAgent.html "class in com.google.adk.agents")

com.google.adk.agents.LoopAgent

* * *

public class LoopAgent extends [BaseAgent](BaseAgent.html "class in com.google.adk.agents")

An agent that runs its sub-agents sequentially in a loop. 

The loop continues until a sub-agent escalates, or until the maximum number of iterations is reached (if specified).

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

Builder for [`LoopAgent`](LoopAgent.html "class in com.google.adk.agents").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents")`

`builder()`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific asynchronous logic.

`protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Agent-specific synchronous logic.

### Methods inherited from class com.google.adk.agents.[BaseAgent](BaseAgent.html "class in com.google.adk.agents")

`[afterAgentCallback](BaseAgent.html#afterAgentCallback\(\)), [beforeAgentCallback](BaseAgent.html#beforeAgentCallback\(\)), [description](BaseAgent.html#description\(\)), [findAgent](BaseAgent.html#findAgent\(java.lang.String\)), [findSubAgent](BaseAgent.html#findSubAgent\(java.lang.String\)), [name](BaseAgent.html#name\(\)), [parentAgent](BaseAgent.html#parentAgent\(\)), [parentAgent](BaseAgent.html#parentAgent\(com.google.adk.agents.BaseAgent\)), [rootAgent](BaseAgent.html#rootAgent\(\)), [runAsync](BaseAgent.html#runAsync\(com.google.adk.agents.InvocationContext\)), [runLive](BaseAgent.html#runLive\(com.google.adk.agents.InvocationContext\)), [subAgents](BaseAgent.html#subAgents\(\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### builder

public static [LoopAgent.Builder](LoopAgent.Builder.html "class in com.google.adk.agents") builder()

    * ### runAsyncImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runAsyncImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from class: `[BaseAgent](BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))`

Agent-specific asynchronous logic.

Specified by:
    `[runAsyncImpl](BaseAgent.html#runAsyncImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.

    * ### runLiveImpl

protected io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLiveImpl([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext)

Description copied from class: `[BaseAgent](BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))`

Agent-specific synchronous logic.

Specified by:
    `[runLiveImpl](BaseAgent.html#runLiveImpl\(com.google.adk.agents.InvocationContext\))` in class `[BaseAgent](BaseAgent.html "class in com.google.adk.agents")`
Parameters:
    `invocationContext` \- Current invocation context.
Returns:
    stream of agent-generated events.




* * *

Copyright (C) 2025\. All rights reserved.
