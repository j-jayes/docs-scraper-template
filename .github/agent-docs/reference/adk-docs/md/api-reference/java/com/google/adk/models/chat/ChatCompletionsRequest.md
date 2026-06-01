JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ChatCompletionsRequest.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models.chat](package-summary.html)
  2. [ChatCompletionsRequest](ChatCompletionsRequest.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. messages
     2. model
     3. audio
     4. frequencyPenalty
     5. logitBias
     6. logprobs
     7. maxCompletionTokens
     8. metadata
     9. modalities
     10. n
     11. parallelToolCalls
     12. prediction
     13. presencePenalty
     14. promptCacheKey
     15. promptCacheRetention
     16. reasoningEffort
     17. responseFormat
     18. safetyIdentifier
     19. seed
     20. serviceTier
     21. stop
     22. store
     23. stream
     24. streamOptions
     25. temperature
     26. toolChoice
     27. tools
     28. topLogprobs
     29. topP
     30. user
     31. verbosity
     32. webSearchOptions
     33. extraBody
  6. Constructor Details
     1. ChatCompletionsRequest()
  7. Method Details
     1. fromLlmRequest(LlmRequest, boolean)

Hide sidebar  Show sidebar

# Class ChatCompletionsRequest

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.models.chat.ChatCompletionsRequest

* * *

public final class ChatCompletionsRequest extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Data Transfer Objects for Chat Completion API requests. 

Can be used to translate from a [`LlmRequest`](../LlmRequest.html "class in com.google.adk.models") into a [`ChatCompletionsRequest`](ChatCompletionsRequest.html "class in com.google.adk.models.chat") using `fromLlmRequest(LlmRequest, boolean)`. 

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`com.google.adk.models.chat.ChatCompletionsRequest.AudioParam`

`audio`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20audio%20%3E%20(schema)

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>`

`extraBody`

Additional body parameters used for specific models, for example: https://ai.google.dev/gemini-api/docs/openai#extra-body

`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang")`

`frequencyPenalty`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20frequency_penalty%20%3E%20(schema)

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang")>`

`logitBias`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20logit_bias%20%3E%20(schema)

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")`

`logprobs`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20logprobs%20%3E%20(schema)

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")`

`maxCompletionTokens`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20max_completion_tokens%20%3E%20(schema)

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.models.chat.ChatCompletionsRequest.Message>`

`messages`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20messages%20%3E%20(schema)

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`metadata`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20metadata%20%3E%20(schema)

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`modalities`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20modalities%20%3E%20(schema)

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`model`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")`

`n`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20n%20%3E%20(schema)

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")`

`parallelToolCalls`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20parallel_tool_calls%20%3E%20(schema)

`com.google.adk.models.chat.ChatCompletionsRequest.Prediction`

`prediction`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prediction%20%3E%20(schema)

`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang")`

`presencePenalty`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20presence_penalty%20%3E%20(schema)

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`promptCacheKey`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prompt_cache_key%20%3E%20(schema)

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`promptCacheRetention`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema)

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`reasoningEffort`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)

`com.google.adk.models.chat.ChatCompletionsRequest.ResponseFormat`

`responseFormat`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`safetyIdentifier`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20safety_identifier%20%3E%20(schema)

`[Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html "class in java.lang")`

`seed`

Deprecated.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`serviceTier`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20service_tier%20%3E%20(schema)

`com.google.adk.models.chat.ChatCompletionsRequest.StopCondition`

`stop`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stop%20%3E%20(schema)

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")`

`store`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20store%20%3E%20(schema)

`[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")`

`stream`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stream%20%3E%20(schema)

`com.google.adk.models.chat.ChatCompletionsRequest.StreamOptions`

`streamOptions`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stream_options%20%3E%20(schema)

`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang")`

`temperature`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20temperature%20%3E%20(schema)

`com.google.adk.models.chat.ChatCompletionsRequest.ToolChoice`

`toolChoice`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)

`[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.models.chat.ChatCompletionsRequest.Tool>`

`tools`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tools%20%3E%20(schema)

`[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")`

`topLogprobs`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20top_logprobs%20%3E%20(schema)

`[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang")`

`topP`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20top_p%20%3E%20(schema)

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`user`

Deprecated, use safety_identifier and prompt_cache_key instead.

`[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`verbosity`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20verbosity%20%3E%20(schema)

`com.google.adk.models.chat.ChatCompletionsRequest.WebSearchOptions`

`webSearchOptions`

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20web_search_options%20%3E%20(schema)

  * ## Constructor Summary

Constructors

Constructor

Description

`ChatCompletionsRequest()`

 

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [ChatCompletionsRequest](ChatCompletionsRequest.html "class in com.google.adk.models.chat")`

`fromLlmRequest([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean responseStreaming)`

Converts a standard [`LlmRequest`](../LlmRequest.html "class in com.google.adk.models") into a [`ChatCompletionsRequest`](ChatCompletionsRequest.html "class in com.google.adk.models.chat") for /chat/completions compatible endpoints.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Field Details

    * ### messages

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.models.chat.ChatCompletionsRequest.Message> messages

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20messages%20%3E%20(schema)

    * ### model

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20model%20%3E%20(schema)

    * ### audio

public com.google.adk.models.chat.ChatCompletionsRequest.AudioParam audio

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20audio%20%3E%20(schema)

    * ### frequencyPenalty

public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang") frequencyPenalty

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20frequency_penalty%20%3E%20(schema)

    * ### logitBias

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang")> logitBias

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20logit_bias%20%3E%20(schema)

    * ### logprobs

public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") logprobs

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20logprobs%20%3E%20(schema)

    * ### maxCompletionTokens

public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") maxCompletionTokens

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20max_completion_tokens%20%3E%20(schema)

    * ### metadata

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> metadata

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20metadata%20%3E%20(schema)

    * ### modalities

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> modalities

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20modalities%20%3E%20(schema)

    * ### n

public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") n

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20n%20%3E%20(schema)

    * ### parallelToolCalls

public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") parallelToolCalls

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20parallel_tool_calls%20%3E%20(schema)

    * ### prediction

public com.google.adk.models.chat.ChatCompletionsRequest.Prediction prediction

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prediction%20%3E%20(schema)

    * ### presencePenalty

public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang") presencePenalty

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20presence_penalty%20%3E%20(schema)

    * ### promptCacheKey

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") promptCacheKey

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prompt_cache_key%20%3E%20(schema)

    * ### promptCacheRetention

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") promptCacheRetention

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20prompt_cache_retention%20%3E%20(schema)

    * ### reasoningEffort

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") reasoningEffort

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20reasoning_effort%20%3E%20(schema)

    * ### responseFormat

public com.google.adk.models.chat.ChatCompletionsRequest.ResponseFormat responseFormat

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20response_format%20%3E%20(schema)

    * ### safetyIdentifier

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") safetyIdentifier

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20safety_identifier%20%3E%20(schema)

    * ### seed

public [Long](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Long.html "class in java.lang") seed

Deprecated. Use temperature instead. See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20seed%20%3E%20(schema)

    * ### serviceTier

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") serviceTier

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20service_tier%20%3E%20(schema)

    * ### stop

public com.google.adk.models.chat.ChatCompletionsRequest.StopCondition stop

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stop%20%3E%20(schema)

    * ### store

public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") store

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20store%20%3E%20(schema)

    * ### stream

public [Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang") stream

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stream%20%3E%20(schema)

    * ### streamOptions

public com.google.adk.models.chat.ChatCompletionsRequest.StreamOptions streamOptions

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20stream_options%20%3E%20(schema)

    * ### temperature

public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang") temperature

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20temperature%20%3E%20(schema)

    * ### toolChoice

public com.google.adk.models.chat.ChatCompletionsRequest.ToolChoice toolChoice

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tool_choice%20%3E%20(schema)

    * ### tools

public [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.adk.models.chat.ChatCompletionsRequest.Tool> tools

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20tools%20%3E%20(schema)

    * ### topLogprobs

public [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang") topLogprobs

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20top_logprobs%20%3E%20(schema)

    * ### topP

public [Double](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html "class in java.lang") topP

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20top_p%20%3E%20(schema)

    * ### user

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") user

Deprecated, use safety_identifier and prompt_cache_key instead. See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20user%20%3E%20(schema)

    * ### verbosity

public [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") verbosity

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20verbosity%20%3E%20(schema)

    * ### webSearchOptions

public com.google.adk.models.chat.ChatCompletionsRequest.WebSearchOptions webSearchOptions

See https://developers.openai.com/api/reference/resources/chat/subresources/completions/methods/create#(resource)%20chat.completions%20%3E%20(method)%20create%20%3E%20(params)%200.non_streaming%20%3E%20(param)%20web_search_options%20%3E%20(schema)

    * ### extraBody

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> extraBody

Additional body parameters used for specific models, for example: https://ai.google.dev/gemini-api/docs/openai#extra-body

  * ## Constructor Details

    * ### ChatCompletionsRequest

public ChatCompletionsRequest()

  * ## Method Details

    * ### fromLlmRequest

public static [ChatCompletionsRequest](ChatCompletionsRequest.html "class in com.google.adk.models.chat") fromLlmRequest([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean responseStreaming)

Converts a standard [`LlmRequest`](../LlmRequest.html "class in com.google.adk.models") into a [`ChatCompletionsRequest`](ChatCompletionsRequest.html "class in com.google.adk.models.chat") for /chat/completions compatible endpoints.

Parameters:
    `llmRequest` \- The internal source request containing contents, configuration, and tool definitions.
    `responseStreaming` \- True if the request asks for a streaming response.
Returns:
    A populated ChatCompletionsRequest ready for JSON serialization.




* * *

Copyright (C) 1980\. All rights reserved.
