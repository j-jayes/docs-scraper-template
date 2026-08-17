JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/MessageConverter.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.springai](package-summary.html)
  2. [MessageConverter](MessageConverter.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. MessageConverter(ObjectMapper)
  5. Method Details
     1. toLlmPrompt(LlmRequest)
     2. toLlmPrompt(LlmRequest, ChatOptions)
     3. getToolRegistry(LlmRequest)
     4. toLlmResponse(ChatResponse)
     5. toLlmResponse(ChatResponse, boolean)

Hide sidebar  Show sidebar

# Class MessageConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.springai.MessageConverter

* * *

public class MessageConverter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Converts between ADK and Spring AI message formats. 

This converter handles the translation between ADK's Content/Part format (based on Google's genai.types) and Spring AI's Message/ChatResponse format. It supports: 

  * Text content in all message types 
  * Tool/function calls in assistant messages 
  * System instructions and configuration options 


Note: Media attachments and tool responses are currently not supported due to Spring AI 1.1.0 API limitations (protected/private constructors). These will be added once Spring AI provides public APIs for these features.

  * ## Constructor Summary

Constructors

Constructor

Description

`MessageConverter(com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConverter.ToolMetadata](ToolConverter.ToolMetadata.html "class in com.google.adk.models.springai")>`

`getToolRegistry([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Gets tool registry from ADK tools for internal tracking.

`org.springframework.ai.chat.prompt.Prompt`

`toLlmPrompt([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Converts an ADK LlmRequest to a Spring AI Prompt.

`org.springframework.ai.chat.prompt.Prompt`

`toLlmPrompt([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, org.springframework.ai.chat.prompt.ChatOptions modelDefaultOptions)`

Converts an ADK LlmRequest to a Spring AI Prompt, using the target model's own default options as the base for the prompt options.

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

`toLlmResponse(org.springframework.ai.chat.model.ChatResponse chatResponse)`

Converts a Spring AI ChatResponse to an ADK LlmResponse.

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

`toLlmResponse(org.springframework.ai.chat.model.ChatResponse chatResponse, boolean isStreaming)`

Converts a Spring AI ChatResponse to an ADK LlmResponse with streaming context.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### MessageConverter

public MessageConverter(com.fasterxml.jackson.databind.ObjectMapper objectMapper)

  * ## Method Details

    * ### toLlmPrompt

public org.springframework.ai.chat.prompt.Prompt toLlmPrompt([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)

Converts an ADK LlmRequest to a Spring AI Prompt.

Parameters:
    `llmRequest` \- The ADK request to convert
Returns:
    A Spring AI Prompt

    * ### toLlmPrompt

public org.springframework.ai.chat.prompt.Prompt toLlmPrompt([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, org.springframework.ai.chat.prompt.ChatOptions modelDefaultOptions)

Converts an ADK LlmRequest to a Spring AI Prompt, using the target model's own default options as the base for the prompt options. 

Provider-specific chat models (for example Spring AI OpenAI `2.0.0`) cast ` Prompt.getOptions()` directly to their own options type (e.g. `OpenAiChatOptions`) in `createRequest(...)`. Passing provider-neutral options such as ` DefaultToolCallingChatOptions` therefore triggers a [`ClassCastException`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ClassCastException.html "class in java.lang"). To stay compatible with any provider, the prompt options are built on top of the model's own default options (obtained via `ChatModel.getOptions()`) so the resulting options keep the concrete type the provider expects, while overlaying the ADK tools and generation config.

Parameters:
    `llmRequest` \- The ADK request to convert
    `modelDefaultOptions` \- The target model's default options, or `null` if unavailable
Returns:
    A Spring AI Prompt

    * ### getToolRegistry

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConverter.ToolMetadata](ToolConverter.ToolMetadata.html "class in com.google.adk.models.springai")> getToolRegistry([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)

Gets tool registry from ADK tools for internal tracking.

Parameters:
    `llmRequest` \- The ADK request containing tools
Returns:
    Map of tool metadata for tracking available tools

    * ### toLlmResponse

public [LlmResponse](../LlmResponse.html "class in com.google.adk.models") toLlmResponse(org.springframework.ai.chat.model.ChatResponse chatResponse)

Converts a Spring AI ChatResponse to an ADK LlmResponse.

Parameters:
    `chatResponse` \- The Spring AI response to convert
Returns:
    An ADK LlmResponse

    * ### toLlmResponse

public [LlmResponse](../LlmResponse.html "class in com.google.adk.models") toLlmResponse(org.springframework.ai.chat.model.ChatResponse chatResponse, boolean isStreaming)

Converts a Spring AI ChatResponse to an ADK LlmResponse with streaming context.

Parameters:
    `chatResponse` \- The Spring AI response to convert
    `isStreaming` \- Whether this is part of a streaming response
Returns:
    An ADK LlmResponse




* * *

Copyright (C) 1980\. All rights reserved.
