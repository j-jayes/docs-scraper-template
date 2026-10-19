JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/RetryConfig.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)
  2. [RetryConfig](RetryConfig.html)
  3. [Builder](RetryConfig.Builder.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. maxAttempts(int)
     2. initialDelay(Duration)
     3. maxDelay(Duration)
     4. backoffFactor(double)
     5. jitter(double)
     6. exceptions(List)
     7. build()

Hide sidebar  Show sidebar

# Class RetryConfig.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.workflow.RetryConfig.Builder

Enclosing class:
    `[RetryConfig](RetryConfig.html "class in com.google.adk.workflow")`

* * *

public abstract static class RetryConfig.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Builder for [`RetryConfig`](RetryConfig.html "class in com.google.adk.workflow").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow")`

`backoffFactor(double backoffFactor)`

 

`final [RetryConfig](RetryConfig.html "class in com.google.adk.workflow")`

`build()`

 

`[RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow")`

`exceptions(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> exceptions)`

 

`abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow")`

`initialDelay([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") initialDelay)`

 

`abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow")`

`jitter(double jitter)`

 

`abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow")`

`maxAttempts(int maxAttempts)`

 

`abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow")`

`maxDelay([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") maxDelay)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### maxAttempts

@CanIgnoreReturnValue public abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow") maxAttempts(int maxAttempts)

    * ### initialDelay

@CanIgnoreReturnValue public abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow") initialDelay([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") initialDelay)

    * ### maxDelay

@CanIgnoreReturnValue public abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow") maxDelay([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") maxDelay)

    * ### backoffFactor

@CanIgnoreReturnValue public abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow") backoffFactor(double backoffFactor)

    * ### jitter

@CanIgnoreReturnValue public abstract [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow") jitter(double jitter)

    * ### exceptions

@CanIgnoreReturnValue public [RetryConfig.Builder](RetryConfig.Builder.html "class in com.google.adk.workflow") exceptions(@Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> exceptions)

    * ### build

public final [RetryConfig](RetryConfig.html "class in com.google.adk.workflow") build()




* * *

Copyright (C) 1980\. All rights reserved.
