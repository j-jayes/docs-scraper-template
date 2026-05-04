JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/EventActions.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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
     1. skipSummarization(Boolean)
     2. stateDelta(Map)
     3. artifactDelta(Map)
     4. deletedArtifactIds(Set)
     5. transferToAgent(String)
     6. escalate(Boolean)
     7. requestedAuthConfigs(Map)
     8. requestedToolConfirmations(Map)
     9. endOfAgent(boolean)
     10. endInvocation(boolean)
     11. compaction(EventCompaction)
     12. merge(EventActions)
     13. build()

Hide sidebar  Show sidebar

# Class EventActions.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.events.EventActions.Builder

Enclosing class:
    `[EventActions](EventActions.html "class in com.google.adk.events")`

* * *

public static class EventActions.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

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

`artifactDelta(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> value)`

 

`[EventActions](EventActions.html "class in com.google.adk.events")`

`build()`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`compaction(@Nullable [EventCompaction](EventCompaction.html "class in com.google.adk.events") value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`deletedArtifactIds([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`endInvocation(boolean endInvocation)`

Deprecated.

Use `endOfAgent(boolean)` instead.

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`endOfAgent(boolean endOfAgent)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`escalate(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") escalate)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`merge([EventActions](EventActions.html "class in com.google.adk.events") other)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`requestedAuthConfigs(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), ? extends [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`requestedToolConfirmations(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConfirmation](ToolConfirmation.html "class in com.google.adk.events")> value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`skipSummarization(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") skipSummarization)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`stateDelta(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> value)`

 

`[EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events")`

`transferToAgent(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentId)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### skipSummarization

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") skipSummarization(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") skipSummarization)

    * ### stateDelta

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") stateDelta(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> value)

    * ### artifactDelta

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") artifactDelta(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> value)

    * ### deletedArtifactIds

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") deletedArtifactIds([Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> value)

    * ### transferToAgent

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") transferToAgent(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentId)

    * ### escalate

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") escalate(@Nullable [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") escalate)

    * ### requestedAuthConfigs

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") requestedAuthConfigs(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), ? extends [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> value)

    * ### requestedToolConfirmations

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") requestedToolConfirmations(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConfirmation](ToolConfirmation.html "class in com.google.adk.events")> value)

    * ### endOfAgent

@CanIgnoreReturnValue public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") endOfAgent(boolean endOfAgent)

    * ### endInvocation

@CanIgnoreReturnValue [@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public [EventActions.Builder](EventActions.Builder.html "class in com.google.adk.events") endInvocation(boolean endInvocation)

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
