JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Package
  * [Use](package-use.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)



Contents

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Related Packages
  3. Classes and Interfaces



# Package com.google.adk.tools

* * *

package com.google.adk.tools

  * Related Packages

Package

Description

[com.google.adk](../package-summary.html)

 

[com.google.adk.tools.applicationintegrationtoolset](applicationintegrationtoolset/package-summary.html)

 

[com.google.adk.tools.mcp](mcp/package-summary.html)

 

[com.google.adk.tools.retrieval](retrieval/package-summary.html)

 

  * All Classes and InterfacesInterfacesClassesAnnotation Interfaces

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

[BaseToolset](BaseToolset.html "interface in com.google.adk.tools")

Base interface for toolsets.

[BuiltInCodeExecutionTool](BuiltInCodeExecutionTool.html "class in com.google.adk.tools")

A built-in code execution tool that is automatically invoked by Gemini 2 models.

[ExitLoopTool](ExitLoopTool.html "class in com.google.adk.tools")

Exits the loop.

[FunctionCallingUtils](FunctionCallingUtils.html "class in com.google.adk.tools")

Utility class for function calling.

[FunctionTool](FunctionTool.html "class in com.google.adk.tools")

FunctionTool implements a customized function calling tool.

[GoogleSearchTool](GoogleSearchTool.html "class in com.google.adk.tools")

A built-in tool that is automatically invoked by Gemini 2 models to retrieve search results from Google Search.

[LoadArtifactsTool](LoadArtifactsTool.html "class in com.google.adk.tools")

A tool that loads artifacts and adds them to the session.

[LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")

A function tool that returns the result asynchronously.

[ToolContext](ToolContext.html "class in com.google.adk.tools")

ToolContext object provides a structured context for executing tools or functions.

[ToolContext.Builder](ToolContext.Builder.html "class in com.google.adk.tools")

Builder for [`ToolContext`](ToolContext.html "class in com.google.adk.tools").

[ToolPredicate](ToolPredicate.html "interface in com.google.adk.tools")

Functional interface to decide whether a tool should be exposed to the LLM based on the current context.




* * *

Copyright (C) 2025\. All rights reserved.
