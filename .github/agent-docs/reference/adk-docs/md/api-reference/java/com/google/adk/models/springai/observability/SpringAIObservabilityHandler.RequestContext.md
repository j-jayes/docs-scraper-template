JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/SpringAIObservabilityHandler.RequestContext.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.springai.observability](package-summary.html)
  2. [SpringAIObservabilityHandler](SpringAIObservabilityHandler.html)
  3. [RequestContext](SpringAIObservabilityHandler.RequestContext.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. RequestContext(String, String, Instant, boolean, Timer.Sample)
  5. Method Details
     1. getModelName()
     2. getRequestType()
     3. getStartTime()
     4. isObservable()
     5. getTimerSample()

Hide sidebar  Show sidebar

# Class SpringAIObservabilityHandler.RequestContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.springai.observability.SpringAIObservabilityHandler.RequestContext

Enclosing class:
    `[SpringAIObservabilityHandler](SpringAIObservabilityHandler.html "class in com.google.adk.models.springai.observability")`

* * *

public static class SpringAIObservabilityHandler.RequestContext extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Context for tracking a single request with Micrometer timer.

  * ## Constructor Summary

Constructors

Constructor

Description

`RequestContext([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") requestType, [Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time") startTime, boolean observable, io.micrometer.core.instrument.Timer.Sample timerSample)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getModelName()`

 

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`getRequestType()`

 

`[Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time")`

`getStartTime()`

 

`io.micrometer.core.instrument.Timer.Sample`

`getTimerSample()`

 

`boolean`

`isObservable()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### RequestContext

public RequestContext([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") requestType, [Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time") startTime, boolean observable, io.micrometer.core.instrument.Timer.Sample timerSample)

  * ## Method Details

    * ### getModelName

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getModelName()

    * ### getRequestType

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") getRequestType()

    * ### getStartTime

public [Instant](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Instant.html "class in java.time") getStartTime()

    * ### isObservable

public boolean isObservable()

    * ### getTimerSample

public io.micrometer.core.instrument.Timer.Sample getTimerSample()




* * *

Copyright (C) 1980\. All rights reserved.
