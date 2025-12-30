JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseLlm.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [BaseLlm](BaseLlm.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. BaseLlm(String)
  5. Method Details
     1. model()
     2. generateContent(LlmRequest, boolean)
     3. connect(LlmRequest)



# Class BaseLlm

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.BaseLlm

Direct Known Subclasses:
    `[Claude](Claude.html "class in com.google.adk.models")`, `[Gemini](Gemini.html "class in com.google.adk.models")`, `[LangChain4j](langchain4j/LangChain4j.html "class in com.google.adk.models.langchain4j")`

* * *

public abstract class BaseLlm extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Abstract base class for Large Language Models (LLMs). 

Provides a common interface for interacting with different LLMs.

  * ## Constructor Summary

Constructors

Constructor

Description

`BaseLlm([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`abstract [BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models")`

`connect([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest)`

Creates a live connection to the LLM.

`abstract io.reactivex.rxjava3.core.Flowable<[LlmResponse](LlmResponse.html "class in com.google.adk.models")>`

`generateContent([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

Generates one content from the given LLM request and tools.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`model()`

Returns the name of the LLM model.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### BaseLlm

public BaseLlm([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model)

  * ## Method Details

    * ### model

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") model()

Returns the name of the LLM model.

Returns:
    The name of the LLM model.

    * ### generateContent

public abstract io.reactivex.rxjava3.core.Flowable<[LlmResponse](LlmResponse.html "class in com.google.adk.models")> generateContent([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)

Generates one content from the given LLM request and tools.

Parameters:
    `llmRequest` \- The LLM request containing the input prompt and parameters.
    `stream` \- A boolean flag indicating whether to stream the response.
Returns:
    A Flowable of LlmResponses. For non-streaming calls, it will only yield one LlmResponse. For streaming calls, it may yield more than one LlmResponse, but all yielded LlmResponses should be treated as one content by merging their parts.

    * ### connect

public abstract [BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models") connect([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest)

Creates a live connection to the LLM.




* * *

Copyright (C) 2025\. All rights reserved.
