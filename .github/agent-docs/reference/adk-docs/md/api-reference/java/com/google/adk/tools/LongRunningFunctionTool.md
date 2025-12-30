JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LongRunningFunctionTool.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [LongRunningFunctionTool](LongRunningFunctionTool.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. create(Method)
     2. create(Class, String)
     3. create(Object, String)



# Class LongRunningFunctionTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](BaseTool.html "class in com.google.adk.tools")

[com.google.adk.tools.FunctionTool](FunctionTool.html "class in com.google.adk.tools")

com.google.adk.tools.LongRunningFunctionTool

* * *

public class LongRunningFunctionTool extends [FunctionTool](FunctionTool.html "class in com.google.adk.tools")

A function tool that returns the result asynchronously.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func)`

 

### Methods inherited from class com.google.adk.tools.[FunctionTool](FunctionTool.html "class in com.google.adk.tools")

`[create](FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method\)), [declaration](FunctionTool.html#declaration\(\)), [runAsync](FunctionTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

### Methods inherited from class com.google.adk.tools.[BaseTool](BaseTool.html "class in com.google.adk.tools")

`[description](BaseTool.html#description\(\)), [longRunning](BaseTool.html#longRunning\(\)), [name](BaseTool.html#name\(\)), [processLlmRequest](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)




* * *

Copyright (C) 2025\. All rights reserved.
