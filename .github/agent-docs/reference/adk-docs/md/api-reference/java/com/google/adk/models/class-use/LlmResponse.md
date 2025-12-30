JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../LlmResponse.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.models](../package-summary.html)
  2. [LlmResponse](../LlmResponse.html)



# Uses of Class  
com.google.adk.models.LlmResponse

Packages that use [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Package

Description

com.google.adk

 

com.google.adk.agents

 

com.google.adk.flows.llmflows

 

com.google.adk.models

 

com.google.adk.models.langchain4j

 

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk](../../package-summary.html)

Methods in [com.google.adk](../../package-summary.html) with parameters of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`static void`

Telemetry.`[traceCallLlm](../../Telemetry.html#traceCallLlm\(com.google.adk.agents.InvocationContext,java.lang.String,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Traces a call to the LLM.

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallback.`[call](../../agents/Callbacks.AfterModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Async callback after LLM response.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallbackSync.`[call](../../agents/Callbacks.AfterModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallback.`[call](../../agents/Callbacks.BeforeModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Async callback before LLM invocation.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallbackSync.`[call](../../agents/Callbacks.BeforeModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallback.`[call](../../agents/Callbacks.AfterModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Async callback after LLM response.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallbackSync.`[call](../../agents/Callbacks.AfterModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) that return [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

ResponseProcessor.ResponseProcessingResult.`[updatedResponse](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#updatedResponse\(\))()`

 

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`static [ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

ResponseProcessor.ResponseProcessingResult.`[create](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#create\(com.google.adk.models.LlmResponse,java.lang.Iterable,java.util.Optional\))([LlmResponse](../LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> transferToAgent)`

 

`protected io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../../events/Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Post-processes the LLM response after receiving it from the LLM.

`io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

ResponseProcessor.`[processResponse](../../flows/llmflows/ResponseProcessor.html#processResponse\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmResponse\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") response)`

Process the LLM response as part of the post-processing stage.

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.models](../package-summary.html)

Methods in [com.google.adk.models](../package-summary.html) that return [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

LlmResponse.Builder.`[build](../LlmResponse.Builder.html#build\(\))()`

 

`static [LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

LlmResponse.`[create](../LlmResponse.html#create\(com.google.genai.types.GenerateContentResponse\))(com.google.genai.types.GenerateContentResponse response)`

 

`static [LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

LlmResponse.`[create](../LlmResponse.html#create\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<com.google.genai.types.Candidate> candidates)`

 

Methods in [com.google.adk.models](../package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

BaseLlm.`[generateContent](../BaseLlm.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

Generates one content from the given LLM request and tools.

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Claude.`[generateContent](../Claude.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Gemini.`[generateContent](../Gemini.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

BaseLlmConnection.`[receive](../BaseLlmConnection.html#receive\(\))()`

Receives the model responses.

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

GeminiLlmConnection.`[receive](../GeminiLlmConnection.html#receive\(\))()`

 

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.models.langchain4j](../langchain4j/package-summary.html)

Methods in [com.google.adk.models.langchain4j](../langchain4j/package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

LangChain4j.`[generateContent](../langchain4j/LangChain4j.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 




* * *

Copyright (C) 2025\. All rights reserved.
