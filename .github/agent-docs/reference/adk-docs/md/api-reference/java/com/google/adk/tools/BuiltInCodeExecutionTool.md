JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BuiltInCodeExecutionTool.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [BuiltInCodeExecutionTool](BuiltInCodeExecutionTool.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. BuiltInCodeExecutionTool()
  5. Method Details
     1. processLlmRequest(LlmRequest.Builder, ToolContext)



# Class BuiltInCodeExecutionTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](BaseTool.html "class in com.google.adk.tools")

com.google.adk.tools.BuiltInCodeExecutionTool

* * *

public final class BuiltInCodeExecutionTool extends [BaseTool](BaseTool.html "class in com.google.adk.tools")

A built-in code execution tool that is automatically invoked by Gemini 2 models. 

This tool operates internally within the model and does not require or perform local code execution.

  * ## Constructor Summary

Constructors

Constructor

Description

`BuiltInCodeExecutionTool()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Completable`

`processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models").

### Methods inherited from class com.google.adk.tools.[BaseTool](BaseTool.html "class in com.google.adk.tools")

`[declaration](BaseTool.html#declaration\(\)), [description](BaseTool.html#description\(\)), [longRunning](BaseTool.html#longRunning\(\)), [name](BaseTool.html#name\(\)), [runAsync](BaseTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### BuiltInCodeExecutionTool

public BuiltInCodeExecutionTool()

  * ## Method Details

    * ### processLlmRequest

public io.reactivex.rxjava3.core.Completable processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))`

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models"). 

This implementation adds the current tool's [`BaseTool.declaration()`](BaseTool.html#declaration\(\)) to the `GenerateContentConfig` within the builder. If a tool with function declarations already exists, the current tool's declaration is merged into it. Otherwise, a new tool definition with the current tool's declaration is created. The current tool itself is also added to the builder's internal list of tools. Override this method for processing the outgoing request.

Overrides:
    `[processLlmRequest](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))` in class `[BaseTool](BaseTool.html "class in com.google.adk.tools")`




* * *

Copyright (C) 2025\. All rights reserved.
