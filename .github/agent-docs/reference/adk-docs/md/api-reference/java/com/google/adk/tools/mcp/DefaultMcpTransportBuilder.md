JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/DefaultMcpTransportBuilder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [DefaultMcpTransportBuilder](DefaultMcpTransportBuilder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. DefaultMcpTransportBuilder()
  5. Method Details
     1. build(Object)



# Class DefaultMcpTransportBuilder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.mcp.DefaultMcpTransportBuilder

All Implemented Interfaces:
    `[McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp")`

* * *

public class DefaultMcpTransportBuilder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp")

The default builder for creating MCP client transports. Supports StdioClientTransport based on `ServerParameters` and the standard HttpClientSseClientTransport based on [`SseServerParameters`](SseServerParameters.html "class in com.google.adk.tools.mcp").

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

`build([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams)`

Builds an McpClientTransport based on the provided connection parameters.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### DefaultMcpTransportBuilder

public DefaultMcpTransportBuilder()

  * ## Method Details

    * ### build

public io.modelcontextprotocol.spec.McpClientTransport build([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams)

Description copied from interface: `[McpTransportBuilder](McpTransportBuilder.html#build\(java.lang.Object\))`

Builds an McpClientTransport based on the provided connection parameters.

Specified by:
    `[build](McpTransportBuilder.html#build\(java.lang.Object\))` in interface `[McpTransportBuilder](McpTransportBuilder.html "interface in com.google.adk.tools.mcp")`
Parameters:
    `connectionParams` \- The parameters required to configure the transport. The type of this object determines the type of transport built.
Returns:
    An instance of McpClientTransport.




* * *

Copyright (C) 2025\. All rights reserved.
