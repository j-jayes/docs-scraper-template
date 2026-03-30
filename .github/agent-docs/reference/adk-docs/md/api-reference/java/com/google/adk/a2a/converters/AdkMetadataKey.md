JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AdkMetadataKey.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.converters](package-summary.html)
  2. [AdkMetadataKey](AdkMetadataKey.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Enum Constant Summary
  4. Method Summary
  5. Enum Constant Details
     1. TASK_ID
     2. CONTEXT_ID
  6. Method Details
     1. values()
     2. valueOf(String)
     3. getType()

Hide sidebar  Show sidebar

# Enum Class AdkMetadataKey

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[AdkMetadataKey](AdkMetadataKey.html "enum class in com.google.adk.a2a.converters")>

com.google.adk.a2a.converters.AdkMetadataKey

All Implemented Interfaces:
    `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io"), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "class or interface in java.lang")<[AdkMetadataKey](AdkMetadataKey.html "enum class in com.google.adk.a2a.converters")>, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html "class or interface in java.lang.constant")`

* * *

public enum AdkMetadataKey extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[AdkMetadataKey](AdkMetadataKey.html "enum class in com.google.adk.a2a.converters")>

Enum for the type of ADK metadata. Adds a prefix used to differentiate A2A-related values stored in custom metadata of an ADK session event.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#nested-class-summary "class or interface in java.lang")

`[Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html "class or interface in java.lang")<E>`

  * ## Enum Constant Summary

Enum Constants

Enum Constant

Description

`CONTEXT_ID`

 

`TASK_ID`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`getType()`

 

`static [AdkMetadataKey](AdkMetadataKey.html "enum class in com.google.adk.a2a.converters")`

`valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Returns the enum constant of this class with the specified name.

`static [AdkMetadataKey](AdkMetadataKey.html "enum class in com.google.adk.a2a.converters")[]`

`values()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone\(\) "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo\(E\) "class or interface in java.lang"), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize\(\) "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode\(\) "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name\(\) "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString\(\) "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf\(java.lang.Class,java.lang.String\) "class or interface in java.lang")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Enum Constant Details

    * ### TASK_ID

public static final [AdkMetadataKey](AdkMetadataKey.html "enum class in com.google.adk.a2a.converters") TASK_ID

    * ### CONTEXT_ID

public static final [AdkMetadataKey](AdkMetadataKey.html "enum class in com.google.adk.a2a.converters") CONTEXT_ID

  * ## Method Details

    * ### values

public static [AdkMetadataKey](AdkMetadataKey.html "enum class in com.google.adk.a2a.converters")[] values()

Returns an array containing the constants of this enum class, in the order they are declared.

Returns:
    an array containing the constants of this enum class, in the order they are declared

    * ### valueOf

public static [AdkMetadataKey](AdkMetadataKey.html "enum class in com.google.adk.a2a.converters") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

Returns the enum constant of this class with the specified name. The string must match _exactly_ an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

Parameters:
    `name` \- the name of the enum constant to be returned.
Returns:
    the enum constant with the specified name
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if this enum class has no constant with the specified name
    `[NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html "class or interface in java.lang")` \- if the argument is null

    * ### getType

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getType()




* * *

Copyright (C) 1980\. All rights reserved.
