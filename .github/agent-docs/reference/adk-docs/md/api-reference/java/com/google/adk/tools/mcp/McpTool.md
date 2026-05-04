JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [McpTool](McpTool.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Constructor Summary
  5. Method Summary
  6. Constructor Details
     1. McpTool(McpSchema.Tool, McpSyncClient, McpSessionManager)
     2. McpTool(McpSchema.Tool, McpSyncClient, McpSessionManager, ObjectMapper)
  7. Method Details
     1. runAsync(Map, ToolContext)

Hide sidebar  Show sidebar

# Class McpTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.tools.BaseTool](../BaseTool.html "class in com.google.adk.tools")

[com.google.adk.tools.mcp.AbstractMcpTool](AbstractMcpTool.html "class in com.google.adk.tools.mcp")<io.modelcontextprotocol.client.McpSyncClient>

com.google.adk.tools.mcp.McpTool

* * *

public final class McpTool extends [AbstractMcpTool](AbstractMcpTool.html "class in com.google.adk.tools.mcp")<io.modelcontextprotocol.client.McpSyncClient>

Initializes a MCP tool. 

This wraps a MCP Tool interface and an active MCP Session. It invokes the MCP Tool through executing the tool from remote MCP Session.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [BaseTool](../BaseTool.html#nested-class-summary "class in com.google.adk.tools")

`[BaseTool.ToolArgsConfig](../BaseTool.ToolArgsConfig.html "class in com.google.adk.tools"), [BaseTool.ToolConfig](../BaseTool.ToolConfig.html "class in com.google.adk.tools")`

Modifier and Type

Class

Description

`static class `

`[BaseTool.ToolArgsConfig](../BaseTool.ToolArgsConfig.html "class in com.google.adk.tools")`

Configuration class for tool arguments that allows arbitrary key-value pairs.

`static class `

`[BaseTool.ToolConfig](../BaseTool.ToolConfig.html "class in com.google.adk.tools")`

Configuration class for a tool definition in YAML/JSON.

  * ## Field Summary

### Fields inherited from class [AbstractMcpTool](AbstractMcpTool.html#field-summary "class in com.google.adk.tools.mcp")

`[mcpSession](AbstractMcpTool.html#mcpSession), [mcpSessionManager](AbstractMcpTool.html#mcpSessionManager), [mcpTool](AbstractMcpTool.html#mcpTool), [objectMapper](AbstractMcpTool.html#objectMapper)`

Modifier and Type

Field

Description

`protected io.modelcontextprotocol.client.McpSyncClient`

`[mcpSession](AbstractMcpTool.html#mcpSession)`

 

`protected final [McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp")`

`[mcpSessionManager](AbstractMcpTool.html#mcpSessionManager)`

 

`protected final io.modelcontextprotocol.spec.McpSchema.Tool`

`[mcpTool](AbstractMcpTool.html#mcpTool)`

 

`protected final com.fasterxml.jackson.databind.ObjectMapper`

`[objectMapper](AbstractMcpTool.html#objectMapper)`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`McpTool(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpSyncClient mcpSession, [McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager)`

Creates a new McpTool with the default ObjectMapper.

`McpTool(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpSyncClient mcpSession, [McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Creates a new McpTool with the default ObjectMapper.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

### Methods inherited from class [AbstractMcpTool](AbstractMcpTool.html#method-summary "class in com.google.adk.tools.mcp")

`[annotations](AbstractMcpTool.html#annotations\(\) "annotations\(\)"), [declaration](AbstractMcpTool.html#declaration\(\) "declaration\(\)"), [getMcpSession](AbstractMcpTool.html#getMcpSession\(\) "getMcpSession\(\)"), [meta](AbstractMcpTool.html#meta\(\) "meta\(\)"), [wrapCallResult](AbstractMcpTool.html#wrapCallResult\(com.fasterxml.jackson.databind.ObjectMapper,java.lang.String,io.modelcontextprotocol.spec.McpSchema.CallToolResult\) "wrapCallResult\(ObjectMapper, String, McpSchema.CallToolResult\)")`

Modifier and Type

Method

Description

`io.modelcontextprotocol.spec.McpSchema.ToolAnnotations`

`[annotations](AbstractMcpTool.html#annotations\(\))()`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.FunctionDeclaration>`

`[declaration](AbstractMcpTool.html#declaration\(\))()`

Gets the `FunctionDeclaration` representation of this tool.

`io.modelcontextprotocol.client.McpSyncClient`

`[getMcpSession](AbstractMcpTool.html#getMcpSession\(\))()`

 

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`[meta](AbstractMcpTool.html#meta\(\))()`

 

`protected static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`[wrapCallResult](AbstractMcpTool.html#wrapCallResult\(com.fasterxml.jackson.databind.ObjectMapper,java.lang.String,io.modelcontextprotocol.spec.McpSchema.CallToolResult\))(com.fasterxml.jackson.databind.ObjectMapper objectMapper, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") mcpToolName, io.modelcontextprotocol.spec.McpSchema.CallToolResult callResult)`

 

### Methods inherited from class [BaseTool](../BaseTool.html#method-summary "class in com.google.adk.tools")

`[customMetadata](../BaseTool.html#customMetadata\(\) "customMetadata\(\)"), [description](../BaseTool.html#description\(\) "description\(\)"), [fromConfig](../BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\) "fromConfig\(BaseTool.ToolConfig, String\)"), [longRunning](../BaseTool.html#longRunning\(\) "longRunning\(\)"), [name](../BaseTool.html#name\(\) "name\(\)"), [processLlmRequest](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\) "processLlmRequest\(LlmRequest.Builder, ToolContext\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, TypeReference\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, ObjectMapper, TypeReference\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,java.lang.Class\) "runAsync\(I, ToolContext, ObjectMapper, Class\)"), [runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,java.lang.Class\) "runAsync\(I, ToolContext, Class\)"), [runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext\) "runAsync\(T, ToolContext\)"), [runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper\) "runAsync\(T, ToolContext, ObjectMapper\)"), [setCustomMetadata](../BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\) "setCustomMetadata\(String, Object\)")`

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`[customMetadata](../BaseTool.html#customMetadata\(\))()`

Returns a read-only view of the tool metadata.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[description](../BaseTool.html#description\(\))()`

 

`static [BaseTool](../BaseTool.html "class in com.google.adk.tools")`

`[fromConfig](../BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\))([BaseTool.ToolConfig](../BaseTool.ToolConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") configAbsPath)`

Creates a tool instance from a config.

`boolean`

`[longRunning](../BaseTool.html#longRunning\(\))()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[name](../BaseTool.html#name\(\))()`

 

`io.reactivex.rxjava3.core.Completable`

`[processLlmRequest](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../../models/LlmRequest.Builder.html "class in com.google.adk.models").

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.core.type.TypeReference\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)`

Calls a tool with generic arguments, returning the results converted to a specified type reference.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,com.fasterxml.jackson.core.type.TypeReference\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, com.fasterxml.jackson.core.type.TypeReference<? extends O> typeReference)`

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified type reference.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,java.lang.Class\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends O> oClass)`

Calls a tool with generic arguments and a custom `ObjectMapper`, returning the results converted to a specified class.

`final <I,O> io.reactivex.rxjava3.core.Single<O>`

`[runAsync](../BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,java.lang.Class\))(I args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends O> oClass)`

Calls a tool with generic arguments, returning the results converted to a specified class.

`final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext\))(T args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool with generic arguments and returns a map of results.

`final <T> io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>>`

`[runAsync](../BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper\))(T args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Calls a tool with generic arguments using a custom `ObjectMapper` and returns a map of results.

`void`

`[setCustomMetadata](../BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") key, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") value)`

Sets custom metadata to the tool associated with a key.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### McpTool

public McpTool(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpSyncClient mcpSession, [McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager)

Creates a new McpTool with the default ObjectMapper.

Parameters:
    `mcpTool` \- The MCP tool to wrap.
    `mcpSession` \- The MCP session to use to call the tool.
    `mcpSessionManager` \- The MCP session manager to use to create new sessions.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- If mcpTool or mcpSession are null.

    * ### McpTool

public McpTool(io.modelcontextprotocol.spec.McpSchema.Tool mcpTool, io.modelcontextprotocol.client.McpSyncClient mcpSession, [McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Creates a new McpTool with the default ObjectMapper.

Parameters:
    `mcpTool` \- The MCP tool to wrap.
    `mcpSession` \- The MCP session to use to call the tool.
    `mcpSessionManager` \- The MCP session manager to use to create new sessions.
    `objectMapper` \- The ObjectMapper to use to convert JSON schemas.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- If mcpTool or mcpSession are null.

  * ## Method Details

    * ### runAsync

public io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>> runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

Calls a tool.

Overrides:
    `[runAsync](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))` in class `[BaseTool](../BaseTool.html "class in com.google.adk.tools")`




* * *

Copyright (C) 1980\. All rights reserved.
