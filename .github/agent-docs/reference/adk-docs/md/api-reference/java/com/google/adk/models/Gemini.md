JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Gemini.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [Gemini](Gemini.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Gemini(String, Client)
     2. Gemini(String, String)
     3. Gemini(String, VertexCredentials)
  6. Method Details
     1. builder()
     2. generateContent(LlmRequest, boolean)
     3. connect(LlmRequest)



# Class Gemini

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.models.BaseLlm](BaseLlm.html "class in com.google.adk.models")

com.google.adk.models.Gemini

* * *

public class Gemini extends [BaseLlm](BaseLlm.html "class in com.google.adk.models")

Represents the Gemini Generative AI model. 

This class provides methods for interacting with the Gemini model, including standard request-response generation and establishing persistent bidirectional connections.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models")`

Builder for [`Gemini`](Gemini.html "class in com.google.adk.models").

  * ## Constructor Summary

Constructors

Constructor

Description

`Gemini([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [VertexCredentials](VertexCredentials.html "class in com.google.adk.models") vertexCredentials)`

Constructs a new Gemini instance with a Google Gemini API key.

`Gemini([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, com.google.genai.Client apiClient)`

Constructs a new Gemini instance.

`Gemini([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") apiKey)`

Constructs a new Gemini instance with a Google Gemini API key.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models")`

`builder()`

Returns a new Builder instance for constructing Gemini objects.

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

    * ### Gemini

public Gemini([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, com.google.genai.Client apiClient)

Constructs a new Gemini instance.

Parameters:
    `modelName` \- The name of the Gemini model to use (e.g., "gemini-2.0-flash").
    `apiClient` \- The genai `Client` instance for making API calls.

    * ### Gemini

public Gemini([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") apiKey)

Constructs a new Gemini instance with a Google Gemini API key.

Parameters:
    `modelName` \- The name of the Gemini model to use (e.g., "gemini-2.0-flash").
    `apiKey` \- The Google Gemini API key.

    * ### Gemini

public Gemini([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") modelName, [VertexCredentials](VertexCredentials.html "class in com.google.adk.models") vertexCredentials)

Constructs a new Gemini instance with a Google Gemini API key.

Parameters:
    `modelName` \- The name of the Gemini model to use (e.g., "gemini-2.0-flash").
    `vertexCredentials` \- The Vertex AI credentials to access the Gemini model.

  * ## Method Details

    * ### builder

public static [Gemini.Builder](Gemini.Builder.html "class in com.google.adk.models") builder()

Returns a new Builder instance for constructing Gemini objects. Note that when building a Gemini object, at least one of apiKey, vertexCredentials, or an explicit apiClient must be set. If multiple are set, the explicit apiClient will take precedence.

Returns:
    A new [`Gemini.Builder`](Gemini.Builder.html "class in com.google.adk.models").

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
