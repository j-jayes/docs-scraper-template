JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/StdioServerParameters.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [StdioServerParameters](StdioServerParameters.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. StdioServerParameters()
  6. Method Details
     1. command()
     2. args()
     3. env()
     4. builder()
     5. toServerParameters()

Hide sidebar  Show sidebar

# Class StdioServerParameters

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.mcp.StdioServerParameters

* * *

public abstract class StdioServerParameters extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Parameters for establishing a MCP stdio connection.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[StdioServerParameters.Builder](StdioServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

Builder for [`StdioServerParameters`](StdioServerParameters.html "class in com.google.adk.tools.mcp").

  * ## Constructor Summary

Constructors

Constructor

Description

`StdioServerParameters()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract @Nullable com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`args()`

Optional arguments for the command.

`static [StdioServerParameters.Builder](StdioServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`builder()`

Creates a new builder for [`StdioServerParameters`](StdioServerParameters.html "class in com.google.adk.tools.mcp").

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`command()`

The command to execute for the stdio server.

`abstract @Nullable com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`env()`

Optional environment variables.

`io.modelcontextprotocol.client.transport.ServerParameters`

`toServerParameters()`

Converts this to a `ServerParameters` instance.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### StdioServerParameters

public StdioServerParameters()

  * ## Method Details

    * ### command

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") command()

The command to execute for the stdio server.

    * ### args

public abstract @Nullable com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> args()

Optional arguments for the command.

    * ### env

public abstract @Nullable com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> env()

Optional environment variables.

    * ### builder

public static [StdioServerParameters.Builder](StdioServerParameters.Builder.html "class in com.google.adk.tools.mcp") builder()

Creates a new builder for [`StdioServerParameters`](StdioServerParameters.html "class in com.google.adk.tools.mcp").

    * ### toServerParameters

public io.modelcontextprotocol.client.transport.ServerParameters toServerParameters()

Converts this to a `ServerParameters` instance.




* * *

Copyright (C) 1980\. All rights reserved.
