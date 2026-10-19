JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Route.Default.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [Route](Route.html)
  3. [Default](Route.Default.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Enum Constant Summary
  4. Field Summary
  5. Method Summary
  6. Enum Constant Details
     1. INSTANCE
  7. Method Details
     1. values()
     2. valueOf(String)

Hide sidebar  Show sidebar

# Enum Class Route.Default

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class in java.lang")<[Route.Default](Route.Default.html "enum class in com.google.adk.workflow")>

com.google.adk.workflow.Route.Default

All Implemented Interfaces:
    `[Route](Route.html "interface in com.google.adk.workflow"), [Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "interface in java.io"), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "interface in java.lang")<[Route.Default](Route.Default.html "enum class in com.google.adk.workflow")>, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html "interface in java.lang.constant")`

Enclosing interface:
    `[Route](Route.html "interface in com.google.adk.workflow")`

* * *

public static enum Route.Default extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class in java.lang")<[Route.Default](Route.Default.html "enum class in com.google.adk.workflow")> implements [Route](Route.html "interface in com.google.adk.workflow")

The fallback edge, followed when no other routed edge of the node matches what it emitted, including when it emitted no route. A node may declare several, which all fire together, but a default cannot share an edge with a concrete route.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#nested-class-summary "class in java.lang")

`[Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html "class in java.lang")<E>`

### Nested classes/interfaces inherited from interface [Route](Route.html#nested-class-summary "interface in com.google.adk.workflow")

`[Route.Default](Route.Default.html "enum class in com.google.adk.workflow"), [Route.Flag](Route.Flag.html "class in com.google.adk.workflow"), [Route.Num](Route.Num.html "class in com.google.adk.workflow"), [Route.Tag](Route.Tag.html "class in com.google.adk.workflow")`

Modifier and Type

Interface

Description

`static enum `

`[Route.Default](Route.Default.html "enum class in com.google.adk.workflow")`

The fallback edge, followed when no other routed edge of the node matches what it emitted, including when it emitted no route.

`static final record `

`[Route.Flag](Route.Flag.html "class in com.google.adk.workflow")`

A route identified by a boolean, for a two-way branch.

`static final record `

`[Route.Num](Route.Num.html "class in com.google.adk.workflow")`

A route identified by an integer.

`static final record `

`[Route.Tag](Route.Tag.html "class in com.google.adk.workflow")`

A route identified by a string, which is the common case.

  * ## Enum Constant Summary

Enum Constants

Enum Constant

Description

`INSTANCE`

 

  * ## Field Summary

### Fields inherited from interface [Route](Route.html#field-summary "interface in com.google.adk.workflow")

`[DEFAULT_ROUTE_SENTINEL](Route.html#DEFAULT_ROUTE_SENTINEL)`

Modifier and Type

Field

Description

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`[DEFAULT_ROUTE_SENTINEL](Route.html#DEFAULT_ROUTE_SENTINEL)`

The string that stands for [`Route.Default`](Route.Default.html "enum class in com.google.adk.workflow") on the wire.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Route.Default](Route.Default.html "enum class in com.google.adk.workflow")`

`valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Returns the enum constant of this class with the specified name.

`static [Route.Default](Route.Default.html "enum class in com.google.adk.workflow")[]`

`values()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone\(\) "clone\(\)"), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo\(E\) "compareTo\(Route.Default\)"), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable\(\) "describeConstable\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize\(\) "finalize\(\)"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass\(\) "getDeclaringClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode\(\) "hashCode\(\)"), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name\(\) "name\(\)"), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal\(\) "ordinal\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString\(\) "toString\(\)"), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf\(java.lang.Class,java.lang.String\) "valueOf\(Class, String\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Enum Constant Details

    * ### INSTANCE

public static final [Route.Default](Route.Default.html "enum class in com.google.adk.workflow") INSTANCE

  * ## Method Details

    * ### values

public static [Route.Default](Route.Default.html "enum class in com.google.adk.workflow")[] values()

Returns an array containing the constants of this enum class, in the order they are declared.

Returns:
    an array containing the constants of this enum class, in the order they are declared

    * ### valueOf

public static [Route.Default](Route.Default.html "enum class in com.google.adk.workflow") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

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
