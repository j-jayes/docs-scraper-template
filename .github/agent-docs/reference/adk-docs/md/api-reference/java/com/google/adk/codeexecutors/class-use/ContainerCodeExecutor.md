JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../ContainerCodeExecutor.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.codeexecutors](../package-summary.html)
  2. [ContainerCodeExecutor](../ContainerCodeExecutor.html)



# Uses of Class  
com.google.adk.codeexecutors.ContainerCodeExecutor

Packages that use [ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")

Package

Description

com.google.adk.codeexecutors

 

  * ## Uses of [ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors") in [com.google.adk.codeexecutors](../package-summary.html)

Methods in [com.google.adk.codeexecutors](../package-summary.html) that return [ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")

Modifier and Type

Method

Description

`static [ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

ContainerCodeExecutor.`[fromDockerPath](../ContainerCodeExecutor.html#fromDockerPath\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") dockerPath)`

Creates a ContainerCodeExecutor from a Dockerfile path.

`static [ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

ContainerCodeExecutor.`[fromDockerPath](../ContainerCodeExecutor.html#fromDockerPath\(java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") dockerPath)`

Creates a ContainerCodeExecutor from a Dockerfile path.

`static [ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

ContainerCodeExecutor.`[fromImage](../ContainerCodeExecutor.html#fromImage\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") image)`

Creates a ContainerCodeExecutor from an image.

`static [ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

ContainerCodeExecutor.`[fromImage](../ContainerCodeExecutor.html#fromImage\(java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") baseUrl, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") image)`

Creates a ContainerCodeExecutor from an image.

`[ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

ContainerCodeExecutor.`[setExecutionTimeoutSeconds](../ContainerCodeExecutor.html#setExecutionTimeoutSeconds\(long\))(long executionTimeoutSeconds)`

Sets the maximum wall-clock time (in seconds) a single execution may run, in the strict sandbox, before its container is force-removed (killed).

`[ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

ContainerCodeExecutor.`[setMemoryLimitBytes](../ContainerCodeExecutor.html#setMemoryLimitBytes\(long\))(long memoryLimitBytes)`

Sets the per-execution container memory limit, in bytes, used by the strict sandbox.

`[ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

ContainerCodeExecutor.`[setNetworkEnabled](../ContainerCodeExecutor.html#setNetworkEnabled\(boolean\))(boolean networkEnabled)`

Enables or disables container networking when the strict sandbox is on.

`[ContainerCodeExecutor](../ContainerCodeExecutor.html "class in com.google.adk.codeexecutors")`

ContainerCodeExecutor.`[setStrictSandbox](../ContainerCodeExecutor.html#setStrictSandbox\(boolean\))(boolean strictSandbox)`

Enables the strict sandbox.




* * *

Copyright (C) 1980\. All rights reserved.
