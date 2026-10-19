JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/JoinNode.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [JoinNode](JoinNode.html)
  3. [Builder](JoinNode.Builder.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. name(String)
     2. description(String)
     3. inputSchema(Schema)
     4. outputSchema(Schema)
     5. build()

Hide sidebar  Show sidebar

# Class JoinNode.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.workflow.JoinNode.Builder

Enclosing class:
    `[JoinNode](JoinNode.html "class in com.google.adk.workflow")`

* * *

public static final class JoinNode.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`JoinNode`](JoinNode.html "class in com.google.adk.workflow"). Only the name is required.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[JoinNode](JoinNode.html "class in com.google.adk.workflow")`

`build()`

 

`[JoinNode.Builder](JoinNode.Builder.html "class in com.google.adk.workflow")`

`description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)`

 

`[JoinNode.Builder](JoinNode.Builder.html "class in com.google.adk.workflow")`

`inputSchema(@Nullable com.google.genai.types.Schema inputSchema)`

Sets the schema that each predecessor's output must match on its own, not the joined map.

`[JoinNode.Builder](JoinNode.Builder.html "class in com.google.adk.workflow")`

`name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

 

`[JoinNode.Builder](JoinNode.Builder.html "class in com.google.adk.workflow")`

`outputSchema(@Nullable com.google.genai.types.Schema outputSchema)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### name

@CanIgnoreReturnValue public [JoinNode.Builder](JoinNode.Builder.html "class in com.google.adk.workflow") name([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

    * ### description

@CanIgnoreReturnValue public [JoinNode.Builder](JoinNode.Builder.html "class in com.google.adk.workflow") description([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") description)

    * ### inputSchema

@CanIgnoreReturnValue public [JoinNode.Builder](JoinNode.Builder.html "class in com.google.adk.workflow") inputSchema(@Nullable com.google.genai.types.Schema inputSchema)

Sets the schema that each predecessor's output must match on its own, not the joined map.

    * ### outputSchema

@CanIgnoreReturnValue public [JoinNode.Builder](JoinNode.Builder.html "class in com.google.adk.workflow") outputSchema(@Nullable com.google.genai.types.Schema outputSchema)

    * ### build

public [JoinNode](JoinNode.html "class in com.google.adk.workflow") build()




* * *

Copyright (C) 1980\. All rights reserved.
