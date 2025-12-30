JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Claude.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [Claude](Claude.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. Claude(String, AnthropicClient)
     2. Claude(String, AnthropicClient, int)
  5. Method Details
     1. generateContent(LlmRequest, boolean)
     2. connect(LlmRequest)



# Class Claude

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.models.BaseLlm](BaseLlm.html "class in com.google.adk.models")

com.google.adk.models.Claude

* * *

public class Claude extends [BaseLlm](BaseLlm.html "class in com.google.adk.models")

Represents the Claude Generative AI model by Anthropic. 

This class provides methods for interacting with Claude models. Streaming and live connections are not currently supported for Claude.

  * ## Constructor Summary

Constructors

Constructor

Description

`Claude([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, com.anthropic.client.AnthropicClient anthropicClient)`

Constructs a new Claude instance.

`Claude([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, com.anthropic.client.AnthropicClient anthropicClient, int maxTokens)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`[BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models")`

`connect([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest)`

Creates a live connection to the LLM.

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](LlmResponse.html "class in com.google.adk.models")>`

`generateContent([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

Generates one content from the given LLM request and tools.

### Methods inherited from class com.google.adk.models.[BaseLlm](BaseLlm.html "class in com.google.adk.models")

`[model](BaseLlm.html#model\(\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Claude

public Claude([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, com.anthropic.client.AnthropicClient anthropicClient)

Constructs a new Claude instance.

Parameters:
    `modelName` \- The name of the Claude model to use (e.g., "claude-3-opus-20240229").
    `anthropicClient` \- The Anthropic API client instance.

    * ### Claude

public Claude([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, com.anthropic.client.AnthropicClient anthropicClient, int maxTokens)

  * ## Method Details

    * ### generateContent

public io.reactivex.rxjava3.core.Flowable<[LlmResponse](LlmResponse.html "class in com.google.adk.models")> generateContent([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)

Description copied from class: `[BaseLlm](BaseLlm.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))`

Generates one content from the given LLM request and tools.

Specified by:
    `[generateContent](BaseLlm.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))` in class `[BaseLlm](BaseLlm.html "class in com.google.adk.models")`
Parameters:
    `llmRequest` \- The LLM request containing the input prompt and parameters.
    `stream` \- A boolean flag indicating whether to stream the response.
Returns:
    A Flowable of LlmResponses. For non-streaming calls, it will only yield one LlmResponse. For streaming calls, it may yield more than one LlmResponse, but all yielded LlmResponses should be treated as one content by merging their parts.

    * ### connect

public [BaseLlmConnection](BaseLlmConnection.html "interface in com.google.adk.models") connect([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest)

Description copied from class: `[BaseLlm](BaseLlm.html#connect\(com.google.adk.models.LlmRequest\))`

Creates a live connection to the LLM.

Specified by:
    `[connect](BaseLlm.html#connect\(com.google.adk.models.LlmRequest\))` in class `[BaseLlm](BaseLlm.html "class in com.google.adk.models")`




* * *

Copyright (C) 2025\. All rights reserved.
