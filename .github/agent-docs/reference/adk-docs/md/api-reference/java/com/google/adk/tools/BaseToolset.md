JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseToolset.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [BaseToolset](BaseToolset.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. getTools(ReadonlyContext)
     2. close()
     3. isToolSelected(BaseTool, Optional, Optional)



# Interface BaseToolset

All Superinterfaces:
    `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`

All Known Implementing Classes:
    `[ApplicationIntegrationToolset](applicationintegrationtoolset/ApplicationIntegrationToolset.html "class in com.google.adk.tools.applicationintegrationtoolset")`, `[McpToolset](mcp/McpToolset.html "class in com.google.adk.tools.mcp")`

* * *

public interface BaseToolset extends [AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")

Base interface for toolsets.

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsDefault Methods

Modifier and Type

Method

Description

`void`

`close()`

Performs cleanup and releases resources held by the toolset.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](BaseTool.html "class in com.google.adk.tools")>`

`getTools([ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Return all tools in the toolset based on the provided context.

`default boolean`

`isToolSelected([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)`

Helper method to be used by implementers that returns true if the given tool is in the provided list of tools of if testing against the given ToolPredicate returns true (otherwise false).




  * ## Method Details

    * ### getTools

io.reactivex.rxjava3.core.Flowable<[BaseTool](BaseTool.html "class in com.google.adk.tools")> getTools([ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)

Return all tools in the toolset based on the provided context.

Parameters:
    `readonlyContext` \- Context used to filter tools available to the agent.
Returns:
    A Single emitting a list of tools available under the specified context.

    * ### close

void close() throws [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")

Performs cleanup and releases resources held by the toolset. 

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

Specified by:
    `[close](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\) "class or interface in java.lang")` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`
Throws:
    `[Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang")`

    * ### isToolSelected

default boolean isToolSelected([BaseTool](BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)

Helper method to be used by implementers that returns true if the given tool is in the provided list of tools of if testing against the given ToolPredicate returns true (otherwise false).

Parameters:
    `tool` \- The tool to check.
    `toolFilter` \- An Optional containing either a ToolPredicate or a List of tool names.
    `readonlyContext` \- The current context.
Returns:
    true if the tool is selected.




* * *

Copyright (C) 2025\. All rights reserved.
