[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.5.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.types](../index.html)/LiveConnectConfig

# LiveConnectConfig

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [LiveConnectConfig](index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val responseModalities: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Modality](../-modality/index.html)>? = null, val temperature: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null, val topP: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null, val topK: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val maxOutputTokens: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val mediaResolution: [MediaResolution](../-media-resolution/index.html)? = null, val seed: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val speechConfig: [SpeechConfig](../-speech-config/index.html)? = null, val thinkingConfig: [ThinkingConfig](../-thinking-config/index.html)? = null, val enableAffectiveDialog: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val systemInstruction: [Content](../-content/index.html)? = null, val tools: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Tool](../-tool/index.html)>? = null, val sessionResumption: [SessionResumptionConfig](../-session-resumption-config/index.html)? = null, val inputAudioTranscription: [AudioTranscriptionConfig](../-audio-transcription-config/index.html)? = null, val outputAudioTranscription: [AudioTranscriptionConfig](../-audio-transcription-config/index.html)? = null, val realtimeInputConfig: [RealtimeInputConfig](../-realtime-input-config/index.html)? = null, val contextWindowCompression: [ContextWindowCompressionConfig](../-context-window-compression-config/index.html)? = null, val proactivity: [ProactivityConfig](../-proactivity-config/index.html)? = null, val safetySettings: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[SafetySetting](../-safety-setting/index.html)>? = null, val explicitVadSignal: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val translationConfig: [TranslationConfig](../-translation-config/index.html)? = null)

Configuration for a live (bidirectional streaming) model connection.

This is sent once, when the connection is established, and governs the whole session; it cannot be changed per turn.

Members

## Constructors

[LiveConnectConfig](-live-connect-config.html)

Link copied to clipboard

common

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

constructor(responseModalities: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Modality](../-modality/index.html)>? = null, temperature: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null, topP: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null, topK: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, maxOutputTokens: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, mediaResolution: [MediaResolution](../-media-resolution/index.html)? = null, seed: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, speechConfig: [SpeechConfig](../-speech-config/index.html)? = null, thinkingConfig: [ThinkingConfig](../-thinking-config/index.html)? = null, enableAffectiveDialog: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, systemInstruction: [Content](../-content/index.html)? = null, tools: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Tool](../-tool/index.html)>? = null, sessionResumption: [SessionResumptionConfig](../-session-resumption-config/index.html)? = null, inputAudioTranscription: [AudioTranscriptionConfig](../-audio-transcription-config/index.html)? = null, outputAudioTranscription: [AudioTranscriptionConfig](../-audio-transcription-config/index.html)? = null, realtimeInputConfig: [RealtimeInputConfig](../-realtime-input-config/index.html)? = null, contextWindowCompression: [ContextWindowCompressionConfig](../-context-window-compression-config/index.html)? = null, proactivity: [ProactivityConfig](../-proactivity-config/index.html)? = null, safetySettings: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[SafetySetting](../-safety-setting/index.html)>? = null, explicitVadSignal: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, translationConfig: [TranslationConfig](../-translation-config/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [LiveConnectConfig](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[contextWindowCompression](context-window-compression.html)

Link copied to clipboard

common

val [contextWindowCompression](context-window-compression.html): [ContextWindowCompressionConfig](../-context-window-compression-config/index.html)?

Keeps the session's context below a given length.

[enableAffectiveDialog](enable-affective-dialog.html)

Link copied to clipboard

common

val [enableAffectiveDialog](enable-affective-dialog.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)?

Whether the model detects emotion and adapts its responses.

[explicitVadSignal](explicit-vad-signal.html)

Link copied to clipboard

common

val [explicitVadSignal](explicit-vad-signal.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)?

Whether the model sends its voice activity detection signals.

[inputAudioTranscription](input-audio-transcription.html)

Link copied to clipboard

common

val [inputAudioTranscription](input-audio-transcription.html): [AudioTranscriptionConfig](../-audio-transcription-config/index.html)?

Transcription of the audio the user sends. Unset disables it.

[maxOutputTokens](max-output-tokens.html)

Link copied to clipboard

common

val [maxOutputTokens](max-output-tokens.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)?

Maximum number of tokens that can be generated in a response.

[mediaResolution](media-resolution.html)

Link copied to clipboard

common

val [mediaResolution](media-resolution.html): [MediaResolution](../-media-resolution/index.html)?

The resolution used when processing media input.

[outputAudioTranscription](output-audio-transcription.html)

Link copied to clipboard

common

val [outputAudioTranscription](output-audio-transcription.html): [AudioTranscriptionConfig](../-audio-transcription-config/index.html)?

Transcription of the audio the model returns. Unset disables it.

[proactivity](proactivity.html)

Link copied to clipboard

common

val [proactivity](proactivity.html): [ProactivityConfig](../-proactivity-config/index.html)?

Whether the model may decline to respond to a prompt.

[realtimeInputConfig](realtime-input-config.html)

Link copied to clipboard

common

val [realtimeInputConfig](realtime-input-config.html): [RealtimeInputConfig](../-realtime-input-config/index.html)?

How realtime input is interpreted as turns, including voice activity detection.

[responseModalities](response-modalities.html)

Link copied to clipboard

common

val [responseModalities](response-modalities.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Modality](../-modality/index.html)>?

The modalities the model may return. Defaults to audio when unset.

[safetySettings](safety-settings.html)

Link copied to clipboard

common

val [safetySettings](safety-settings.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[SafetySetting](../-safety-setting/index.html)>?

Safety settings to apply to the session.

[seed](seed.html)

Link copied to clipboard

common

val [seed](seed.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)?

Fixing the seed makes the model attempt to give the same response to repeated requests.

[sessionResumption](session-resumption.html)

Link copied to clipboard

common

val [sessionResumption](session-resumption.html): [SessionResumptionConfig](../-session-resumption-config/index.html)?

Configuration of the session resumption mechanism.

[speechConfig](speech-config.html)

Link copied to clipboard

common

val [speechConfig](speech-config.html): [SpeechConfig](../-speech-config/index.html)?

The speech generation configuration.

[systemInstruction](system-instruction.html)

Link copied to clipboard

common

val [systemInstruction](system-instruction.html): [Content](../-content/index.html)?

Instructions for the model. Only text parts are supported.

[temperature](temperature.html)

Link copied to clipboard

common

val [temperature](temperature.html): [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)?

Degree of randomness in token selection.

[thinkingConfig](thinking-config.html)

Link copied to clipboard

common

val [thinkingConfig](thinking-config.html): [ThinkingConfig](../-thinking-config/index.html)?

Config for thinking features. Setting it for a model that does not support thinking is an error.

[tools](tools.html)

Link copied to clipboard

common

val [tools](tools.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Tool](../-tool/index.html)>?

Tools the model may call to generate its next response.

[topK](top-k.html)

Link copied to clipboard

common

val [topK](top-k.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)?

The number of highest-probability tokens to sample from at each step.

[topP](top-p.html)

Link copied to clipboard

common

val [topP](top-p.html): [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)?

Tokens are selected from the most to least probable until their probabilities sum to this value.

[translationConfig](translation-config.html)

Link copied to clipboard

common

val [translationConfig](translation-config.html): [TranslationConfig](../-translation-config/index.html)?

Real-time speech-to-speech translation, for translation models.

## Functions

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [LiveConnectConfig.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
