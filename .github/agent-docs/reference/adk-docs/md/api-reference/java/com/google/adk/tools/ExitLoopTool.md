JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ExitLoopTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.ExitLoopTool

* * *

public final class ExitLoopTool extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




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
