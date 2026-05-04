JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpToolset.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [McpToolset](McpToolset.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Constructor Summary
  5. Method Summary
  6. Field Details
     1. CONFIG_TYPE
  7. Constructor Details
     1. McpToolset(SseServerParameters, ObjectMapper, ToolPredicate)
     2. McpToolset(SseServerParameters, ObjectMapper, List)
     3. McpToolset(SseServerParameters, ObjectMapper)
     4. McpToolset(ServerParameters, ObjectMapper, ToolPredicate)
     5. McpToolset(ServerParameters, ObjectMapper, List)
     6. McpToolset(ServerParameters, ObjectMapper)
     7. McpToolset(SseServerParameters)
     8. McpToolset(ServerParameters)
     9. McpToolset(McpSessionManager, ObjectMapper, ToolPredicate)
     10. McpToolset(McpSessionManager, ObjectMapper, List)
     11. McpToolset(McpSessionManager, ObjectMapper)
     12. McpToolset(StreamableHttpServerParameters, ObjectMapper, ToolPredicate)
     13. McpToolset(StreamableHttpServerParameters, ObjectMapper, List)
     14. McpToolset(StreamableHttpServerParameters, ObjectMapper)
     15. McpToolset(StreamableHttpServerParameters)
  8. Method Details
     1. getTools(ReadonlyContext)
     2. close()
     3. fromConfig(BaseTool.ToolConfig, String)

Hide sidebar  Show sidebar

# Class McpToolset

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.mcp.McpToolset

All Implemented Interfaces:
    `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools"), [AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`

* * *

public class McpToolset extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")

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

`[McpToolset.McpToolsetConfig](McpToolset.McpToolsetConfig.html "class in com.google.adk.tools.mcp")`

Configuration class for MCPToolset.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`protected static final [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [McpToolset.McpToolsetConfig](McpToolset.McpToolsetConfig.html "class in com.google.adk.tools.mcp")>`

`CONFIG_TYPE`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`McpToolset([McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Initializes the McpToolset with an McpSessionManager and no tool filter.

`McpToolset([McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)`

Initializes the McpToolset with an McpSessionManager.

`McpToolset([McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)`

Initializes the McpToolset with an McpSessionManager.

`McpToolset([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams)`

Initializes the McpToolset with SSE server parameters, using the ObjectMapper used across the ADK and no tool filter.

`McpToolset([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Initializes the McpToolset with SSE server parameters and no tool filter.

`McpToolset([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)`

Initializes the McpToolset with SSE server parameters.

`McpToolset([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)`

Initializes the McpToolset with SSE server parameters.

`McpToolset([StreamableHttpServerParameters](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp") connectionParams)`

Initializes the McpToolset with Streamable HTTP server parameters, using the ObjectMapper used across the ADK and no tool filter.

`McpToolset([StreamableHttpServerParameters](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Initializes the McpToolset with Streamable HTTP server parameters and no tool filter.

`McpToolset([StreamableHttpServerParameters](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)`

Initializes the McpToolset with Streamable HTTP server parameters.

`McpToolset([StreamableHttpServerParameters](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)`

Initializes the McpToolset with Streamable HTTP server parameters.

`McpToolset(io.modelcontextprotocol.client.transport.ServerParameters connectionParams)`

Initializes the McpToolset with local server parameters, using the ObjectMapper used across the ADK and no tool filter.

`McpToolset(io.modelcontextprotocol.client.transport.ServerParameters connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Initializes the McpToolset with local server parameters and no tool filter.

`McpToolset(io.modelcontextprotocol.client.transport.ServerParameters connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)`

Initializes the McpToolset with local server parameters.

`McpToolset(io.modelcontextprotocol.client.transport.ServerParameters connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)`

Initializes the McpToolset with local server parameters.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`close()`

Performs cleanup and releases resources held by the toolset.

`static [McpToolset](McpToolset.html "class in com.google.adk.tools.mcp")`

`fromConfig([BaseTool.ToolConfig](../BaseTool.ToolConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a McpToolset instance from a config.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

`getTools([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Return all tools in the toolset based on the provided context.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [BaseToolset](../BaseToolset.html#method-summary "interface in com.google.adk.tools")

`[isToolSelected](../BaseToolset.html#isToolSelected\(com.google.adk.tools.BaseTool,java.lang.Object,com.google.adk.agents.ReadonlyContext\) "isToolSelected\(BaseTool, Object, ReadonlyContext\)")`

Modifier and Type

Method

Description

`default boolean`

`[isToolSelected](../BaseToolset.html#isToolSelected\(com.google.adk.tools.BaseTool,java.lang.Object,com.google.adk.agents.ReadonlyContext\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, @Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") toolFilter, @Nullable [ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Checks if a tool should be selected based on a filter.




  * ## Field Details

    * ### CONFIG_TYPE

protected static final [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [McpToolset.McpToolsetConfig](McpToolset.McpToolsetConfig.html "class in com.google.adk.tools.mcp")> CONFIG_TYPE

  * ## Constructor Details

    * ### McpToolset

public McpToolset([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)

Initializes the McpToolset with SSE server parameters.

Parameters:
    `connectionParams` \- The SSE connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolPredicate` \- A [`ToolPredicate`](../ToolPredicate.html "interface in com.google.adk.tools")

    * ### McpToolset

public McpToolset([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)

Initializes the McpToolset with SSE server parameters.

Parameters:
    `connectionParams` \- The SSE connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolNames` \- A list of tool names

    * ### McpToolset

public McpToolset([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Initializes the McpToolset with SSE server parameters and no tool filter.

Parameters:
    `connectionParams` \- The SSE connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.

    * ### McpToolset

public McpToolset(io.modelcontextprotocol.client.transport.ServerParameters connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)

Initializes the McpToolset with local server parameters.

Parameters:
    `connectionParams` \- The local server connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolPredicate` \- A [`ToolPredicate`](../ToolPredicate.html "interface in com.google.adk.tools")

    * ### McpToolset

public McpToolset(io.modelcontextprotocol.client.transport.ServerParameters connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)

Initializes the McpToolset with local server parameters.

Parameters:
    `connectionParams` \- The local server connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolNames` \- A list of tool names

    * ### McpToolset

public McpToolset(io.modelcontextprotocol.client.transport.ServerParameters connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Initializes the McpToolset with local server parameters and no tool filter.

Parameters:
    `connectionParams` \- The local server connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.

    * ### McpToolset

public McpToolset([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams)

Initializes the McpToolset with SSE server parameters, using the ObjectMapper used across the ADK and no tool filter.

Parameters:
    `connectionParams` \- The SSE connection parameters to the MCP server.

    * ### McpToolset

public McpToolset(io.modelcontextprotocol.client.transport.ServerParameters connectionParams)

Initializes the McpToolset with local server parameters, using the ObjectMapper used across the ADK and no tool filter.

Parameters:
    `connectionParams` \- The local server connection parameters to the MCP server.

    * ### McpToolset

public McpToolset([McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)

Initializes the McpToolset with an McpSessionManager.

Parameters:
    `mcpSessionManager` \- A McpSessionManager instance for testing.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolPredicate` \- A [`ToolPredicate`](../ToolPredicate.html "interface in com.google.adk.tools")

    * ### McpToolset

public McpToolset([McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)

Initializes the McpToolset with an McpSessionManager.

Parameters:
    `mcpSessionManager` \- A McpSessionManager instance for testing.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolNames` \- A list of tool names

    * ### McpToolset

public McpToolset([McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Initializes the McpToolset with an McpSessionManager and no tool filter.

Parameters:
    `mcpSessionManager` \- A McpSessionManager instance for testing.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.

    * ### McpToolset

public McpToolset([StreamableHttpServerParameters](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)

Initializes the McpToolset with Streamable HTTP server parameters.

Parameters:
    `connectionParams` \- The Streamable HTTP connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolPredicate` \- A [`ToolPredicate`](../ToolPredicate.html "interface in com.google.adk.tools")

    * ### McpToolset

public McpToolset([StreamableHttpServerParameters](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)

Initializes the McpToolset with Streamable HTTP server parameters.

Parameters:
    `connectionParams` \- The Streamable HTTP connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.
    `toolNames` \- A list of tool names

    * ### McpToolset

public McpToolset([StreamableHttpServerParameters](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Initializes the McpToolset with Streamable HTTP server parameters and no tool filter.

Parameters:
    `connectionParams` \- The Streamable HTTP connection parameters to the MCP server.
    `objectMapper` \- An ObjectMapper instance for parsing schemas.

    * ### McpToolset

public McpToolset([StreamableHttpServerParameters](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp") connectionParams)

Initializes the McpToolset with Streamable HTTP server parameters, using the ObjectMapper used across the ADK and no tool filter.

Parameters:
    `connectionParams` \- The Streamable HTTP connection parameters to the MCP server.

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
    `[close](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\))` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`
Specified by:
    `[close](../BaseToolset.html#close\(\))` in interface `[BaseToolset](../BaseToolset.html "interface in com.google.adk.tools")`

    * ### fromConfig

public static [McpToolset](McpToolset.html "class in com.google.adk.tools.mcp") fromConfig([BaseTool.ToolConfig](../BaseTool.ToolConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath) throws [ConfigAgentUtils.ConfigurationException](../../agents/ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")

Creates a McpToolset instance from a config.

Parameters:
    `config` \- The config for the McpToolset.
    `configAbsPath` \- The absolute path to the config file that contains the McpToolset config.
Returns:
    The McpToolset instance.
Throws:
    `[ConfigAgentUtils.ConfigurationException](../../agents/ConfigAgentUtils.ConfigurationException.html "class in com.google.adk.agents")` \- if the McpToolset cannot be created from the config.




* * *

Copyright (C) 1980\. All rights reserved.
