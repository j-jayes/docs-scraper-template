JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BuiltInCodeExecutor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.codeexecutors](package-summary.html)
  2. [BuiltInCodeExecutor](BuiltInCodeExecutor.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. BuiltInCodeExecutor()
  5. Method Details
     1. executeCode(InvocationContext, CodeExecutionUtils.CodeExecutionInput)
     2. processLlmRequest(LlmRequest.Builder)

Hide sidebar  Show sidebar

# Class BuiltInCodeExecutor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

[com.google.adk.codeexecutors.BaseCodeExecutor](BaseCodeExecutor.html "class in com.google.adk.codeexecutors")

com.google.adk.codeexecutors.BuiltInCodeExecutor

* * *

public class BuiltInCodeExecutor extends [BaseCodeExecutor](BaseCodeExecutor.html "class in com.google.adk.codeexecutors")

A code executor that uses the Model's built-in code executor. 

Currently only supports Gemini 2.0+ models, but will be expanded to other models.

  * ## Constructor Summary

Constructors

Constructor

Description

`BuiltInCodeExecutor()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[CodeExecutionUtils.CodeExecutionResult](CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors")`

`executeCode([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [CodeExecutionUtils.CodeExecutionInput](CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors") codeExecutionInput)`

Executes code and return the code execution result.

`void`

`processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder)`

Pre-process the LLM request for Gemini 2.0+ models to use the code execution tool.

### Methods inherited from class [BaseCodeExecutor](BaseCodeExecutor.html#method-summary "class in com.google.adk.codeexecutors")

`[codeBlockDelimiters](BaseCodeExecutor.html#codeBlockDelimiters\(\) "codeBlockDelimiters\(\)"), [errorRetryAttempts](BaseCodeExecutor.html#errorRetryAttempts\(\) "errorRetryAttempts\(\)"), [executionResultDelimiters](BaseCodeExecutor.html#executionResultDelimiters\(\) "executionResultDelimiters\(\)"), [optimizeDataFile](BaseCodeExecutor.html#optimizeDataFile\(\) "optimizeDataFile\(\)"), [stateful](BaseCodeExecutor.html#stateful\(\) "stateful\(\)")`

### Methods inherited from class [JsonBaseModel](../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### BuiltInCodeExecutor

public BuiltInCodeExecutor()

  * ## Method Details

    * ### executeCode

public [CodeExecutionUtils.CodeExecutionResult](CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors") executeCode([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [CodeExecutionUtils.CodeExecutionInput](CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors") codeExecutionInput)

Description copied from class: `[BaseCodeExecutor](BaseCodeExecutor.html#executeCode\(com.google.adk.agents.InvocationContext,com.google.adk.codeexecutors.CodeExecutionUtils.CodeExecutionInput\))`

Executes code and return the code execution result. 

This method may perform blocking operations.

Specified by:
    `[executeCode](BaseCodeExecutor.html#executeCode\(com.google.adk.agents.InvocationContext,com.google.adk.codeexecutors.CodeExecutionUtils.CodeExecutionInput\))` in class `[BaseCodeExecutor](BaseCodeExecutor.html "class in com.google.adk.codeexecutors")`
Parameters:
    `invocationContext` \- The invocation context of the code execution.
    `codeExecutionInput` \- The code execution input.
Returns:
    The code execution result.

    * ### processLlmRequest

public void processLlmRequest([LlmRequest.Builder](../models/LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder)

Pre-process the LLM request for Gemini 2.0+ models to use the code execution tool.




* * *

Copyright (C) 1980\. All rights reserved.
