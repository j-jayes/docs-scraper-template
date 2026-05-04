JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../LlmRequest.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](../package-summary.html)
  2. [LlmRequest](../LlmRequest.html)



# Uses of Class  
com.google.adk.models.LlmRequest

Packages that use [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Package

Description

com.google.adk.agents

 

com.google.adk.flows.llmflows

 

com.google.adk.models

 

com.google.adk.models.langchain4j

 

com.google.adk.models.springai

 

com.google.adk.plugins.recordings

 

com.google.adk.telemetry

 

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.OnModelErrorCallback.`[call](../../agents/Callbacks.OnModelErrorCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest,java.lang.Exception\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

Async callback when model call fails.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.OnModelErrorCallbackSync.`[call](../../agents/Callbacks.OnModelErrorCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest,java.lang.Exception\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

 

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) that return [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

RequestProcessor.RequestProcessingResult.`[updatedRequest](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html#updatedRequest\(\))()`

Updated LLM request.

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`static [RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

RequestProcessor.RequestProcessingResult.`[create](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html#create\(com.google.adk.models.LlmRequest,java.lang.Iterable\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") updatedRequest, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events)`

Creates a new [`RequestProcessor.RequestProcessingResult`](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows").

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse,io.opentelemetry.context.Context\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../../events/Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse, io.opentelemetry.context.Context parentContext)`

Post-processes the LLM response after receiving it from the LLM.

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

AgentTransfer.`[processRequest](../../flows/llmflows/AgentTransfer.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Basic.`[processRequest](../../flows/llmflows/Basic.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Compaction.`[processRequest](../../flows/llmflows/Compaction.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Contents.`[processRequest](../../flows/llmflows/Contents.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Identity.`[processRequest](../../flows/llmflows/Identity.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

Instructions.`[processRequest](../../flows/llmflows/Instructions.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

OutputSchema.`[processRequest](../../flows/llmflows/OutputSchema.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") request)`

 

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](../../flows/llmflows/RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

RequestConfirmationLlmRequestProcessor.`[processRequest](../../flows/llmflows/RequestConfirmationLlmRequestProcessor.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

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

 

`static [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

GeminiUtil.`[prepareGenenerateContentRequest](../GeminiUtil.html#prepareGenenerateContentRequest\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean sanitize)`

Prepares an [`LlmRequest`](../LlmRequest.html "class in com.google.adk.models") for the GenerateContent API.

`static [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

GeminiUtil.`[prepareGenenerateContentRequest](../GeminiUtil.html#prepareGenenerateContentRequest\(com.google.adk.models.LlmRequest,boolean,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean sanitize, boolean stripThoughts)`

Prepares an [`LlmRequest`](../LlmRequest.html "class in com.google.adk.models") for the GenerateContent API.

`static [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

GeminiUtil.`[removeClientFunctionCallId](../GeminiUtil.html#removeClientFunctionCallId\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Removes client-side function call IDs from the request.

`static [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

GeminiUtil.`[sanitizeRequestForGeminiApi](../GeminiUtil.html#sanitizeRequestForGeminiApi\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Sanitizes the request to ensure it is compatible with the Gemini API backend.

Methods in [com.google.adk.models](../package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

ApigeeLlm.`[connect](../ApigeeLlm.html#connect\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

`abstract [BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

BaseLlm.`[connect](../BaseLlm.html#connect\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Creates a live connection to the LLM.

`[BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

Claude.`[connect](../Claude.html#connect\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

`[BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

Gemini.`[connect](../Gemini.html#connect\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

ApigeeLlm.`[generateContent](../ApigeeLlm.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

`abstract io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

BaseLlm.`[generateContent](../BaseLlm.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

Generates one content from the given LLM request and tools.

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Claude.`[generateContent](../Claude.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Gemini.`[generateContent](../Gemini.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

`static [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

GeminiUtil.`[prepareGenenerateContentRequest](../GeminiUtil.html#prepareGenenerateContentRequest\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean sanitize)`

Prepares an [`LlmRequest`](../LlmRequest.html "class in com.google.adk.models") for the GenerateContent API.

`static [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

GeminiUtil.`[prepareGenenerateContentRequest](../GeminiUtil.html#prepareGenenerateContentRequest\(com.google.adk.models.LlmRequest,boolean,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean sanitize, boolean stripThoughts)`

Prepares an [`LlmRequest`](../LlmRequest.html "class in com.google.adk.models") for the GenerateContent API.

`static [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

GeminiUtil.`[removeClientFunctionCallId](../GeminiUtil.html#removeClientFunctionCallId\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Removes client-side function call IDs from the request.

`static [LlmRequest](../LlmRequest.html "class in com.google.adk.models")`

GeminiUtil.`[sanitizeRequestForGeminiApi](../GeminiUtil.html#sanitizeRequestForGeminiApi\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Sanitizes the request to ensure it is compatible with the Gemini API backend.

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk.models.langchain4j](../langchain4j/package-summary.html)

Methods in [com.google.adk.models.langchain4j](../langchain4j/package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

LangChain4j.`[connect](../langchain4j/LangChain4j.html#connect\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

LangChain4j.`[generateContent](../langchain4j/LangChain4j.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk.models.springai](../springai/package-summary.html)

Methods in [com.google.adk.models.springai](../springai/package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[BaseLlmConnection](../BaseLlmConnection.html "interface in com.google.adk.models")`

SpringAI.`[connect](../springai/SpringAI.html#connect\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

SpringAI.`[generateContent](../springai/SpringAI.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"), [ToolConverter.ToolMetadata](../springai/ToolConverter.ToolMetadata.html "class in com.google.adk.models.springai")>`

MessageConverter.`[getToolRegistry](../springai/MessageConverter.html#getToolRegistry\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Gets tool registry from ADK tools for internal tracking.

`org.springframework.ai.chat.prompt.Prompt`

MessageConverter.`[toLlmPrompt](../springai/MessageConverter.html#toLlmPrompt\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

Converts an ADK LlmRequest to a Spring AI Prompt.

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk.plugins.recordings](../../plugins/recordings/package-summary.html)

Methods in [com.google.adk.plugins.recordings](../../plugins/recordings/package-summary.html) that return types with arguments of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmRequest](../LlmRequest.html "class in com.google.adk.models")>`

LlmRecording.`[llmRequest](../../plugins/recordings/LlmRecording.html#llmRequest\(\))()`

The LLM request.

Methods in [com.google.adk.plugins.recordings](../../plugins/recordings/package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [LlmRecording.Builder](../../plugins/recordings/LlmRecording.Builder.html "class in com.google.adk.plugins.recordings")`

LlmRecording.Builder.`[llmRequest](../../plugins/recordings/LlmRecording.Builder.html#llmRequest\(com.google.adk.models.LlmRequest\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

  * ## Uses of [LlmRequest](../LlmRequest.html "class in com.google.adk.models") in [com.google.adk.telemetry](../../telemetry/package-summary.html)

Methods in [com.google.adk.telemetry](../../telemetry/package-summary.html) with parameters of type [LlmRequest](../LlmRequest.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`static void`

Tracing.`[traceCallLlm](../../telemetry/Tracing.html#traceCallLlm\(io.opentelemetry.api.trace.Span,com.google.adk.agents.InvocationContext,java.lang.String,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse,java.lang.Exception\))(io.opentelemetry.api.trace.Span span, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse, @Nullable [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

Traces a call to the LLM.




* * *

Copyright (C) 1980\. All rights reserved.
