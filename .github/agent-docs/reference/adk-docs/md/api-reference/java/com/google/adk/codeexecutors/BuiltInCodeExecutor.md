JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BuiltInCodeExecutor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

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

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`[codeBlockDelimiters](BaseCodeExecutor.html#codeBlockDelimiters\(\))()`

The list of the enclosing delimiters to identify the code blocks.

`int`

`[errorRetryAttempts](BaseCodeExecutor.html#errorRetryAttempts\(\))()`

The number of attempts to retry on consecutive code execution errors.

`com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`[executionResultDelimiters](BaseCodeExecutor.html#executionResultDelimiters\(\))()`

The delimiters to format the code execution result.

`boolean`

`[optimizeDataFile](BaseCodeExecutor.html#optimizeDataFile\(\))()`

If true, extract and process data files from the model request and attach them to the code executor.

`boolean`

`[stateful](BaseCodeExecutor.html#stateful\(\))()`

Whether the code executor is stateful.

### Methods inherited from class [JsonBaseModel](../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

Modifier and Type

Method

Description

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\))(com.fasterxml.jackson.databind.JsonNode jsonNode, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a JsonNode to an object of the given type.

`static <T extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")>  
T`

`[fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") jsonString, [Class](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Class.html "class in java.lang")<T> clazz)`

Deserializes a Json string to an object of the given type.

`static com.fasterxml.jackson.databind.ObjectMapper`

`[getMapper](../JsonBaseModel.html#getMapper\(\))()`

Returns the mutable ObjectMapper instance used by ADK.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJson](../JsonBaseModel.html#toJson\(\))()`

Serializes this object (i.e., the ObjectMappper instance used by ADK) to a Json string.

`protected static com.fasterxml.jackson.databind.JsonNode`

`[toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a JsonNode.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\))([Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") object)`

Serializes an object to a Json string.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




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
