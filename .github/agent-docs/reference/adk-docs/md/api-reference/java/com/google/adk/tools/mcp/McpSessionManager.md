JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpSessionManager.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [McpSessionManager](McpSessionManager.html)



Contents  

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

Hide sidebar  Show sidebar

# Class McpSessionManager

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.mcp.McpSessionManager

* * *

public class McpSessionManager extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Manages MCP client sessions. 

This class provides methods for creating and initializing MCP client sessions, handling different connection parameters and transport builders.

  * ## Constructor Summary

Constructors

Constructor

Description

`McpSessionManager([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams)`

 

`McpSessionManager([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)`

 

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

`initializeAsyncSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams)`

 

`static io.modelcontextprotocol.client.McpAsyncClient`

`initializeAsyncSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)`

 

`static io.modelcontextprotocol.client.McpSyncClient`

`initializeSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams)`

 

`static io.modelcontextprotocol.client.McpSyncClient`

`initializeSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### McpSessionManager

public McpSessionManager([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams)

    * ### McpSessionManager

public McpSessionManager([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)

  * ## Method Details

    * ### createSession

public io.modelcontextprotocol.client.McpSyncClient createSession()

    * ### initializeSession

public static io.modelcontextprotocol.client.McpSyncClient initializeSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams)

    * ### initializeSession

public static io.modelcontextprotocol.client.McpSyncClient initializeSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)

    * ### createAsyncSession

public io.modelcontextprotocol.client.McpAsyncClient createAsyncSession()

    * ### initializeAsyncSession

public static io.modelcontextprotocol.client.McpAsyncClient initializeAsyncSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams)

    * ### initializeAsyncSession

public static io.modelcontextprotocol.client.McpAsyncClient initializeAsyncSession([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams, [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp") transportBuilder)




* * *

Copyright (C) 1980\. All rights reserved.
