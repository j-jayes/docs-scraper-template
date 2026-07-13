JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Instrumentation.ClosableTelemetryScope.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.telemetry](package-summary.html)
  2. [Instrumentation](Instrumentation.html)
  3. [ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html)



Contents  

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. startTimeNanos
     2. span
     3. scope
     4. telemetryContext
     5. caughtError
     6. closed
  5. Method Details
     1. context()
     2. setError(Throwable)
     3. close()
     4. beforeSpanEnd()
     5. recordMetrics(Duration, Throwable)
     6. handleMetricsError(RuntimeException)

Hide sidebar  Show sidebar

# Class Instrumentation.ClosableTelemetryScope

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.telemetry.Instrumentation.ClosableTelemetryScope

All Implemented Interfaces:
    `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`

Direct Known Subclasses:
    `[Instrumentation.AgentInvocation](Instrumentation.AgentInvocation.html "class in com.google.adk.telemetry"), [Instrumentation.ToolExecution](Instrumentation.ToolExecution.html "class in com.google.adk.telemetry")`

Enclosing class:
    `[Instrumentation](Instrumentation.html "class in com.google.adk.telemetry")`

* * *

public abstract static class Instrumentation.ClosableTelemetryScope extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")

Base class for AutoCloseable telemetry tracking scopes.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`protected @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang")`

`caughtError`

The error caught during execution, if any.

`protected final [AtomicBoolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html "class in java.util.concurrent.atomic")`

`closed`

Whether this scope has been closed.

`protected final io.opentelemetry.context.Scope`

`scope`

The OpenTelemetry scope associated with this span.

`protected final io.opentelemetry.api.trace.Span`

`span`

The OpenTelemetry span associated with this scope.

`protected final long`

`startTimeNanos`

The start time of the scope in nanoseconds.

`protected final [Instrumentation.TelemetryContext](Instrumentation.TelemetryContext.html "class in com.google.adk.telemetry")`

`telemetryContext`

The telemetry context for this scope.

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`protected void`

`beforeSpanEnd()`

Hook for subclasses to run code before span ends.

`final void`

`close()`

Closes the scope and ends the underlying span, recording any applicable metrics.

`[Instrumentation.TelemetryContext](Instrumentation.TelemetryContext.html "class in com.google.adk.telemetry")`

`context()`

Retrieves the telemetry context associated with this scope.

`protected abstract void`

`handleMetricsError([RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class in java.lang") e)`

Hook for subclasses to handle metrics recording errors.

`protected abstract void`

`recordMetrics([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") elapsed, @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Hook for subclasses to record metrics.

`void`

`setError([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") caughtError)`

Records an error on the span and sets its status to error.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### startTimeNanos

protected final long startTimeNanos

The start time of the scope in nanoseconds.

    * ### span

protected final io.opentelemetry.api.trace.Span span

The OpenTelemetry span associated with this scope.

    * ### scope

protected final io.opentelemetry.context.Scope scope

The OpenTelemetry scope associated with this span.

    * ### telemetryContext

protected final [Instrumentation.TelemetryContext](Instrumentation.TelemetryContext.html "class in com.google.adk.telemetry") telemetryContext

The telemetry context for this scope.

    * ### caughtError

protected @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") caughtError

The error caught during execution, if any.

    * ### closed

protected final [AtomicBoolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html "class in java.util.concurrent.atomic") closed

Whether this scope has been closed.

  * ## Method Details

    * ### context

public [Instrumentation.TelemetryContext](Instrumentation.TelemetryContext.html "class in com.google.adk.telemetry") context()

Retrieves the telemetry context associated with this scope.

Returns:
    The [`Instrumentation.TelemetryContext`](Instrumentation.TelemetryContext.html "class in com.google.adk.telemetry").

    * ### setError

public void setError([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") caughtError)

Records an error on the span and sets its status to error.

Parameters:
    `caughtError` \- The throwable caught during execution.

    * ### close

public final void close()

Closes the scope and ends the underlying span, recording any applicable metrics.

Specified by:
    `[close](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html#close\(\))` in interface `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`

    * ### beforeSpanEnd

protected void beforeSpanEnd()

Hook for subclasses to run code before span ends.

    * ### recordMetrics

protected abstract void recordMetrics([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") elapsed, @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)

Hook for subclasses to record metrics.

    * ### handleMetricsError

protected abstract void handleMetricsError([RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class in java.lang") e)

Hook for subclasses to handle metrics recording errors.




* * *

Copyright (C) 1980\. All rights reserved.
