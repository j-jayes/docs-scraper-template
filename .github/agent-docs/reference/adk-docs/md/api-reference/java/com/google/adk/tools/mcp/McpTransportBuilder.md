JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/McpTransportBuilder.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [McpTransportBuilder](McpTransportBuilder.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. build(Object)



# Interface McpTransportBuilder

All Known Implementing Classes:
    `[DefaultMcpTransportBuilder](DefaultMcpTransportBuilder.html "class in com.google.adk.tools.mcp")`

* * *

public interface McpTransportBuilder

Interface for building McpClientTransport instances. Implementations of this interface are responsible for constructing concrete McpClientTransport objects based on the provided connection parameters.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.modelcontextprotocol.spec.McpClientTransport`

`build([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams)`

Builds an McpClientTransport based on the provided connection parameters.




  * ## Method Details

    * ### build

io.modelcontextprotocol.spec.McpClientTransport build([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") connectionParams)

Builds an McpClientTransport based on the provided connection parameters.

Parameters:
    `connectionParams` \- The parameters required to configure the transport. The type of this object determines the type of transport built.
Returns:
    An instance of McpClientTransport.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if the connectionParams are not supported or invalid.




* * *

Copyright (C) 2025\. All rights reserved.
