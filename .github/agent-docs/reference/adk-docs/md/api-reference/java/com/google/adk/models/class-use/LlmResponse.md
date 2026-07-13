JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../LlmResponse.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.models](../package-summary.html)
  2. [LlmResponse](../LlmResponse.html)



# Uses of Class  
com.google.adk.models.LlmResponse

Packages that use [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Package

Description

com.google.adk.agents

 

com.google.adk.flows.llmflows

 

com.google.adk.models

 

com.google.adk.models.chat

 

com.google.adk.models.langchain4j

 

com.google.adk.models.springai

 

com.google.adk.plugins

 

com.google.adk.plugins.agentanalytics

 

com.google.adk.plugins.recordings

 

com.google.adk.telemetry

 

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.agents](../../agents/package-summary.html)

Methods in [com.google.adk.agents](../../agents/package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallback.`[call](../../agents/Callbacks.AfterModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Async callback after LLM response.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallbackSync.`[call](../../agents/Callbacks.AfterModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallback.`[call](../../agents/Callbacks.BeforeModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder)`

Async callback before LLM invocation.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallbackSync.`[call](../../agents/Callbacks.BeforeModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequestBuilder)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.OnModelErrorCallback.`[call](../../agents/Callbacks.OnModelErrorCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest,java.lang.Exception\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

Async callback when model call fails.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.OnModelErrorCallbackSync.`[call](../../agents/Callbacks.OnModelErrorCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest,java.lang.Exception\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

 

Methods in [com.google.adk.agents](../../agents/package-summary.html) with parameters of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallback.`[call](../../agents/Callbacks.AfterModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Async callback after LLM response.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallbackSync.`[call](../../agents/Callbacks.AfterModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html)

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) that return [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

ResponseProcessor.ResponseProcessingResult.`[updatedResponse](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#updatedResponse\(\))()`

Updated LLM response.

Methods in [com.google.adk.flows.llmflows](../../flows/llmflows/package-summary.html) with parameters of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`static [ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

ResponseProcessor.ResponseProcessingResult.`[create](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#create\(com.google.adk.models.LlmResponse,java.lang.Iterable\))([LlmResponse](../LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events)`

 

`static [ResponseProcessor.ResponseProcessingResult](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

ResponseProcessor.ResponseProcessingResult.`[create](../../flows/llmflows/ResponseProcessor.ResponseProcessingResult.html#create\(com.google.adk.models.LlmResponse,java.lang.Iterable,java.lang.String\))([LlmResponse](../LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") transferToAgent)`

 

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

BaseLlmFlow.`[postprocess](../../flows/llmflows/BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse,io.opentelemetry.context.Context\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../../events/Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse, io.opentelemetry.context.Context parentContext)`

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

LlmResponse.`[create](../LlmResponse.html#create\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<com.google.genai.types.Candidate> candidates)`

 

Methods in [com.google.adk.models](../package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

ApigeeLlm.`[generateContent](../ApigeeLlm.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

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

 

Methods in [com.google.adk.models](../package-summary.html) with parameters of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`static [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<com.google.genai.types.Part>`

GeminiUtil.`[getPart0FromLlmResponse](../GeminiUtil.html#getPart0FromLlmResponse\(com.google.adk.models.LlmResponse\))([LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Extracts the first part of an LlmResponse, if available.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

GeminiUtil.`[getTextFromLlmResponse](../GeminiUtil.html#getTextFromLlmResponse\(com.google.adk.models.LlmResponse\))([LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Extracts text content from the first part of an LlmResponse, if available.

`static boolean`

GeminiUtil.`[shouldEmitAccumulatedText](../GeminiUtil.html#shouldEmitAccumulatedText\(com.google.adk.models.LlmResponse\))([LlmResponse](../LlmResponse.html "class in com.google.adk.models") currentLlmResponse)`

Determines if accumulated text should be emitted based on the current LlmResponse.

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.models.chat](../chat/package-summary.html)

Methods in [com.google.adk.models.chat](../chat/package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

ChatCompletionsClient.`[complete](../chat/ChatCompletionsClient.html#complete\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

Generates a conversational response from the chat completions endpoint based on the provided messages.

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

ChatCompletionsHttpClient.`[complete](../chat/ChatCompletionsHttpClient.html#complete\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.models.langchain4j](../langchain4j/package-summary.html)

Methods in [com.google.adk.models.langchain4j](../langchain4j/package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

LangChain4j.`[generateContent](../langchain4j/LangChain4j.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.models.springai](../springai/package-summary.html)

Methods in [com.google.adk.models.springai](../springai/package-summary.html) that return [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

StreamingResponseAggregator.`[getFinalResponse](../springai/StreamingResponseAggregator.html#getFinalResponse\(\))()`

Returns the final aggregated response and resets the aggregator.

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

StreamingResponseAggregator.`[processStreamingResponse](../springai/StreamingResponseAggregator.html#processStreamingResponse\(com.google.adk.models.LlmResponse\))([LlmResponse](../LlmResponse.html "class in com.google.adk.models") response)`

Processes a streaming LlmResponse and returns the current aggregated state.

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

MessageConverter.`[toLlmResponse](../springai/MessageConverter.html#toLlmResponse\(org.springframework.ai.chat.model.ChatResponse\))(org.springframework.ai.chat.model.ChatResponse chatResponse)`

Converts a Spring AI ChatResponse to an ADK LlmResponse.

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

MessageConverter.`[toLlmResponse](../springai/MessageConverter.html#toLlmResponse\(org.springframework.ai.chat.model.ChatResponse,boolean\))(org.springframework.ai.chat.model.ChatResponse chatResponse, boolean isStreaming)`

Converts a Spring AI ChatResponse to an ADK LlmResponse with streaming context.

Methods in [com.google.adk.models.springai](../springai/package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

SpringAI.`[generateContent](../springai/SpringAI.html#generateContent\(com.google.adk.models.LlmRequest,boolean\))([LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, boolean stream)`

 

Methods in [com.google.adk.models.springai](../springai/package-summary.html) with parameters of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`[LlmResponse](../LlmResponse.html "class in com.google.adk.models")`

StreamingResponseAggregator.`[processStreamingResponse](../springai/StreamingResponseAggregator.html#processStreamingResponse\(com.google.adk.models.LlmResponse\))([LlmResponse](../LlmResponse.html "class in com.google.adk.models") response)`

Processes a streaming LlmResponse and returns the current aggregated state.

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.plugins](../../plugins/package-summary.html)

Methods in [com.google.adk.plugins](../../plugins/package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

LoggingPlugin.`[afterModelCallback](../../plugins/LoggingPlugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Plugin.`[afterModelCallback](../../plugins/Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Callback executed after a response is received from the model.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

PluginManager.`[afterModelCallback](../../plugins/PluginManager.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

ContextFilterPlugin.`[beforeModelCallback](../../plugins/ContextFilterPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Filters the LLM request context by trimming recent turns and applying any custom filter.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

GlobalInstructionPlugin.`[beforeModelCallback](../../plugins/GlobalInstructionPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

LoggingPlugin.`[beforeModelCallback](../../plugins/LoggingPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Plugin.`[beforeModelCallback](../../plugins/Plugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Callback executed before a request is sent to the model.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

PluginManager.`[beforeModelCallback](../../plugins/PluginManager.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

ReplayPlugin.`[beforeModelCallback](../../plugins/ReplayPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

LoggingPlugin.`[onModelErrorCallback](../../plugins/LoggingPlugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

 

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Plugin.`[onModelErrorCallback](../../plugins/Plugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

Callback executed when a model call encounters an error.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

PluginManager.`[onModelErrorCallback](../../plugins/PluginManager.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

 

Methods in [com.google.adk.plugins](../../plugins/package-summary.html) with parameters of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

LoggingPlugin.`[afterModelCallback](../../plugins/LoggingPlugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`default io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

Plugin.`[afterModelCallback](../../plugins/Plugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

Callback executed after a response is received from the model.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

PluginManager.`[afterModelCallback](../../plugins/PluginManager.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html)

Methods in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

BigQueryAgentAnalyticsPlugin.`[afterModelCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

BigQueryAgentAnalyticsPlugin.`[beforeModelCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#beforeModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest)`

Callback before LLM call.

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

BigQueryAgentAnalyticsPlugin.`[onModelErrorCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#onModelErrorCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest.Builder,java.lang.Throwable\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest.Builder](../LlmRequest.Builder.html "class in com.google.adk.models") llmRequest, [Throwable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Throwable.html "class in java.lang") error)`

 

Methods in [com.google.adk.plugins.agentanalytics](../../plugins/agentanalytics/package-summary.html) with parameters of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>`

BigQueryAgentAnalyticsPlugin.`[afterModelCallback](../../plugins/agentanalytics/BigQueryAgentAnalyticsPlugin.html#afterModelCallback\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../../agents/CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.plugins.recordings](../../plugins/recordings/package-summary.html)

Methods in [com.google.adk.plugins.recordings](../../plugins/recordings/package-summary.html) that return types with arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")>>`

LlmRecording.`[llmResponses](../../plugins/recordings/LlmRecording.html#llmResponses\(\))()`

The LLM responses.

Method parameters in [com.google.adk.plugins.recordings](../../plugins/recordings/package-summary.html) with type arguments of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`abstract [LlmRecording.Builder](../../plugins/recordings/LlmRecording.Builder.html "class in com.google.adk.plugins.recordings")`

LlmRecording.Builder.`[llmResponses](../../plugins/recordings/LlmRecording.Builder.html#llmResponses\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[LlmResponse](../LlmResponse.html "class in com.google.adk.models")> llmResponses)`

 

  * ## Uses of [LlmResponse](../LlmResponse.html "class in com.google.adk.models") in [com.google.adk.telemetry](../../telemetry/package-summary.html)

Methods in [com.google.adk.telemetry](../../telemetry/package-summary.html) with parameters of type [LlmResponse](../LlmResponse.html "class in com.google.adk.models")

Modifier and Type

Method

Description

`static void`

Tracing.`[traceCallLlm](../../telemetry/Tracing.html#traceCallLlm\(io.opentelemetry.api.trace.Span,com.google.adk.agents.InvocationContext,java.lang.String,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse,java.lang.Exception\))(io.opentelemetry.api.trace.Span span, [InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventId, [LlmRequest](../LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../LlmResponse.html "class in com.google.adk.models") llmResponse, @Nullable [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

Traces a call to the LLM.




* * *

Copyright (C) 1980\. All rights reserved.
