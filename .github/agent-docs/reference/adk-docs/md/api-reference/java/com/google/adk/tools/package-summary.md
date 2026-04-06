JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Package
  * [Use](package-use.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)



Contents

  1. Description
  2. Related Packages
  3. Classes and Interfaces

Hide sidebar  Show sidebar

# Package com.google.adk.tools

* * *

package com.google.adk.tools

  * Related Packages

Package

Description

[com.google.adk](../package-summary.html)

 

[com.google.adk.tools.applicationintegrationtoolset](applicationintegrationtoolset/package-summary.html)

 

[com.google.adk.tools.computeruse](computeruse/package-summary.html)

 

[com.google.adk.tools.mcp](mcp/package-summary.html)

 

[com.google.adk.tools.retrieval](retrieval/package-summary.html)

 

  * All Classes and InterfacesInterfacesClassesRecord ClassesAnnotation Interfaces

Class

Description

[AgentTool](AgentTool.html "class in com.google.adk.tools")

AgentTool implements a tool that allows an agent to call another agent.

[Annotations](Annotations.html "class in com.google.adk.tools")

Annotations for tools.

[Annotations.Schema](Annotations.Schema.html "annotation interface in com.google.adk.tools")

The annotation for binding the 'Schema' input.

[BaseTool](BaseTool.html "class in com.google.adk.tools")

The base class for all ADK tools.

[BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools")

Configuration class for tool arguments that allows arbitrary key-value pairs.

[BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools")

Configuration class for a tool definition in YAML/JSON.

[BaseToolset](BaseToolset.html "interface in com.google.adk.tools")

Base interface for toolsets.

[BuiltInCodeExecutionTool](BuiltInCodeExecutionTool.html "class in com.google.adk.tools")

A built-in code execution tool that is automatically invoked by Gemini 2 models.

[ExampleTool](ExampleTool.html "class in com.google.adk.tools")

A tool that injects (few-shot) examples into the outgoing LLM request as system instructions.

[ExampleTool.Builder](ExampleTool.Builder.html "class in com.google.adk.tools")

Builder for [`ExampleTool`](ExampleTool.html "class in com.google.adk.tools").

[ExitLoopTool](ExitLoopTool.html "class in com.google.adk.tools")

Tool for exiting execution of [`LoopAgent`](../agents/LoopAgent.html "class in com.google.adk.agents").

[FunctionCallingUtils](FunctionCallingUtils.html "class in com.google.adk.tools")

Utility class for function calling.

[FunctionTool](FunctionTool.html "class in com.google.adk.tools")

FunctionTool implements a customized function calling tool.

[GoogleMapsTool](GoogleMapsTool.html "class in com.google.adk.tools")

A built-in tool that is automatically invoked by Gemini 2 models to retrieve search results from Google Maps.

[GoogleSearchAgentTool](GoogleSearchAgentTool.html "class in com.google.adk.tools")

A tool that wraps a sub-agent that only uses google_search tool.

[GoogleSearchTool](GoogleSearchTool.html "class in com.google.adk.tools")

A built-in tool that is automatically invoked by Gemini 2 and 3 models to retrieve search results from Google Search.

[LoadArtifactsTool](LoadArtifactsTool.html "class in com.google.adk.tools")

A tool that loads artifacts and adds them to the session.

[LoadMemoryResponse](LoadMemoryResponse.html "class in com.google.adk.tools")

The response from a load memory tool invocation.

[LoadMemoryTool](LoadMemoryTool.html "class in com.google.adk.tools")

A tool that loads memory for the current user.

[LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")

A function tool that returns the result asynchronously.

[NamedToolPredicate](NamedToolPredicate.html "class in com.google.adk.tools")

 

[SetModelResponseTool](SetModelResponseTool.html "class in com.google.adk.tools")

Internal tool used for output schema workaround.

[ToolContext](ToolContext.html "class in com.google.adk.tools")

ToolContext object provides a structured context for executing tools or functions.

[ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools")

Builder for [`ToolContext`](ToolContext.html "class in com.google.adk.tools").

[ToolPredicate](ToolPredicate.html "interface in com.google.adk.tools")

Functional interface to decide whether a tool should be exposed to the LLM based on the current context.

[UrlContextTool](UrlContextTool.html "class in com.google.adk.tools")

A built-in tool that is automatically invoked by Gemini 2 and 3 models to retrieve information from the given URLs.

[VertexAiSearchAgentTool](VertexAiSearchAgentTool.html "class in com.google.adk.tools")

A tool that wraps a sub-agent that only uses vertex_ai_search tool.

[VertexAiSearchTool](VertexAiSearchTool.html "class in com.google.adk.tools")

A built-in tool using Vertex AI Search.

[VertexAiSearchTool.Builder](VertexAiSearchTool.Builder.html "class in com.google.adk.tools")

Builder for [`VertexAiSearchTool`](VertexAiSearchTool.html "class in com.google.adk.tools").




* * *

Copyright (C) 1980\. All rights reserved.
