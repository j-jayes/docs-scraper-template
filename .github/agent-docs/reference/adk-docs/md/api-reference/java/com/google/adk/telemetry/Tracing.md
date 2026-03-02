JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Tracing.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.telemetry](package-summary.html)
  2. [Tracing](Tracing.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. setTracerForTesting(Tracer)
     2. traceAgentInvocation(Span, String, String, InvocationContext)
     3. traceToolCall(String, String, String, Map)
     4. traceToolResponse(String, Event)
     5. traceCallLlm(InvocationContext, String, LlmRequest, LlmResponse)
     6. traceSendData(InvocationContext, String, List)
     7. getTracer()
     8. traceFlowable(Context, Span, Supplier)
     9. trace(String)
     10. trace(String, Context)
     11. traceAgent(String, String, String, InvocationContext)

Hide sidebar  Show sidebar

# Class Tracing

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.telemetry.Tracing

* * *

public class Tracing extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility class for capturing and reporting telemetry data within the ADK. This class provides methods to trace various aspects of the agent's execution, including tool calls, tool responses, LLM interactions, and data handling. It leverages OpenTelemetry for tracing and logging for detailed information. These traces can then be exported through the ADK Dev Server UI.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static final class `

`[Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<[T](Tracing.TracerProvider.html#type-param-T "type parameter in Tracing.TracerProvider")>`

A transformer that manages an OpenTelemetry span and scope for RxJava streams.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static io.opentelemetry.api.trace.Tracer`

`getTracer()`

Gets the tracer.

`static void`

`setTracerForTesting(io.opentelemetry.api.trace.Tracer tracer)`

Sets the OpenTelemetry instance to be used for tracing.

`static <T> [Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T>`

`trace([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") spanName)`

Returns a transformer that traces the execution of an RxJava stream.

`static <T> [Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T>`

`trace([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") spanName, io.opentelemetry.context.Context parentContext)`

Returns a transformer that traces the execution of an RxJava stream with an explicit parent context.

`static <T> [Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T>`

`traceAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") spanName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentDescription, [InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Returns a transformer that traces an agent invocation.

`static void`

`traceAgentInvocation(io.opentelemetry.api.trace.Span span, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentDescription, [InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Sets span attributes immediately available on agent invocation according to OTEL semconv version 1.37.

`static void`

`traceCallLlm([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [LlmRequest](../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Traces a call to the LLM.

`static <T> io.reactivex.rxjava3.core.Flowable<T>`

`traceFlowable(io.opentelemetry.context.Context spanContext, io.opentelemetry.api.trace.Span span, [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html "class or interface in java.util.function")<io.reactivex.rxjava3.core.Flowable<T>> flowableSupplier)`

Executes a Flowable with an OpenTelemetry Scope active for its entire lifecycle.

`static void`

`traceSendData([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> data)`

Traces the sending of data (history or new content) to the agent/model.

`static void`

`traceToolCall([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolDescription, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolType, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args)`

Traces tool call arguments.

`static void`

`traceToolResponse([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [Event](../events/Event.html "class in com.google.adk.events") functionResponseEvent)`

Traces tool response event.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### setTracerForTesting

public static void setTracerForTesting(io.opentelemetry.api.trace.Tracer tracer)

Sets the OpenTelemetry instance to be used for tracing. This is for testing purposes only.

    * ### traceAgentInvocation

public static void traceAgentInvocation(io.opentelemetry.api.trace.Span span, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentDescription, [InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Sets span attributes immediately available on agent invocation according to OTEL semconv version 1.37.

Parameters:
    `span` \- Span on which attributes are set.
    `agentName` \- Agent name from which attributes are gathered.
    `agentDescription` \- Agent description from which attributes are gathered.
    `invocationContext` \- InvocationContext from which attributes are gathered.

    * ### traceToolCall

public static void traceToolCall([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolDescription, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolType, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args)

Traces tool call arguments.

Parameters:
    `args` \- The arguments to the tool call.

    * ### traceToolResponse

public static void traceToolResponse([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [Event](../events/Event.html "class in com.google.adk.events") functionResponseEvent)

Traces tool response event.

Parameters:
    `eventId` \- The ID of the event.
    `functionResponseEvent` \- The function response event.

    * ### traceCallLlm

public static void traceCallLlm([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [LlmRequest](../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../models/LlmResponse.html "class in com.google.adk.models") llmResponse)

Traces a call to the LLM.

Parameters:
    `invocationContext` \- The invocation context.
    `eventId` \- The ID of the event associated with this LLM call/response.
    `llmRequest` \- The LLM request object.
    `llmResponse` \- The LLM response object.

    * ### traceSendData

public static void traceSendData([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> data)

Traces the sending of data (history or new content) to the agent/model.

Parameters:
    `invocationContext` \- The invocation context.
    `eventId` \- The ID of the event, if applicable.
    `data` \- A list of content objects being sent.

    * ### getTracer

public static io.opentelemetry.api.trace.Tracer getTracer()

Gets the tracer.

Returns:
    The tracer.

    * ### traceFlowable

public static <T> io.reactivex.rxjava3.core.Flowable<T> traceFlowable(io.opentelemetry.context.Context spanContext, io.opentelemetry.api.trace.Span span, [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html "class or interface in java.util.function")<io.reactivex.rxjava3.core.Flowable<T>> flowableSupplier)

Executes a Flowable with an OpenTelemetry Scope active for its entire lifecycle. 

This helper manages the OpenTelemetry Scope lifecycle for RxJava Flowables to ensure proper context propagation across async boundaries. The scope remains active from when the Flowable is returned through all operators until stream completion (onComplete, onError, or cancel). 

**Why not try-with-resources?** RxJava Flowables execute lazily - operators run at subscription time, not at chain construction time. Using try-with-resources would close the scope before the Flowable subscribes, causing Context.current() to return ROOT in nested operations and breaking parent-child span relationships (fragmenting traces). 

The scope is properly closed via doFinally when the stream terminates, ensuring no resource leaks regardless of completion mode (success, error, or cancellation).

Type Parameters:
    `T` \- The type of items emitted by the Flowable
Parameters:
    `spanContext` \- The context containing the span to activate
    `span` \- The span to end when the stream completes
    `flowableSupplier` \- Supplier that creates the Flowable to execute with active scope
Returns:
    Flowable with OpenTelemetry scope lifecycle management

    * ### trace

public static <T> [Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T> trace([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") spanName)

Returns a transformer that traces the execution of an RxJava stream.

Type Parameters:
    `T` \- The type of the stream.
Parameters:
    `spanName` \- The name of the span to create.
Returns:
    A TracerProvider that can be used with .compose().

    * ### trace

public static <T> [Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T> trace([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") spanName, io.opentelemetry.context.Context parentContext)

Returns a transformer that traces the execution of an RxJava stream with an explicit parent context.

Type Parameters:
    `T` \- The type of the stream.
Parameters:
    `spanName` \- The name of the span to create.
    `parentContext` \- The explicit parent context for the span.
Returns:
    A TracerProvider that can be used with .compose().

    * ### traceAgent

public static <T> [Tracing.TracerProvider](Tracing.TracerProvider.html "class in com.google.adk.telemetry")<T> traceAgent([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") spanName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") agentDescription, [InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Returns a transformer that traces an agent invocation.

Type Parameters:
    `T` \- The type of the stream.
Parameters:
    `spanName` \- The name of the span to create.
    `agentName` \- The name of the agent.
    `agentDescription` \- The description of the agent.
    `invocationContext` \- The invocation context.
Returns:
    A TracerProvider configured for agent invocation.




* * *

Copyright (C) 1980\. All rights reserved.
