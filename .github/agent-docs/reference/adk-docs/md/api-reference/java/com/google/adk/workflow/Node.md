JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Node.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [Node](Node.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. name()
     2. description()
     3. rerunOnResume()
     4. waitForOutput()
     5. config()
     6. inputSchema()
     7. outputSchema()
     8. stateSchema()
     9. requiresAllPredecessors()
     10. runNode(Context, Object)

Hide sidebar  Show sidebar

# Interface Node

All Known Implementing Classes:
    `[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents"), [BaseNode](BaseNode.html "class in com.google.adk.workflow"), [JoinNode](JoinNode.html "class in com.google.adk.workflow"), [LlmAgent](../agents/LlmAgent.html "class in com.google.adk.agents"), [LoopAgent](../agents/LoopAgent.html "class in com.google.adk.agents"), [ParallelAgent](../agents/ParallelAgent.html "class in com.google.adk.agents"), [PlannerAgent](../agents/PlannerAgent.html "class in com.google.adk.agents"), [RemoteA2AAgent](../a2a/agent/RemoteA2AAgent.html "class in com.google.adk.a2a.agent"), [SequentialAgent](../agents/SequentialAgent.html "class in com.google.adk.agents"), [Start](Start.html "class in com.google.adk.workflow"), [Workflow](Workflow.html "class in com.google.adk.workflow")`

* * *

public interface Node

A unit of work in a workflow graph. Node names must be unique within a graph. Every member except `name()` and `description()` is experimental, so implementing this interface is too.

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsDefault Methods

Modifier and Type

Method

Description

`default [NodeConfig](NodeConfig.html "class in com.google.adk.workflow")`

`config()`

Returns the node's retry policy and execution timeout.

`default [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`description()`

Returns what the node does, for humans and for a model that may call it.

`default [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`inputSchema()`

Returns the schema the node's input must match.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`name()`

Returns the name that identifies the node within its graph.

`default [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`outputSchema()`

Returns the schema that the node's output value must match.

`default boolean`

`requiresAllPredecessors()`

Returns `true` if the node runs only once every predecessor has completed, receiving all their outputs keyed by node name, as a fan-in node does.

`default boolean`

`rerunOnResume()`

Returns `true` if a resumed node runs again from scratch, rather than completing with the resuming answer as its output.

`io.reactivex.rxjava3.core.Flowable<?>`

`runNode([Context](../agents/Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

Runs the node on `nodeInput`, the output it receives from its predecessors.

`default [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`stateSchema()`

Returns the schema declaring the state keys the node uses.

`default boolean`

`waitForOutput()`

Returns `true` if the node stays re-triggerable until it produces an output or a route, instead of completing when its run completes.




  * ## Method Details

    * ### name

[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name()

Returns the name that identifies the node within its graph.

    * ### description

default [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description()

Returns what the node does, for humans and for a model that may call it.

    * ### rerunOnResume

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") default boolean rerunOnResume()

Returns `true` if a resumed node runs again from scratch, rather than completing with the resuming answer as its output.

    * ### waitForOutput

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") default boolean waitForOutput()

Returns `true` if the node stays re-triggerable until it produces an output or a route, instead of completing when its run completes.

    * ### config

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") default [NodeConfig](NodeConfig.html "class in com.google.adk.workflow") config()

Returns the node's retry policy and execution timeout.

    * ### inputSchema

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") default [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema> inputSchema()

Returns the schema the node's input must match.

    * ### outputSchema

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") default [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema> outputSchema()

Returns the schema that the node's output value must match. The content of a message-as-output event is not checked against this schema.

    * ### stateSchema

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") default [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema> stateSchema()

Returns the schema declaring the state keys the node uses. Child nodes inherit it unless they declare their own.

    * ### requiresAllPredecessors

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") default boolean requiresAllPredecessors()

Returns `true` if the node runs only once every predecessor has completed, receiving all their outputs keyed by node name, as a fan-in node does.

    * ### runNode

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") io.reactivex.rxjava3.core.Flowable<?> runNode([Context](../agents/Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)

Runs the node on `nodeInput`, the output it receives from its predecessors. 

An emitted [`Event`](../events/Event.html "class in com.google.adk.events") passes through, and any other emitted value becomes the node's output (at most one per run); emit nothing for no output, since RxJava forbids null. The wildcard lets an implementation return a `Flowable` of its own type.




* * *

Copyright (C) 1980\. All rights reserved.
