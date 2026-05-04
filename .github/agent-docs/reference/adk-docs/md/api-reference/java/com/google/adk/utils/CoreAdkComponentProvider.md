JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/CoreAdkComponentProvider.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.utils](package-summary.html)
  2. [CoreAdkComponentProvider](CoreAdkComponentProvider.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. CoreAdkComponentProvider()
  5. Method Details
     1. getAgentClasses()
     2. getToolClasses()
     3. getToolInstances()

Hide sidebar  Show sidebar

# Class CoreAdkComponentProvider

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.utils.CoreAdkComponentProvider

All Implemented Interfaces:
    `[AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")`

* * *

public class CoreAdkComponentProvider extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")

Provides ADK components that are part of core.

  * ## Constructor Summary

Constructors

Constructor

Description

`CoreAdkComponentProvider()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")>>`

`getAgentClasses()`

Returns agent classes for [`LlmAgent`](../agents/LlmAgent.html "class in com.google.adk.agents"), [`LoopAgent`](../agents/LoopAgent.html "class in com.google.adk.agents"), [`ParallelAgent`](../agents/ParallelAgent.html "class in com.google.adk.agents") and [`SequentialAgent`](../agents/SequentialAgent.html "class in com.google.adk.agents").

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>>`

`getToolClasses()`

Returns tool classes for [`AgentTool`](../tools/AgentTool.html "class in com.google.adk.tools"), [`LongRunningFunctionTool`](../tools/LongRunningFunctionTool.html "class in com.google.adk.tools") and [`ExampleTool`](../tools/ExampleTool.html "class in com.google.adk.tools").

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>`

`getToolInstances()`

Returns tool instances for [`LoadArtifactsTool`](../tools/LoadArtifactsTool.html "class in com.google.adk.tools"), [`ExitLoopTool`](../tools/ExitLoopTool.html "class in com.google.adk.tools") and [`UrlContextTool`](../tools/UrlContextTool.html "class in com.google.adk.tools").

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [AdkComponentProvider](AdkComponentProvider.html#method-summary "interface in com.google.adk.utils")

`[getToolsetClasses](AdkComponentProvider.html#getToolsetClasses\(\) "getToolsetClasses\(\)")`

Modifier and Type

Method

Description

`default [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseToolset](../tools/BaseToolset.html "interface in com.google.adk.tools")>>`

`[getToolsetClasses](AdkComponentProvider.html#getToolsetClasses\(\))()`

Returns a list of toolset classes to register.




  * ## Constructor Details

    * ### CoreAdkComponentProvider

public CoreAdkComponentProvider()

  * ## Method Details

    * ### getAgentClasses

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents")>> getAgentClasses()

Returns agent classes for [`LlmAgent`](../agents/LlmAgent.html "class in com.google.adk.agents"), [`LoopAgent`](../agents/LoopAgent.html "class in com.google.adk.agents"), [`ParallelAgent`](../agents/ParallelAgent.html "class in com.google.adk.agents") and [`SequentialAgent`](../agents/SequentialAgent.html "class in com.google.adk.agents").

Specified by:
    `[getAgentClasses](AdkComponentProvider.html#getAgentClasses\(\))` in interface `[AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")`
Returns:
    a list of agent classes.

    * ### getToolClasses

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<? extends [BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")>> getToolClasses()

Returns tool classes for [`AgentTool`](../tools/AgentTool.html "class in com.google.adk.tools"), [`LongRunningFunctionTool`](../tools/LongRunningFunctionTool.html "class in com.google.adk.tools") and [`ExampleTool`](../tools/ExampleTool.html "class in com.google.adk.tools").

Specified by:
    `[getToolClasses](AdkComponentProvider.html#getToolClasses\(\))` in interface `[AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")`
Returns:
    a list of tool classes.

    * ### getToolInstances

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[BaseTool](../tools/BaseTool.html "class in com.google.adk.tools")> getToolInstances()

Returns tool instances for [`LoadArtifactsTool`](../tools/LoadArtifactsTool.html "class in com.google.adk.tools"), [`ExitLoopTool`](../tools/ExitLoopTool.html "class in com.google.adk.tools") and [`UrlContextTool`](../tools/UrlContextTool.html "class in com.google.adk.tools").

Specified by:
    `[getToolInstances](AdkComponentProvider.html#getToolInstances\(\))` in interface `[AdkComponentProvider](AdkComponentProvider.html "interface in com.google.adk.utils")`
Returns:
    a map of tool instances.




* * *

Copyright (C) 1980\. All rights reserved.
