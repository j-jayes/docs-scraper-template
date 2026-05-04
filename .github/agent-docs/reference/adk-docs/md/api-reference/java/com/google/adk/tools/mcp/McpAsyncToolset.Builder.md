JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpAsyncToolset.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [McpAsyncToolset](McpAsyncToolset.html)
  3. [Builder](McpAsyncToolset.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. connectionParams(ServerParameters)
     2. connectionParams(SseServerParameters)
     3. mcpSessionManager(McpSessionManager)
     4. objectMapper(ObjectMapper)
     5. toolFilter(List)
     6. toolFilter(ToolPredicate)
     7. build()

Hide sidebar  Show sidebar

# Class McpAsyncToolset.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.mcp.McpAsyncToolset.Builder

Enclosing class:
    `[McpAsyncToolset](McpAsyncToolset.html "class in com.google.adk.tools.mcp")`

* * *

public static class McpAsyncToolset.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for McpAsyncToolset

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[McpAsyncToolset](McpAsyncToolset.html "class in com.google.adk.tools.mcp")`

`build()`

 

`[McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")`

`connectionParams([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams)`

 

`[McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")`

`connectionParams(io.modelcontextprotocol.client.transport.ServerParameters connectionParams)`

 

`[McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")`

`mcpSessionManager([McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager)`

 

`[McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")`

`objectMapper(com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

 

`[McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")`

`toolFilter(@Nullable [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)`

 

`[McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")`

`toolFilter([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### connectionParams

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") connectionParams(io.modelcontextprotocol.client.transport.ServerParameters connectionParams)

    * ### connectionParams

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") connectionParams([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams)

    * ### mcpSessionManager

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") mcpSessionManager([McpSessionManager](McpSessionManager.html "class in com.google.adk.tools.mcp") mcpSessionManager)

    * ### objectMapper

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") objectMapper(com.fasterxml.jackson.databind.ObjectMapper objectMapper)

    * ### toolFilter

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") toolFilter([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> toolNames)

    * ### toolFilter

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") toolFilter(@Nullable [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)

    * ### build

public [McpAsyncToolset](McpAsyncToolset.html "class in com.google.adk.tools.mcp") build()




* * *

Copyright (C) 1980\. All rights reserved.
