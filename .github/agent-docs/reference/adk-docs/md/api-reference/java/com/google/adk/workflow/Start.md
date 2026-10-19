JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Start.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [Start](Start.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. INSTANCE
  5. Method Details
     1. name()
     2. runNode(Context, Object)

Hide sidebar  Show sidebar

# Class Start

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.workflow.Start

All Implemented Interfaces:
    `[Node](Node.html "interface in com.google.adk.workflow")`

* * *

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public final class Start extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [Node](Node.html "interface in com.google.adk.workflow")

The node that marks where a workflow graph starts. It never runs: the workflow passes its own input to the nodes that `Start` has edges to.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [Start](Start.html "class in com.google.adk.workflow")`

`INSTANCE`

The start node that every graph uses.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`name()`

Returns the name that identifies the node within its graph.

`io.reactivex.rxjava3.core.Flowable<?>`

`runNode([Context](../agents/Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

Runs the node on `nodeInput`, the output it receives from its predecessors.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [Node](Node.html#method-summary "interface in com.google.adk.workflow")

`[config](Node.html#config\(\) "config\(\)"), [description](Node.html#description\(\) "description\(\)"), [inputSchema](Node.html#inputSchema\(\) "inputSchema\(\)"), [outputSchema](Node.html#outputSchema\(\) "outputSchema\(\)"), [requiresAllPredecessors](Node.html#requiresAllPredecessors\(\) "requiresAllPredecessors\(\)"), [rerunOnResume](Node.html#rerunOnResume\(\) "rerunOnResume\(\)"), [stateSchema](Node.html#stateSchema\(\) "stateSchema\(\)"), [waitForOutput](Node.html#waitForOutput\(\) "waitForOutput\(\)")`

Modifier and Type

Method

Description

`default [NodeConfig](NodeConfig.html "class in com.google.adk.workflow")`

`[config](Node.html#config\(\))()`

Returns the node's retry policy and execution timeout.

`default [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[description](Node.html#description\(\))()`

Returns what the node does, for humans and for a model that may call it.

`default [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`[inputSchema](Node.html#inputSchema\(\))()`

Returns the schema the node's input must match.

`default [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`[outputSchema](Node.html#outputSchema\(\))()`

Returns the schema that the node's output value must match.

`default boolean`

`[requiresAllPredecessors](Node.html#requiresAllPredecessors\(\))()`

Returns `true` if the node runs only once every predecessor has completed, receiving all their outputs keyed by node name, as a fan-in node does.

`default boolean`

`[rerunOnResume](Node.html#rerunOnResume\(\))()`

Returns `true` if a resumed node runs again from scratch, rather than completing with the resuming answer as its output.

`default [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`[stateSchema](Node.html#stateSchema\(\))()`

Returns the schema declaring the state keys the node uses.

`default boolean`

`[waitForOutput](Node.html#waitForOutput\(\))()`

Returns `true` if the node stays re-triggerable until it produces an output or a route, instead of completing when its run completes.




  * ## Field Details

    * ### INSTANCE

public static final [Start](Start.html "class in com.google.adk.workflow") INSTANCE

The start node that every graph uses.

  * ## Method Details

    * ### name

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name()

Description copied from interface: `[Node](Node.html#name\(\))`

Returns the name that identifies the node within its graph.

Specified by:
    `[name](Node.html#name\(\))` in interface `[Node](Node.html "interface in com.google.adk.workflow")`

    * ### runNode

public io.reactivex.rxjava3.core.Flowable<?> runNode([Context](../agents/Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)

Description copied from interface: `[Node](Node.html#runNode\(com.google.adk.agents.Context,java.lang.Object\))`

Runs the node on `nodeInput`, the output it receives from its predecessors. 

An emitted [`Event`](../events/Event.html "class in com.google.adk.events") passes through, and any other emitted value becomes the node's output (at most one per run); emit nothing for no output, since RxJava forbids null. The wildcard lets an implementation return a `Flowable` of its own type.

Specified by:
    `[runNode](Node.html#runNode\(com.google.adk.agents.Context,java.lang.Object\))` in interface `[Node](Node.html "interface in com.google.adk.workflow")`




* * *

Copyright (C) 1980\. All rights reserved.
