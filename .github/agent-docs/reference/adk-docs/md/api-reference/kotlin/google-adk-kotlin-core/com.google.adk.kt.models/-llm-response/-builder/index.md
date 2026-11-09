[ google-adk-kotlin ](../../../../index.html) Toggle table of contents 

1.5.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../../index.html)/[com.google.adk.kt.models](../../index.html)/[LlmResponse](../index.html)/Builder

# Builder

common

class [Builder](index.html)

Fluent builder for [LlmResponse](../index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

Members

## Constructors

[Builder](-builder.html)

Link copied to clipboard

common

constructor()

## Functions

[avgLogprobs](avg-logprobs.html)

Link copied to clipboard

common

fun [avgLogprobs](avg-logprobs.html)(avgLogprobs: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)?): [LlmResponse.Builder](index.html)

[build](build.html)

Link copied to clipboard

common

fun [build](build.html)(): [LlmResponse](../index.html)

[cacheMetadata](cache-metadata.html)

Link copied to clipboard

common

fun [cacheMetadata](cache-metadata.html)(cacheMetadata: [CacheMetadata](../../-cache-metadata/index.html)?): [LlmResponse.Builder](index.html)

[citationMetadata](citation-metadata.html)

Link copied to clipboard

common

fun [citationMetadata](citation-metadata.html)(citationMetadata: [CitationMetadata](../../../com.google.adk.kt.types/-citation-metadata/index.html)?): [LlmResponse.Builder](index.html)

[content](content.html)

Link copied to clipboard

common

fun [content](content.html)(content: [Content](../../../com.google.adk.kt.types/-content/index.html)?): [LlmResponse.Builder](index.html)

[customMetadata](custom-metadata.html)

Link copied to clipboard

common

fun [customMetadata](custom-metadata.html)(customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>?): [LlmResponse.Builder](index.html)

[errorCode](error-code.html)

Link copied to clipboard

common

fun [errorCode](error-code.html)(errorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?): [LlmResponse.Builder](index.html)

[errorMessage](error-message.html)

Link copied to clipboard

common

fun [errorMessage](error-message.html)(errorMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?): [LlmResponse.Builder](index.html)

[finishReason](finish-reason.html)

Link copied to clipboard

common

fun [finishReason](finish-reason.html)(finishReason: [FinishReason](../../../com.google.adk.kt.types/-finish-reason/index.html)?): [LlmResponse.Builder](index.html)

[goAway](go-away.html)

Link copied to clipboard

common

fun [goAway](go-away.html)(goAway: [LiveServerGoAway](../../../com.google.adk.kt.types/-live-server-go-away/index.html)?): [LlmResponse.Builder](index.html)

[groundingMetadata](grounding-metadata.html)

Link copied to clipboard

common

fun [groundingMetadata](grounding-metadata.html)(groundingMetadata: [GroundingMetadata](../../../com.google.adk.kt.types/-grounding-metadata/index.html)?): [LlmResponse.Builder](index.html)

[inputTranscription](input-transcription.html)

Link copied to clipboard

common

fun [inputTranscription](input-transcription.html)(inputTranscription: [Transcription](../../../com.google.adk.kt.types/-transcription/index.html)?): [LlmResponse.Builder](index.html)

[interactionStatus](interaction-status.html)

Link copied to clipboard

common

fun [interactionStatus](interaction-status.html)(interactionStatus: [InteractionStatus](../../../com.google.adk.kt.types/-interaction-status/index.html)?): [LlmResponse.Builder](index.html)

[interrupted](interrupted.html)

Link copied to clipboard

common

fun [interrupted](interrupted.html)(interrupted: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [LlmResponse.Builder](index.html)

[liveSessionId](live-session-id.html)

Link copied to clipboard

common

fun [liveSessionId](live-session-id.html)(liveSessionId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?): [LlmResponse.Builder](index.html)

[liveSessionResumptionUpdate](live-session-resumption-update.html)

Link copied to clipboard

common

fun [liveSessionResumptionUpdate](live-session-resumption-update.html)(liveSessionResumptionUpdate: [LiveServerSessionResumptionUpdate](../../../com.google.adk.kt.types/-live-server-session-resumption-update/index.html)?): [LlmResponse.Builder](index.html)

[logprobsResult](logprobs-result.html)

Link copied to clipboard

common

fun [logprobsResult](logprobs-result.html)(logprobsResult: [LogprobsResult](../../../com.google.adk.kt.types/-logprobs-result/index.html)?): [LlmResponse.Builder](index.html)

[modelVersion](model-version.html)

Link copied to clipboard

common

fun [modelVersion](model-version.html)(modelVersion: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?): [LlmResponse.Builder](index.html)

[outputTranscription](output-transcription.html)

Link copied to clipboard

common

fun [outputTranscription](output-transcription.html)(outputTranscription: [Transcription](../../../com.google.adk.kt.types/-transcription/index.html)?): [LlmResponse.Builder](index.html)

[partial](partial.html)

Link copied to clipboard

common

fun [partial](partial.html)(partial: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [LlmResponse.Builder](index.html)

[turnComplete](turn-complete.html)

Link copied to clipboard

common

fun [turnComplete](turn-complete.html)(turnComplete: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)?): [LlmResponse.Builder](index.html)

[turnCompleteReason](turn-complete-reason.html)

Link copied to clipboard

common

fun [turnCompleteReason](turn-complete-reason.html)(turnCompleteReason: [TurnCompleteReason](../../../com.google.adk.kt.types/-turn-complete-reason/index.html)?): [LlmResponse.Builder](index.html)

[usageMetadata](usage-metadata.html)

Link copied to clipboard

common

fun [usageMetadata](usage-metadata.html)(usageMetadata: [UsageMetadata](../../../com.google.adk.kt.types/-usage-metadata/index.html)?): [LlmResponse.Builder](index.html)

[voiceActivity](voice-activity.html)

Link copied to clipboard

common

fun [voiceActivity](voice-activity.html)(voiceActivity: [VoiceActivity](../../../com.google.adk.kt.types/-voice-activity/index.html)?): [LlmResponse.Builder](index.html)

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
