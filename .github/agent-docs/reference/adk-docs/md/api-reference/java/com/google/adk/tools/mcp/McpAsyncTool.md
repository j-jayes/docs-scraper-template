JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpAsyncTool.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [McpAsyncTool](McpAsyncTool.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. McpAsyncTool(McpSchema.Tool, McpAsyncClient, McpSessionManager)
     2. McpAsyncTool(McpSchema.Tool, McpAsyncClient, McpSessionManager, ObjectMapper)
  5. Method Details
     1. getMcpSession()
     2. toGeminiSchema(McpSchema.JsonSchema)
     3. declaration()
     4. runAsync(Map, ToolContext)



# Class McpAsyncTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](../BaseTool.html "class in com.google.adk.tools")

com.google.adk.tools.mcp.McpAsyncTool

* * *

public final class McpAsyncTool extends [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Initializes a MCP tool. 

This wraps a MCP Tool interface and an active MCP Session. It invokes the MCP Tool through executing the tool from remote MCP Session.

  * ## Constructor Summary

Constructors

Constructor

Description

`McpAsyncTool(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpAsyncClient mcpSession, [McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager)`

Creates a new McpAsyncTool with the default ObjectMapper.

`McpAsyncTool(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpAsyncClient mcpSession, [McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Creates a new McpAsyncTool

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration>`

`declaration()`

Gets the `FunctionDeclaration` representation of this tool.

`io.modelcontextprotocol.client.McpAsyncClient`

`getMcpSession()`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

`com.google.genai.types.Schema`

`toGeminiSchema(io.modelcontextprotocol.spec.McpSchema.JsonSchema openApiSchema)`

 

### Methods inherited from class com.google.adk.tools.[BaseTool](../BaseTool.html "class in com.google.adk.tools")

`[description](../BaseTool.html#description\(\)), [longRunning](../BaseTool.html#longRunning\(\)), [name](../BaseTool.html#name\(\)), [processLlmRequest](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### McpAsyncTool

public McpAsyncTool(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpAsyncClient mcpSession, [McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager)

Creates a new McpAsyncTool with the default ObjectMapper.

Parameters:
    `mcpTool` \- The MCP tool to wrap.
    `mcpSession` \- The MCP session to use to call the tool.
    `mcpSessionManager` \- The MCP session manager to use to create new sessions.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- If mcpTool or mcpSession are null.

    * ### McpAsyncTool

public McpAsyncTool(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpAsyncClient mcpSession, [McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Creates a new McpAsyncTool

Parameters:
    `mcpTool` \- The MCP tool to wrap.
    `mcpSession` \- The MCP session to use to call the tool.
    `mcpSessionManager` \- The MCP session manager to use to create new sessions.
    `objectMapper` \- The ObjectMapper to use to convert JSON schemas.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- If mcpTool or mcpSession are null.

  * ## Method Details

    * ### getMcpSession

public io.modelcontextprotocol.client.McpAsyncClient getMcpSession()

    * ### toGeminiSchema

public com.google.genai.types.Schema toGeminiSchema(io.modelcontextprotocol.spec.McpSchema.JsonSchema openApiSchema)

    * ### declaration

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration> declaration()

Description copied from class: `[BaseTool](../BaseTool.html#declaration\(\))`

Gets the `FunctionDeclaration` representation of this tool.

Overrides:
    `[declaration](../BaseTool.html#declaration\(\))` in class `[BaseTool](../BaseTool.html "class in com.google.adk.tools")`

    * ### runAsync

public io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

Calls a tool.

Overrides:
    `[runAsync](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))` in class `[BaseTool](../BaseTool.html "class in com.google.adk.tools")`




* * *

Copyright (C) 2025\. All rights reserved.
