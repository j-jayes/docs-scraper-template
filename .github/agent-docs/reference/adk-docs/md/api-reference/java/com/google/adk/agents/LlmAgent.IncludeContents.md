JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/LlmAgent.IncludeContents.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [LlmAgent](LlmAgent.html)
  3. [IncludeContents](LlmAgent.IncludeContents.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Enum Constant Summary
  4. Method Summary
  5. Enum Constant Details
     1. DEFAULT
     2. NONE
  6. Method Details
     1. values()
     2. valueOf(String)

Hide sidebar  Show sidebar

# Enum Class LlmAgent.IncludeContents

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class in java.lang")<[LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")>

com.google.adk.agents.LlmAgent.IncludeContents

All Implemented Interfaces:
    `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "interface in java.io"), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "interface in java.lang")<[LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")>, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html "interface in java.lang.constant")`

Enclosing class:
    `[LlmAgent](LlmAgent.html "class in com.google.adk.agents")`

* * *

public static enum LlmAgent.IncludeContents extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class in java.lang")<[LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")>

Enum to define if contents of previous events should be included in requests to the underlying LLM.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#nested-class-summary "class in java.lang")

`[Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html "class in java.lang")<E>`

  * ## Enum Constant Summary

Enum Constants

Enum Constant

Description

`DEFAULT`

 

`NONE`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")`

`valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Returns the enum constant of this class with the specified name.

`static [LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")[]`

`values()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone\(\) "clone\(\)"), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo\(E\) "compareTo\(LlmAgent.IncludeContents\)"), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable\(\) "describeConstable\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize\(\) "finalize\(\)"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass\(\) "getDeclaringClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode\(\) "hashCode\(\)"), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name\(\) "name\(\)"), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal\(\) "ordinal\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString\(\) "toString\(\)"), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf\(java.lang.Class,java.lang.String\) "valueOf\(Class, String\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Enum Constant Details

    * ### DEFAULT

public static final [LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") DEFAULT

    * ### NONE

public static final [LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") NONE

  * ## Method Details

    * ### values

public static [LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents")[] values()

Returns an array containing the constants of this enum class, in the order they are declared.

Returns:
    an array containing the constants of this enum class, in the order they are declared

    * ### valueOf

public static [LlmAgent.IncludeContents](LlmAgent.IncludeContents.html "enum class in com.google.adk.agents") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

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
