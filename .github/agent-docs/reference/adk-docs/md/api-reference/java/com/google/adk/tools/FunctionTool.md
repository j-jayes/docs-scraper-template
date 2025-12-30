JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/FunctionTool.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [FunctionTool](FunctionTool.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. FunctionTool(Object, Method, boolean)
  5. Method Details
     1. create(Object, Method)
     2. create(Method)
     3. create(Class, String)
     4. create(Object, String)
     5. declaration()
     6. runAsync(Map, ToolContext)



# Class FunctionTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](BaseTool.html "class in com.google.adk.tools")

com.google.adk.tools.FunctionTool

Direct Known Subclasses:
    `[LongRunningFunctionTool](LongRunningFunctionTool.html "class in com.google.adk.tools")`

* * *

public class FunctionTool extends [BaseTool](BaseTool.html "class in com.google.adk.tools")

FunctionTool implements a customized function calling tool.

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

`protected `

`FunctionTool([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func, boolean isLongRunning)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)`

 

`static [FunctionTool](FunctionTool.html "class in com.google.adk.tools")`

`create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func)`

 

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration>`

`declaration()`

Gets the `FunctionDeclaration` representation of this tool.

`io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>>`

`runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Calls a tool.

### Methods inherited from class com.google.adk.tools.[BaseTool](BaseTool.html "class in com.google.adk.tools")

`[description](BaseTool.html#description\(\)), [longRunning](BaseTool.html#longRunning\(\)), [name](BaseTool.html#name\(\)), [processLlmRequest](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### FunctionTool

protected FunctionTool(@Nullable [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func, boolean isLongRunning)

  * ## Method Details

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Method](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/reflect/Method.html "class or interface in java.lang.reflect") func)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class or interface in java.lang")<?> cls, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)

    * ### create

public static [FunctionTool](FunctionTool.html "class in com.google.adk.tools") create([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") instance, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") methodName)

    * ### declaration

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.FunctionDeclaration> declaration()

Description copied from class: `[BaseTool](BaseTool.html#declaration\(\))`

Gets the `FunctionDeclaration` representation of this tool.

Overrides:
    `[declaration](BaseTool.html#declaration\(\))` in class `[BaseTool](BaseTool.html "class in com.google.adk.tools")`

    * ### runAsync

public io.reactivex.rxjava3.core.Single<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>> runAsync([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

Calls a tool.

Overrides:
    `[runAsync](BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))` in class `[BaseTool](BaseTool.html "class in com.google.adk.tools")`




* * *

Copyright (C) 2025\. All rights reserved.
