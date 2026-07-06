JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Metrics.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.telemetry](package-summary.html)
  2. [Metrics](Metrics.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. setMeterForTesting(Meter)
     2. recordAgentInvocationDuration(String, Duration, Throwable)
     3. recordAgentRequestSize(String, Content)
     4. recordAgentResponseSize(String, List)
     5. recordAgentWorkflowSteps(String, List)
     6. recordToolExecutionDuration(String, String, Duration, Throwable)
     7. recordToolRequestSize(String, String, Map)
     8. recordToolResponseSize(String, String, Event)

Hide sidebar  Show sidebar

# Class Metrics

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.telemetry.Metrics

* * *

public final class Metrics extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Utility class for recording OpenTelemetry metrics within the ADK.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static void`

`recordAgentInvocationDuration([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") duration, @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Records the duration of the agent invocation.

`static void`

`recordAgentRequestSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, @Nullable com.google.genai.types.Content userContent)`

Records the size of the agent request.

`static void`

`recordAgentResponseSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)`

Records the size of the agent response by extracting content from events.

`static void`

`recordAgentWorkflowSteps([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)`

Records the number of steps in the agent workflow by counting the number of events.

`static void`

`recordToolExecutionDuration([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") duration, @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Records the duration of the tool execution.

`static void`

`recordToolRequestSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> functionArgs)`

Records the size of the tool request.

`static void`

`recordToolResponseSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, @Nullable [Event](../events/Event.html "class in com.google.adk.events") responseEvent)`

Records the size of the tool response.

`static void`

`setMeterForTesting(io.opentelemetry.api.metrics.Meter meter)`

Sets the OpenTelemetry Meter to be used for metrics.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### setMeterForTesting

public static void setMeterForTesting(io.opentelemetry.api.metrics.Meter meter)

Sets the OpenTelemetry Meter to be used for metrics. This is for testing purposes only.

    * ### recordAgentInvocationDuration

public static void recordAgentInvocationDuration([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") duration, @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)

Records the duration of the agent invocation.

    * ### recordAgentRequestSize

public static void recordAgentRequestSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, @Nullable com.google.genai.types.Content userContent)

Records the size of the agent request.

    * ### recordAgentResponseSize

public static void recordAgentResponseSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, @Nullable [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)

Records the size of the agent response by extracting content from events.

    * ### recordAgentWorkflowSteps

public static void recordAgentWorkflowSteps([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[Event](../events/Event.html "class in com.google.adk.events")> events)

Records the number of steps in the agent workflow by counting the number of events.

    * ### recordToolExecutionDuration

public static void recordToolExecutionDuration([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, [Duration](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/time/Duration.html "class in java.time") duration, @Nullable [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)

Records the duration of the tool execution.

    * ### recordToolRequestSize

public static void recordToolRequestSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> functionArgs)

Records the size of the tool request.

    * ### recordToolResponseSize

public static void recordToolResponseSize([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") agentName, @Nullable [Event](../events/Event.html "class in com.google.adk.events") responseEvent)

Records the size of the tool response.




* * *

Copyright (C) 1980\. All rights reserved.
