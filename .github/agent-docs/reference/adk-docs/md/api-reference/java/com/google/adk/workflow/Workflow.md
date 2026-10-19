JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Workflow.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [Workflow](Workflow.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. builder()
     2. edges()
     3. maxConcurrency()
     4. runNode(Context, Object)

Hide sidebar  Show sidebar

# Class Workflow

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.workflow.BaseNode](BaseNode.html "class in com.google.adk.workflow")

com.google.adk.workflow.Workflow

All Implemented Interfaces:
    `[Node](Node.html "interface in com.google.adk.workflow")`

* * *

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public final class Workflow extends [BaseNode](BaseNode.html "class in com.google.adk.workflow")

A graph of nodes that is itself a node, so a workflow can go wherever a node can, including in another workflow.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static final class `

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

Builder for [`Workflow`](Workflow.html "class in com.google.adk.workflow").

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`builder()`

 

`com.google.common.collect.ImmutableList<[Edge](Edge.html "class in com.google.adk.workflow")>`

`edges()`

Returns the edges of the workflow's graph.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")>`

`maxConcurrency()`

Returns the maximum number of nodes the workflow runs at once, or empty if there is no limit.

`io.reactivex.rxjava3.core.Flowable<?>`

`runNode([Context](../agents/Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

Runs the node on `nodeInput`, the output it receives from its predecessors.

### Methods inherited from class [BaseNode](BaseNode.html#method-summary "class in com.google.adk.workflow")

`[config](BaseNode.html#config\(\) "config\(\)"), [description](BaseNode.html#description\(\) "description\(\)"), [inputSchema](BaseNode.html#inputSchema\(\) "inputSchema\(\)"), [name](BaseNode.html#name\(\) "name\(\)"), [outputSchema](BaseNode.html#outputSchema\(\) "outputSchema\(\)"), [rerunOnResume](BaseNode.html#rerunOnResume\(\) "rerunOnResume\(\)"), [stateSchema](BaseNode.html#stateSchema\(\) "stateSchema\(\)"), [waitForOutput](BaseNode.html#waitForOutput\(\) "waitForOutput\(\)")`

Modifier and Type

Method

Description

`[NodeConfig](NodeConfig.html "class in com.google.adk.workflow")`

`[config](BaseNode.html#config\(\))()`

Returns the node's retry policy and execution timeout.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[description](BaseNode.html#description\(\))()`

Returns what the node does, for humans and for a model that may call it.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`[inputSchema](BaseNode.html#inputSchema\(\))()`

Returns the schema the node's input must match.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](BaseNode.html#name\(\))()`

Returns the name that identifies the node within its graph.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`[outputSchema](BaseNode.html#outputSchema\(\))()`

Returns the schema that the node's output value must match.

`boolean`

`[rerunOnResume](BaseNode.html#rerunOnResume\(\))()`

Returns `true` if a resumed node runs again from scratch, rather than completing with the resuming answer as its output.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`[stateSchema](BaseNode.html#stateSchema\(\))()`

Returns the schema declaring the state keys the node uses.

`boolean`

`[waitForOutput](BaseNode.html#waitForOutput\(\))()`

Returns `true` if the node stays re-triggerable until it produces an output or a route, instead of completing when its run completes.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [Node](Node.html#method-summary "interface in com.google.adk.workflow")

`[requiresAllPredecessors](Node.html#requiresAllPredecessors\(\) "requiresAllPredecessors\(\)")`

Modifier and Type

Method

Description

`default boolean`

`[requiresAllPredecessors](Node.html#requiresAllPredecessors\(\))()`

Returns `true` if the node runs only once every predecessor has completed, receiving all their outputs keyed by node name, as a fan-in node does.




  * ## Method Details

    * ### builder

public static [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") builder()

    * ### edges

public com.google.common.collect.ImmutableList<[Edge](Edge.html "class in com.google.adk.workflow")> edges()

Returns the edges of the workflow's graph.

    * ### maxConcurrency

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> maxConcurrency()

Returns the maximum number of nodes the workflow runs at once, or empty if there is no limit.

    * ### runNode

public io.reactivex.rxjava3.core.Flowable<?> runNode([Context](../agents/Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)

Description copied from interface: `[Node](Node.html#runNode\(com.google.adk.agents.Context,java.lang.Object\))`

Runs the node on `nodeInput`, the output it receives from its predecessors. 

An emitted [`Event`](../events/Event.html "class in com.google.adk.events") passes through, and any other emitted value becomes the node's output (at most one per run); emit nothing for no output, since RxJava forbids null. The wildcard lets an implementation return a `Flowable` of its own type.




* * *

Copyright (C) 1980\. All rights reserved.
