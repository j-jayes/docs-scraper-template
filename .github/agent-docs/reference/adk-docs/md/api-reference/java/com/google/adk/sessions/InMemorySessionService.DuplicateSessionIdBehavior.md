JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/InMemorySessionService.DuplicateSessionIdBehavior.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.sessions](package-summary.html)
  2. [InMemorySessionService](InMemorySessionService.html)
  3. [DuplicateSessionIdBehavior](InMemorySessionService.DuplicateSessionIdBehavior.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Enum Constant Summary
  4. Method Summary
  5. Enum Constant Details
     1. OVERWRITE
     2. REJECT
  6. Method Details
     1. values()
     2. valueOf(String)

Hide sidebar  Show sidebar

# Enum Class InMemorySessionService.DuplicateSessionIdBehavior

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class in java.lang")<[InMemorySessionService.DuplicateSessionIdBehavior](InMemorySessionService.DuplicateSessionIdBehavior.html "enum class in com.google.adk.sessions")>

com.google.adk.sessions.InMemorySessionService.DuplicateSessionIdBehavior

All Implemented Interfaces:
    `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "interface in java.io"), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "interface in java.lang")<[InMemorySessionService.DuplicateSessionIdBehavior](InMemorySessionService.DuplicateSessionIdBehavior.html "enum class in com.google.adk.sessions")>, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html "interface in java.lang.constant")`

Enclosing class:
    `[InMemorySessionService](InMemorySessionService.html "class in com.google.adk.sessions")`

* * *

public static enum InMemorySessionService.DuplicateSessionIdBehavior extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class in java.lang")<[InMemorySessionService.DuplicateSessionIdBehavior](InMemorySessionService.DuplicateSessionIdBehavior.html "enum class in com.google.adk.sessions")>

What `createSession` does when `sessionId` is already in use.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#nested-class-summary "class in java.lang")

`[Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html "class in java.lang")<E>`

  * ## Enum Constant Summary

Enum Constants

Enum Constant

Description

`OVERWRITE`

Deprecated.

Construct the service with `REJECT` instead, which becomes the default in a future release.

`REJECT`

Rejects the call with [`SessionException`](SessionException.html "class in com.google.adk.sessions").

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [InMemorySessionService.DuplicateSessionIdBehavior](InMemorySessionService.DuplicateSessionIdBehavior.html "enum class in com.google.adk.sessions")`

`valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)`

Returns the enum constant of this class with the specified name.

`static [InMemorySessionService.DuplicateSessionIdBehavior](InMemorySessionService.DuplicateSessionIdBehavior.html "enum class in com.google.adk.sessions")[]`

`values()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone\(\) "clone\(\)"), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo\(E\) "compareTo\(InMemorySessionService.DuplicateSessionIdBehavior\)"), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable\(\) "describeConstable\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize\(\) "finalize\(\)"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass\(\) "getDeclaringClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode\(\) "hashCode\(\)"), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name\(\) "name\(\)"), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal\(\) "ordinal\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString\(\) "toString\(\)"), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf\(java.lang.Class,java.lang.String\) "valueOf\(Class, String\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Enum Constant Details

    * ### OVERWRITE

[@Deprecated](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html "annotation interface in java.lang") public static final [InMemorySessionService.DuplicateSessionIdBehavior](InMemorySessionService.DuplicateSessionIdBehavior.html "enum class in com.google.adk.sessions") OVERWRITE

Deprecated.

Construct the service with `REJECT` instead, which becomes the default in a future release.

Replaces the stored session, discarding its events and state.

    * ### REJECT

public static final [InMemorySessionService.DuplicateSessionIdBehavior](InMemorySessionService.DuplicateSessionIdBehavior.html "enum class in com.google.adk.sessions") REJECT

Rejects the call with [`SessionException`](SessionException.html "class in com.google.adk.sessions"). Becomes the default in a future release.

  * ## Method Details

    * ### values

public static [InMemorySessionService.DuplicateSessionIdBehavior](InMemorySessionService.DuplicateSessionIdBehavior.html "enum class in com.google.adk.sessions")[] values()

Returns an array containing the constants of this enum class, in the order they are declared.

Returns:
    an array containing the constants of this enum class, in the order they are declared

    * ### valueOf

public static [InMemorySessionService.DuplicateSessionIdBehavior](InMemorySessionService.DuplicateSessionIdBehavior.html "enum class in com.google.adk.sessions") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") name)

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
