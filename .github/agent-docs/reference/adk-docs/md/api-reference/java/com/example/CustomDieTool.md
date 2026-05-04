JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../index.html)
  * Class
  * [Use](class-use/CustomDieTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../deprecated-list.html)
  * [Index](../../index-all.html)
  * [Search](../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example](package-summary.html)
  2. [CustomDieTool](CustomDieTool.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. ROLL_DIE_INSTANCE
     2. CHECK_PRIME_INSTANCE
     3. EXAMPLE_TOOL_INSTANCE
  6. Constructor Details
     1. CustomDieTool()
  7. Method Details
     1. rollDie(int, ToolContext)
     2. checkPrime(List)

Hide sidebar  Show sidebar

# Class CustomDieTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.CustomDieTool

* * *

public class CustomDieTool extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Tools for the user-defined config agent demo.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [FunctionTool](../google/adk/tools/FunctionTool.html "class in com.google.adk.tools")`

`CHECK_PRIME_INSTANCE`

 

`static final [ExampleTool](../google/adk/tools/ExampleTool.html "class in com.google.adk.tools")`

`EXAMPLE_TOOL_INSTANCE`

 

`static final [FunctionTool](../google/adk/tools/FunctionTool.html "class in com.google.adk.tools")`

`ROLL_DIE_INSTANCE`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`CustomDieTool()`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`checkPrime([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> nums)`

 

`static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`rollDie(int sides, [ToolContext](../google/adk/tools/ToolContext.html "class in com.google.adk.tools") toolContext)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### ROLL_DIE_INSTANCE

public static final [FunctionTool](../google/adk/tools/FunctionTool.html "class in com.google.adk.tools") ROLL_DIE_INSTANCE

    * ### CHECK_PRIME_INSTANCE

public static final [FunctionTool](../google/adk/tools/FunctionTool.html "class in com.google.adk.tools") CHECK_PRIME_INSTANCE

    * ### EXAMPLE_TOOL_INSTANCE

public static final [ExampleTool](../google/adk/tools/ExampleTool.html "class in com.google.adk.tools") EXAMPLE_TOOL_INSTANCE

  * ## Constructor Details

    * ### CustomDieTool

public CustomDieTool()

  * ## Method Details

    * ### rollDie

public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> rollDie(int sides, [ToolContext](../google/adk/tools/ToolContext.html "class in com.google.adk.tools") toolContext)

    * ### checkPrime

public static [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> checkPrime([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> nums)




* * *

Copyright (C) 1980\. All rights reserved.
