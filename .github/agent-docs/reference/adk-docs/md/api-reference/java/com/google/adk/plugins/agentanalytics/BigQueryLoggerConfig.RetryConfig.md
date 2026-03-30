JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BigQueryLoggerConfig.RetryConfig.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.plugins.agentanalytics](package-summary.html)
  2. [BigQueryLoggerConfig](BigQueryLoggerConfig.html)
  3. [RetryConfig](BigQueryLoggerConfig.RetryConfig.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. RetryConfig()
  6. Method Details
     1. maxRetries()
     2. initialDelay()
     3. multiplier()
     4. maxDelay()
     5. builder()

Hide sidebar  Show sidebar

# Class BigQueryLoggerConfig.RetryConfig

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.RetryConfig

Enclosing class:
    `[BigQueryLoggerConfig](BigQueryLoggerConfig.html "class in com.google.adk.plugins.agentanalytics")`

* * *

public abstract static class BigQueryLoggerConfig.RetryConfig extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Retry configuration for BigQuery writes.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

Builder for [`BigQueryLoggerConfig.RetryConfig`](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics").

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

`static [BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`builder()`

 

`abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time")`

`initialDelay()`

 

`abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time")`

`maxDelay()`

 

`abstract int`

`maxRetries()`

 

`abstract double`

`multiplier()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### RetryConfig

public RetryConfig()

  * ## Method Details

    * ### maxRetries

public abstract int maxRetries()

    * ### initialDelay

public abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") initialDelay()

    * ### multiplier

public abstract double multiplier()

    * ### maxDelay

public abstract [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") maxDelay()

    * ### builder

public static [BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") builder()




* * *

Copyright (C) 1980\. All rights reserved.
