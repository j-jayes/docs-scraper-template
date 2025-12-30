JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../SseServerParameters.Builder.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.tools.mcp](../package-summary.html)
  2. [SseServerParameters](../SseServerParameters.html)
  3. [Builder](../SseServerParameters.Builder.html)



# Uses of Class  
com.google.adk.tools.mcp.SseServerParameters.Builder

Packages that use [SseServerParameters.Builder](../SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")

Package

Description

com.google.adk.tools.mcp

 

  * ## Uses of [SseServerParameters.Builder](../SseServerParameters.Builder.html "class in com.google.adk.tools.mcp") in [com.google.adk.tools.mcp](../package-summary.html)

Methods in [com.google.adk.tools.mcp](../package-summary.html) that return [SseServerParameters.Builder](../SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")

Modifier and Type

Method

Description

`static [SseServerParameters.Builder](../SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

SseServerParameters.`[builder](../SseServerParameters.html#builder\(\))()`

Creates a new builder for [`SseServerParameters`](../SseServerParameters.html "class in com.google.adk.tools.mcp").

`abstract [SseServerParameters.Builder](../SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

SseServerParameters.Builder.`[headers](../SseServerParameters.Builder.html#headers\(java.util.Map\))([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> headers)`

Sets the headers for the SSE connection request.

`abstract [SseServerParameters.Builder](../SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

SseServerParameters.Builder.`[sseReadTimeout](../SseServerParameters.Builder.html#sseReadTimeout\(java.time.Duration\))([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") sseReadTimeout)`

Sets the timeout for reading data from the SSE stream.

`abstract [SseServerParameters.Builder](../SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

SseServerParameters.Builder.`[timeout](../SseServerParameters.Builder.html#timeout\(java.time.Duration\))([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") timeout)`

Sets the timeout for the initial connection attempt.

`abstract [SseServerParameters.Builder](../SseServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

SseServerParameters.Builder.`[url](../SseServerParameters.Builder.html#url\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") url)`

Sets the URL of the SSE server.




* * *

Copyright (C) 2025\. All rights reserved.
