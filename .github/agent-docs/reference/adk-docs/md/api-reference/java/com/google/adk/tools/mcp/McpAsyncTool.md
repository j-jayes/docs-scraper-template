JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpAsyncTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [McpAsyncTool](McpAsyncTool.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Constructor Summary
  5. Method Summary
  6. Constructor Details
     1. McpAsyncTool(McpSchema.Tool, McpAsyncClient, McpSessionManager)
     2. McpAsyncTool(McpSchema.Tool, McpAsyncClient, McpSessionManager, ObjectMapper)
  7. Method Details
     1. runAsync(Map, ToolContext)

Hide sidebar  Show sidebar

# Class McpAsyncTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](../BaseTool.html "class in com.google.adk.tools")

[com.google.adk.tools.mcp.AbstractMcpTool](AbstractMcpTool.html "class in com.google.adk.tools.mcp")<io.modelcontextprotocol.client.McpAsyncClient>

com.google.adk.tools.mcp.McpAsyncTool

* * *

public final class McpAsyncTool extends [AbstractMcpTool](AbstractMcpTool.html "class in com.google.adk.tools.mcp")<io.modelcontextprotocol.client.McpAsyncClient>

Initializes a MCP tool. 

This wraps a MCP Tool interface and an active MCP Session. It invokes the MCP Tool through executing the tool from remote MCP Session.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [BaseTool](../BaseTool.html#nested-class-summary "class in com.google.adk.tools")

`[BaseTool.ToolArgsConfig](../BaseTool.ToolArgsConfig.html "class in com.google.adk.tools"), [BaseTool.ToolConfig](../BaseTool.ToolConfig.html "class in com.google.adk.tools")`

  * ## Field Summary

### Fields inherited from class [AbstractMcpTool](AbstractMcpTool.html#field-summary "class in com.google.adk.tools.mcp")

`[mcpSession](AbstractMcpTool.html#mcpSession), [mcpSessionManager](AbstractMcpTool.html#mcpSessionManager), [mcpTool](AbstractMcpTool.html#mcpTool), [objectMapper](AbstractMcpTool.html#objectMapper)`

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

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

### Methods inherited from class [AbstractMcpTool](AbstractMcpTool.html#method-summary "class in com.google.adk.tools.mcp")

`[annotations](AbstractMcpTool.html#annotations\(\) "annotations\(\)"), [declaration](AbstractMcpTool.html#declaration\(\) "declaration\(\)"), [getMcpSession](AbstractMcpTool.html#getMcpSession\(\) "getMcpSession\(\)"), [meta](AbstractMcpTool.html#meta\(\) "meta\(\)"), [wrapCallResult](AbstractMcpTool.html#wrapCallResult\(com.fasterxml.jackson.databind.ObjectMapper,java.lang.String,io.modelcontextprotocol.spec.McpSchema.CallToolResult\) "wrapCallResult\(ObjectMapper, String, McpSchema.CallToolResult\)")`

### Methods inherited from class [BaseTool](../BaseTool.html#method-summary "class in com.google.adk.tools")

`[customMetadata](../BaseTool.html#customMetadata\(\) "customMetadata\(\)"), [description](../BaseTool.html#description\(\) "description\(\)"), [fromConfig](../BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\) "fromConfig\(BaseTool.ToolConfig, String\)"), [longRunning](../BaseTool.html#longRunning\(\) "longRunning\(\)"), [name](../BaseTool.html#name\(\) "name\(\)"), [processLlmRequest](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\) "processLlmRequest\(LlmRequest.Builder, ToolContext\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, TypeReference\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, ObjectMapper, TypeReference\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,java.lang.Class\) "runAsync\(I, ToolContext, ObjectMapper, Class\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,java.lang.Class\) "runAsync\(I, ToolContext, Class\)"), [runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext\) "runAsync\(T, ToolContext\)"), [runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper\) "runAsync\(T, ToolContext, ObjectMapper\)"), [setCustomMetadata](../BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\) "setCustomMetadata\(String, Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

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

    * ### runAsync

public io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

Calls a tool.

Overrides:
    `[runAsync](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))` in class `[BaseTool](../BaseTool.html "class in com.google.adk.tools")`




* * *

Copyright (C) 1980\. All rights reserved.
