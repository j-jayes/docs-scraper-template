JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ExitLoopTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.tools](package-summary.html)
  2. [ExitLoopTool](ExitLoopTool.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. INSTANCE
  5. Method Details
     1. exitLoop(ToolContext)

Hide sidebar  Show sidebar

# Class ExitLoopTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.tools.ExitLoopTool

* * *

public final class ExitLoopTool extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Tool for exiting execution of [`LoopAgent`](../agents/LoopAgent.html "class in com.google.adk.agents").

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`INSTANCE`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static void`

`exitLoop([ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Exit the [`LoopAgent`](../agents/LoopAgent.html "class in com.google.adk.agents") execution.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### INSTANCE

public static final [FunctionTool](FunctionTool.html "class in com.google.adk.tools") INSTANCE

  * ## Method Details

    * ### exitLoop

public static void exitLoop([ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Exit the [`LoopAgent`](../agents/LoopAgent.html "class in com.google.adk.agents") execution. 

Usage example in an LlmAgent: 
          
          LlmAgent subAgent = LlmAgent.builder()
              .addTool(ExitLoopTool.INSTANCE)
              .build();
          

The @Schema name and description is consistent with the Python version. 

Refer to: https://github.com/google/adk-python/blob/main/src/google/adk/tools/exit_loop_tool.py




* * *

Copyright (C) 1980\. All rights reserved.
