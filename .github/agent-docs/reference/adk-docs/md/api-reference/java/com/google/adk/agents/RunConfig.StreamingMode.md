JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/RunConfig.StreamingMode.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [RunConfig](RunConfig.html)
  3. [StreamingMode](RunConfig.StreamingMode.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Enum Constant Summary
  4. Method Summary
  5. Enum Constant Details
     1. NONE
     2. SSE
     3. BIDI
  6. Method Details
     1. values()
     2. valueOf(String)



# Enum Class RunConfig.StreamingMode

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")>

com.google.adk.agents.RunConfig.StreamingMode

All Implemented Interfaces:
    `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io")`, `[Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "class or interface in java.lang")<[RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")>`, `[Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html "class or interface in java.lang.constant")`

Enclosing class:
    `[RunConfig](RunConfig.html "class in com.google.adk.agents")`

* * *

public static enum RunConfig.StreamingMode extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")>

Streaming mode for the runner. Required for BaseAgent.runLive() to work.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")

`[Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html "class or interface in java.lang")<[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html#type-param-E "class or interface in java.lang") extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[E](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html#type-param-E "class or interface in java.lang")>>`

  * ## Enum Constant Summary

Enum Constants

Enum Constant

Description

`BIDI`

 

`NONE`

 

`SSE`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")`

`valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Returns the enum constant of this class with the specified name.

`static [RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")[]`

`values()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class java.lang.[Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone\(\) "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo\(E\) "class or interface in java.lang"), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize\(\) "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode\(\) "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name\(\) "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString\(\) "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf\(java.lang.Class,java.lang.String\) "class or interface in java.lang")`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Enum Constant Details

    * ### NONE

public static final [RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") NONE

    * ### SSE

public static final [RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") SSE

    * ### BIDI

public static final [RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") BIDI

  * ## Method Details

    * ### values

public static [RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents")[] values()

Returns an array containing the constants of this enum class, in the order they are declared.

Returns:
    an array containing the constants of this enum class, in the order they are declared

    * ### valueOf

public static [RunConfig.StreamingMode](RunConfig.StreamingMode.html "enum class in com.google.adk.agents") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

Returns the enum constant of this class with the specified name. The string must match _exactly_ an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

Parameters:
    `name` \- the name of the enum constant to be returned.
Returns:
    the enum constant with the specified name
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if this enum class has no constant with the specified name
    `[NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html "class or interface in java.lang")` \- if the argument is null




* * *

Copyright (C) 2025\. All rights reserved.
