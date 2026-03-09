JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/CodeExecutionUtils.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.codeexecutors](package-summary.html)
  2. [CodeExecutionUtils](CodeExecutionUtils.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. buildCodeExecutionResultPart(CodeExecutionUtils.CodeExecutionResult)
     2. buildExecutableCodePart(String)
     3. convertCodeExecutionParts(Content, List, List)
     4. extractCodeAndTruncateContent(Content.Builder, List)

Hide sidebar  Show sidebar

# Class CodeExecutionUtils

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.codeexecutors.CodeExecutionUtils

* * *

public final class CodeExecutionUtils extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility functions for code execution.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[CodeExecutionUtils.CodeExecutionInput](CodeExecutionUtils.CodeExecutionInput.html "class in com.google.adk.codeexecutors")`

A structure that contains the input of code execution.

`static class `

`[CodeExecutionUtils.CodeExecutionResult](CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors")`

A structure that contains the result of code execution.

`static class `

`[CodeExecutionUtils.File](CodeExecutionUtils.File.html "class in com.google.adk.codeexecutors")`

A structure that contains a file name and its content.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static com.google.genai.types.Part`

`buildCodeExecutionResultPart([CodeExecutionUtils.CodeExecutionResult](CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors") result)`

 

`static com.google.genai.types.Part`

`buildExecutableCodePart([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") code)`

 

`static com.google.genai.types.Content`

`convertCodeExecutionParts(com.google.genai.types.Content content, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> codeBlockDelimiters, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> executionResultDelimiters)`

Converts the code execution parts to text parts in a Content.

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`extractCodeAndTruncateContent(com.google.genai.types.Content.Builder contentBuilder, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> codeBlockDelimiters)`

Extracts the first code block from the content and truncates everything after it.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### buildCodeExecutionResultPart

public static com.google.genai.types.Part buildCodeExecutionResultPart([CodeExecutionUtils.CodeExecutionResult](CodeExecutionUtils.CodeExecutionResult.html "class in com.google.adk.codeexecutors") result)

    * ### buildExecutableCodePart

public static com.google.genai.types.Part buildExecutableCodePart([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") code)

    * ### convertCodeExecutionParts

public static com.google.genai.types.Content convertCodeExecutionParts(com.google.genai.types.Content content, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> codeBlockDelimiters, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> executionResultDelimiters)

Converts the code execution parts to text parts in a Content.

Parameters:
    `content` \- The content to convert.
    `codeBlockDelimiters` \- The delimiters to format the code block.
    `executionResultDelimiters` \- The delimiters to format the code execution result.
Returns:
    The updated content.

    * ### extractCodeAndTruncateContent

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> extractCodeAndTruncateContent(com.google.genai.types.Content.Builder contentBuilder, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>> codeBlockDelimiters)

Extracts the first code block from the content and truncates everything after it.

Parameters:
    `contentBuilder` \- The content builder to extract the code from and modify.
    `codeBlockDelimiters` \- The list of the enclosing delimiters to identify the code blocks.
Returns:
    The extracted code if found.




* * *

Copyright (C) 1980\. All rights reserved.
