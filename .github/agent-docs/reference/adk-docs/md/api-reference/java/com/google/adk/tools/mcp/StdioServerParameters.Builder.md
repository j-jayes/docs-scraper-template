JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/StdioServerParameters.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools.mcp](package-summary.html)
  2. [StdioServerParameters](StdioServerParameters.html)
  3. [Builder](StdioServerParameters.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. command(String)
     2. args(List)
     3. env(Map)
     4. build()

Hide sidebar  Show sidebar

# Class StdioServerParameters.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.mcp.StdioServerParameters.Builder

Enclosing class:
    `[StdioServerParameters](StdioServerParameters.html "class in com.google.adk.tools.mcp")`

* * *

public abstract static class StdioServerParameters.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`StdioServerParameters`](StdioServerParameters.html "class in com.google.adk.tools.mcp").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`abstract [StdioServerParameters.Builder](StdioServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`args(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> args)`

Sets the arguments for the command.

`abstract [StdioServerParameters](StdioServerParameters.html "class in com.google.adk.tools.mcp")`

`build()`

Builds a new [`StdioServerParameters`](StdioServerParameters.html "class in com.google.adk.tools.mcp") instance.

`abstract [StdioServerParameters.Builder](StdioServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`command([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") command)`

Sets the command to execute for the stdio server.

`abstract [StdioServerParameters.Builder](StdioServerParameters.Builder.html "class in com.google.adk.tools.mcp")`

`env(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> env)`

Sets the environment variables.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### command

public abstract [StdioServerParameters.Builder](StdioServerParameters.Builder.html "class in com.google.adk.tools.mcp") command([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") command)

Sets the command to execute for the stdio server.

    * ### args

public abstract [StdioServerParameters.Builder](StdioServerParameters.Builder.html "class in com.google.adk.tools.mcp") args(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> args)

Sets the arguments for the command.

    * ### env

public abstract [StdioServerParameters.Builder](StdioServerParameters.Builder.html "class in com.google.adk.tools.mcp") env(@Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> env)

Sets the environment variables.

    * ### build

public abstract [StdioServerParameters](StdioServerParameters.html "class in com.google.adk.tools.mcp") build()

Builds a new [`StdioServerParameters`](StdioServerParameters.html "class in com.google.adk.tools.mcp") instance.




* * *

Copyright (C) 1980\. All rights reserved.
