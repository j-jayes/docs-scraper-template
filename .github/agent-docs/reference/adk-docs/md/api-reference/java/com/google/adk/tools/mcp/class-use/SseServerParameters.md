JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../SseServerParameters.html)
  * Use
  * [Tree](../package-tree.html)
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

`[McpToolset](../McpToolset.html#%3Cinit%3E\(com.google.adk.tools.mcp.SseServerParameters,com.fasterxml.jackson.databind.ObjectMapper,java.util.Optional\))([SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, com.fasterxml.jackson.databind.ObjectMapper objectMapper, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter)`

Initializes the McpToolset with SSE server parameters.

` `

`[McpToolset](../McpToolset.html#%3Cinit%3E\(com.google.adk.tools.mcp.SseServerParameters,java.util.Optional\))([SseServerParameters](../SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> toolFilter)`

Initializes the McpToolset with SSE server parameters, using the ObjectMapper used across the ADK.




* * *

Copyright (C) 2025\. All rights reserved.
