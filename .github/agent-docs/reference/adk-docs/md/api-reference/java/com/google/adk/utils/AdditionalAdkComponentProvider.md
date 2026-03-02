JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdditionalAdkComponentProvider.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.utils](package-summary.html)
  2. [AdditionalAdkComponentProvider](AdditionalAdkComponentProvider.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. AdditionalAdkComponentProvider()
  5. Method Details
     1. getToolInstances()
     2. getToolsetClasses()

Hide sidebar  Show sidebar

# Class AdditionalAdkComponentProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.utils.AdditionalAdkComponentProvider

All Implemented Interfaces:
    `[AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")`

* * *

public final class AdditionalAdkComponentProvider extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")

Provides ADK components that are part of core.

  * ## Constructor Summary

Constructors

Constructor

Description

`AdditionalAdkComponentProvider()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`getToolInstances()`

Returns tool instances for [`GoogleSearchTool`](../tools/GoogleSearchTool.html "class in com.google.adk.tools") and [`GoogleMapsTool`](../tools/GoogleMapsTool.html "class in com.google.adk.tools").

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>>`

`getToolsetClasses()`

Returns toolset classes for [`McpToolset`](../tools/mcp/McpToolset.html "class in com.google.adk.tools.mcp").

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`

### Methods inherited from interface [AdkComponentProvider](AdkComponentProvider.html#method-summary "interface in com.google.adk.utils")

`[getAgentClasses](AdkComponentProvider.html#getAgentClasses\(\) "getAgentClasses\(\)"), [getToolClasses](AdkComponentProvider.html#getToolClasses\(\) "getToolClasses\(\)")`




  * ## Constructor Details

    * ### AdditionalAdkComponentProvider

public AdditionalAdkComponentProvider()

  * ## Method Details

    * ### getToolInstances

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> getToolInstances()

Returns tool instances for [`GoogleSearchTool`](../tools/GoogleSearchTool.html "class in com.google.adk.tools") and [`GoogleMapsTool`](../tools/GoogleMapsTool.html "class in com.google.adk.tools").

Specified by:
    `[getToolInstances](AdkComponentProvider.html#getToolInstances\(\))` in interface `[AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")`
Returns:
    a map of tool instances.

    * ### getToolsetClasses

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<? extends [BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>> getToolsetClasses()

Returns toolset classes for [`McpToolset`](../tools/mcp/McpToolset.html "class in com.google.adk.tools.mcp").

Specified by:
    `[getToolsetClasses](AdkComponentProvider.html#getToolsetClasses\(\))` in interface `[AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")`
Returns:
    a list of toolset classes.




* * *

Copyright (C) 1980\. All rights reserved.
