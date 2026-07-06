JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Instrumentation.AgentInvocation.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.telemetry](package-summary.html)
  2. [Instrumentation](Instrumentation.html)
  3. [AgentInvocation](Instrumentation.AgentInvocation.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. AgentInvocation(InvocationContext, BaseAgent, Context)
  6. Method Details
     1. getCtx()
     2. addEvent(Event)
     3. recordMetrics(Duration, Throwable)
     4. handleMetricsError(RuntimeException)

Hide sidebar  Show sidebar

# Class Instrumentation.AgentInvocation

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.telemetry.Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html "class in com.google.adk.telemetry")

com.google.adk.telemetry.Instrumentation.AgentInvocation

All Implemented Interfaces:
    `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`

Enclosing class:
    `[Instrumentation](Instrumentation.html "class in com.google.adk.telemetry")`

* * *

public static final class Instrumentation.AgentInvocation extends [Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html "class in com.google.adk.telemetry")

AutoCloseable telemetry tracking scope for agent invocations.

  * ## Field Summary

### Fields inherited from class [Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html#field-summary "class in com.google.adk.telemetry")

`[caughtError](Instrumentation.ClosableTelemetryScope.html#caughtError), [closed](Instrumentation.ClosableTelemetryScope.html#closed), [scope](Instrumentation.ClosableTelemetryScope.html#scope), [span](Instrumentation.ClosableTelemetryScope.html#span), [startTimeNanos](Instrumentation.ClosableTelemetryScope.html#startTimeNanos), [telemetryContext](Instrumentation.ClosableTelemetryScope.html#telemetryContext)`

Modifier and Type

Field

Description

`protected @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang")`

`[caughtError](Instrumentation.ClosableTelemetryScope.html#caughtError)`

 

`protected final [AtomicBoolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html "class in java.util.concurrent.atomic")`

`[closed](Instrumentation.ClosableTelemetryScope.html#closed)`

 

`protected final io.opentelemetry.context.Scope`

`[scope](Instrumentation.ClosableTelemetryScope.html#scope)`

 

`protected final io.opentelemetry.api.trace.Span`

`[span](Instrumentation.ClosableTelemetryScope.html#span)`

 

`protected final long`

`[startTimeNanos](Instrumentation.ClosableTelemetryScope.html#startTimeNanos)`

 

`protected final [Instrumentation.TelemetryContext](Instrumentation.TelemetryContext.html "class in com.google.adk.telemetry")`

`[telemetryContext](Instrumentation.ClosableTelemetryScope.html#telemetryContext)`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`AgentInvocation([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") ctx, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, io.opentelemetry.context.Context parentContext)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`addEvent([Event](../events/Event.html "class in com.google.adk.events") event)`

 

`[InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents")`

`getCtx()`

 

`protected void`

`handleMetricsError([RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class in java.lang") e)`

Hook for subclasses to handle metrics recording errors.

`protected void`

`recordMetrics([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") elapsed, @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Hook for subclasses to record metrics.

### Methods inherited from class [Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html#method-summary "class in com.google.adk.telemetry")

`[beforeSpanEnd](Instrumentation.ClosableTelemetryScope.html#beforeSpanEnd\(\) "beforeSpanEnd\(\)"), [close](Instrumentation.ClosableTelemetryScope.html#close\(\) "close\(\)"), [context](Instrumentation.ClosableTelemetryScope.html#context\(\) "context\(\)"), [setError](Instrumentation.ClosableTelemetryScope.html#setError\(java.lang.Throwable\) "setError\(Throwable\)")`

Modifier and Type

Method

Description

`protected void`

`[beforeSpanEnd](Instrumentation.ClosableTelemetryScope.html#beforeSpanEnd\(\))()`

Hook for subclasses to run code before span ends.

`final void`

`[close](Instrumentation.ClosableTelemetryScope.html#close\(\))()`

 

`[Instrumentation.TelemetryContext](Instrumentation.TelemetryContext.html "class in com.google.adk.telemetry")`

`[context](Instrumentation.ClosableTelemetryScope.html#context\(\))()`

 

`void`

`[setError](Instrumentation.ClosableTelemetryScope.html#setError\(java.lang.Throwable\))([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") caughtError)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### AgentInvocation

public AgentInvocation([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") ctx, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, io.opentelemetry.context.Context parentContext)

  * ## Method Details

    * ### getCtx

public [InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") getCtx()

    * ### addEvent

public void addEvent([Event](../events/Event.html "class in com.google.adk.events") event)

    * ### recordMetrics

protected void recordMetrics([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") elapsed, @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)

Description copied from class: `[Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html#recordMetrics\(java.time.Duration,java.lang.Throwable\))`

Hook for subclasses to record metrics.

Specified by:
    `[recordMetrics](Instrumentation.ClosableTelemetryScope.html#recordMetrics\(java.time.Duration,java.lang.Throwable\))` in class `[Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html "class in com.google.adk.telemetry")`

    * ### handleMetricsError

protected void handleMetricsError([RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class in java.lang") e)

Description copied from class: `[Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html#handleMetricsError\(java.lang.RuntimeException\))`

Hook for subclasses to handle metrics recording errors.

Specified by:
    `[handleMetricsError](Instrumentation.ClosableTelemetryScope.html#handleMetricsError\(java.lang.RuntimeException\))` in class `[Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html "class in com.google.adk.telemetry")`




* * *

Copyright (C) 1980\. All rights reserved.
