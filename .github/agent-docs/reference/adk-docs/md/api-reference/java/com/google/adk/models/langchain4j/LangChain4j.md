JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/LangChain4j.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.models.langchain4j](package-summary.html)
  2. [LangChain4j](LangChain4j.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. LangChain4j(ChatModel)
     2. LangChain4j(ChatModel, String)
     3. LangChain4j(StreamingChatModel)
     4. LangChain4j(StreamingChatModel, String)
     5. LangChain4j(ChatModel, StreamingChatModel, String)
  5. Method Details
     1. generateContent(LlmRequest, boolean)
     2. connect(LlmRequest)



# Class LangChain4j

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.models.BaseLlm](../BaseLlm.html "class in com.google.adk.models")

com.google.adk.models.langchain4j.LangChain4j

* * *

@Experimental public class LangChain4j extends [BaseLlm](../BaseLlm.html "class in com.google.adk.models")

  * ## Constructor Summary

Constructors

Constructor

Description

`LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel)`

 

`LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel, dev.langchain4j.model.chat.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

 

`LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

 

`LangChain4j(dev.langchain4j.model.chat.StreamingChatModel streamingChatModel)`

 

`LangChain4j(dev.langchain4j.model.chat.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)`

 

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

### Methods inherited from class com.google.adk.models.[BaseLlm](../BaseLlm.html "class in com.google.adk.models")

`[model](../BaseLlm.html#model\(\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### LangChain4j

public LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel)

    * ### LangChain4j

public LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)

    * ### LangChain4j

public LangChain4j(dev.langchain4j.model.chat.StreamingChatModel streamingChatModel)

    * ### LangChain4j

public LangChain4j(dev.langchain4j.model.chat.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)

    * ### LangChain4j

public LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel, dev.langchain4j.model.chat.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName)

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

Copyright (C) 2025\. All rights reserved.
