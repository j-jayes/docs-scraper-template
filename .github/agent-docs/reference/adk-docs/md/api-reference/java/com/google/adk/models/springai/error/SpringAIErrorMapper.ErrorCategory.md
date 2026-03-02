JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/SpringAIErrorMapper.ErrorCategory.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.models.springai.error](package-summary.html)
  2. [SpringAIErrorMapper](SpringAIErrorMapper.html)
  3. [ErrorCategory](SpringAIErrorMapper.ErrorCategory.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Enum Constant Summary
  4. Method Summary
  5. Enum Constant Details
     1. AUTH_ERROR
     2. RATE_LIMITED
     3. NETWORK_ERROR
     4. CLIENT_ERROR
     5. SERVER_ERROR
     6. TIMEOUT_ERROR
     7. MODEL_ERROR
     8. UNKNOWN_ERROR
  6. Method Details
     1. values()
     2. valueOf(String)

Hide sidebar  Show sidebar

# Enum Class SpringAIErrorMapper.ErrorCategory

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[java.lang.Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")>

com.google.adk.models.springai.error.SpringAIErrorMapper.ErrorCategory

All Implemented Interfaces:
    `[Serializable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html "class or interface in java.io"), [Comparable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html "class or interface in java.lang")<[SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")>, [Constable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html "class or interface in java.lang.constant")`

Enclosing class:
    `[SpringAIErrorMapper](SpringAIErrorMapper.html "class in com.google.adk.models.springai.error")`

* * *

public static enum SpringAIErrorMapper.ErrorCategory extends [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html "class or interface in java.lang")<[SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")>

Error categories for different types of failures.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#nested-class-summary "class or interface in java.lang")

`[Enum.EnumDesc](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html "class or interface in java.lang")<E>`

  * ## Enum Constant Summary

Enum Constants

Enum Constant

Description

`AUTH_ERROR`

Authentication or authorization errors

`CLIENT_ERROR`

Invalid request parameters or format

`MODEL_ERROR`

Model-specific errors (model not found, unsupported features)

`NETWORK_ERROR`

Network connectivity issues

`RATE_LIMITED`

Rate limiting or quota exceeded

`SERVER_ERROR`

Server-side errors from the AI provider

`TIMEOUT_ERROR`

Timeout errors

`UNKNOWN_ERROR`

Unknown or unclassified errors

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")`

`valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)`

Returns the enum constant of this class with the specified name.

`static [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")[]`

`values()`

Returns an array containing the constants of this enum class, in the order they are declared.

### Methods inherited from class [Enum](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone\(\) "class or interface in java.lang"), [compareTo](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo\(E\) "class or interface in java.lang"), [describeConstable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize\(\) "class or interface in java.lang"), [getDeclaringClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode\(\) "class or interface in java.lang"), [name](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name\(\) "class or interface in java.lang"), [ordinal](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString\(\) "class or interface in java.lang"), [valueOf](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf\(java.lang.Class,java.lang.String\) "class or interface in java.lang")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Enum Constant Details

    * ### AUTH_ERROR

public static final [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") AUTH_ERROR

Authentication or authorization errors

    * ### RATE_LIMITED

public static final [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") RATE_LIMITED

Rate limiting or quota exceeded

    * ### NETWORK_ERROR

public static final [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") NETWORK_ERROR

Network connectivity issues

    * ### CLIENT_ERROR

public static final [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") CLIENT_ERROR

Invalid request parameters or format

    * ### SERVER_ERROR

public static final [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") SERVER_ERROR

Server-side errors from the AI provider

    * ### TIMEOUT_ERROR

public static final [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") TIMEOUT_ERROR

Timeout errors

    * ### MODEL_ERROR

public static final [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") MODEL_ERROR

Model-specific errors (model not found, unsupported features)

    * ### UNKNOWN_ERROR

public static final [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") UNKNOWN_ERROR

Unknown or unclassified errors

  * ## Method Details

    * ### values

public static [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")[] values()

Returns an array containing the constants of this enum class, in the order they are declared.

Returns:
    an array containing the constants of this enum class, in the order they are declared

    * ### valueOf

public static [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") valueOf([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") name)

Returns the enum constant of this class with the specified name. The string must match _exactly_ an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

Parameters:
    `name` \- the name of the enum constant to be returned.
Returns:
    the enum constant with the specified name
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class or interface in java.lang")` \- if this enum class has no constant with the specified name
    `[NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html "class or interface in java.lang")` \- if the argument is null




* * *

Copyright (C) 1980\. All rights reserved.
