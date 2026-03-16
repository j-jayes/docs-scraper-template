JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseCodeExecutor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.codeexecutors](package-summary.html)
  2. [BaseCodeExecutor](BaseCodeExecutor.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. BaseCodeExecutor()
  5. Method Details
     1. optimizeDataFile()
     2. stateful()
     3. errorRetryAttempts()
     4. codeBlockDelimiters()
     5. executionResultDelimiters()
     6. executeCode(InvocationContext, CodeExecutionUtils.CodeExecutionInput)

Hide sidebar  Show sidebar

# Class BaseCodeExecutor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

com.google.adk.codeexecutors.BaseCodeExecutor

Direct Known Subclasses:
    `[BuiltInCodeExecutor](BuiltInCodeExecutor.html "class in com.google.adk.codeexecutors"), [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors"), [VertexAiCodeExecutor](VertexAiCodeExecutor.html "class in com.google.adk.codeexecutors")`

* * *

public abstract class BaseCodeExecutor extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

Abstract base class for all code executors. 

The code executor allows the agent to execute code blocks from model responses and incorporate the execution results into the final response.

  * ## Constructor Summary

Constructors

Constructor

Description

`BaseCodeExecutor()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>>`

`codeBlockDelimiters()`

The list of the enclosing delimiters to identify the code blocks.

`int`

`errorRetryAttempts()`

The number of attempts to retry on consecutive code execution errors.

`abstract [CodeExecutionUtils.CodeExecutionResult](CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors")`

`executeCode([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [CodeExecutionUtils.CodeExecutionInput](CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors") codeExecutionInput)`

Executes code and return the code execution result.

`com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`executionResultDelimiters()`

The delimiters to format the code execution result.

`boolean`

`optimizeDataFile()`

If true, extract and process data files from the model request and attach them to the code executor.

`boolean`

`stateful()`

Whether the code executor is stateful.

### Methods inherited from class [JsonBaseModel](../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### BaseCodeExecutor

public BaseCodeExecutor()

  * ## Method Details

    * ### optimizeDataFile

public boolean optimizeDataFile()

If true, extract and process data files from the model request and attach them to the code executor. 

Supported data file MimeTypes are [text/csv]. Default to False.

    * ### stateful

public boolean stateful()

Whether the code executor is stateful. Default to False.

    * ### errorRetryAttempts

public int errorRetryAttempts()

The number of attempts to retry on consecutive code execution errors. 

Default to 2.

    * ### codeBlockDelimiters

public com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> codeBlockDelimiters()

The list of the enclosing delimiters to identify the code blocks. 

Each inner list contains a pair of start and end delimiters. This supports multiple pairs of delimiters. 

For example, the delimiter ('```python\n', '\n```') can be used to identify code blocks with the following format: 

```python 

print("hello") 

```

    * ### executionResultDelimiters

public com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> executionResultDelimiters()

The delimiters to format the code execution result.

    * ### executeCode

public abstract [CodeExecutionUtils.CodeExecutionResult](CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors") executeCode([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [CodeExecutionUtils.CodeExecutionInput](CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors") codeExecutionInput)

Executes code and return the code execution result. 

This method may perform blocking operations.

Parameters:
    `invocationContext` \- The invocation context of the code execution.
    `codeExecutionInput` \- The code execution input.
Returns:
    The code execution result.




* * *

Copyright (C) 1980\. All rights reserved.
