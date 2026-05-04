JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Callbacks.OnToolErrorCallback.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [Callbacks](Callbacks.html)
  3. [OnToolErrorCallback](Callbacks.OnToolErrorCallback.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. call(InvocationContext, BaseTool, Map, ToolContext, Exception)

Hide sidebar  Show sidebar

# Interface Callbacks.OnToolErrorCallback

Enclosing class:
    `[Callbacks](Callbacks.html "class in com.google.adk.agents")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "annotation interface in java.lang") public static interface Callbacks.OnToolErrorCallback

Async callback interface for handling errors that occur during a tool invocation.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`call([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> input, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

Async callback when tool call fails.




  * ## Method Details

    * ### call

io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> call([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> input, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)

Async callback when tool call fails.

Parameters:
    `invocationContext` \- Invocation context.
    `baseTool` \- Tool instance.
    `input` \- Tool input arguments.
    `toolContext` \- Tool context.
    `error` \- The exception that occurred.
Returns:
    override result, or empty to continue with error.




* * *

Copyright (C) 1980\. All rights reserved.
