JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/GeminiUtil.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.models](package-summary.html)
  2. [GeminiUtil](GeminiUtil.html)



Contents 

  1. Description
  2. Field Summary
  3. Method Summary
  4. Field Details
     1. CONTINUE_OUTPUT_MESSAGE
  5. Method Details
     1. prepareGenenerateContentRequest(LlmRequest, boolean)
     2. prepareGenenerateContentRequest(LlmRequest, boolean, boolean)
     3. sanitizeRequestForGeminiApi(LlmRequest)
     4. removeClientFunctionCallId(LlmRequest)
     5. getPart0FromLlmResponse(LlmResponse)
     6. getTextFromLlmResponse(LlmResponse)
     7. shouldEmitAccumulatedText(LlmResponse)
     8. stripThoughts(List)
     9. toGenerateContentResponseUsageMetadata(UsageMetadata)

Hide sidebar  Show sidebar

# Class GeminiUtil

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.models.GeminiUtil

* * *

public final class GeminiUtil extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Request / Response utilities for [`Gemini`](Gemini.html "class in com.google.adk.models").

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`CONTINUE_OUTPUT_MESSAGE`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Part>`

`getPart0FromLlmResponse([LlmResponse](LlmResponse.html "class in com.google.adk.models") llmResponse)`

Extracts the first part of an LlmResponse, if available.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")`

`getTextFromLlmResponse([LlmResponse](LlmResponse.html "class in com.google.adk.models") llmResponse)`

Extracts text content from the first part of an LlmResponse, if available.

`static [LlmRequest](LlmRequest.html "class in com.google.adk.models")`

`prepareGenenerateContentRequest([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest, boolean sanitize)`

Prepares an [`LlmRequest`](LlmRequest.html "class in com.google.adk.models") for the GenerateContent API.

`static [LlmRequest](LlmRequest.html "class in com.google.adk.models")`

`prepareGenenerateContentRequest([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest, boolean sanitize, boolean stripThoughts)`

Prepares an [`LlmRequest`](LlmRequest.html "class in com.google.adk.models") for the GenerateContent API.

`static [LlmRequest](LlmRequest.html "class in com.google.adk.models")`

`removeClientFunctionCallId([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest)`

Removes client-side function call IDs from the request.

`static [LlmRequest](LlmRequest.html "class in com.google.adk.models")`

`sanitizeRequestForGeminiApi([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest)`

Sanitizes the request to ensure it is compatible with the Gemini API backend.

`static boolean`

`shouldEmitAccumulatedText([LlmResponse](LlmResponse.html "class in com.google.adk.models") currentLlmResponse)`

Determines if accumulated text should be emitted based on the current LlmResponse.

`static com.google.common.collect.ImmutableList<com.google.genai.types.Content>`

`stripThoughts([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> originalContents)`

Removes any `Part` that contains only a `thought` from the content list.

`static com.google.genai.types.GenerateContentResponseUsageMetadata`

`toGenerateContentResponseUsageMetadata(com.google.genai.types.UsageMetadata usageMetadata)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### CONTINUE_OUTPUT_MESSAGE

public static final [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") CONTINUE_OUTPUT_MESSAGE

See Also:
    
      * [Constant Field Values](../../../../constant-values.html#com.google.adk.models.GeminiUtil.CONTINUE_OUTPUT_MESSAGE)

  * ## Method Details

    * ### prepareGenenerateContentRequest

public static [LlmRequest](LlmRequest.html "class in com.google.adk.models") prepareGenenerateContentRequest([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest, boolean sanitize)

Prepares an [`LlmRequest`](LlmRequest.html "class in com.google.adk.models") for the GenerateContent API. 

This method can optionally sanitize the request and ensures that the last content part is from the user to prompt a model response.

Parameters:
    `llmRequest` \- The original [`LlmRequest`](LlmRequest.html "class in com.google.adk.models").
    `sanitize` \- Whether to sanitize the request to be compatible with the Gemini API backend.
Returns:
    The prepared [`LlmRequest`](LlmRequest.html "class in com.google.adk.models").

    * ### prepareGenenerateContentRequest

public static [LlmRequest](LlmRequest.html "class in com.google.adk.models") prepareGenenerateContentRequest([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest, boolean sanitize, boolean stripThoughts)

Prepares an [`LlmRequest`](LlmRequest.html "class in com.google.adk.models") for the GenerateContent API. 

This method can optionally sanitize the request and ensures that the last content part is from the user to prompt a model response. It also strips out any parts marked as "thoughts" and removes client-side function call IDs as some LLM APIs reject requests with client-side function call IDs.

Parameters:
    `llmRequest` \- The original [`LlmRequest`](LlmRequest.html "class in com.google.adk.models").
    `sanitize` \- Whether to sanitize the request to be compatible with the Gemini API backend.
Returns:
    The prepared [`LlmRequest`](LlmRequest.html "class in com.google.adk.models").

    * ### sanitizeRequestForGeminiApi

public static [LlmRequest](LlmRequest.html "class in com.google.adk.models") sanitizeRequestForGeminiApi([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest)

Sanitizes the request to ensure it is compatible with the Gemini API backend. Required as there are some parameters that if included in the request will raise a runtime error if sent to the wrong backend (e.g. image names only work on Vertex AI).

Parameters:
    `llmRequest` \- The request to sanitize.
Returns:
    The sanitized request.

    * ### removeClientFunctionCallId

public static [LlmRequest](LlmRequest.html "class in com.google.adk.models") removeClientFunctionCallId([LlmRequest](LlmRequest.html "class in com.google.adk.models") llmRequest)

Removes client-side function call IDs from the request. 

Client-side function call IDs are internal to the ADK and should not be sent to the model. This method iterates through the contents and parts, removing the ID from any `FunctionCall` or `FunctionResponse` parts.

Parameters:
    `llmRequest` \- The request to process.
Returns:
    A new [`LlmRequest`](LlmRequest.html "class in com.google.adk.models") with function call IDs removed.

    * ### getPart0FromLlmResponse

public static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Part> getPart0FromLlmResponse([LlmResponse](LlmResponse.html "class in com.google.adk.models") llmResponse)

Extracts the first part of an LlmResponse, if available.

Parameters:
    `llmResponse` \- The LlmResponse to extract the first part from.
Returns:
    The first part, or an empty optional if not found.

    * ### getTextFromLlmResponse

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") getTextFromLlmResponse([LlmResponse](LlmResponse.html "class in com.google.adk.models") llmResponse)

Extracts text content from the first part of an LlmResponse, if available.

Parameters:
    `llmResponse` \- The LlmResponse to extract text from.
Returns:
    The text content, or an empty string if not found.

    * ### shouldEmitAccumulatedText

public static boolean shouldEmitAccumulatedText([LlmResponse](LlmResponse.html "class in com.google.adk.models") currentLlmResponse)

Determines if accumulated text should be emitted based on the current LlmResponse. We flush if current response is not a text continuation (e.g., no content, no parts, or the first part is not inline_data, meaning it's something else or just empty, thereby warranting a flush of preceding text).

Parameters:
    `currentLlmResponse` \- The current LlmResponse being processed.
Returns:
    True if accumulated text should be emitted, false otherwise.

    * ### stripThoughts

public static com.google.common.collect.ImmutableList<com.google.genai.types.Content> stripThoughts([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Content> originalContents)

Removes any `Part` that contains only a `thought` from the content list.

    * ### toGenerateContentResponseUsageMetadata

public static com.google.genai.types.GenerateContentResponseUsageMetadata toGenerateContentResponseUsageMetadata(com.google.genai.types.UsageMetadata usageMetadata)




* * *

Copyright (C) 1980\. All rights reserved.
