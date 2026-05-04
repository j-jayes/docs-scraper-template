JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/SpringAIErrorMapper.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.springai.error](package-summary.html)
  2. [SpringAIErrorMapper](SpringAIErrorMapper.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. SpringAIErrorMapper()
  6. Method Details
     1. mapError(Throwable)
     2. isRetryable(SpringAIErrorMapper.ErrorCategory)
     3. getRetryDelay(SpringAIErrorMapper.RetryStrategy, int)

Hide sidebar  Show sidebar

# Class SpringAIErrorMapper

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.springai.error.SpringAIErrorMapper

* * *

public class SpringAIErrorMapper extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Maps Spring AI exceptions to appropriate ADK exceptions and error handling strategies. 

This class provides: 

  * Exception classification and mapping 
  * Retry strategy recommendations 
  * Error message normalization 
  * Rate limiting detection 


  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static enum `

`[SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error")`

Error categories for different types of failures.

`static class `

`[SpringAIErrorMapper.MappedError](SpringAIErrorMapper.MappedError.html "class in com.google.adk.models.springai.error")`

Container for mapped error information.

`static enum `

`[SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error")`

Retry strategy recommendations.

  * ## Constructor Summary

Constructors

Constructor

Description

`SpringAIErrorMapper()`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static long`

`getRetryDelay([SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") strategy, int attempt)`

Gets the recommended delay before retrying based on the retry strategy.

`static boolean`

`isRetryable([SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") category)`

Determines if an error is retryable based on its category.

`static [SpringAIErrorMapper.MappedError](SpringAIErrorMapper.MappedError.html "class in com.google.adk.models.springai.error")`

`mapError([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") exception)`

Maps a Spring AI exception to an error category and retry strategy.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### SpringAIErrorMapper

public SpringAIErrorMapper()

  * ## Method Details

    * ### mapError

public static [SpringAIErrorMapper.MappedError](SpringAIErrorMapper.MappedError.html "class in com.google.adk.models.springai.error") mapError([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") exception)

Maps a Spring AI exception to an error category and retry strategy.

Parameters:
    `exception` \- the Spring AI exception
Returns:
    mapped error information

    * ### isRetryable

public static boolean isRetryable([SpringAIErrorMapper.ErrorCategory](SpringAIErrorMapper.ErrorCategory.html "enum class in com.google.adk.models.springai.error") category)

Determines if an error is retryable based on its category.

Parameters:
    `category` \- the error category
Returns:
    true if the error is potentially retryable

    * ### getRetryDelay

public static long getRetryDelay([SpringAIErrorMapper.RetryStrategy](SpringAIErrorMapper.RetryStrategy.html "enum class in com.google.adk.models.springai.error") strategy, int attempt)

Gets the recommended delay before retrying based on the retry strategy.

Parameters:
    `strategy` \- the retry strategy
    `attempt` \- the retry attempt number (0-based)
Returns:
    delay in milliseconds




* * *

Copyright (C) 1980\. All rights reserved.
