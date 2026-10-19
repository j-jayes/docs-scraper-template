JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseNode.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [BaseNode](BaseNode.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. BaseNode(String, String)
     2. BaseNode(String, String, boolean, boolean, NodeConfig, Schema, Schema, Schema)
  5. Method Details
     1. name()
     2. description()
     3. rerunOnResume()
     4. waitForOutput()
     5. config()
     6. inputSchema()
     7. outputSchema()
     8. stateSchema()

Hide sidebar  Show sidebar

# Class BaseNode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.workflow.BaseNode

All Implemented Interfaces:
    `[Node](Node.html "interface in com.google.adk.workflow")`

Direct Known Subclasses:
    `[BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents"), [JoinNode](JoinNode.html "class in com.google.adk.workflow"), [Workflow](Workflow.html "class in com.google.adk.workflow")`

* * *

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public abstract class BaseNode extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [Node](Node.html "interface in com.google.adk.workflow")

Base class for nodes in a workflow graph. It is meant for the framework's own nodes; to write a node, implement [`Node`](Node.html "interface in com.google.adk.workflow"). Subclasses implement [`Node.runNode(Context, Object)`](Node.html#runNode\(com.google.adk.agents.Context,java.lang.Object\)), and the framework turns each emission into an [`Event`](../events/Event.html "class in com.google.adk.events").

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`BaseNode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)`

Creates a node with every property other than its name and description at its default.

`protected `

`BaseNode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description, boolean rerunOnResume, boolean waitForOutput, [NodeConfig](NodeConfig.html "class in com.google.adk.workflow") config, @Nullable com.google.genai.types.Schema inputSchema, @Nullable com.google.genai.types.Schema outputSchema, @Nullable com.google.genai.types.Schema stateSchema)`

Creates a node; each parameter sets the [`Node`](Node.html "interface in com.google.adk.workflow") property of the same name.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[NodeConfig](NodeConfig.html "class in com.google.adk.workflow")`

`config()`

Returns the node's retry policy and execution timeout.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`description()`

Returns what the node does, for humans and for a model that may call it.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`inputSchema()`

Returns the schema the node's input must match.

`final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`name()`

Returns the name that identifies the node within its graph.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`outputSchema()`

Returns the schema that the node's output value must match.

`boolean`

`rerunOnResume()`

Returns `true` if a resumed node runs again from scratch, rather than completing with the resuming answer as its output.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema>`

`stateSchema()`

Returns the schema declaring the state keys the node uses.

`boolean`

`waitForOutput()`

Returns `true` if the node stays re-triggerable until it produces an output or a route, instead of completing when its run completes.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [Node](Node.html#method-summary "interface in com.google.adk.workflow")

`[requiresAllPredecessors](Node.html#requiresAllPredecessors\(\) "requiresAllPredecessors\(\)"), [runNode](Node.html#runNode\(com.google.adk.agents.Context,java.lang.Object\) "runNode\(Context, Object\)")`

Modifier and Type

Method

Description

`default boolean`

`[requiresAllPredecessors](Node.html#requiresAllPredecessors\(\))()`

Returns `true` if the node runs only once every predecessor has completed, receiving all their outputs keyed by node name, as a fan-in node does.

`io.reactivex.rxjava3.core.Flowable<?>`

`[runNode](Node.html#runNode\(com.google.adk.agents.Context,java.lang.Object\))([Context](../agents/Context.html "class in com.google.adk.agents") context, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") nodeInput)`

Runs the node on `nodeInput`, the output it receives from its predecessors.




  * ## Constructor Details

    * ### BaseNode

protected BaseNode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)

Creates a node with every property other than its name and description at its default.

    * ### BaseNode

protected BaseNode([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description, boolean rerunOnResume, boolean waitForOutput, [NodeConfig](NodeConfig.html "class in com.google.adk.workflow") config, @Nullable com.google.genai.types.Schema inputSchema, @Nullable com.google.genai.types.Schema outputSchema, @Nullable com.google.genai.types.Schema stateSchema)

Creates a node; each parameter sets the [`Node`](Node.html "interface in com.google.adk.workflow") property of the same name.

  * ## Method Details

    * ### name

public final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name()

Description copied from interface: `[Node](Node.html#name\(\))`

Returns the name that identifies the node within its graph.

Specified by:
    `[name](Node.html#name\(\))` in interface `[Node](Node.html "interface in com.google.adk.workflow")`

    * ### description

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description()

Description copied from interface: `[Node](Node.html#description\(\))`

Returns what the node does, for humans and for a model that may call it.

Specified by:
    `[description](Node.html#description\(\))` in interface `[Node](Node.html "interface in com.google.adk.workflow")`

    * ### rerunOnResume

public boolean rerunOnResume()

Description copied from interface: `[Node](Node.html#rerunOnResume\(\))`

Returns `true` if a resumed node runs again from scratch, rather than completing with the resuming answer as its output.

Specified by:
    `[rerunOnResume](Node.html#rerunOnResume\(\))` in interface `[Node](Node.html "interface in com.google.adk.workflow")`

    * ### waitForOutput

public boolean waitForOutput()

Description copied from interface: `[Node](Node.html#waitForOutput\(\))`

Returns `true` if the node stays re-triggerable until it produces an output or a route, instead of completing when its run completes.

Specified by:
    `[waitForOutput](Node.html#waitForOutput\(\))` in interface `[Node](Node.html "interface in com.google.adk.workflow")`

    * ### config

public [NodeConfig](NodeConfig.html "class in com.google.adk.workflow") config()

Description copied from interface: `[Node](Node.html#config\(\))`

Returns the node's retry policy and execution timeout.

Specified by:
    `[config](Node.html#config\(\))` in interface `[Node](Node.html "interface in com.google.adk.workflow")`

    * ### inputSchema

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema> inputSchema()

Description copied from interface: `[Node](Node.html#inputSchema\(\))`

Returns the schema the node's input must match.

Specified by:
    `[inputSchema](Node.html#inputSchema\(\))` in interface `[Node](Node.html "interface in com.google.adk.workflow")`

    * ### outputSchema

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema> outputSchema()

Description copied from interface: `[Node](Node.html#outputSchema\(\))`

Returns the schema that the node's output value must match. The content of a message-as-output event is not checked against this schema.

Specified by:
    `[outputSchema](Node.html#outputSchema\(\))` in interface `[Node](Node.html "interface in com.google.adk.workflow")`

    * ### stateSchema

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Schema> stateSchema()

Description copied from interface: `[Node](Node.html#stateSchema\(\))`

Returns the schema declaring the state keys the node uses. Child nodes inherit it unless they declare their own.

Specified by:
    `[stateSchema](Node.html#stateSchema\(\))` in interface `[Node](Node.html "interface in com.google.adk.workflow")`




* * *

Copyright (C) 1980\. All rights reserved.
