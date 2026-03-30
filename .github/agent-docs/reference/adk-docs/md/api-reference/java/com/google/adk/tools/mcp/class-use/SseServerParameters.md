JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../SseServerParameters.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.tools.mcp](../package-summary.html)
  2. [SseServerParameters](../SseServerParameters.html)



# Uses of Class  
com.google.adk.tools.mcp.SseServerParameters

Packages that use [SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp")

Package

Description

com.google.adk.tools.mcp

 

  * ## Uses of [SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp") in [com.google.adk.tools.mcp](../package-summary.html)

Methods in [com.google.adk.tools.mcp](../package-summary.html) that return [SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp")

Modifier and Type

Method

Description

`abstract [SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp")`

SseServerParameters.Builder.`[build](../SseServerParameters.Builder.html#build\(\))()`

Builds a new [`SseServerParameters`](../SseServerParameters.html "class in com.google.adk.tools.mcp") instance.

`[SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp")`

McpToolset.McpToolsetConfig.`[sseServerParams](../McpToolset.McpToolsetConfig.html#sseServerParams\(\))()`

 

Methods in [com.google.adk.tools.mcp](../package-summary.html) with parameters of type [SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp")

Modifier and Type

Method

Description

`[McpAsyncToolset.Builder](../McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")`

McpAsyncToolset.Builder.`[connectionParams](../McpAsyncToolset.Builder.html#connectionParams\(com.google.adk.tools.mcp.SseServerParameters\))([SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams)`

 

`void`

McpToolset.McpToolsetConfig.`[setSseServerParams](../McpToolset.McpToolsetConfig.html#setSseServerParams\(com.google.adk.tools.mcp.SseServerParameters\))([SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp") sseServerParams)`

 

Constructors in [com.google.adk.tools.mcp](../package-summary.html) with parameters of type [SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp")

Modifier

Constructor

Description

` `

`[McpToolset](../McpToolset.html#%3Cinit%3E\(com.google.adk.tools.mcp.SseServerParameters\))([SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams)`

Initializes the McpToolset with SSE server parameters, using the ObjectMapper used across the ADK and no tool filter.

` `

`[McpToolset](../McpToolset.html#%3Cinit%3E\(com.google.adk.tools.mcp.SseServerParameters,com.fasterxml.jackson.databind.ObjectMapper\))([SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Initializes the McpToolset with SSE server parameters and no tool filter.

` `

`[McpToolset](../McpToolset.html#%3Cinit%3E\(com.google.adk.tools.mcp.SseServerParameters,com.fasterxml.jackson.databind.ObjectMapper,com.google.adk.tools.ToolPredicate\))([SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [ToolPredicate](../../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)`

Initializes the McpToolset with SSE server parameters.

` `

`[McpToolset](../McpToolset.html#%3Cinit%3E\(com.google.adk.tools.mcp.SseServerParameters,com.fasterxml.jackson.databind.ObjectMapper,java.util.List\))([SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> toolNames)`

Initializes the McpToolset with SSE server parameters.




* * *

Copyright (C) 1980\. All rights reserved.
