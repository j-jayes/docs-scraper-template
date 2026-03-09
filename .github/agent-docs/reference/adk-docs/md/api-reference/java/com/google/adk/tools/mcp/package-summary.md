JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Package
  * [Use](package-use.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.mcp](package-summary.html)



Contents

  1. Description
  2. Related Packages
  3. Classes and Interfaces

Hide sidebar  Show sidebar

# Package com.google.adk.tools.mcp

* * *

package com.google.adk.tools.mcp

  * Related Packages

Package

Description

[com.google.adk.tools](../package-summary.html)

 

[com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html)

 

[com.google.adk.tools.retrieval](../retrieval/package-summary.html)

 

  * All Classes and InterfacesInterfacesClassesException Classes

Class

Description

[AbstractMcpTool](AbstractMcpTool.html "class in com.google.adk.tools.mcp")<T>

Base class for MCP tools.

[ConversionUtils](ConversionUtils.html "class in com.google.adk.tools.mcp")

Utility class for converting between different representations of MCP tools.

[DefaultMcpTransportBuilder](DefaultMcpTransportBuilder.html "class in com.google.adk.tools.mcp")

The default builder for creating MCP client transports.

[McpAsyncTool](McpAsyncTool.html "class in com.google.adk.tools.mcp")

Initializes a MCP tool.

[McpAsyncToolset](McpAsyncToolset.html "class in com.google.adk.tools.mcp")

Connects to a MCP Server, and retrieves MCP Tools into ADK Tools.

[McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")

Builder for McpAsyncToolset

[McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp")

Manages MCP client sessions.

[McpTool](McpTool.html "class in com.google.adk.tools.mcp")

Initializes a MCP tool.

[McpToolException](McpToolException.html "class in com.google.adk.tools.mcp")

Base exception for all errors originating from `AbstractMcpTool` and its subclasses.

[McpToolException.McpToolDeclarationException](McpToolException.McpToolDeclarationException.html "class in com.google.adk.tools.mcp")

Exception thrown when there's an error during MCP tool declaration generated.

[McpToolset](McpToolset.html "class in com.google.adk.tools.mcp")

Connects to a MCP Server, and retrieves MCP Tools into ADK Tools.

[McpToolset.McpToolsetConfig](McpToolset.McpToolsetConfig.html "class in com.google.adk.tools.mcp")

Configuration class for MCPToolset.

[McpToolsetException](McpToolsetException.html "class in com.google.adk.tools.mcp")

Base exception for all errors originating from `McpToolset`.

[McpToolsetException.McpInitializationException](McpToolsetException.McpInitializationException.html "class in com.google.adk.tools.mcp")

Exception thrown when there's an error during MCP session initialization.

[McpToolsetException.McpToolLoadingException](McpToolsetException.McpToolLoadingException.html "class in com.google.adk.tools.mcp")

Exception thrown when there's an error during loading tools from the MCP server.

[McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp")

Interface for building McpClientTransport instances.

[SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp")

Parameters for establishing a MCP Server-Sent Events (SSE) connection.

[SseServerParameters.Builder](SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")

Builder for [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp").

[StdioConnectionParameters](StdioConnectionParameters.html "class in com.google.adk.tools.mcp")

 

[StdioConnectionParameters.Builder](StdioConnectionParameters.Builder.html "class in com.google.adk.tools.mcp")

 

[StdioServerParameters](StdioServerParameters.html "class in com.google.adk.tools.mcp")

Parameters for establishing a MCP stdio connection.

[StdioServerParameters.Builder](StdioServerParameters.Builder.html "class in com.google.adk.tools.mcp")

Builder for [`StdioServerParameters`](StdioServerParameters.html "class in com.google.adk.tools.mcp").

[StreamableHttpServerParameters](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp")

Server parameters for Streamable HTTP client transport.

[StreamableHttpServerParameters.Builder](StreamableHttpServerParameters.Builder.html "class in com.google.adk.tools.mcp")

Builder for [`StreamableHttpServerParameters`](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp").




* * *

Copyright (C) 1980\. All rights reserved.
