[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.5.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.models](../index.html)/LlmResponse

# LlmResponse

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [LlmResponse](index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val content: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, val usageMetadata: [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)? = null, val finishReason: [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)? = null, val errorMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val partial: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val interrupted: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val modelVersion: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)? = null, val groundingMetadata: [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)? = null, val errorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null, val avgLogprobs: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, val logprobsResult: [LogprobsResult](../../com.google.adk.kt.types/-logprobs-result/index.html)? = null, val cacheMetadata: [CacheMetadata](../-cache-metadata/index.html)? = null, val turnComplete: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val turnCompleteReason: [TurnCompleteReason](../../com.google.adk.kt.types/-turn-complete-reason/index.html)? = null, val interactionStatus: [InteractionStatus](../../com.google.adk.kt.types/-interaction-status/index.html)? = null, val inputTranscription: [Transcription](../../com.google.adk.kt.types/-transcription/index.html)? = null, val outputTranscription: [Transcription](../../com.google.adk.kt.types/-transcription/index.html)? = null, val liveSessionId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val liveSessionResumptionUpdate: [LiveServerSessionResumptionUpdate](../../com.google.adk.kt.types/-live-server-session-resumption-update/index.html)? = null, val goAway: [LiveServerGoAway](../../com.google.adk.kt.types/-live-server-go-away/index.html)? = null, val voiceActivity: [VoiceActivity](../../com.google.adk.kt.types/-voice-activity/index.html)? = null)

LLM response class that provides the first candidate response from the model if available. Otherwise, contains the error code and message.

Members

## Constructors

[LlmResponse](-llm-response.html)

Link copied to clipboard

common

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

constructor(content: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, usageMetadata: [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)? = null, finishReason: [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)? = null, errorMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, partial: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, interrupted: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, modelVersion: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, citationMetadata: [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)? = null, groundingMetadata: [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)? = null, errorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null, avgLogprobs: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, logprobsResult: [LogprobsResult](../../com.google.adk.kt.types/-logprobs-result/index.html)? = null, cacheMetadata: [CacheMetadata](../-cache-metadata/index.html)? = null, turnComplete: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, turnCompleteReason: [TurnCompleteReason](../../com.google.adk.kt.types/-turn-complete-reason/index.html)? = null, interactionStatus: [InteractionStatus](../../com.google.adk.kt.types/-interaction-status/index.html)? = null, inputTranscription: [Transcription](../../com.google.adk.kt.types/-transcription/index.html)? = null, outputTranscription: [Transcription](../../com.google.adk.kt.types/-transcription/index.html)? = null, liveSessionId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, liveSessionResumptionUpdate: [LiveServerSessionResumptionUpdate](../../com.google.adk.kt.types/-live-server-session-resumption-update/index.html)? = null, goAway: [LiveServerGoAway](../../com.google.adk.kt.types/-live-server-go-away/index.html)? = null, voiceActivity: [VoiceActivity](../../com.google.adk.kt.types/-voice-activity/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [LlmResponse](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[avgLogprobs](avg-logprobs.html)

Link copied to clipboard

common

val [avgLogprobs](avg-logprobs.html): [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)?

[cacheMetadata](cache-metadata.html)

Link copied to clipboard

common

val [cacheMetadata](cache-metadata.html): [CacheMetadata](../-cache-metadata/index.html)?

Context cache metadata for this response, populated when context caching is enabled. `null` when caching is disabled or no cache information is available.

[citationMetadata](citation-metadata.html)

Link copied to clipboard

common

val [citationMetadata](citation-metadata.html): [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)?

The citation metadata of the response.

[content](content.html)

Link copied to clipboard

common

val [content](content.html): [Content](../../com.google.adk.kt.types/-content/index.html)?

The generative content of the response. This should only contain content from the user or the model, and not any framework or system-generated data.

[customMetadata](custom-metadata.html)

Link copied to clipboard

common

val [customMetadata](custom-metadata.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>?

Optional key-value pairs labeling the response. The entire map must be JSON serializable.

[errorCode](error-code.html)

Link copied to clipboard

common

val [errorCode](error-code.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

Error code if the response is an error. The code varies by model.

[errorMessage](error-message.html)

Link copied to clipboard

common

val [errorMessage](error-message.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

Error message if the response is an error.

[finishReason](finish-reason.html)

Link copied to clipboard

common

val [finishReason](finish-reason.html): [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)?

The finish reason of the response.

[goAway](go-away.html)

Link copied to clipboard

common

val [goAway](go-away.html): [LiveServerGoAway](../../com.google.adk.kt.types/-live-server-go-away/index.html)?

Warning that the server will stop serving this connection shortly. Live only.

[groundingMetadata](grounding-metadata.html)

Link copied to clipboard

common

val [groundingMetadata](grounding-metadata.html): [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)?

The grounding metadata of the response.

[inputTranscription](input-transcription.html)

Link copied to clipboard

common

val [inputTranscription](input-transcription.html): [Transcription](../../com.google.adk.kt.types/-transcription/index.html)?

Transcription of the audio the user sent. Live only.

[interactionStatus](interaction-status.html)

Link copied to clipboard

common

val [interactionStatus](interaction-status.html): [InteractionStatus](../../com.google.adk.kt.types/-interaction-status/index.html)?

Whether the model is still working on the prompt, reported only with [turnComplete](../../../google-adk-kotlin-core/com.google.adk.kt.models/-llm-response/--root--.html); see [InteractionStatus](../../com.google.adk.kt.types/-interaction-status/index.html). On a completed turn, `null` means the model does not report it and is done. Live only.

[interrupted](interrupted.html)

Link copied to clipboard

common

val [interrupted](interrupted.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Flag indicating that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

[liveSessionId](live-session-id.html)

Link copied to clipboard

common

val [liveSessionId](live-session-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

Identifier of the live session this response came from. Live only.

[liveSessionResumptionUpdate](live-session-resumption-update.html)

Link copied to clipboard

common

val [liveSessionResumptionUpdate](live-session-resumption-update.html): [LiveServerSessionResumptionUpdate](../../com.google.adk.kt.types/-live-server-session-resumption-update/index.html)?

A handle for resuming this session on a later connection. Live only.

[logprobsResult](logprobs-result.html)

Link copied to clipboard

common

val [logprobsResult](logprobs-result.html): [LogprobsResult](../../com.google.adk.kt.types/-logprobs-result/index.html)?

[modelVersion](model-version.html)

Link copied to clipboard

common

val [modelVersion](model-version.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The model version used to generate the response.

[outputTranscription](output-transcription.html)

Link copied to clipboard

common

val [outputTranscription](output-transcription.html): [Transcription](../../com.google.adk.kt.types/-transcription/index.html)?

Transcription of the audio the model returned. Live only.

[partial](partial.html)

Link copied to clipboard

common

val [partial](partial.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether this response is an incomplete fragment of a streamed response, such as a text chunk or an unfinished transcription. Only used in streaming mode.

[turnComplete](turn-complete.html)

Link copied to clipboard

common

val [turnComplete](turn-complete.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)?

Whether the model has finished its turn. Live only.

[turnCompleteReason](turn-complete-reason.html)

Link copied to clipboard

common

val [turnCompleteReason](turn-complete-reason.html): [TurnCompleteReason](../../com.google.adk.kt.types/-turn-complete-reason/index.html)?

Why the turn ended, when it ended for a reason other than ordinary completion. Live only.

[usageMetadata](usage-metadata.html)

Link copied to clipboard

common

val [usageMetadata](usage-metadata.html): [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)?

The usage metadata of the LlmResponse.

[voiceActivity](voice-activity.html)

Link copied to clipboard

common

val [voiceActivity](voice-activity.html): [VoiceActivity](../../com.google.adk.kt.types/-voice-activity/index.html)?

A server-detected change in whether the user is speaking. Live only.

## Functions

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [LlmResponse.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
