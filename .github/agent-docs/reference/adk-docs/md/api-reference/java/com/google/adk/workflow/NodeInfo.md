JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/NodeInfo.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [NodeInfo](NodeInfo.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. NodeInfo()
  6. Method Details
     1. path()
     2. outputFor()
     3. messageAsOutput()
     4. builder()
     5. toBuilder()

Hide sidebar  Show sidebar

# Class NodeInfo

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.workflow.NodeInfo

* * *

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public abstract class NodeInfo extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

The identity of the workflow-node activation that emitted an [`Event`](../events/Event.html "class in com.google.adk.events").

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[NodeInfo.Builder](NodeInfo.Builder.html "class in com.google.adk.workflow")`

Builder for [`NodeInfo`](NodeInfo.html "class in com.google.adk.workflow").

  * ## Constructor Summary

Constructors

Constructor

Description

`NodeInfo()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [NodeInfo.Builder](NodeInfo.Builder.html "class in com.google.adk.workflow")`

`builder()`

 

`abstract boolean`

`messageAsOutput()`

Returns `true` if this event's content is the node's output, so no separate output event follows.

`abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`outputFor()`

Returns the node paths this event's output counts for: the emitting node's path, followed by the paths of the ancestor workflows that use this event as their output.

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`path()`

Returns the emitting node's path.

`abstract [NodeInfo.Builder](NodeInfo.Builder.html "class in com.google.adk.workflow")`

`toBuilder()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### NodeInfo

public NodeInfo()

  * ## Method Details

    * ### path

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") path()

Returns the emitting node's path. Segments are `/`-separated and each is ` name@runId`, so a node of workflow `wf` reads `wf@1/a@1`; an empty path means the event did not come from a workflow node.

    * ### outputFor

public abstract com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> outputFor()

Returns the node paths this event's output counts for: the emitting node's path, followed by the paths of the ancestor workflows that use this event as their output. It is set on an event that carries the node's output, either in its `output` field or as a message-as-output event whose content is the output; an empty list means the output counts for no node.

    * ### messageAsOutput

public abstract boolean messageAsOutput()

Returns `true` if this event's content is the node's output, so no separate output event follows.

    * ### builder

public static [NodeInfo.Builder](NodeInfo.Builder.html "class in com.google.adk.workflow") builder()

    * ### toBuilder

public abstract [NodeInfo.Builder](NodeInfo.Builder.html "class in com.google.adk.workflow") toBuilder()




* * *

Copyright (C) 1980\. All rights reserved.
