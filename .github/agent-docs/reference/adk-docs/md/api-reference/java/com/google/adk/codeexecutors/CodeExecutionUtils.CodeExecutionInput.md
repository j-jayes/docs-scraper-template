JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/CodeExecutionUtils.CodeExecutionInput.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.codeexecutors](package-summary.html)
  2. [CodeExecutionUtils](CodeExecutionUtils.html)
  3. [CodeExecutionInput](CodeExecutionUtils.CodeExecutionInput.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. CodeExecutionInput()
  6. Method Details
     1. code()
     2. inputFiles()
     3. executionId()
     4. builder()

Hide sidebar  Show sidebar

# Class CodeExecutionUtils.CodeExecutionInput

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

com.google.adk.codeexecutors.CodeExecutionUtils.CodeExecutionInput

Enclosing class:
    `[CodeExecutionUtils](CodeExecutionUtils.html "class in com.google.adk.codeexecutors")`

* * *

public abstract static class CodeExecutionUtils.CodeExecutionInput extends [JsonBaseModel](../JsonBaseModel.html "class in com.google.adk")

A structure that contains the input of code execution.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[CodeExecutionUtils.CodeExecutionInput.Builder](CodeExecutionUtils.CodeExecutionInput.Builder.html "class in com.google.adk.codeexecutors")`

Builder for [`CodeExecutionUtils.CodeExecutionInput`](CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors").

  * ## Constructor Summary

Constructors

Constructor

Description

`CodeExecutionInput()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [CodeExecutionUtils.CodeExecutionInput.Builder](CodeExecutionUtils.CodeExecutionInput.Builder.html "class in com.google.adk.codeexecutors")`

`builder()`

 

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`code()`

The code to execute.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`executionId()`

The execution ID for the stateful code execution.

`abstract com.google.common.collect.ImmutableList<[CodeExecutionUtils.File](CodeExecutionUtils.File.html "class in com.google.adk.codeexecutors")>`

`inputFiles()`

The input files available to the code.

### Methods inherited from class [JsonBaseModel](../JsonBaseModel.html#method-summary "class in com.google.adk")

`[fromJsonNode](../JsonBaseModel.html#fromJsonNode\(com.fasterxml.jackson.databind.JsonNode,java.lang.Class\) "fromJsonNode\(JsonNode, Class\)"), [fromJsonString](../JsonBaseModel.html#fromJsonString\(java.lang.String,java.lang.Class\) "fromJsonString\(String, Class\)"), [getMapper](../JsonBaseModel.html#getMapper\(\) "getMapper\(\)"), [toJson](../JsonBaseModel.html#toJson\(\) "toJson\(\)"), [toJsonNode](../JsonBaseModel.html#toJsonNode\(java.lang.Object\) "toJsonNode\(Object\)"), [toJsonString](../JsonBaseModel.html#toJsonString\(java.lang.Object\) "toJsonString\(Object\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### CodeExecutionInput

public CodeExecutionInput()

  * ## Method Details

    * ### code

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") code()

The code to execute.

    * ### inputFiles

public abstract com.google.common.collect.ImmutableList<[CodeExecutionUtils.File](CodeExecutionUtils.File.html "class in com.google.adk.codeexecutors")> inputFiles()

The input files available to the code.

    * ### executionId

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> executionId()

The execution ID for the stateful code execution.

    * ### builder

public static [CodeExecutionUtils.CodeExecutionInput.Builder](CodeExecutionUtils.CodeExecutionInput.Builder.html "class in com.google.adk.codeexecutors") builder()




* * *

Copyright (C) 1980\. All rights reserved.
