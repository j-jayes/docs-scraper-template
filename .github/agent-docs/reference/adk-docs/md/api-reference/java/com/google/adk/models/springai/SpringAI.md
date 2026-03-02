JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/SpringAI.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.models.springai](package-summary.html)
  2. [SpringAI](SpringAI.html)



Contents 

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. SpringAI(ChatModel)
     2. SpringAI(ChatModel, String)
     3. SpringAI(StreamingChatModel)
     4. SpringAI(StreamingChatModel, String)
     5. SpringAI(ChatModel, StreamingChatModel, String)
     6. SpringAI(ChatModel, StreamingChatModel, String, SpringAIProperties.Observability)
     7. SpringAI(ChatModel, String, SpringAIProperties.Observability)
     8. SpringAI(StreamingChatModel, String, SpringAIProperties.Observability)
  5. Method Details
     1. generateContent(LlmRequest, boolean)
     2. connect(LlmRequest)

Hide sidebar  Show sidebar

# Class SpringAI

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.models.BaseLlm](../BaseLlm.html "class in com.google.adk.models")

com.google.adk.models.springai.SpringAI

* * *

public class SpringAI extends [BaseLlm](../BaseLlm.html "class in com.google.adk.models")

Spring AI implementation of BaseLlm that wraps Spring AI ChatModel and StreamingChatModel. 

This adapter allows Spring AI models to be used within the ADK framework by converting between ADK's LlmRequest/LlmResponse format and Spring AI's Prompt/ChatResponse format.

  * ## Constructor Summary

Constructors

Constructor

Description

`SpringAI(org.springframework.ai.chat.model.ChatModel chatModel)`

 

`SpringAI(org.springframework.ai.chat.model.ChatModel chatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

 

`SpringAI(org.springframework.ai.chat.model.ChatModel chatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [SpringAIProperties.Observability](properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") observabilityConfig)`

 

`SpringAI(org.springframework.ai.chat.model.ChatModel chatModel, org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

 

`SpringAI(org.springframework.ai.chat.model.ChatModel chatModel, org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [SpringAIProperties.Observability](properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") observabilityConfig)`

 

`SpringAI(org.springframework.ai.chat.model.StreamingChatModel streamingChatModel)`

 

`SpringAI(org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

 

`SpringAI(org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [SpringAIProperties.Observability](properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") observabilityConfig)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

`connect([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Creates a live connection to the LLM.

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

`generateContent([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

Generates one content from the given LLM request and tools.

### Methods inherited from class [BaseLlm](../BaseLlm.html#method-summary "class in com.google.adk.models")

`[model](../BaseLlm.html#model\(\) "model\(\)")`

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### SpringAI

public SpringAI(org.springframework.ai.chat.model.ChatModel chatModel)

    * ### SpringAI

public SpringAI(org.springframework.ai.chat.model.ChatModel chatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)

    * ### SpringAI

public SpringAI(org.springframework.ai.chat.model.StreamingChatModel streamingChatModel)

    * ### SpringAI

public SpringAI(org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)

    * ### SpringAI

public SpringAI(org.springframework.ai.chat.model.ChatModel chatModel, org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)

    * ### SpringAI

public SpringAI(org.springframework.ai.chat.model.ChatModel chatModel, org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [SpringAIProperties.Observability](properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") observabilityConfig)

    * ### SpringAI

public SpringAI(org.springframework.ai.chat.model.ChatModel chatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [SpringAIProperties.Observability](properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") observabilityConfig)

    * ### SpringAI

public SpringAI(org.springframework.ai.chat.model.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [SpringAIProperties.Observability](properties/SpringAIProperties.Observability.html "class in com.google.adk.models.springai.properties") observabilityConfig)

  * ## Method Details

    * ### generateContent

public io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")> generateContent([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)

Description copied from class: `[BaseLlm](../BaseLlm.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))`

Generates one content from the given LLM request and tools.

Specified by:
    `[generateContent](../BaseLlm.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))` in class `[BaseLlm](../BaseLlm.html "class in com.google.adk.models")`
Parameters:
    `llmRequest` \- The LLM request containing the input prompt and parameters.
    `stream` \- A boolean flag indicating whether to stream the response.
Returns:
    A Flowable of LlmResponses. For non-streaming calls, it will only yield one LlmResponse. For streaming calls, it may yield more than one LlmResponse, but all yielded LlmResponses should be treated as one content by merging their parts.

    * ### connect

public [BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models") connect([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)

Description copied from class: `[BaseLlm](../BaseLlm.html#connect\(com.google.adk.models.LlmRequest\))`

Creates a live connection to the LLM.

Specified by:
    `[connect](../BaseLlm.html#connect\(com.google.adk.models.LlmRequest\))` in class `[BaseLlm](../BaseLlm.html "class in com.google.adk.models")`




* * *

Copyright (C) 1980\. All rights reserved.
