JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../LlmRequest.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.models](../package-summary.html)
  2. [LlmRequest](../LlmRequest.html)



# Uses of Class  
com.google.adk.models.LlmRequest

Packages that use [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Package

Description

com.google.adk

 

com.google.adk.agents

 

com.google.adk.flows.llmflows

 

com.google.adk.models

 

com.google.adk.models.langchain4j

 

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk](../../package-summary.html)

Methods in [com.google.adk](../../package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`static void`

Telemetry.`[traceCallLlm](../../Telemetry.html#traceCallLlm\(com.google.adk.agents.InvocationContext,java.lang.String,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") eventId, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Traces a call to the LLM.

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallback.`[call](../../agents/Callbacks.BeforeModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Async callback before LLM invocation.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallbackSync.`[call](../../agents/Callbacks.BeforeModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) that return [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

RequestProcessor.RequestProcessingResult.`[updatedRequest](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html#updatedRequest\(\))()`

 

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`static [RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

RequestProcessor.RequestProcessingResult.`[create](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html#create\(com.google.adk.models.LlmRequest,java.lang.Iterable\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") updatedRequest, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events)`

 

`protected io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../../events/Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Post-processes the LLM response after receiving it from the LLM.

`protected io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

BaseLlmFlow.`[preprocess](../../flows/llmflows/BaseLlmFlow.html#preprocess\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Pre-processes the LLM request before sending it to the LLM.

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

AgentTransfer.`[processRequest](../../flows/llmflows/AgentTransfer.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Basic.`[processRequest](../../flows/llmflows/Basic.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Contents.`[processRequest](../../flows/llmflows/Contents.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Examples.`[processRequest](../../flows/llmflows/Examples.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Identity.`[processRequest](../../flows/llmflows/Identity.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Instructions.`[processRequest](../../flows/llmflows/Instructions.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

RequestProcessor.`[processRequest](../../flows/llmflows/RequestProcessor.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

Process the LLM request as part of the pre-processing stage.

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk.models](../package-summary.html)

Methods in [com.google.adk.models](../package-summary.html) that return [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

LlmRequest.Builder.`[build](../LlmRequest.Builder.html#build\(\))()`

 

Methods in [com.google.adk.models](../package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

BaseLlm.`[connect](../BaseLlm.html#connect\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Creates a live connection to the LLM.

`[BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

Claude.`[connect](../Claude.html#connect\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

`[BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

Gemini.`[connect](../Gemini.html#connect\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

`abstract io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

BaseLlm.`[generateContent](../BaseLlm.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

Generates one content from the given LLM request and tools.

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Claude.`[generateContent](../Claude.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Gemini.`[generateContent](../Gemini.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk.models.langchain4j](../langchain4j/package-summary.html)

Methods in [com.google.adk.models.langchain4j](../langchain4j/package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

LangChain4j.`[connect](../langchain4j/LangChain4j.html#connect\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

LangChain4j.`[generateContent](../langchain4j/LangChain4j.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 




* * *

Copyright (C) 2025\. All rights reserved.
