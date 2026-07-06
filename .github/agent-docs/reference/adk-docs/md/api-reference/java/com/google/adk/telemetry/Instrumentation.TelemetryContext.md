JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Instrumentation.TelemetryContext.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.telemetry](package-summary.html)
  2. [Instrumentation](Instrumentation.html)
  3. [TelemetryContext](Instrumentation.TelemetryContext.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. TelemetryContext(Context)
  5. Method Details
     1. otelContext()
     2. functionResponseEvent()
     3. setFunctionResponseEvent(Event)

Hide sidebar  Show sidebar

# Class Instrumentation.TelemetryContext

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.telemetry.Instrumentation.TelemetryContext

Enclosing class:
    `[Instrumentation](Instrumentation.html "class in com.google.adk.telemetry")`

* * *

public static final class Instrumentation.TelemetryContext extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Stores all telemetry related state.

  * ## Constructor Summary

Constructors

Constructor

Description

`TelemetryContext(io.opentelemetry.context.Context otelContext)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`@Nullable [Event](../events/Event.html "class in com.google.adk.events")`

`functionResponseEvent()`

 

`io.opentelemetry.context.Context`

`otelContext()`

 

`void`

`setFunctionResponseEvent(@Nullable [Event](../events/Event.html "class in com.google.adk.events") functionResponseEvent)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### TelemetryContext

public TelemetryContext(io.opentelemetry.context.Context otelContext)

  * ## Method Details

    * ### otelContext

public io.opentelemetry.context.Context otelContext()

    * ### functionResponseEvent

public @Nullable [Event](../events/Event.html "class in com.google.adk.events") functionResponseEvent()

    * ### setFunctionResponseEvent

public void setFunctionResponseEvent(@Nullable [Event](../events/Event.html "class in com.google.adk.events") functionResponseEvent)




* * *

Copyright (C) 1980\. All rights reserved.
