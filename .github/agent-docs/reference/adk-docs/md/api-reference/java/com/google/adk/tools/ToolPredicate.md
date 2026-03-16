JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ToolPredicate.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [ToolPredicate](ToolPredicate.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. test(BaseTool, Optional)
     2. test(BaseTool, ReadonlyContext)

Hide sidebar  Show sidebar

# Interface ToolPredicate

All Known Implementing Classes:
    `[NamedToolPredicate](NamedToolPredicate.html "class in com.google.adk.tools")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "class or interface in java.lang") public interface ToolPredicate

Functional interface to decide whether a tool should be exposed to the LLM based on the current context.

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsDefault MethodsDeprecated Methods

Modifier and Type

Method

Description

`default boolean`

`test([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, [ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Decides if the given tool is selected.

`boolean`

`test([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)`

Deprecated.

Use `test(BaseTool, ReadonlyContext)` instead.




  * ## Method Details

    * ### test

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") boolean test([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)

Deprecated.

Use `test(BaseTool, ReadonlyContext)` instead.

Decides if the given tool is selected.

Parameters:
    `tool` \- The tool to check.
    `readonlyContext` \- The current context.
Returns:
    true if the tool should be selected, false otherwise.

    * ### test

default boolean test([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, @Nullable [ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)

Decides if the given tool is selected.

Parameters:
    `tool` \- The tool to check.
    `readonlyContext` \- The current context.
Returns:
    true if the tool should be selected, false otherwise.




* * *

Copyright (C) 1980\. All rights reserved.
