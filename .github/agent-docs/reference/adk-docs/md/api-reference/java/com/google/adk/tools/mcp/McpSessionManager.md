JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpSessionManager.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [McpSessionManager](McpSessionManager.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. McpSessionManager(Object)
     2. McpSessionManager(Object, McpTransportBuilder)
  5. Method Details
     1. createSession()
     2. initializeSession(Object)
     3. initializeSession(Object, McpTransportBuilder)
     4. createAsyncSession()
     5. initializeAsyncSession(Object)
     6. initializeAsyncSession(Object, McpTransportBuilder)



# Class McpSessionManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.mcp.McpSessionManager

* * *

public class McpSessionManager extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Manages MCP client sessions. 

This class provides methods for creating and initializing MCP client sessions, handling different connection parameters and transport builders.

  * ## Constructor Summary

Constructors

Constructor

Description

`McpSessionManager([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams)`

 

`McpSessionManager([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.modelcontextprotocol.client.McpAsyncClient`

`createAsyncSession()`

 

`io.modelcontextprotocol.client.McpSyncClient`

`createSession()`

 

`static io.modelcontextprotocol.client.McpAsyncClient`

`initializeAsyncSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams)`

 

`static io.modelcontextprotocol.client.McpAsyncClient`

`initializeAsyncSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)`

 

`static io.modelcontextprotocol.client.McpSyncClient`

`initializeSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams)`

 

`static io.modelcontextprotocol.client.McpSyncClient`

`initializeSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### McpSessionManager

public McpSessionManager([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams)

    * ### McpSessionManager

public McpSessionManager([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)

  * ## Method Details

    * ### createSession

public io.modelcontextprotocol.client.McpSyncClient createSession()

    * ### initializeSession

public static io.modelcontextprotocol.client.McpSyncClient initializeSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams)

    * ### initializeSession

public static io.modelcontextprotocol.client.McpSyncClient initializeSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)

    * ### createAsyncSession

public io.modelcontextprotocol.client.McpAsyncClient createAsyncSession()

    * ### initializeAsyncSession

public static io.modelcontextprotocol.client.McpAsyncClient initializeAsyncSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams)

    * ### initializeAsyncSession

public static io.modelcontextprotocol.client.McpAsyncClient initializeAsyncSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)




* * *

Copyright (C) 2025\. All rights reserved.
