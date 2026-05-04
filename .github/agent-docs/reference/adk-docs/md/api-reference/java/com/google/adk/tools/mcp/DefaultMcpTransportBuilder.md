JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/DefaultMcpTransportBuilder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [DefaultMcpTransportBuilder](DefaultMcpTransportBuilder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. DefaultMcpTransportBuilder()
  5. Method Details
     1. build(Object)

Hide sidebar  Show sidebar

# Class DefaultMcpTransportBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.mcp.DefaultMcpTransportBuilder

All Implemented Interfaces:
    `[McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp")`

* * *

public class DefaultMcpTransportBuilder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp")

The default builder for creating MCP client transports. Supports StdioClientTransport based on `ServerParameters`, HttpClientSseClientTransport based on [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp"), and HttpClientStreamableHttpTransport based on [`StreamableHttpServerParameters`](StreamableHttpServerParameters.html "class in com.google.adk.tools.mcp").

  * ## Constructor Summary

Constructors

Constructor

Description

`DefaultMcpTransportBuilder()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.modelcontextprotocol.spec.McpClientTransport`

`build([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams)`

Builds an McpClientTransport based on the provided connection parameters.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### DefaultMcpTransportBuilder

public DefaultMcpTransportBuilder()

  * ## Method Details

    * ### build

public io.modelcontextprotocol.spec.McpClientTransport build([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") connectionParams)

Description copied from interface: `[McpTransportBuilder](McpTransportBuilder.html#build\(java.lang.Object\))`

Builds an McpClientTransport based on the provided connection parameters.

Specified by:
    `[build](McpTransportBuilder.html#build\(java.lang.Object\))` in interface `[McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp")`
Parameters:
    `connectionParams` \- The parameters required to configure the transport. The type of this object determines the type of transport built.
Returns:
    An instance of McpClientTransport.




* * *

Copyright (C) 1980\. All rights reserved.
