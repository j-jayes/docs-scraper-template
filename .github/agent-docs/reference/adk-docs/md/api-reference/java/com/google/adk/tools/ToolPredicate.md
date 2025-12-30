JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ToolPredicate.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [ToolPredicate](ToolPredicate.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. test(BaseTool, Optional)



# Interface ToolPredicate

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "class or interface in java.lang") public interface ToolPredicate

Functional interface to decide whether a tool should be exposed to the LLM based on the current context.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`boolean`

`test([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)`

Decides if the given tool is selected.




  * ## Method Details

    * ### test

boolean test([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)

Decides if the given tool is selected.

Parameters:
    `tool` \- The tool to check.
    `readonlyContext` \- The current context.
Returns:
    true if the tool should be selected, false otherwise.




* * *

Copyright (C) 2025\. All rights reserved.
