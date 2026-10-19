JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/RetryConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [RetryConfig](RetryConfig.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Field Summary
  4. Constructor Summary
  5. Method Summary
  6. Field Details
     1. DEFAULT_MAX_ATTEMPTS
     2. DEFAULT_INITIAL_DELAY
     3. DEFAULT_MAX_DELAY
     4. DEFAULT_BACKOFF_FACTOR
     5. DEFAULT_JITTER
  7. Constructor Details
     1. RetryConfig()
  8. Method Details
     1. maxAttempts()
     2. initialDelay()
     3. maxDelay()
     4. backoffFactor()
     5. jitter()
     6. exceptions()
     7. builder()
     8. toBuilder()

Hide sidebar  Show sidebar

# Class RetryConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.workflow.RetryConfig

* * *

[@Experimental](../annotations/Experimental.html "annotation interface in com.google.adk.annotations") public abstract class RetryConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

How a node is retried when it fails. The builder initializes each property to its ` DEFAULT_` constant, except `exceptions()`, which starts unset.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow")`

Builder for [`RetryConfig`](RetryConfig.html "class in com.google.adk.workflow").

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final double`

`DEFAULT_BACKOFF_FACTOR`

The default for `backoffFactor()`.

`static final [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")`

`DEFAULT_INITIAL_DELAY`

The default for `initialDelay()`.

`static final double`

`DEFAULT_JITTER`

The default for `jitter()`.

`static final int`

`DEFAULT_MAX_ATTEMPTS`

The default for `maxAttempts()`.

`static final [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")`

`DEFAULT_MAX_DELAY`

The default for `maxDelay()`.

  * ## Constructor Summary

Constructors

Constructor

Description

`RetryConfig()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract double`

`backoffFactor()`

Returns the multiplier applied to the delay after each attempt.

`static [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow")`

`builder()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`exceptions()`

Returns the simple type names of the failures to retry on, matched exactly with no subclass match.

`abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")`

`initialDelay()`

Returns the delay before the first retry.

`abstract double`

`jitter()`

Returns the randomness factor, not a duration: the delay is spread over `delay * (1 +/- jitter)`.

`abstract int`

`maxAttempts()`

Returns the maximum number of attempts, including the first, so 0 or 1 means no retry.

`abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time")`

`maxDelay()`

Returns the ceiling on any single delay.

`abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow")`

`toBuilder()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### DEFAULT_MAX_ATTEMPTS

public static final int DEFAULT_MAX_ATTEMPTS

The default for `maxAttempts()`.

See Also:
    
      * [Constant Field Values](../../../../constant-values.html#com.google.adk.workflow.RetryConfig.DEFAULT_MAX_ATTEMPTS)

    * ### DEFAULT_INITIAL_DELAY

public static final [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") DEFAULT_INITIAL_DELAY

The default for `initialDelay()`.

    * ### DEFAULT_MAX_DELAY

public static final [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") DEFAULT_MAX_DELAY

The default for `maxDelay()`.

    * ### DEFAULT_BACKOFF_FACTOR

public static final double DEFAULT_BACKOFF_FACTOR

The default for `backoffFactor()`.

See Also:
    
      * [Constant Field Values](../../../../constant-values.html#com.google.adk.workflow.RetryConfig.DEFAULT_BACKOFF_FACTOR)

    * ### DEFAULT_JITTER

public static final double DEFAULT_JITTER

The default for `jitter()`.

See Also:
    
      * [Constant Field Values](../../../../constant-values.html#com.google.adk.workflow.RetryConfig.DEFAULT_JITTER)

  * ## Constructor Details

    * ### RetryConfig

public RetryConfig()

  * ## Method Details

    * ### maxAttempts

public abstract int maxAttempts()

Returns the maximum number of attempts, including the first, so 0 or 1 means no retry.

    * ### initialDelay

public abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") initialDelay()

Returns the delay before the first retry.

    * ### maxDelay

public abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") maxDelay()

Returns the ceiling on any single delay.

    * ### backoffFactor

public abstract double backoffFactor()

Returns the multiplier applied to the delay after each attempt.

    * ### jitter

public abstract double jitter()

Returns the randomness factor, not a duration: the delay is spread over `delay * (1 +/- jitter)`. Zero removes randomness.

    * ### exceptions

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> exceptions()

Returns the simple type names of the failures to retry on, matched exactly with no subclass match. When unset, any failure is retried; an empty list retries none.

    * ### builder

public static [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow") builder()

    * ### toBuilder

public abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow") toBuilder()




* * *

Copyright (C) 1980\. All rights reserved.
