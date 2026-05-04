JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/CodeExecutorContext.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.codeexecutors](package-summary.html)
  2. [CodeExecutorContext](CodeExecutorContext.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. CodeExecutorContext(Map)
  5. Method Details
     1. getStateDelta()
     2. getExecutionId()
     3. setExecutionId(String)
     4. getProcessedFileNames()
     5. addProcessedFileNames(List)
     6. getInputFiles()
     7. addInputFiles(List)
     8. clearInputFiles()
     9. getErrorCount(String)
     10. incrementErrorCount(String)
     11. resetErrorCount(String)
     12. updateCodeExecutionResult(String, String, String, String)

Hide sidebar  Show sidebar

# Class CodeExecutorContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.codeexecutors.CodeExecutorContext

* * *

public class CodeExecutorContext extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

The persistent context used to configure the code executor.

  * ## Constructor Summary

Constructors

Constructor

Description

`CodeExecutorContext([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> sessionState)`

Initializes the code executor context.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`addInputFiles([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[CodeExecutionUtils.File](CodeExecutionUtils.File.html "class in com.google.adk.codeexecutors")> inputFiles)`

Adds the input files to the code executor context.

`void`

`addProcessedFileNames([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> fileNames)`

Adds the processed file name to the session state.

`void`

`clearInputFiles()`

Removes the input files and processed file names to the code executor context.

`int`

`getErrorCount([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId)`

Gets the error count from the session state.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`getExecutionId()`

Gets the session ID for the code executor.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[CodeExecutionUtils.File](CodeExecutionUtils.File.html "class in com.google.adk.codeexecutors")>`

`getInputFiles()`

Gets the code executor input file names from the session state.

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`getProcessedFileNames()`

Gets the processed file names from the session state.

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`getStateDelta()`

Gets the state delta to update in the persistent session state.

`void`

`incrementErrorCount([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId)`

Increments the error count from the session state.

`void`

`resetErrorCount([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId)`

Resets the error count from the session state.

`void`

`setExecutionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)`

Sets the session ID for the code executor.

`void`

`updateCodeExecutionResult([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") code, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resultStdout, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resultStderr)`

Updates the code execution result.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### CodeExecutorContext

public CodeExecutorContext([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> sessionState)

Initializes the code executor context.

Parameters:
    `sessionState` \- The session state to get the code executor context from.

  * ## Method Details

    * ### getStateDelta

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> getStateDelta()

Gets the state delta to update in the persistent session state.

Returns:
    The state delta to update in the persistent session state.

    * ### getExecutionId

public [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> getExecutionId()

Gets the session ID for the code executor.

Returns:
    The session ID for the code executor context.

    * ### setExecutionId

public void setExecutionId([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)

Sets the session ID for the code executor.

Parameters:
    `sessionId` \- The session ID for the code executor.

    * ### getProcessedFileNames

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> getProcessedFileNames()

Gets the processed file names from the session state.

Returns:
    A list of processed file names in the code executor context.

    * ### addProcessedFileNames

public void addProcessedFileNames([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> fileNames)

Adds the processed file name to the session state.

Parameters:
    `fileNames` \- The processed file names to add to the session state.

    * ### getInputFiles

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[CodeExecutionUtils.File](CodeExecutionUtils.File.html "class in com.google.adk.codeexecutors")> getInputFiles()

Gets the code executor input file names from the session state.

Returns:
    A list of input files in the code executor context.

    * ### addInputFiles

public void addInputFiles([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[CodeExecutionUtils.File](CodeExecutionUtils.File.html "class in com.google.adk.codeexecutors")> inputFiles)

Adds the input files to the code executor context.

Parameters:
    `inputFiles` \- The input files to add to the code executor context.

    * ### clearInputFiles

public void clearInputFiles()

Removes the input files and processed file names to the code executor context.

    * ### getErrorCount

public int getErrorCount([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId)

Gets the error count from the session state.

Parameters:
    `invocationId` \- The invocation ID to get the error count for.
Returns:
    The error count for the given invocation ID.

    * ### incrementErrorCount

public void incrementErrorCount([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId)

Increments the error count from the session state.

Parameters:
    `invocationId` \- The invocation ID to increment the error count for.

    * ### resetErrorCount

public void resetErrorCount([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId)

Resets the error count from the session state.

Parameters:
    `invocationId` \- The invocation ID to reset the error count for.

    * ### updateCodeExecutionResult

public void updateCodeExecutionResult([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") invocationId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") code, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resultStdout, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") resultStderr)

Updates the code execution result.

Parameters:
    `invocationId` \- The invocation ID to update the code execution result for.
    `code` \- The code to execute.
    `resultStdout` \- The standard output of the code execution.
    `resultStderr` \- The standard error of the code execution.




* * *

Copyright (C) 1980\. All rights reserved.
