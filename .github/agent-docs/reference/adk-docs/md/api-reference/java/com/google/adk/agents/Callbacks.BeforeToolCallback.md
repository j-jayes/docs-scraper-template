JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Callbacks.BeforeToolCallback.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [Callbacks](Callbacks.html)
  3. [BeforeToolCallback](Callbacks.BeforeToolCallback.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. call(InvocationContext, BaseTool, Map, ToolContext)



# Interface Callbacks.BeforeToolCallback

Enclosing class:
    `[Callbacks](Callbacks.html "class in com.google.adk.agents")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "class or interface in java.lang") public static interface Callbacks.BeforeToolCallback

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`call([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

Async callback before tool runs.




  * ## Method Details

    * ### call

io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> call([InvocationContext](InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../tools/ToolContext.html "class in com.google.adk.tools") toolContext)

Async callback before tool runs.

Parameters:
    `invocationContext` \- Invocation context.
    `baseTool` \- Tool instance.
    `input` \- Tool input arguments.
    `toolContext` \- Tool context.
Returns:
    override result, or empty to continue.




* * *

Copyright (C) 2025\. All rights reserved.
