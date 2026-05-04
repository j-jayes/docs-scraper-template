JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdditionalAdkComponentProvider.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.utils.AdditionalAdkComponentProvider

All Implemented Interfaces:
    `[AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")`

* * *

public final class AdditionalAdkComponentProvider extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")

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

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`getToolInstances()`

Returns tool instances for [`GoogleSearchTool`](../tools/GoogleSearchTool.html "class in com.google.adk.tools") and [`GoogleMapsTool`](../tools/GoogleMapsTool.html "class in com.google.adk.tools").

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>>`

`getToolsetClasses()`

Returns toolset classes for [`McpToolset`](../tools/mcp/McpToolset.html "class in com.google.adk.tools.mcp").

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [AdkComponentProvider](AdkComponentProvider.html#method-summary "interface in com.google.adk.utils")

`[getAgentClasses](AdkComponentProvider.html#getAgentClasses\(\) "getAgentClasses\(\)"), [getToolClasses](AdkComponentProvider.html#getToolClasses\(\) "getToolClasses\(\)")`

Modifier and Type

Method

Description

`default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")>>`

`[getAgentClasses](AdkComponentProvider.html#getAgentClasses\(\))()`

Returns a list of agent classes to register.

`default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>>`

`[getToolClasses](AdkComponentProvider.html#getToolClasses\(\))()`

Returns a list of tool classes to register.




  * ## Constructor Details

    * ### AdditionalAdkComponentProvider

public AdditionalAdkComponentProvider()

  * ## Method Details

    * ### getToolInstances

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> getToolInstances()

Returns tool instances for [`GoogleSearchTool`](../tools/GoogleSearchTool.html "class in com.google.adk.tools") and [`GoogleMapsTool`](../tools/GoogleMapsTool.html "class in com.google.adk.tools").

Specified by:
    `[getToolInstances](AdkComponentProvider.html#getToolInstances\(\))` in interface `[AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")`
Returns:
    a map of tool instances.

    * ### getToolsetClasses

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>> getToolsetClasses()

Returns toolset classes for [`McpToolset`](../tools/mcp/McpToolset.html "class in com.google.adk.tools.mcp").

Specified by:
    `[getToolsetClasses](AdkComponentProvider.html#getToolsetClasses\(\))` in interface `[AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")`
Returns:
    a list of toolset classes.




* * *

Copyright (C) 1980\. All rights reserved.
