JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/A2ASendMessageExecutor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.a2a](package-summary.html)
  2. [A2ASendMessageExecutor](A2ASendMessageExecutor.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. A2ASendMessageExecutor(InMemorySessionService, String)
     2. A2ASendMessageExecutor(BaseAgent, String, Duration)
  6. Method Details
     1. execute(Message, A2ASendMessageExecutor.AgentExecutionStrategy)
     2. execute(Message)

Hide sidebar  Show sidebar

# Class A2ASendMessageExecutor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.a2a.A2ASendMessageExecutor

* * *

public final class A2ASendMessageExecutor extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Shared SendMessage execution between HTTP service and other integrations. 

**EXPERIMENTAL:** Subject to change, rename, or removal in any future patch release. Do not use in production code.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static interface `

`[A2ASendMessageExecutor.AgentExecutionStrategy](A2ASendMessageExecutor.AgentExecutionStrategy.html "interface in com.google.adk.a2a")`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`A2ASendMessageExecutor([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") agentTimeout)`

 

`A2ASendMessageExecutor([InMemorySessionService](../sessions/InMemorySessionService.html "class in com.google.adk.sessions") sessionService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<io.a2a.spec.Message>`

`execute(@Nullable io.a2a.spec.Message request)`

 

`io.reactivex.rxjava3.core.Single<io.a2a.spec.Message>`

`execute(@Nullable io.a2a.spec.Message request, [A2ASendMessageExecutor.AgentExecutionStrategy](A2ASendMessageExecutor.AgentExecutionStrategy.html "interface in com.google.adk.a2a") agentExecutionStrategy)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### A2ASendMessageExecutor

public A2ASendMessageExecutor([InMemorySessionService](../sessions/InMemorySessionService.html "class in com.google.adk.sessions") sessionService, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName)

    * ### A2ASendMessageExecutor

public A2ASendMessageExecutor([BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") agentTimeout)

  * ## Method Details

    * ### execute

public io.reactivex.rxjava3.core.Single<io.a2a.spec.Message> execute(@Nullable io.a2a.spec.Message request, [A2ASendMessageExecutor.AgentExecutionStrategy](A2ASendMessageExecutor.AgentExecutionStrategy.html "interface in com.google.adk.a2a") agentExecutionStrategy)

    * ### execute

public io.reactivex.rxjava3.core.Single<io.a2a.spec.Message> execute(@Nullable io.a2a.spec.Message request)




* * *

Copyright (C) 1980\. All rights reserved.
