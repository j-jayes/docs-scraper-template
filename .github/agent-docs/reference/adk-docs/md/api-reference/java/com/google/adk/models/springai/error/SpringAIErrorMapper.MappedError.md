JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/SpringAIErrorMapper.MappedError.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.models.springai.error](package-summary.html)
  2. [SpringAIErrorMapper](SpringAIErrorMapper.html)
  3. [MappedError](SpringAIErrorMapper.MappedError.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. MappedError(SpringAIErrorMapper.ErrorCategory, SpringAIErrorMapper.RetryStrategy, String)
  5. Method Details
     1. getCategory()
     2. getRetryStrategy()
     3. getNormalizedMessage()
     4. isRetryable()
     5. getRetryDelay(int)
     6. toString()

Hide sidebar  Show sidebar

# Class SpringAIErrorMapper.MappedError

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.springai.error.SpringAIErrorMapper.MappedError

Enclosing class:
    `[SpringAIErrorMapper](SpringAIErrorMapper.html "class in com.google.adk.models.springai.error")`

* * *

public static class SpringAIErrorMapper.MappedError extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Container for mapped error information.

  * ## Constructor Summary

Constructors

Constructor

Description

`MappedError([SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") category, [SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") retryStrategy, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") normalizedMessage)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")`

`getCategory()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`getNormalizedMessage()`

 

`long`

`getRetryDelay(int attempt)`

 

`[SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")`

`getRetryStrategy()`

 

`boolean`

`isRetryable()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`toString()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### MappedError

public MappedError([SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") category, [SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") retryStrategy, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") normalizedMessage)

  * ## Method Details

    * ### getCategory

public [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") getCategory()

    * ### getRetryStrategy

public [SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") getRetryStrategy()

    * ### getNormalizedMessage

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getNormalizedMessage()

    * ### isRetryable

public boolean isRetryable()

    * ### getRetryDelay

public long getRetryDelay(int attempt)

    * ### toString

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toString()

Overrides:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang")` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")`




* * *

Copyright (C) 1980\. All rights reserved.
