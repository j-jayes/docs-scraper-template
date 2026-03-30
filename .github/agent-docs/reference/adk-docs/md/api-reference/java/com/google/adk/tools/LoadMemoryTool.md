JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LoadMemoryTool.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.tools](package-summary.html)
  2. [LoadMemoryTool](LoadMemoryTool.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. LoadMemoryTool()
  6. Method Details
     1. loadMemory(String, ToolContext)
     2. processLlmRequest(LlmRequest.Builder, ToolContext)

Hide sidebar  Show sidebar

# Class LoadMemoryTool

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.tools.BaseTool](BaseTool.html "class in com.google.adk.tools")

[com.google.adk.tools.FunctionTool](FunctionTool.html "class in com.google.adk.tools")

com.google.adk.tools.LoadMemoryTool

* * *

public class LoadMemoryTool extends [FunctionTool](FunctionTool.html "class in com.google.adk.tools")

A tool that loads memory for the current user. 

NOTE: Currently this tool only uses text part from the memory.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [BaseTool](BaseTool.html#nested-class-summary "class in com.google.adk.tools")

`[BaseTool.ToolArgsConfig](BaseTool.ToolArgsConfig.html "class in com.google.adk.tools"), [BaseTool.ToolConfig](BaseTool.ToolConfig.html "class in com.google.adk.tools")`

  * ## Constructor Summary

Constructors

Constructor

Description

`LoadMemoryTool()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static io.reactivex.rxjava3.core.Single<[LoadMemoryResponse](LoadMemoryResponse.html "class in com.google.adk.tools")>`

`loadMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") query, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Loads the memory for the current user.

`io.reactivex.rxjava3.core.Completable`

`processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)`

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models").

### Methods inherited from class [FunctionTool](FunctionTool.html#method-summary "class in com.google.adk.tools")

`[callLive](FunctionTool.html#callLive\(java.util.Map,com.google.adk.tools.ToolContext,com.google.adk.agents.InvocationContext\) "callLive\(Map, ToolContext, InvocationContext\)"), [create](FunctionTool.html#create\(java.lang.Class,java.lang.String\) "create\(Class, String\)"), [create](FunctionTool.html#create\(java.lang.Class,java.lang.String,boolean\) "create\(Class, String, boolean\)"), [create](FunctionTool.html#create\(java.lang.Class,java.lang.String,boolean,boolean\) "create\(Class, String, boolean, boolean\)"), [create](FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method\) "create\(Object, Method\)"), [create](FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method,boolean\) "create\(Object, Method, boolean\)"), [create](FunctionTool.html#create\(java.lang.Object,java.lang.reflect.Method,boolean,boolean\) "create\(Object, Method, boolean, boolean\)"), [create](FunctionTool.html#create\(java.lang.Object,java.lang.String\) "create\(Object, String\)"), [create](FunctionTool.html#create\(java.lang.Object,java.lang.String,boolean\) "create\(Object, String, boolean\)"), [create](FunctionTool.html#create\(java.lang.Object,java.lang.String,boolean,boolean\) "create\(Object, String, boolean, boolean\)"), [create](FunctionTool.html#create\(java.lang.reflect.Method\) "create\(Method\)"), [create](FunctionTool.html#create\(java.lang.reflect.Method,boolean\) "create\(Method, boolean\)"), [create](FunctionTool.html#create\(java.lang.reflect.Method,boolean,boolean\) "create\(Method, boolean, boolean\)"), [declaration](FunctionTool.html#declaration\(\) "declaration\(\)"), [func](FunctionTool.html#func\(\) "func\(\)"), [isStreaming](FunctionTool.html#isStreaming\(\) "isStreaming\(\)"), [runAsync](FunctionTool.html#runAsync\(java.util.Map,com.google.adk.tools.ToolContext\) "runAsync\(Map, ToolContext\)")`

### Methods inherited from class [BaseTool](BaseTool.html#method-summary "class in com.google.adk.tools")

`[customMetadata](BaseTool.html#customMetadata\(\) "customMetadata\(\)"), [description](BaseTool.html#description\(\) "description\(\)"), [fromConfig](BaseTool.html#fromConfig\(com.google.adk.tools.BaseTool.ToolConfig,java.lang.String\) "fromConfig\(BaseTool.ToolConfig, String\)"), [longRunning](BaseTool.html#longRunning\(\) "longRunning\(\)"), [name](BaseTool.html#name\(\) "name\(\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, TypeReference\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,com.fasterxml.jackson.core.type.TypeReference\) "runAsync\(I, ToolContext, ObjectMapper, TypeReference\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper,java.lang.Class\) "runAsync\(I, ToolContext, ObjectMapper, Class\)"), [runAsync](BaseTool.html#runAsync\(I,com.google.adk.tools.ToolContext,java.lang.Class\) "runAsync\(I, ToolContext, Class\)"), [runAsync](BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext\) "runAsync\(T, ToolContext\)"), [runAsync](BaseTool.html#runAsync\(T,com.google.adk.tools.ToolContext,com.fasterxml.jackson.databind.ObjectMapper\) "runAsync\(T, ToolContext, ObjectMapper\)"), [setCustomMetadata](BaseTool.html#setCustomMetadata\(java.lang.String,java.lang.Object\) "setCustomMetadata\(String, Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### LoadMemoryTool

public LoadMemoryTool()

  * ## Method Details

    * ### loadMemory

public static io.reactivex.rxjava3.core.Single<[LoadMemoryResponse](LoadMemoryResponse.html "class in com.google.adk.tools")> loadMemory([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") query, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Loads the memory for the current user.

Parameters:
    `query` \- The query to load memory for.
Returns:
    A list of memory results.

    * ### processLlmRequest

public io.reactivex.rxjava3.core.Completable processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder, [ToolContext](ToolContext.html "class in com.google.adk.tools") toolContext)

Description copied from class: `[BaseTool](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))`

Processes the outgoing [`LlmRequest.Builder`](../models/LlmRequest.Builder.html "class in com.google.adk.models"). 

This implementation adds the current tool's [`BaseTool.declaration()`](BaseTool.html#declaration\(\)) to the `GenerateContentConfig` within the builder. If a tool with function declarations already exists, the current tool's declaration is merged into it. Otherwise, a new tool definition with the current tool's declaration is created. The current tool itself is also added to the builder's internal list of tools. Override this method for processing the outgoing request.

Overrides:
    `[processLlmRequest](BaseTool.html#processLlmRequest\(com.google.adk.models.LlmRequest.Builder,com.google.adk.tools.ToolContext\))` in class `[BaseTool](BaseTool.html "class in com.google.adk.tools")`




* * *

Copyright (C) 1980\. All rights reserved.
