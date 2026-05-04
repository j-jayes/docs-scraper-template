JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AgentExecutorConfig.OutputMode.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.a2a.executor](package-summary.html)
  2. [AgentExecutorConfig](AgentExecutorConfig.html)
  3. [OutputMode](AgentExecutorConfig.OutputMode.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Enum Constant Summary
  4. Method Summary
  5. Enum Constant Details
     1. ARTIFACT_PER_RUN
     2. ARTIFACT_PER_EVENT
  6. Method Details
     1. values()
     2. valueOf(String)

Hide sidebar  Show sidebar

# Enum Class AgentExecutorConfig.OutputMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class in java.lang")<[AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor")>

com.google.adk.a2a.executor.AgentExecutorConfig.OutputMode

All Implemented Interfaces:
    `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "interface in java.io"), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "interface in java.lang")<[AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor")>, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html "interface in java.lang.constant")`

Enclosing class:
    `[AgentExecutorConfig](AgentExecutorConfig.html "class in com.google.adk.a2a.executor")`

* * *

public static enum AgentExecutorConfig.OutputMode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class in java.lang")<[AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor")>

Output mode for the agent executor. 

ARTIFACT_PER_RUN: The agent executor will return one artifact per run. 

ARTIFACT_PER_EVENT: The agent executor will return one artifact per event.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#nested-class-summary "class in java.lang")

`[Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html "class in java.lang")<E>`

  * ## Enum Constant Summary

Enum Constants

Enum Constant

Description

`ARTIFACT_PER_EVENT`

 

`ARTIFACT_PER_RUN`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor")`

`valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Returns the enum constant of this class with the specified name.

`static [AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor")[]`

`values()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone\(\) "clone\(\)"), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo\(E\) "compareTo\(AgentExecutorConfig.OutputMode\)"), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable\(\) "describeConstable\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize\(\) "finalize\(\)"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass\(\) "getDeclaringClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode\(\) "hashCode\(\)"), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name\(\) "name\(\)"), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal\(\) "ordinal\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString\(\) "toString\(\)"), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf\(java.lang.Class,java.lang.String\) "valueOf\(Class, String\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Enum Constant Details

    * ### ARTIFACT_PER_RUN

public static final [AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor") ARTIFACT_PER_RUN

    * ### ARTIFACT_PER_EVENT

public static final [AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor") ARTIFACT_PER_EVENT

  * ## Method Details

    * ### values

public static [AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor")[] values()

Returns an array containing the constants of this enum class, in the order they are declared.

Returns:
    an array containing the constants of this enum class, in the order they are declared

    * ### valueOf

public static [AgentExecutorConfig.OutputMode](AgentExecutorConfig.OutputMode.html "enum class in com.google.adk.a2a.executor") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

Returns the enum constant of this class with the specified name. The string must match _exactly_ an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

Parameters:
    `name` \- the name of the enum constant to be returned.
Returns:
    the enum constant with the specified name
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- if this enum class has no constant with the specified name
    `[NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html "class in java.lang")` \- if the argument is null




* * *

Copyright (C) 1980\. All rights reserved.
