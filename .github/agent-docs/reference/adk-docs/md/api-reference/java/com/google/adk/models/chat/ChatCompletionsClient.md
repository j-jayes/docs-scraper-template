JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ChatCompletionsClient.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.chat](package-summary.html)
  2. [ChatCompletionsClient](ChatCompletionsClient.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. complete(LlmRequest, boolean)

Hide sidebar  Show sidebar

# Interface ChatCompletionsClient

All Known Implementing Classes:
    `[ChatCompletionsHttpClient](ChatCompletionsHttpClient.html "class in com.google.adk.models.chat")`

* * *

public interface ChatCompletionsClient

A client for interacting with OpenAI-compatible chat completions endpoints. 

Supports both non-streaming responses (single [`LlmResponse`](../LlmResponse.html "class in com.google.adk.models") emission) and streaming Server-Sent Events (SSE) responses (multiple incremental [`LlmResponse`](../LlmResponse.html "class in com.google.adk.models") emissions). See the [OpenAI Chat Completions API reference](https://developers.openai.com/api/reference/resources/chat) for the wire protocol.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

`complete([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

Generates a conversational response from the chat completions endpoint based on the provided messages.




  * ## Method Details

    * ### complete

io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")> complete([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)

Generates a conversational response from the chat completions endpoint based on the provided messages. This encapsulates building the payload, sending the request to the completions endpoint, and initiating the handling of complete calls.

Parameters:
    `llmRequest` \- The request containing the model, configuration, and sequence of messages.
    `stream` \- Whether to request a streaming response.
Returns:
    A `Flowable` emitting the discrete (or combined) [`LlmResponse`](../LlmResponse.html "class in com.google.adk.models") objects.




* * *

Copyright (C) 1980\. All rights reserved.
