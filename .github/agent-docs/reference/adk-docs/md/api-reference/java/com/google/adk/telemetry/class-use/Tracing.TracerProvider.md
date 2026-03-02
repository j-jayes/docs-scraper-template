JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Tracing.TracerProvider.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.telemetry](../package-summary.html)
  2. [Tracing](../Tracing.html)
  3. [TracerProvider](../Tracing.TracerProvider.html)



# Uses of Class  
com.google.adk.telemetry.Tracing.TracerProvider

Packages that use [Tracing.TracerProvider](../Tracing.TracerProvider.html "class in com.google.adk.telemetry")

Package

Description

com.google.adk.telemetry

 

  * ## Uses of [Tracing.TracerProvider](../Tracing.TracerProvider.html "class in com.google.adk.telemetry") in [com.google.adk.telemetry](../package-summary.html)

Methods in [com.google.adk.telemetry](../package-summary.html) that return [Tracing.TracerProvider](../Tracing.TracerProvider.html "class in com.google.adk.telemetry")

Modifier and Type

Method

Description

`[Tracing.TracerProvider](../Tracing.TracerProvider.html "class in com.google.adk.telemetry")<[T](../Tracing.TracerProvider.html#type-param-T "type parameter in Tracing.TracerProvider")>`

Tracing.TracerProvider.`[configure](../Tracing.TracerProvider.html#configure\(java.util.function.Consumer\))([Consumer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Consumer.html "class or interface in java.util.function")<io.opentelemetry.api.trace.Span> configurer)`

Configures the span created by this transformer.

`[Tracing.TracerProvider](../Tracing.TracerProvider.html "class in com.google.adk.telemetry")<[T](../Tracing.TracerProvider.html#type-param-T "type parameter in Tracing.TracerProvider")>`

Tracing.TracerProvider.`[setParent](../Tracing.TracerProvider.html#setParent\(io.opentelemetry.context.Context\))(io.opentelemetry.context.Context parentContext)`

Sets an explicit parent context for the span created by this transformer.

`static <T> [Tracing.TracerProvider](../Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T>`

Tracing.`[trace](../Tracing.html#trace\(java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") spanName)`

Returns a transformer that traces the execution of an RxJava stream.

`static <T> [Tracing.TracerProvider](../Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T>`

Tracing.`[trace](../Tracing.html#trace\(java.lang.String,io.opentelemetry.context.Context\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") spanName, io.opentelemetry.context.Context parentContext)`

Returns a transformer that traces the execution of an RxJava stream with an explicit parent context.

`static <T> [Tracing.TracerProvider](../Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T>`

Tracing.`[traceAgent](../Tracing.html#traceAgent\(java.lang.String,java.lang.String,java.lang.String,com.google.adk.agents.InvocationContext\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") spanName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentDescription, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Returns a transformer that traces an agent invocation.




* * *

Copyright (C) 1980\. All rights reserved.
