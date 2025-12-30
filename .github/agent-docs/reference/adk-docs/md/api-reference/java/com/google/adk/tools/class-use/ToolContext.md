JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../ToolContext.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools](../package-summary.html)
  2. [ToolContext](../ToolContext.html)



# Uses of Class  
com.google.adk.tools.ToolContext

Packages that use [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Package

Description

com.google.adk.agents

 

com.google.adk.flows.llmflows

 

com.google.adk.tools

 

com.google.adk.tools.applicationintegrationtoolset

 

com.google.adk.tools.mcp

 

com.google.adk.tools.retrieval

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.AfterToolCallback.`[call](../../agents/Callbacks.AfterToolCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Object\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") response)`

Async callback after tool runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.AfterToolCallbackSync.`[call](../../agents/Callbacks.AfterToolCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext,java.lang.Object\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext, [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") response)`

 

`io.reactivex.rxjava3.core.Maybe<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.BeforeToolCallback.`[call](../../agents/Callbacks.BeforeToolCallback.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Async callback before tool runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

Callbacks.BeforeToolCallbackSync.`[call](../../agents/Callbacks.BeforeToolCallbackSync.html#call\(com.google.adk.agents.InvocationContext,com.google.adk.tools.BaseTool,java.util.Map,com.google.adk.tools.ToolContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [BaseTool](../BaseTool.html "class in com.google.adk.tools") baseTool, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> input, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`static void`

AgentTransfer.`[transferToAgent](../../flows/llmflows/AgentTransfer.html#transferToAgent\(java.lang.String,com.google.adk.tools.ToolContext\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Marks the target agent for transfer using the tool context.

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.tools](../package-summary.html)

Methods in [com.google.adk.tools](../package-summary.html) that return [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`[ToolContext](../ToolContext.html "class in com.google.adk.tools")`

ToolContext.Builder.`[build](../ToolContext.Builder.html#build\(\))()`

 

Methods in [com.google.adk.tools](../package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

LoadArtifactsTool.`[appendArtifactsToLlmRequest](../LoadArtifactsTool.html#appendArtifactsToLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`static void`

ExitLoopTool.`[exitLoop](../ExitLoopTool.html#exitLoop\(com.google.adk.tools.ToolContext\))([ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

BaseTool.`[processLlmRequest](../BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../../models/LlmRequest.Builder.html "class in com.google.adk.models").

`io.reactivex.rxjava3.core.Completable`

BuiltInCodeExecutionTool.`[processLlmRequest](../BuiltInCodeExecutionTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

GoogleSearchTool.`[processLlmRequest](../GoogleSearchTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Completable`

LoadArtifactsTool.`[processLlmRequest](../LoadArtifactsTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

AgentTool.`[runAsync](../AgentTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

BaseTool.`[runAsync](../BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

FunctionTool.`[runAsync](../FunctionTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

LoadArtifactsTool.`[runAsync](../LoadArtifactsTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html)

Methods in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

IntegrationConnectorTool.`[runAsync](../applicationintegrationtoolset/IntegrationConnectorTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.tools.mcp](../mcp/package-summary.html)

Methods in [com.google.adk.tools.mcp](../mcp/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

McpAsyncTool.`[runAsync](../mcp/McpAsyncTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

McpTool.`[runAsync](../mcp/McpTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

  * ## Uses of [ToolContext](../ToolContext.html "class in com.google.adk.tools") in [com.google.adk.tools.retrieval](../retrieval/package-summary.html)

Methods in [com.google.adk.tools.retrieval](../retrieval/package-summary.html) with parameters of type [ToolContext](../ToolContext.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

VertexAiRagRetrieval.`[processLlmRequest](../retrieval/VertexAiRagRetrieval.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))([LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

VertexAiRagRetrieval.`[runAsync](../retrieval/VertexAiRagRetrieval.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](../ToolContext.html "class in com.google.adk.tools") toolContext)`

 




* * *

Copyright (C) 2025\. All rights reserved.
