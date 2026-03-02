JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * Class
  * [Use](class-use/SpringAIObservabilityHandler.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.models.springai.observability](package-summary.html)
  2. [SpringAIObservabilityHandler](SpringAIObservabilityHandler.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. SpringAIObservabilityHandler(SpringAIProperties.Observability)
     2. SpringAIObservabilityHandler(SpringAIProperties.Observability, MeterRegistry)
  6. Method Details
     1. startRequest(String, String)
     2. recordSuccess(SpringAIObservabilityHandler.RequestContext, int, int, int)
     3. recordError(SpringAIObservabilityHandler.RequestContext, Throwable)
     4. logRequest(String, String)
     5. logResponse(String, String)
     6. getMeterRegistry()

Hide sidebar  Show sidebar

# Class SpringAIObservabilityHandler

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.springai.observability.SpringAIObservabilityHandler

* * *

public class SpringAIObservabilityHandler extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Handles observability features for Spring AI integration using Micrometer. 

This class provides: 

  * Metrics collection for request latency, token counts, and error rates via Micrometer 
  * Request/response logging with configurable content inclusion 
  * Performance monitoring for streaming and non-streaming requests 
  * Integration with any Micrometer-compatible metrics backend (Prometheus, Datadog, etc.) 


  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[SpringAIObservabilityHandler.RequestContext](SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability")`

Context for tracking a single request with Micrometer timer.

  * ## Constructor Summary

Constructors

Constructor

Description

`SpringAIObservabilityHandler([SpringAIProperties.Observability](../properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") config)`

Creates an observability handler with a default SimpleMeterRegistry.

`SpringAIObservabilityHandler([SpringAIProperties.Observability](../properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") config, io.micrometer.core.instrument.MeterRegistry meterRegistry)`

Creates an observability handler with a custom MeterRegistry.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.micrometer.core.instrument.MeterRegistry`

`getMeterRegistry()`

Gets the Micrometer MeterRegistry for direct access to metrics.

`void`

`logRequest([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") content, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

Logs request content if enabled.

`void`

`logResponse([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") content, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

Logs response content if enabled.

`void`

`recordError([SpringAIObservabilityHandler.RequestContext](SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability") context, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)`

Records a failed request.

`void`

`recordSuccess([SpringAIObservabilityHandler.RequestContext](SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability") context, int tokenCount, int inputTokens, int outputTokens)`

Records the completion of a successful request.

`[SpringAIObservabilityHandler.RequestContext](SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability")`

`startRequest([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") requestType)`

Records the start of a request.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### SpringAIObservabilityHandler

public SpringAIObservabilityHandler([SpringAIProperties.Observability](../properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") config)

Creates an observability handler with a default SimpleMeterRegistry.

Parameters:
    `config` \- the observability configuration

    * ### SpringAIObservabilityHandler

public SpringAIObservabilityHandler([SpringAIProperties.Observability](../properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") config, io.micrometer.core.instrument.MeterRegistry meterRegistry)

Creates an observability handler with a custom MeterRegistry.

Parameters:
    `config` \- the observability configuration
    `meterRegistry` \- the Micrometer meter registry to use for metrics

  * ## Method Details

    * ### startRequest

public [SpringAIObservabilityHandler.RequestContext](SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability") startRequest([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") requestType)

Records the start of a request.

Parameters:
    `modelName` \- the name of the model being used
    `requestType` \- the type of request (e.g., "chat", "streaming")
Returns:
    a request context for tracking the request

    * ### recordSuccess

public void recordSuccess([SpringAIObservabilityHandler.RequestContext](SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability") context, int tokenCount, int inputTokens, int outputTokens)

Records the completion of a successful request.

Parameters:
    `context` \- the request context
    `tokenCount` \- the number of tokens processed (input + output)
    `inputTokens` \- the number of input tokens
    `outputTokens` \- the number of output tokens

    * ### recordError

public void recordError([SpringAIObservabilityHandler.RequestContext](SpringAIObservabilityHandler.RequestContext.html "class in com.google.adk.models.springai.observability") context, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class or interface in java.lang") error)

Records a failed request.

Parameters:
    `context` \- the request context
    `error` \- the error that occurred

    * ### logRequest

public void logRequest([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") content, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)

Logs request content if enabled.

Parameters:
    `content` \- the request content
    `modelName` \- the model name

    * ### logResponse

public void logResponse([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") content, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)

Logs response content if enabled.

Parameters:
    `content` \- the response content
    `modelName` \- the model name

    * ### getMeterRegistry

public io.micrometer.core.instrument.MeterRegistry getMeterRegistry()

Gets the Micrometer MeterRegistry for direct access to metrics. 

This allows users to export metrics to any Micrometer-compatible backend (Prometheus, Datadog, CloudWatch, etc.) or query metrics programmatically.

Returns:
    the MeterRegistry instance




* * *

Copyright (C) 1980\. All rights reserved.
