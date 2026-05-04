JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/LangChain4j.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.langchain4j](package-summary.html)
  2. [LangChain4j](LangChain4j.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. LangChain4j(ChatModel)
     2. LangChain4j(ChatModel, String)
     3. LangChain4j(StreamingChatModel)
     4. LangChain4j(StreamingChatModel, String)
     5. LangChain4j(ChatModel, StreamingChatModel, String)
  6. Method Details
     1. chatModel()
     2. streamingChatModel()
     3. objectMapper()
     4. modelName()
     5. tokenCountEstimator()
     6. model()
     7. builder()
     8. generateContent(LlmRequest, boolean)
     9. connect(LlmRequest)

Hide sidebar  Show sidebar

# Class LangChain4j

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.models.BaseLlm](../BaseLlm.html "class in com.google.adk.models")

com.google.adk.models.langchain4j.LangChain4j

* * *

public abstract class LangChain4j extends [BaseLlm](../BaseLlm.html "class in com.google.adk.models")

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[LangChain4j.Builder](LangChain4j.Builder.html "class in com.google.adk.models.langchain4j")`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel)`

 

`LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel, dev.langchain4j.model.chat.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName)`

 

`LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName)`

 

`LangChain4j(dev.langchain4j.model.chat.StreamingChatModel streamingChatModel)`

 

`LangChain4j(dev.langchain4j.model.chat.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName)`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [LangChain4j.Builder](LangChain4j.Builder.html "class in com.google.adk.models.langchain4j")`

`builder()`

 

`abstract @Nullable dev.langchain4j.model.chat.ChatModel`

`chatModel()`

 

`[BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

`connect([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Creates a live connection to the LLM.

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

`generateContent([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

Generates one content from the given LLM request and tools.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`model()`

Returns the name of the LLM model.

`abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`modelName()`

 

`abstract com.fasterxml.jackson.databind.ObjectMapper`

`objectMapper()`

 

`abstract @Nullable dev.langchain4j.model.chat.StreamingChatModel`

`streamingChatModel()`

 

`abstract @Nullable dev.langchain4j.model.TokenCountEstimator`

`tokenCountEstimator()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### LangChain4j

public LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel)

    * ### LangChain4j

public LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName)

    * ### LangChain4j

public LangChain4j(dev.langchain4j.model.chat.StreamingChatModel streamingChatModel)

    * ### LangChain4j

public LangChain4j(dev.langchain4j.model.chat.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName)

    * ### LangChain4j

public LangChain4j(dev.langchain4j.model.chat.ChatModel chatModel, dev.langchain4j.model.chat.StreamingChatModel streamingChatModel, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName)

  * ## Method Details

    * ### chatModel

public abstract @Nullable dev.langchain4j.model.chat.ChatModel chatModel()

    * ### streamingChatModel

public abstract @Nullable dev.langchain4j.model.chat.StreamingChatModel streamingChatModel()

    * ### objectMapper

public abstract com.fasterxml.jackson.databind.ObjectMapper objectMapper()

    * ### modelName

public abstract [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") modelName()

    * ### tokenCountEstimator

public abstract @Nullable dev.langchain4j.model.TokenCountEstimator tokenCountEstimator()

    * ### model

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model()

Description copied from class: `[BaseLlm](../BaseLlm.html#model\(\))`

Returns the name of the LLM model.

Overrides:
    `[model](../BaseLlm.html#model\(\))` in class `[BaseLlm](../BaseLlm.html "class in com.google.adk.models")`
Returns:
    The name of the LLM model.

    * ### builder

public static [LangChain4j.Builder](LangChain4j.Builder.html "class in com.google.adk.models.langchain4j") builder()

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
