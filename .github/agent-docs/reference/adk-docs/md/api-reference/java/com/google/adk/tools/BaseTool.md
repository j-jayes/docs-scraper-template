JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseTool.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [BaseTool](BaseTool.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. BaseTool(String, String)
     2. BaseTool(String, String, boolean)
  5. Method Details
     1. name()
     2. description()
     3. longRunning()
     4. declaration()
     5. runAsync(Map, ToolContext)
     6. processLlmRequest(LlmRequest.Builder, ToolContext)



# Class BaseTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.BaseTool

Direct Known Subclasses:
    `[AgentTool](AgentTool.html "class in com.google.adk.tools")`, `[BaseRetrievalTool](retrieval/BaseRetrievalTool.html "class in com.google.adk.tools.retrieval")`, `[BuiltInCodeExecutionTool](BuiltInCodeExecutionTool.html "class in com.google.adk.tools")`, `[FunctionTool](FunctionTool.html "class in com.google.adk.tools")`, `[GoogleSearchTool](GoogleSearchTool.html "class in com.google.adk.tools")`, `[IntegrationConnectorTool](applicationintegrationtoolset/IntegrationConnectorTool.html "class in com.google.adk.tools.applicationintegrationtoolset")`, `[LoadArtifactsTool](LoadArtifactsTool.html "class in com.google.adk.tools")`, `[McpAsyncTool](mcp/McpAsyncTool.html "class in com.google.adk.tools.mcp")`, `[McpTool](mcp/McpTool.html "class in com.google.adk.tools.mcp")`

* * *

public abstract class BaseTool extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

The base class for all ADK tools.

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`BaseTool([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)`

 

`protected `

`BaseTool([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, boolean isLongRunning)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration>`

`declaration()`

Gets the `FunctionDeclaration` representation of this tool.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`description()`

 

`boolean`

`longRunning()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`name()`

 

`io.reactivex.rxjava3.core.Completable`

`processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models").

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### BaseTool

protected BaseTool(@Nonnull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, @Nonnull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description)

    * ### BaseTool

protected BaseTool(@Nonnull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name, @Nonnull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description, boolean isLongRunning)

  * ## Method Details

    * ### name

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name()

    * ### description

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") description()

    * ### longRunning

public boolean longRunning()

    * ### declaration

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration> declaration()

Gets the `FunctionDeclaration` representation of this tool.

    * ### runAsync

public io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Calls a tool.

    * ### processLlmRequest

@CanIgnoreReturnValue public io.reactivex.rxjava3.core.Completable processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models"). 

This implementation adds the current tool's `declaration()` to the `GenerateContentConfig` within the builder. If a tool with function declarations already exists, the current tool's declaration is merged into it. Otherwise, a new tool definition with the current tool's declaration is created. The current tool itself is also added to the builder's internal list of tools. Override this method for processing the outgoing request.




* * *

Copyright (C) 2025\. All rights reserved.
