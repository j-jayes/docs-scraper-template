JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseTool.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools](../package-summary.html)
  2. [BaseTool](../BaseTool.html)



# Uses of Class  
com.google.adk.tools.BaseTool

Packages that use [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Package

Description

com.google.adk.agents

 

com.google.adk.flows.llmflows

 

com.google.adk.models

 

com.google.adk.tools

 

com.google.adk.tools.applicationintegrationtoolset

 

com.google.adk.tools.mcp

 

com.google.adk.tools.retrieval

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

LlmAgent.`[canonicalTools](../../agents/LlmAgent.html#canonicalTools\(\))()`

Overload of canonicalTools that defaults to an empty context.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

LlmAgent.`[canonicalTools](../../agents/LlmAgent.html#canonicalTools\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") context)`

Convenience overload of canonicalTools that accepts a non-optional ReadonlyContext.

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

LlmAgent.`[canonicalTools](../../agents/LlmAgent.html#canonicalTools\(java.util.Optional\))([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents")> context)`

Constructs the list of tools for this agent based on the [`LlmAgent.tools()`](../../agents/LlmAgent.html#tools\(\)) field.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

LlmAgent.`[tools](../../agents/LlmAgent.html#tools\(\))()`

 

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

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

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Method parameters in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with type arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`static [Set](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Set.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

Functions.`[getLongRunningFunctionCalls](../../flows/llmflows/Functions.html#getLongRunningFunctionCalls\(java.util.List,java.util.Map\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.FunctionCall> functionCalls, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools)`

 

`static io.reactivex.rxjava3.core.Maybe<[Event](../../events/Event.html "class in com.google.adk.events")>`

Functions.`[handleFunctionCalls](../../flows/llmflows/Functions.html#handleFunctionCalls\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,java.util.Map\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [Event](../../events/Event.html "class in com.google.adk.events") functionCallEvent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.models](../../models/package-summary.html)

Methods in [com.google.adk.models](../../models/package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`abstract [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

LlmRequest.`[tools](../../models/LlmRequest.html#tools\(\))()`

Returns a map of tools available to the LLM.

Method parameters in [com.google.adk.models](../../models/package-summary.html) with type arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`final [LlmRequest.Builder](../../models/LlmRequest.Builder.html "class in com.google.adk.models")`

LlmRequest.Builder.`[appendTools](../../models/LlmRequest.Builder.html#appendTools\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[BaseTool](../BaseTool.html "class in com.google.adk.tools")> tools)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools](../package-summary.html)

Subclasses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools](../package-summary.html)

Modifier and Type

Class

Description

`class `

`[AgentTool](../AgentTool.html "class in com.google.adk.tools")`

AgentTool implements a tool that allows an agent to call another agent.

`final class `

`[BuiltInCodeExecutionTool](../BuiltInCodeExecutionTool.html "class in com.google.adk.tools")`

A built-in code execution tool that is automatically invoked by Gemini 2 models.

`class `

`[FunctionTool](../FunctionTool.html "class in com.google.adk.tools")`

FunctionTool implements a customized function calling tool.

`final class `

`[GoogleSearchTool](../GoogleSearchTool.html "class in com.google.adk.tools")`

A built-in tool that is automatically invoked by Gemini 2 models to retrieve search results from Google Search.

`final class `

`[LoadArtifactsTool](../LoadArtifactsTool.html "class in com.google.adk.tools")`

A tool that loads artifacts and adds them to the session.

`class `

`[LongRunningFunctionTool](../LongRunningFunctionTool.html "class in com.google.adk.tools")`

A function tool that returns the result asynchronously.

Methods in [com.google.adk.tools](../package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

BaseToolset.`[getTools](../BaseToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

Return all tools in the toolset based on the provided context.

Methods in [com.google.adk.tools](../package-summary.html) with parameters of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`default boolean`

BaseToolset.`[isToolSelected](../BaseToolset.html#isToolSelected\(com.google.adk.tools.BaseTool,java.util.Optional,java.util.Optional\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)`

Helper method to be used by implementers that returns true if the given tool is in the provided list of tools of if testing against the given ToolPredicate returns true (otherwise false).

`boolean`

ToolPredicate.`[test](../ToolPredicate.html#test\(com.google.adk.tools.BaseTool,java.util.Optional\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents")> readonlyContext)`

Decides if the given tool is selected.

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html)

Subclasses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html)

Modifier and Type

Class

Description

`class `

`[IntegrationConnectorTool](../applicationintegrationtoolset/IntegrationConnectorTool.html "class in com.google.adk.tools.applicationintegrationtoolset")`

Application Integration Tool

Methods in [com.google.adk.tools.applicationintegrationtoolset](../applicationintegrationtoolset/package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

ApplicationIntegrationToolset.`[getTools](../applicationintegrationtoolset/ApplicationIntegrationToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))(@Nullable [ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.mcp](../mcp/package-summary.html)

Subclasses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.mcp](../mcp/package-summary.html)

Modifier and Type

Class

Description

`final class `

`[McpAsyncTool](../mcp/McpAsyncTool.html "class in com.google.adk.tools.mcp")`

Initializes a MCP tool.

`final class `

`[McpTool](../mcp/McpTool.html "class in com.google.adk.tools.mcp")`

Initializes a MCP tool.

Methods in [com.google.adk.tools.mcp](../mcp/package-summary.html) that return types with arguments of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[BaseTool](../BaseTool.html "class in com.google.adk.tools")>`

McpToolset.`[getTools](../mcp/McpToolset.html#getTools\(com.google.adk.agents.ReadonlyContext\))([ReadonlyContext](../../agents/ReadonlyContext.html "class in com.google.adk.agents") readonlyContext)`

 

Methods in [com.google.adk.tools.mcp](../mcp/package-summary.html) with parameters of type [BaseTool](../BaseTool.html "class in com.google.adk.tools")

Modifier and Type

Method

Description

`io.modelcontextprotocol.spec.McpSchema.Tool`

ConversionUtils.`[adkToMcpToolType](../mcp/ConversionUtils.html#adkToMcpToolType\(com.google.adk.tools.BaseTool\))([BaseTool](../BaseTool.html "class in com.google.adk.tools") tool)`

 

  * ## Uses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.retrieval](../retrieval/package-summary.html)

Subclasses of [BaseTool](../BaseTool.html "class in com.google.adk.tools") in [com.google.adk.tools.retrieval](../retrieval/package-summary.html)

Modifier and Type

Class

Description

`class `

`[BaseRetrievalTool](../retrieval/BaseRetrievalTool.html "class in com.google.adk.tools.retrieval")`

Base class for retrieval tools.

`class `

`[VertexAiRagRetrieval](../retrieval/VertexAiRagRetrieval.html "class in com.google.adk.tools.retrieval")`

A retrieval tool that fetches context from Vertex AI RAG.




* * *

Copyright (C) 2025\. All rights reserved.
