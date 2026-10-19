JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Workflow.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [Workflow](Workflow.html)
  3. [Builder](Workflow.Builder.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. name(String)
     2. edges(List)
     3. edges(Edge...)
     4. description(String)
     5. maxConcurrency(int)
     6. rerunOnResume(boolean)
     7. waitForOutput(boolean)
     8. config(NodeConfig)
     9. inputSchema(Schema)
     10. outputSchema(Schema)
     11. stateSchema(Schema)
     12. build()

Hide sidebar  Show sidebar

# Class Workflow.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.workflow.Workflow.Builder

Enclosing class:
    `[Workflow](Workflow.html "class in com.google.adk.workflow")`

* * *

public static final class Workflow.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`Workflow`](Workflow.html "class in com.google.adk.workflow"). Only the name is required. Unlike other nodes, a workflow reruns from scratch when resumed unless `rerunOnResume` turns that off.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Workflow](Workflow.html "class in com.google.adk.workflow")`

`build()`

 

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`config([NodeConfig](NodeConfig.html "class in com.google.adk.workflow") config)`

 

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)`

 

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`edges([Edge](Edge.html "class in com.google.adk.workflow")... edges)`

 

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`edges([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Edge](Edge.html "class in com.google.adk.workflow")> edges)`

 

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`inputSchema(@Nullable com.google.genai.types.Schema inputSchema)`

 

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`maxConcurrency(int maxConcurrency)`

Sets the maximum number of nodes to run at once, which must be at least 1.

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`outputSchema(@Nullable com.google.genai.types.Schema outputSchema)`

 

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`rerunOnResume(boolean rerunOnResume)`

 

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`stateSchema(@Nullable com.google.genai.types.Schema stateSchema)`

 

`[Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow")`

`waitForOutput(boolean waitForOutput)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### name

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### edges

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") edges([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Edge](Edge.html "class in com.google.adk.workflow")> edges)

    * ### edges

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") edges([Edge](Edge.html "class in com.google.adk.workflow")... edges)

    * ### description

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)

    * ### maxConcurrency

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") maxConcurrency(int maxConcurrency)

Sets the maximum number of nodes to run at once, which must be at least 1. A workflow without one has no limit.

    * ### rerunOnResume

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") rerunOnResume(boolean rerunOnResume)

    * ### waitForOutput

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") waitForOutput(boolean waitForOutput)

    * ### config

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") config([NodeConfig](NodeConfig.html "class in com.google.adk.workflow") config)

    * ### inputSchema

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") inputSchema(@Nullable com.google.genai.types.Schema inputSchema)

    * ### outputSchema

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") outputSchema(@Nullable com.google.genai.types.Schema outputSchema)

    * ### stateSchema

@CanIgnoreReturnValue public [Workflow.Builder](Workflow.Builder.html "class in com.google.adk.workflow") stateSchema(@Nullable com.google.genai.types.Schema stateSchema)

    * ### build

public [Workflow](Workflow.html "class in com.google.adk.workflow") build()




* * *

Copyright (C) 1980\. All rights reserved.
