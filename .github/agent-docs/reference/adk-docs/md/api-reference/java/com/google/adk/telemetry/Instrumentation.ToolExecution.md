JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Instrumentation.ToolExecution.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.telemetry](package-summary.html)
  2. [Instrumentation](Instrumentation.html)
  3. [ToolExecution](Instrumentation.ToolExecution.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ToolExecution(BaseTool, BaseAgent, Map, Context)
  6. Method Details
     1. beforeSpanEnd()
     2. recordMetrics(Duration, Throwable)
     3. handleMetricsError(RuntimeException)

Hide sidebar  Show sidebar

# Class Instrumentation.ToolExecution

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.telemetry.Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html "class in com.google.adk.telemetry")

com.google.adk.telemetry.Instrumentation.ToolExecution

All Implemented Interfaces:
    `[AutoCloseable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/AutoCloseable.html "interface in java.lang")`

Enclosing class:
    `[Instrumentation](Instrumentation.html "class in com.google.adk.telemetry")`

* * *

public static final class Instrumentation.ToolExecution extends [Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html "class in com.google.adk.telemetry")

AutoCloseable telemetry tracking scope for tool executions.

  * ## Field Summary

### Fields inherited from class [Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html#field-summary "class in com.google.adk.telemetry")

`[caughtError](Instrumentation.ClosableTelemetryScope.html#caughtError), [closed](Instrumentation.ClosableTelemetryScope.html#closed), [scope](Instrumentation.ClosableTelemetryScope.html#scope), [span](Instrumentation.ClosableTelemetryScope.html#span), [startTimeNanos](Instrumentation.ClosableTelemetryScope.html#startTimeNanos), [telemetryContext](Instrumentation.ClosableTelemetryScope.html#telemetryContext)`

Modifier and Type

Field

Description

`protected @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang")`

`[caughtError](Instrumentation.ClosableTelemetryScope.html#caughtError)`

The error caught during execution, if any.

`protected final [AtomicBoolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/atomic/AtomicBoolean.html "class in java.util.concurrent.atomic")`

`[closed](Instrumentation.ClosableTelemetryScope.html#closed)`

Whether this scope has been closed.

`protected final io.opentelemetry.context.Scope`

`[scope](Instrumentation.ClosableTelemetryScope.html#scope)`

The OpenTelemetry scope associated with this span.

`protected final io.opentelemetry.api.trace.Span`

`[span](Instrumentation.ClosableTelemetryScope.html#span)`

The OpenTelemetry span associated with this scope.

`protected final long`

`[startTimeNanos](Instrumentation.ClosableTelemetryScope.html#startTimeNanos)`

The start time of the scope in nanoseconds.

`protected final [Instrumentation.TelemetryContext](Instrumentation.TelemetryContext.html "class in com.google.adk.telemetry")`

`[telemetryContext](Instrumentation.ClosableTelemetryScope.html#telemetryContext)`

The telemetry context for this scope.

  * ## Constructor Summary

Constructors

Constructor

Description

`ToolExecution([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> functionArgs, io.opentelemetry.context.Context parentContext)`

Constructs a new `ToolExecution` telemetry scope.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`protected void`

`beforeSpanEnd()`

Traces the tool execution attributes on the span before it ends.

`protected void`

`handleMetricsError([RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class in java.lang") e)`

Handles errors that occur while recording metrics for the tool execution.

`protected void`

`recordMetrics([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") elapsed, @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Records metrics for the tool execution including duration, request size, and response size.

### Methods inherited from class [Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html#method-summary "class in com.google.adk.telemetry")

`[close](Instrumentation.ClosableTelemetryScope.html#close\(\) "close\(\)"), [context](Instrumentation.ClosableTelemetryScope.html#context\(\) "context\(\)"), [setError](Instrumentation.ClosableTelemetryScope.html#setError\(java.lang.Throwable\) "setError\(Throwable\)")`

Modifier and Type

Method

Description

`final void`

`[close](Instrumentation.ClosableTelemetryScope.html#close\(\))()`

Closes the scope and ends the underlying span, recording any applicable metrics.

`[Instrumentation.TelemetryContext](Instrumentation.TelemetryContext.html "class in com.google.adk.telemetry")`

`[context](Instrumentation.ClosableTelemetryScope.html#context\(\))()`

Retrieves the telemetry context associated with this scope.

`void`

`[setError](Instrumentation.ClosableTelemetryScope.html#setError\(java.lang.Throwable\))([Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") caughtError)`

Records an error on the span and sets its status to error.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ToolExecution

public ToolExecution([BaseTool](../tools/BaseTool.html "class in com.google.adk.tools") tool, [BaseAgent](../agents/BaseAgent.html "class in com.google.adk.agents") agent, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> functionArgs, io.opentelemetry.context.Context parentContext)

Constructs a new `ToolExecution` telemetry scope.

Parameters:
    `tool` \- The tool being executed.
    `agent` \- The agent invoking the tool.
    `functionArgs` \- The arguments passed to the tool.
    `parentContext` \- The OpenTelemetry parent context.

  * ## Method Details

    * ### beforeSpanEnd

protected void beforeSpanEnd()

Traces the tool execution attributes on the span before it ends.

Overrides:
    `[beforeSpanEnd](Instrumentation.ClosableTelemetryScope.html#beforeSpanEnd\(\))` in class `[Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html "class in com.google.adk.telemetry")`

    * ### recordMetrics

protected void recordMetrics([Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") elapsed, @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)

Records metrics for the tool execution including duration, request size, and response size.

Specified by:
    `[recordMetrics](Instrumentation.ClosableTelemetryScope.html#recordMetrics\(java.time.Duration,java.lang.Throwable\))` in class `[Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html "class in com.google.adk.telemetry")`
Parameters:
    `elapsed` \- The total execution duration.
    `error` \- The exception thrown during execution, if any.

    * ### handleMetricsError

protected void handleMetricsError([RuntimeException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/RuntimeException.html "class in java.lang") e)

Handles errors that occur while recording metrics for the tool execution.

Specified by:
    `[handleMetricsError](Instrumentation.ClosableTelemetryScope.html#handleMetricsError\(java.lang.RuntimeException\))` in class `[Instrumentation.ClosableTelemetryScope](Instrumentation.ClosableTelemetryScope.html "class in com.google.adk.telemetry")`
Parameters:
    `e` \- The runtime exception encountered during metrics recording.




* * *

Copyright (C) 1980\. All rights reserved.
