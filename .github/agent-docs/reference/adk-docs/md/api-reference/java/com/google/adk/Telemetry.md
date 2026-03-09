JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/Telemetry.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)



  1. [com.google.adk](package-summary.html)
  2. [Telemetry](Telemetry.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. setTracerForTesting(Tracer)
     2. traceToolCall(Map)
     3. traceToolResponse(InvocationContext, String, Event)
     4. traceCallLlm(InvocationContext, String, LlmRequest, LlmResponse)
     5. traceSendData(InvocationContext, String, List)
     6. getTracer()
     7. traceFlowable(Context, Span, Supplier)

Hide sidebar  Show sidebar

# Class Telemetry

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.Telemetry

* * *

public class Telemetry extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility class for capturing and reporting telemetry data within the ADK. This class provides methods to trace various aspects of the agent's execution, including tool calls, tool responses, LLM interactions, and data handling. It leverages OpenTelemetry for tracing and logging for detailed information. These traces can then be exported through the ADK Dev Server UI.

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

`static void`

`traceCallLlm([InvocationContext](agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [LlmRequest](models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Traces a call to the LLM.

`static <T> io.reactivex.rxjava3.core.Flowable<T>`

`traceFlowable(io.opentelemetry.context.Context spanContext, io.opentelemetry.api.trace.Span span, [Supplier](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/Supplier.html "class or interface in java.util.function")<io.reactivex.rxjava3.core.Flowable<T>> flowableSupplier)`

Executes a Flowable with an OpenTelemetry Scope active for its entire lifecycle.

`static void`

`traceSendData([InvocationContext](agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> data)`

Traces the sending of data (history or new content) to the agent/model.

`static void`

`traceToolCall([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args)`

Traces tool call arguments.

`static void`

`traceToolResponse([InvocationContext](agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [Event](events/Event.html "class in com.google.adk.events") functionResponseEvent)`

Traces tool response event.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

    * ### setTracerForTesting

public static void setTracerForTesting(io.opentelemetry.api.trace.Tracer tracer)

Sets the OpenTelemetry instance to be used for tracing. This is for testing purposes only.

    * ### traceToolCall

public static void traceToolCall([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args)

Traces tool call arguments.

Parameters:
    `args` \- The arguments to the tool call.

    * ### traceToolResponse

public static void traceToolResponse([InvocationContext](agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [Event](events/Event.html "class in com.google.adk.events") functionResponseEvent)

Traces tool response event.

Parameters:
    `invocationContext` \- The invocation context for the current agent run.
    `eventId` \- The ID of the event.
    `functionResponseEvent` \- The function response event.

    * ### traceCallLlm

public static void traceCallLlm([InvocationContext](agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [LlmRequest](models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](models/LlmResponse.html "class in com.google.adk.models") llmResponse)

Traces a call to the LLM.

Parameters:
    `invocationContext` \- The invocation context.
    `eventId` \- The ID of the event associated with this LLM call/response.
    `llmRequest` \- The LLM request object.
    `llmResponse` \- The LLM response object.

    * ### traceSendData

public static void traceSendData([InvocationContext](agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> data)

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




* * *

Copyright (C) 1980\. All rights reserved.
