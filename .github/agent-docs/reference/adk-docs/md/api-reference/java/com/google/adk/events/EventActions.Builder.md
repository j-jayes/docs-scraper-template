JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/EventActions.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.events](package-summary.html)
  2. [EventActions](EventActions.html)
  3. [Builder](EventActions.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. skipSummarization(boolean)
     2. stateDelta(ConcurrentMap)
     3. artifactDelta(Map)
     4. deletedArtifactIds(Set)
     5. transferToAgent(String)
     6. escalate(boolean)
     7. requestedAuthConfigs(ConcurrentMap)
     8. requestedToolConfirmations(Map)
     9. endOfAgent(boolean)
     10. endInvocation(boolean)
     11. compaction(EventCompaction)
     12. merge(EventActions)
     13. build()

Hide sidebar  Show sidebar

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

All MethodsInstance MethodsConcrete MethodsDeprecated Methods

Modifier and Type

Method

Description

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`artifactDelta([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> value)`

 

`[EventActions](EventActions.html "class in com.google.adk.events")`

`build()`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`compaction(@Nullable [EventCompaction](EventCompaction.html "class in com.google.adk.events") value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`deletedArtifactIds([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`endInvocation(boolean endInvocation)`

Deprecated.

Use `endOfAgent(boolean)` instead.

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`endOfAgent(boolean endOfAgent)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`escalate(boolean escalate)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`merge([EventActions](EventActions.html "class in com.google.adk.events") other)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`requestedAuthConfigs([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`requestedToolConfirmations(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConfirmation](ToolConfirmation.html "class in com.google.adk.events")> value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`skipSummarization(boolean skipSummarization)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`stateDelta([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`transferToAgent(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentId)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

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

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") artifactDelta([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> value)

    * ### deletedArtifactIds

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") deletedArtifactIds([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> value)

    * ### transferToAgent

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") transferToAgent(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentId)

    * ### escalate

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") escalate(boolean escalate)

    * ### requestedAuthConfigs

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") requestedAuthConfigs([ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> value)

    * ### requestedToolConfirmations

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") requestedToolConfirmations(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConfirmation](ToolConfirmation.html "class in com.google.adk.events")> value)

    * ### endOfAgent

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") endOfAgent(boolean endOfAgent)

    * ### endInvocation

@CanIgnoreReturnValue [@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") endInvocation(boolean endInvocation)

Deprecated.

Use `endOfAgent(boolean)` instead.

    * ### compaction

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") compaction(@Nullable [EventCompaction](EventCompaction.html "class in com.google.adk.events") value)

    * ### merge

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") merge([EventActions](EventActions.html "class in com.google.adk.events") other)

    * ### build

public [EventActions](EventActions.html "class in com.google.adk.events") build()




* * *

Copyright (C) 1980\. All rights reserved.
