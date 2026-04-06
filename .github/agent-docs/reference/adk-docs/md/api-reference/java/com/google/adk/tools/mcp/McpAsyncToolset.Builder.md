JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpAsyncToolset.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



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
     3. objectMapper(ObjectMapper)
     4. toolFilter(List)
     5. toolFilter(ToolPredicate)
     6. build()

Hide sidebar  Show sidebar

# Class McpAsyncToolset.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.mcp.McpAsyncToolset.Builder

Enclosing class:
    `[McpAsyncToolset](McpAsyncToolset.html "class in com.google.adk.tools.mcp")`

* * *

public static class McpAsyncToolset.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`objectMapper(com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

 

`[McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")`

`toolFilter(@Nullable [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)`

 

`[McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp")`

`toolFilter([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> toolNames)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### connectionParams

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") connectionParams(io.modelcontextprotocol.client.transport.ServerParameters connectionParams)

    * ### connectionParams

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") connectionParams([SseServerParameters](SseServerParameters.html "class in com.google.adk.tools.mcp") connectionParams)

    * ### objectMapper

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") objectMapper(com.fasterxml.jackson.databind.ObjectMapper objectMapper)

    * ### toolFilter

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") toolFilter([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> toolNames)

    * ### toolFilter

@CanIgnoreReturnValue public [McpAsyncToolset.Builder](McpAsyncToolset.Builder.html "class in com.google.adk.tools.mcp") toolFilter(@Nullable [ToolPredicate](../ToolPredicate.html "interface in com.google.adk.tools") toolPredicate)

    * ### build

public [McpAsyncToolset](McpAsyncToolset.html "class in com.google.adk.tools.mcp") build()




* * *

Copyright (C) 1980\. All rights reserved.
