JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ContainerCodeExecutor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`ContainerCodeExecutor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") image, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dockerPath)`

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

`fromDockerPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dockerPath)`

Creates a ContainerCodeExecutor from a Dockerfile path.

`static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

`fromDockerPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dockerPath)`

Creates a ContainerCodeExecutor from a Dockerfile path.

`static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

`fromImage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") image)`

Creates a ContainerCodeExecutor from an image.

`static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

`fromImage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") image)`

Creates a ContainerCodeExecutor from an image.

`boolean`

`optimizeDataFile()`

If true, extract and process data files from the model request and attach them to the code executor.

`boolean`

`stateful()`

Whether the code executor is stateful.

### Methods inherited from class [BaseCodeExecutor](BaseCodeExecutor.html#method-summary "class in com.google.adk.codeexecutors")

`[codeBlockDelimiters](BaseCodeExecutor.html#codeBlockDelimiters\(\) "codeBlockDelimiters\(\)"), [errorRetryAttempts](BaseCodeExecutor.html#errorRetryAttempts\(\) "errorRetryAttempts\(\)"), [executionResultDelimiters](BaseCodeExecutor.html#executionResultDelimiters\(\) "executionResultDelimiters\(\)")`

### Methods inherited from class [JsonBaseModel](../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### ContainerCodeExecutor

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "class or interface in java.lang") public ContainerCodeExecutor([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") image, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dockerPath)

Deprecated.

Use one of the static factory methods instead.

Initializes the ContainerCodeExecutor. Either dockerPath or image must be set.

  * ## Method Details

    * ### fromImage

public static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors") fromImage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") image)

Creates a ContainerCodeExecutor from an image.

Parameters:
    `baseUrl` \- The base url of the user hosted Docker client.
    `image` \- The tag of the predefined image or custom image to run on the container.

    * ### fromImage

public static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors") fromImage([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") image)

Creates a ContainerCodeExecutor from an image.

Parameters:
    `image` \- The tag of the predefined image or custom image to run on the container.

    * ### fromDockerPath

public static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors") fromDockerPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dockerPath)

Creates a ContainerCodeExecutor from a Dockerfile path.

Parameters:
    `baseUrl` \- The base url of the user hosted Docker client.
    `dockerPath` \- The path to the directory containing the Dockerfile.

    * ### fromDockerPath

public static [ContainerCodeExecutor](ContainerCodeExecutor.html "class in com.google.adk.codeexecutors") fromDockerPath([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") dockerPath)

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
