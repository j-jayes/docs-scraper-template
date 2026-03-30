JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BigQueryLoggerConfig.RetryConfig.Builder.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.plugins.agentanalytics](package-summary.html)
  2. [BigQueryLoggerConfig](BigQueryLoggerConfig.html)
  3. [RetryConfig](BigQueryLoggerConfig.RetryConfig.html)
  4. [Builder](BigQueryLoggerConfig.RetryConfig.Builder.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Builder()
  5. Method Details
     1. setMaxRetries(int)
     2. setInitialDelay(Duration)
     3. setMultiplier(double)
     4. setMaxDelay(Duration)
     5. build()

Hide sidebar  Show sidebar

# Class BigQueryLoggerConfig.RetryConfig.Builder

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.plugins.agentanalytics.BigQueryLoggerConfig.RetryConfig.Builder

Enclosing class:
    `[BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics")`

* * *

public abstract static class BigQueryLoggerConfig.RetryConfig.Builder extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Builder for [`BigQueryLoggerConfig.RetryConfig`](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics").

  * ## Constructor Summary

Constructors

Constructor

Description

`Builder()`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`abstract [BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics")`

`build()`

 

`abstract [BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setInitialDelay([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") initialDelay)`

 

`abstract [BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setMaxDelay([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") maxDelay)`

 

`abstract [BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setMaxRetries(int maxRetries)`

 

`abstract [BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics")`

`setMultiplier(double multiplier)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Builder

public Builder()

  * ## Method Details

    * ### setMaxRetries

public abstract [BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setMaxRetries(int maxRetries)

    * ### setInitialDelay

public abstract [BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setInitialDelay([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") initialDelay)

    * ### setMultiplier

public abstract [BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setMultiplier(double multiplier)

    * ### setMaxDelay

public abstract [BigQueryLoggerConfig.RetryConfig.Builder](BigQueryLoggerConfig.RetryConfig.Builder.html "class in com.google.adk.plugins.agentanalytics") setMaxDelay([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class or interface in java.time") maxDelay)

    * ### build

public abstract [BigQueryLoggerConfig.RetryConfig](BigQueryLoggerConfig.RetryConfig.html "class in com.google.adk.plugins.agentanalytics") build()




* * *

Copyright (C) 1980\. All rights reserved.
