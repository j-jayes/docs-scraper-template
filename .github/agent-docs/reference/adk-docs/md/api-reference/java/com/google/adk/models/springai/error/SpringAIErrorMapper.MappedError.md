JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/SpringAIErrorMapper.MappedError.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

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

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.springai.error.SpringAIErrorMapper.MappedError

Enclosing class:
    `[SpringAIErrorMapper](SpringAIErrorMapper.html "class in com.google.adk.models.springai.error")`

* * *

public static class SpringAIErrorMapper.MappedError extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Container for mapped error information.

  * ## Constructor Summary

Constructors

Constructor

Description

`MappedError([SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") category, [SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") retryStrategy, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") normalizedMessage)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")`

`getCategory()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getNormalizedMessage()`

 

`long`

`getRetryDelay(int attempt)`

 

`[SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")`

`getRetryStrategy()`

 

`boolean`

`isRetryable()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`toString()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### MappedError

public MappedError([SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") category, [SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") retryStrategy, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") normalizedMessage)

  * ## Method Details

    * ### getCategory

public [SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") getCategory()

    * ### getRetryStrategy

public [SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") getRetryStrategy()

    * ### getNormalizedMessage

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getNormalizedMessage()

    * ### isRetryable

public boolean isRetryable()

    * ### getRetryDelay

public long getRetryDelay(int attempt)

    * ### toString

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toString()

Overrides:
    `[toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\))` in class `[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")`




* * *

Copyright (C) 1980\. All rights reserved.
