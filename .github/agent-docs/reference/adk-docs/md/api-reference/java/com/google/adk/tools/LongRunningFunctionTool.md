JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LongRunningFunctionTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [LongRunningFunctionTool](LongRunningFunctionTool.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. create(Method)
     2. create(Method, boolean)
     3. create(Class, String)
     4. create(Class, String, boolean)
     5. create(Object, String)
     6. create(Object, String, boolean)
     7. create(Object, Method)
     8. create(Object, Method, boolean)
     9. create(FunctionTool)
     10. fromConfig(BaseTool.ToolArgsConfig, String)

Hide sidebar  Show sidebar

# Class LongRunningFunctionTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](BaseTool.html "class in com.google.adk.tools")

[com.google.adk.tools.FunctionTool](FunctionTool.html "class in com.google.adk.tools")

com.google.adk.tools.LongRunningFunctionTool

* * *

public class LongRunningFunctionTool extends [FunctionTool](FunctionTool.html "class in com.google.adk.tools")

A function tool that returns the result asynchronously.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [BaseTool](BaseTool.html#nested-class-summary "class in com.google.adk.tools")

`[BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools"), [BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools")`

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([FunctionTool](FunctionTool.html "class in com.google.adk.tools") tool)`

Creates a LongRunningFunctionTool from a FunctionTool.

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName, boolean requireConfirmation)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") method)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") method, boolean requireConfirmation)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName, boolean requireConfirmation)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func, boolean requireConfirmation)`

 

`static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

`fromConfig([BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)`

 

### Methods inherited from class [FunctionTool](FunctionTool.html#method-summary "class in com.google.adk.tools")

`[callLive](FunctionTool.html#callLive\(java.util.Map,com.google.adk.tools.ToolContext,com.google.adk.agents.InvocationContext\) "callLive\(Map, ToolContext, InvocationContext\)"), [create](FunctionTool.html#create\(java.lang.Class,java.lang.String,boolean,boolean\) "create\(Class, String, boolean, boolean\)"), [create](FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method,boolean,boolean\) "create\(Object, Method, boolean, boolean\)"), [create](FunctionTool.html#create\(java.lang.Object,java.lang.String,boolean,boolean\) "create\(Object, String, boolean, boolean\)"), [create](FunctionTool.html#create\(java.lang.reflect.Method,boolean,boolean\) "create\(Method, boolean, boolean\)"), [declaration](FunctionTool.html#declaration\(\) "declaration\(\)"), [func](FunctionTool.html#func\(\) "func\(\)"), [isStreaming](FunctionTool.html#isStreaming\(\) "isStreaming\(\)"), [runAsync](FunctionTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\) "runAsync\(Map, ToolContext\)")`

### Methods inherited from class [BaseTool](BaseTool.html#method-summary "class in com.google.adk.tools")

`[customMetadata](BaseTool.html#customMetadata\(\) "customMetadata\(\)"), [description](BaseTool.html#description\(\) "description\(\)"), [fromConfig](BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\) "fromConfig\(BaseTool.ToolConfig, String\)"), [longRunning](BaseTool.html#longRunning\(\) "longRunning\(\)"), [name](BaseTool.html#name\(\) "name\(\)"), [processLlmRequest](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\) "processLlmRequest\(LlmRequest.Builder, ToolContext\)"), [setCustomMetadata](BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\) "setCustomMetadata\(String, Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func, boolean requireConfirmation)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName, boolean requireConfirmation)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName, boolean requireConfirmation)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") method)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") method, boolean requireConfirmation)

    * ### create

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") create([FunctionTool](FunctionTool.html "class in com.google.adk.tools") tool)

Creates a LongRunningFunctionTool from a FunctionTool.

    * ### fromConfig

public static [LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools") fromConfig([BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools") config, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") configAbsPath)




* * *

Copyright (C) 1980\. All rights reserved.
