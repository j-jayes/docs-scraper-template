JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ChatCompletionsHttpClient.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.chat](package-summary.html)
  2. [ChatCompletionsHttpClient](ChatCompletionsHttpClient.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ChatCompletionsHttpClient(HttpOptions)
     2. ChatCompletionsHttpClient(HttpOptions, ExecutorService)
  5. Method Details
     1. complete(LlmRequest, boolean)

Hide sidebar  Show sidebar

# Class ChatCompletionsHttpClient

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.chat.ChatCompletionsHttpClient

All Implemented Interfaces:
    `[ChatCompletionsClient](ChatCompletionsClient.html "interface in com.google.adk.models.chat")`

* * *

public final class ChatCompletionsHttpClient extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [ChatCompletionsClient](ChatCompletionsClient.html "interface in com.google.adk.models.chat")

An OkHttp-based implementation of [`ChatCompletionsClient`](ChatCompletionsClient.html "interface in com.google.adk.models.chat") that targets OpenAI-compatible chat completions endpoints. Both non-streaming responses (single [`LlmResponse`](../LlmResponse.html "class in com.google.adk.models") emission) and streaming Server-Sent Events (SSE) responses (multiple incremental [`LlmResponse`](../LlmResponse.html "class in com.google.adk.models") emissions) are supported.

  * ## Constructor Summary

Constructors

Constructor

Description

`ChatCompletionsHttpClient(com.google.genai.types.HttpOptions httpOptions)`

Constructs a new [`ChatCompletionsHttpClient`](ChatCompletionsHttpClient.html "class in com.google.adk.models.chat") that facilitates API interaction with the standard `/chat/completions` REST endpoint.

`ChatCompletionsHttpClient(com.google.genai.types.HttpOptions httpOptions, [ExecutorService](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ExecutorService.html "interface in java.util.concurrent") httpExecutorService)`

Constructs a [`ChatCompletionsHttpClient`](ChatCompletionsHttpClient.html "class in com.google.adk.models.chat") whose HTTP dispatcher runs on ` httpExecutorService`.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

`complete([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

Generates a conversational response from the chat completions endpoint based on the provided messages.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ChatCompletionsHttpClient

public ChatCompletionsHttpClient(com.google.genai.types.HttpOptions httpOptions)

Constructs a new [`ChatCompletionsHttpClient`](ChatCompletionsHttpClient.html "class in com.google.adk.models.chat") that facilitates API interaction with the standard `/chat/completions` REST endpoint. 

All configuration is sourced from the supplied `HttpOptions`: 
      * `HttpOptions.baseUrl()` \-- **required**. The base URL of the chat completions endpoint. The `chat/completions` path segments are appended automatically using `HttpUrl`, which handles trailing slashes and percent-encoding deterministically. Set via `HttpOptions.builder().baseUrl("https://...").build()`. 
      * `HttpOptions.headers()` \-- optional. Extra HTTP headers to include in outgoing requests. The `Content-Type` header is set automatically and cannot be overridden. Set via `HttpOptions.builder().headers(Map.of("Authorization", "Bearer ...")) `. 
      * `HttpOptions.timeout()` \-- optional. Per-call timeout in milliseconds. A missing timeout defaults to 5 minutes (`DEFAULT_CALL_TIMEOUT`). A timeout of `0` is respected as the explicit caller opt-in to infinite wait. Set via ` HttpOptions.builder().timeout(10_000).build()`. 

Example: 
            
            HttpOptions options =
                HttpOptions.builder()
                    .baseUrl("https://example.com/v1/")
                    .headers(ImmutableMap.of("Authorization", "Bearer my-token"))
                    .timeout(30_000)
                    .build();
            ChatCompletionsHttpClient client = new ChatCompletionsHttpClient(options);
            

Parameters:
    `httpOptions` \- HTTP configuration. Must not be `null`, and `HttpOptions.baseUrl()` must be present and parseable as an HTTP(S) URL.
Throws:
    `[IllegalArgumentException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html "class in java.lang")` \- if `httpOptions.baseUrl()` is missing or is not a valid HTTP(S) URL.

    * ### ChatCompletionsHttpClient

public ChatCompletionsHttpClient(com.google.genai.types.HttpOptions httpOptions, [ExecutorService](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ExecutorService.html "interface in java.util.concurrent") httpExecutorService)

Constructs a [`ChatCompletionsHttpClient`](ChatCompletionsHttpClient.html "class in com.google.adk.models.chat") whose HTTP dispatcher runs on ` httpExecutorService`. Pass [`HttpClientFactory.daemonExecutor(String)`](../../internal/http/HttpClientFactory.html#daemonExecutor\(java.lang.String\)) so a standalone or CLI JVM can exit once work is done, or a container-managed executor in a managed environment.

Parameters:
    `httpOptions` \- HTTP configuration; see `ChatCompletionsHttpClient(HttpOptions)`.
    `httpExecutorService` \- executor for the HTTP dispatcher threads.

  * ## Method Details

    * ### complete

public io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")> complete([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)

Description copied from interface: `[ChatCompletionsClient](ChatCompletionsClient.html#complete\(com.google.adk.models.LlmRequest,boolean\))`

Generates a conversational response from the chat completions endpoint based on the provided messages. This encapsulates building the payload, sending the request to the completions endpoint, and initiating the handling of complete calls.

Specified by:
    `[complete](ChatCompletionsClient.html#complete\(com.google.adk.models.LlmRequest,boolean\))` in interface `[ChatCompletionsClient](ChatCompletionsClient.html "interface in com.google.adk.models.chat")`
Parameters:
    `llmRequest` \- The request containing the model, configuration, and sequence of messages.
    `stream` \- Whether to request a streaming response.
Returns:
    A `Flowable` emitting the discrete (or combined) [`LlmResponse`](../LlmResponse.html "class in com.google.adk.models") objects.




* * *

Copyright (C) 1980\. All rights reserved.
