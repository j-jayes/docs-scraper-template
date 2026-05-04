JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ContainerCodeExecutor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.codeexecutors](package-summary.html)
  2. [ContainerCodeExecutor](ContainerCodeExecutor.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ContainerCodeExecutor(String, String, String)
  5. Method Details
     1. fromImage(String, String)
     2. fromImage(String)
     3. fromDockerPath(String, String)
     4. fromDockerPath(String)
     5. stateful()
     6. optimizeDataFile()
     7. executeCode(InvocationContext, CodeExecutionUtils.CodeExecutionInput)

Hide sidebar  Show sidebar

# Class ContainerCodeExecutor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

[com.google.adk.codeexecutors.BaseCodeExecutor](BaseCodeExecutor.html "class in com.google.adk.codeexecutors")

com.google.adk.codeexecutors.ContainerCodeExecutor

* * *

public class ContainerCodeExecutor extends [BaseCodeExecutor](BaseCodeExecutor.html "class in com.google.adk.codeexecutors")

A code executor that uses a custom container to execute code.

  * ## Constructor Summary

Constructors

Constructor

Description

`ContainerCodeExecutor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") image, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") dockerPath)`

Deprecated.

Use one of the static factory methods instead.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[CodeExecutionUtils.CodeExecutionResult](CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors")`

`executeCode([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [CodeExecutionUtils.CodeExecutionInput](CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors") codeExecutionInput)`

Executes code and return the code execution result.

`static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

`fromDockerPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") dockerPath)`

Creates a ContainerCodeExecutor from a Dockerfile path.

`static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

`fromDockerPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") dockerPath)`

Creates a ContainerCodeExecutor from a Dockerfile path.

`static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

`fromImage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") image)`

Creates a ContainerCodeExecutor from an image.

`static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

`fromImage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") image)`

Creates a ContainerCodeExecutor from an image.

`boolean`

`optimizeDataFile()`

If true, extract and process data files from the model request and attach them to the code executor.

`boolean`

`stateful()`

Whether the code executor is stateful.

### Methods inherited from class [BaseCodeExecutor](BaseCodeExecutor.html#method-summary "class in com.google.adk.codeexecutors")

`[codeBlockDelimiters](BaseCodeExecutor.html#codeBlockDelimiters\(\) "codeBlockDelimiters\(\)"), [errorRetryAttempts](BaseCodeExecutor.html#errorRetryAttempts\(\) "errorRetryAttempts\(\)"), [executionResultDelimiters](BaseCodeExecutor.html#executionResultDelimiters\(\) "executionResultDelimiters\(\)")`

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

    * ### ContainerCodeExecutor

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public ContainerCodeExecutor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") image, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") dockerPath)

Deprecated.

Use one of the static factory methods instead.

Initializes the ContainerCodeExecutor. Either dockerPath or image must be set.

  * ## Method Details

    * ### fromImage

public static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors") fromImage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") image)

Creates a ContainerCodeExecutor from an image.

Parameters:
    `baseUrl` \- The base url of the user hosted Docker client.
    `image` \- The tag of the predefined image or custom image to run on the container.

    * ### fromImage

public static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors") fromImage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") image)

Creates a ContainerCodeExecutor from an image.

Parameters:
    `image` \- The tag of the predefined image or custom image to run on the container.

    * ### fromDockerPath

public static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors") fromDockerPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") dockerPath)

Creates a ContainerCodeExecutor from a Dockerfile path.

Parameters:
    `baseUrl` \- The base url of the user hosted Docker client.
    `dockerPath` \- The path to the directory containing the Dockerfile.

    * ### fromDockerPath

public static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors") fromDockerPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") dockerPath)

Creates a ContainerCodeExecutor from a Dockerfile path.

Parameters:
    `dockerPath` \- The path to the directory containing the Dockerfile.

    * ### stateful

public boolean stateful()

Description copied from class: `[BaseCodeExecutor](BaseCodeExecutor.html#stateful\(\))`

Whether the code executor is stateful. Default to False.

Overrides:
    `[stateful](BaseCodeExecutor.html#stateful\(\))` in class `[BaseCodeExecutor](BaseCodeExecutor.html "class in com.google.adk.codeexecutors")`

    * ### optimizeDataFile

public boolean optimizeDataFile()

Description copied from class: `[BaseCodeExecutor](BaseCodeExecutor.html#optimizeDataFile\(\))`

If true, extract and process data files from the model request and attach them to the code executor. 

Supported data file MimeTypes are [text/csv]. Default to False.

Overrides:
    `[optimizeDataFile](BaseCodeExecutor.html#optimizeDataFile\(\))` in class `[BaseCodeExecutor](BaseCodeExecutor.html "class in com.google.adk.codeexecutors")`

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




* * *

Copyright (C) 1980\. All rights reserved.
