JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/Telemetry.html)
  * [Tree](package-tree.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)



  1. [com.google.adk](package-summary.html)
  2. [Telemetry](Telemetry.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. traceToolCall(Map)
     2. traceToolResponse(InvocationContext, String, Event)
     3. traceCallLlm(InvocationContext, String, LlmRequest, LlmResponse)
     4. traceSendData(InvocationContext, String, List)
     5. getTracer()



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

`traceCallLlm([InvocationContext](agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [LlmRequest](models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Traces a call to the LLM.

`static void`

`traceSendData([InvocationContext](agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> data)`

Traces the sending of data (history or new content) to the agent/model.

`static void`

`traceToolCall([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> args)`

Traces tool call arguments.

`static void`

`traceToolResponse([InvocationContext](agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [Event](events/Event.html "class in com.google.adk.events") functionResponseEvent)`

Traces tool response event.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Method Details

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




* * *

Copyright (C) 2025\. All rights reserved.
