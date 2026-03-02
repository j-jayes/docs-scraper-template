JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/MessageConverter.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



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
     2. getToolRegistry(LlmRequest)
     3. toLlmResponse(ChatResponse)
     4. toLlmResponse(ChatResponse, boolean)

Hide sidebar  Show sidebar

# Class MessageConverter

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.springai.MessageConverter

* * *

public class MessageConverter extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConverter.ToolMetadata](ToolConverter.ToolMetadata.html "class in com.google.adk.models.springai")>`

`getToolRegistry([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Gets tool registry from ADK tools for internal tracking.

`org.springframework.ai.chat.prompt.Prompt`

`toLlmPrompt([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Converts an ADK LlmRequest to a Spring AI Prompt.

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

`toLlmResponse(org.springframework.ai.chat.model.ChatResponse chatResponse)`

Converts a Spring AI ChatResponse to an ADK LlmResponse.

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

`toLlmResponse(org.springframework.ai.chat.model.ChatResponse chatResponse, boolean isStreaming)`

Converts a Spring AI ChatResponse to an ADK LlmResponse with streaming context.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




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

    * ### getToolRegistry

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"), [ToolConverter.ToolMetadata](ToolConverter.ToolMetadata.html "class in com.google.adk.models.springai")> getToolRegistry([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)

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
