JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/EventActions.Builder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.events](package-summary.html)
  2. [EventActions](EventActions.html)
  3. [Builder](EventActions.Builder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. skipSummarization(boolean)
     2. stateDelta(ConcurrentMap)
     3. artifactDelta(ConcurrentMap)
     4. transferToAgent(String)
     5. escalate(boolean)
     6. requestedAuthConfigs(ConcurrentMap)
     7. endInvocation(boolean)
     8. merge(EventActions)
     9. build()



# Class EventActions.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.events.EventActions.Builder

Enclosing class:
    `[EventActions](EventActions.html "class in com.google.adk.events")`

* * *

public static class EventActions.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`EventActions`](EventActions.html "class in com.google.adk.events").

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

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`artifactDelta([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), com.google.genai.types.Part> value)`

 

`[EventActions](EventActions.html "class in com.google.adk.events")`

`build()`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`endInvocation(boolean endInvocation)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`escalate(boolean escalate)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`merge([EventActions](EventActions.html "class in com.google.adk.events") other)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`requestedAuthConfigs([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`skipSummarization(boolean skipSummarization)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`stateDelta([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`transferToAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentId)`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### skipSummarization

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") skipSummarization(boolean skipSummarization)

    * ### stateDelta

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") stateDelta([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> value)

    * ### artifactDelta

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") artifactDelta([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), com.google.genai.types.Part> value)

    * ### transferToAgent

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") transferToAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentId)

    * ### escalate

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") escalate(boolean escalate)

    * ### requestedAuthConfigs

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") requestedAuthConfigs([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> value)

    * ### endInvocation

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") endInvocation(boolean endInvocation)

    * ### merge

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") merge([EventActions](EventActions.html "class in com.google.adk.events") other)

    * ### build

public [EventActions](EventActions.html "class in com.google.adk.events") build()




* * *

Copyright (C) 2025\. All rights reserved.
