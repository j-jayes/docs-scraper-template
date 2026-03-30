JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../McpSessionManager.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.tools.mcp](../package-summary.html)
  2. [McpSessionManager](../McpSessionManager.html)



# Uses of Class  
com.google.adk.tools.mcp.McpSessionManager

Packages that use [McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp")

Package

Description

com.google.adk.tools.mcp

 

  * ## Uses of [McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp") in [com.google.adk.tools.mcp](../package-summary.html)

Fields in [com.google.adk.tools.mcp](../package-summary.html) declared as [McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp")

Modifier and Type

Field

Description

`protected final [McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp")`

AbstractMcpTool.`[mcpSessionManager](../AbstractMcpTool.html#mcpSessionManager)`

 

Constructors in [com.google.adk.tools.mcp](../package-summary.html) with parameters of type [McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp")

Modifier

Constructor

Description

`protected `

`[AbstractMcpTool](../AbstractMcpTool.html#%3Cinit%3E\(io.modelcontextprotocol.spec.McpSchema.Tool,T,com.google.adk.tools.mcp.McpSessionManager,com.fasterxml.jackson.databind.ObjectMapper\))(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, [T](../AbstractMcpTool.html#type-param-T "type parameter in AbstractMcpTool") mcpSession, [McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

 

` `

`[McpAsyncTool](../McpAsyncTool.html#%3Cinit%3E\(io.modelcontextprotocol.spec.McpSchema.Tool,io.modelcontextprotocol.client.McpAsyncClient,com.google.adk.tools.mcp.McpSessionManager\))(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpAsyncClient mcpSession, [McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager)`

Creates a new McpAsyncTool with the default ObjectMapper.

` `

`[McpAsyncTool](../McpAsyncTool.html#%3Cinit%3E\(io.modelcontextprotocol.spec.McpSchema.Tool,io.modelcontextprotocol.client.McpAsyncClient,com.google.adk.tools.mcp.McpSessionManager,com.fasterxml.jackson.databind.ObjectMapper\))(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpAsyncClient mcpSession, [McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Creates a new McpAsyncTool

` `

`[McpTool](../McpTool.html#%3Cinit%3E\(io.modelcontextprotocol.spec.McpSchema.Tool,io.modelcontextprotocol.client.McpSyncClient,com.google.adk.tools.mcp.McpSessionManager\))(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpSyncClient mcpSession, [McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager)`

Creates a new McpTool with the default ObjectMapper.

` `

`[McpTool](../McpTool.html#%3Cinit%3E\(io.modelcontextprotocol.spec.McpSchema.Tool,io.modelcontextprotocol.client.McpSyncClient,com.google.adk.tools.mcp.McpSessionManager,com.fasterxml.jackson.databind.ObjectMapper\))(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpSyncClient mcpSession, [McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Creates a new McpTool with the default ObjectMapper.

` `

`[McpToolset](../McpToolset.html#%3Cinit%3E\(com.google.adk.tools.mcp.McpSessionManager,com.fasterxml.jackson.databind.ObjectMapper\))([McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Initializes the McpToolset with an McpSessionManager and no tool filter.

` `

`[McpToolset](../McpToolset.html#%3Cinit%3E\(com.google.adk.tools.mcp.McpSessionManager,com.fasterxml.jackson.databind.ObjectMapper,com.google.adk.tools.ToolPredicate\))([McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [ToolPredicate](../../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)`

Initializes the McpToolset with an McpSessionManager.

` `

`[McpToolset](../McpToolset.html#%3Cinit%3E\(com.google.adk.tools.mcp.McpSessionManager,com.fasterxml.jackson.databind.ObjectMapper,java.util.List\))([McpSessionManager](../McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> toolNames)`

Initializes the McpToolset with an McpSessionManager.




* * *

Copyright (C) 1980\. All rights reserved.
