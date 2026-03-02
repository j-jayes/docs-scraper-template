JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpAsyncToolset.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [McpAsyncToolset](McpAsyncToolset.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. McpAsyncToolset(SseServerParameters, ObjectMapper, Optional)
     2. McpAsyncToolset(ServerParameters, ObjectMapper, Optional)
     3. McpAsyncToolset(McpSessionManager, ObjectMapper, Optional)
  6. Method Details
     1. getTools(ReadonlyContext)
     2. close()

Hide sidebar  Show sidebar

# Class McpAsyncToolset

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.mcp.McpAsyncToolset

All Implemented Interfaces:
    `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools"), [AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`

* * *

public class McpAsyncToolset extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

Connects to a MCP Server, and retrieves MCP Tools into ADK Tools. 

Attributes: 

  * `connectionParams`: The connection parameters to the MCP server. Can be either ` ServerParameters` or `SseServerParameters`. 
  * `session`: The MCP session being initialized with the connection. 


  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")`

Builder for McpAsyncToolset

  * ## Constructor Summary

Constructors

Constructor

Description

`McpAsyncToolset([McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter)`

Initializes the McpAsyncToolset with a provided McpSessionManager.

`McpAsyncToolset([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter)`

Initializes the McpAsyncToolset with SSE server parameters.

`McpAsyncToolset(io.modelcontextprotocol.client.transport.ServerParameters connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter)`

Initializes the McpAsyncToolset with local server parameters.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`close()`

Performs cleanup and releases resources held by the toolset.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

`getTools([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Return all tools in the toolset based on the provided context.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`

### Methods inherited from interface [BaseToolset](../BaseToolset.html#method-summary "interface in com.google.adk.tools")

`[isToolSelected](../BaseToolset.html#isToolSelected\(com.google.adk.tools.BaseTool,java.lang.Object,com.google.adk.agents.ReadonlyContext\) "isToolSelected\(BaseTool, Object, ReadonlyContext\)"), [isToolSelected](../BaseToolset.html#isToolSelected\(com.google.adk.tools.BaseTool,java.util.Optional,java.util.Optional\) "isToolSelected\(BaseTool, Optional, Optional\)")`




  * ## Constructor Details

    * ### McpAsyncToolset

public McpAsyncToolset([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter)

Initializes the McpAsyncToolset with SSE server parameters.

Parameters:
    `connectionParams` \- The SSE connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolFilter` \- An Optional containing either a ToolPredicate or a List of tool names.

    * ### McpAsyncToolset

public McpAsyncToolset(io.modelcontextprotocol.client.transport.ServerParameters connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter)

Initializes the McpAsyncToolset with local server parameters.

Parameters:
    `connectionParams` \- The local server connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolFilter` \- An Optional containing either a ToolPredicate or a List of tool names.

    * ### McpAsyncToolset

public McpAsyncToolset([McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter)

Initializes the McpAsyncToolset with a provided McpSessionManager.

Parameters:
    `mcpSessionManager` \- The session manager for MCP connections.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolFilter` \- An Optional containing either a ToolPredicate or a List of tool names.

  * ## Method Details

    * ### getTools

public io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")> getTools([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)

Description copied from interface: `[BaseToolset](../BaseToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))`

Return all tools in the toolset based on the provided context.

Specified by:
    `[getTools](../BaseToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))` in interface `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")`
Parameters:
    `readonlyContext` \- Context used to filter tools available to the agent.
Returns:
    A Single emitting a list of tools available under the specified context.

    * ### close

public void close()

Description copied from interface: `[BaseToolset](../BaseToolset.html#close\(\))`

Performs cleanup and releases resources held by the toolset. 

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

Specified by:
    `[close](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\) "class or interface in java.lang")` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "class or interface in java.lang")`
Specified by:
    `[close](../BaseToolset.html#close\(\))` in interface `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")`




* * *

Copyright (C) 1980\. All rights reserved.
