JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/AdkComponentProvider.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.utils](package-summary.html)
  2. [AdkComponentProvider](AdkComponentProvider.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. getAgentClasses()
     2. getToolClasses()
     3. getToolsetClasses()
     4. getToolInstances()

Hide sidebar  Show sidebar

# Interface AdkComponentProvider

All Known Implementing Classes:
    `[AdditionalAdkComponentProvider](AdditionalAdkComponentProvider.html "class in com.google.adk.utils"), [CoreAdkComponentProvider](CoreAdkComponentProvider.html "class in com.google.adk.utils")`

* * *

public interface AdkComponentProvider

Service provider interface for ADK components to be registered in [`ComponentRegistry`](ComponentRegistry.html "class in com.google.adk.utils").

  * ## Method Summary

All MethodsInstance MethodsDefault Methods

Modifier and Type

Method

Description

`default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")>>`

`getAgentClasses()`

Returns a list of agent classes to register.

`default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>>`

`getToolClasses()`

Returns a list of tool classes to register.

`default [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`getToolInstances()`

Returns a map of tool instances to register, with tool name as key.

`default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>>`

`getToolsetClasses()`

Returns a list of toolset classes to register.




  * ## Method Details

    * ### getAgentClasses

default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")>> getAgentClasses()

Returns a list of agent classes to register.

Returns:
    a list of agent classes.

    * ### getToolClasses

default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>> getToolClasses()

Returns a list of tool classes to register.

Returns:
    a list of tool classes.

    * ### getToolsetClasses

default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>> getToolsetClasses()

Returns a list of toolset classes to register.

Returns:
    a list of toolset classes.

    * ### getToolInstances

default [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> getToolInstances()

Returns a map of tool instances to register, with tool name as key.

Returns:
    a map of tool instances.




* * *

Copyright (C) 1980\. All rights reserved.
