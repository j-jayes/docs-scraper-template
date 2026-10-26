[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/RunConfig

# RunConfig

common

data class [RunConfig](index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val streamingMode: [StreamingMode](../-streaming-mode/index.html) = StreamingMode.NONE, val maxLlmCalls: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 500, val customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>? = null, val responseModalities: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Modality](../../com.google.adk.kt.types/-modality/index.html)> = emptyList(), val speechConfig: [SpeechConfig](../../com.google.adk.kt.types/-speech-config/index.html)? = null, val outputAudioTranscription: [AudioTranscriptionConfig](../../com.google.adk.kt.types/-audio-transcription-config/index.html)? = AudioTranscriptionConfig(), val inputAudioTranscription: [AudioTranscriptionConfig](../../com.google.adk.kt.types/-audio-transcription-config/index.html)? = AudioTranscriptionConfig(), val realtimeInputConfig: [RealtimeInputConfig](../../com.google.adk.kt.types/-realtime-input-config/index.html)? = null, val explicitVadSignal: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val translationConfig: [TranslationConfig](../../com.google.adk.kt.types/-translation-config/index.html)? = null, val enableAffectiveDialog: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val proactivity: [ProactivityConfig](../../com.google.adk.kt.types/-proactivity-config/index.html)? = null, val sessionResumption: [SessionResumptionConfig](../../com.google.adk.kt.types/-session-resumption-config/index.html)? = null, val contextWindowCompression: [ContextWindowCompressionConfig](../../com.google.adk.kt.types/-context-window-compression-config/index.html)? = null)

Configs for runtime behavior of agents.

Properties from [responseModalities](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-run-config/--root--.html) onwards apply only to a live connection, which is configured once when it opens and cannot be changed per turn. They only take effect through the experimental live API.

Members

## Constructors

[RunConfig](-run-config.html)

Link copied to clipboard

common

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

constructor(streamingMode: [StreamingMode](../-streaming-mode/index.html) = StreamingMode.NONE, maxLlmCalls: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 500, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>? = null, responseModalities: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Modality](../../com.google.adk.kt.types/-modality/index.html)> = emptyList(), speechConfig: [SpeechConfig](../../com.google.adk.kt.types/-speech-config/index.html)? = null, outputAudioTranscription: [AudioTranscriptionConfig](../../com.google.adk.kt.types/-audio-transcription-config/index.html)? = AudioTranscriptionConfig(), inputAudioTranscription: [AudioTranscriptionConfig](../../com.google.adk.kt.types/-audio-transcription-config/index.html)? = AudioTranscriptionConfig(), realtimeInputConfig: [RealtimeInputConfig](../../com.google.adk.kt.types/-realtime-input-config/index.html)? = null, explicitVadSignal: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, translationConfig: [TranslationConfig](../../com.google.adk.kt.types/-translation-config/index.html)? = null, enableAffectiveDialog: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, proactivity: [ProactivityConfig](../../com.google.adk.kt.types/-proactivity-config/index.html)? = null, sessionResumption: [SessionResumptionConfig](../../com.google.adk.kt.types/-session-resumption-config/index.html)? = null, contextWindowCompression: [ContextWindowCompressionConfig](../../com.google.adk.kt.types/-context-window-compression-config/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [RunConfig](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[contextWindowCompression](context-window-compression.html)

Link copied to clipboard

common

val [contextWindowCompression](context-window-compression.html): [ContextWindowCompressionConfig](../../com.google.adk.kt.types/-context-window-compression-config/index.html)?

Keeps the session's context below a given length.

[customMetadata](custom-metadata.html)

Link copied to clipboard

common

val [customMetadata](custom-metadata.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>?

Custom metadata for the current invocation.

[enableAffectiveDialog](enable-affective-dialog.html)

Link copied to clipboard

common

val [enableAffectiveDialog](enable-affective-dialog.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)?

Whether the model detects emotion and adapts its responses.

[explicitVadSignal](explicit-vad-signal.html)

Link copied to clipboard

common

val [explicitVadSignal](explicit-vad-signal.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)?

Whether the model sends its voice activity detection signals. Only the Vertex AI backend accepts `true`; Gemini API clients reject it.

[inputAudioTranscription](input-audio-transcription.html)

Link copied to clipboard

common

val [inputAudioTranscription](input-audio-transcription.html): [AudioTranscriptionConfig](../../com.google.adk.kt.types/-audio-transcription-config/index.html)?

Transcription of the audio the user sends. Enabled by default with automatic language detection; set to null to disable it.

[maxLlmCalls](max-llm-calls.html)

Link copied to clipboard

common

val [maxLlmCalls](max-llm-calls.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

Limit on the total number of LLM calls per run. A positive value is enforced, except by a live run, which ignores it; a value <= 0 means unbounded.

[outputAudioTranscription](output-audio-transcription.html)

Link copied to clipboard

common

val [outputAudioTranscription](output-audio-transcription.html): [AudioTranscriptionConfig](../../com.google.adk.kt.types/-audio-transcription-config/index.html)?

Transcription of the audio the model returns. Enabled by default with automatic language detection; set to null to disable it.

[proactivity](proactivity.html)

Link copied to clipboard

common

val [proactivity](proactivity.html): [ProactivityConfig](../../com.google.adk.kt.types/-proactivity-config/index.html)?

Whether the model may decline to respond to a prompt.

[realtimeInputConfig](realtime-input-config.html)

Link copied to clipboard

common

val [realtimeInputConfig](realtime-input-config.html): [RealtimeInputConfig](../../com.google.adk.kt.types/-realtime-input-config/index.html)?

How realtime input is interpreted as turns, including voice activity detection.

[responseModalities](response-modalities.html)

Link copied to clipboard

common

val [responseModalities](response-modalities.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Modality](../../com.google.adk.kt.types/-modality/index.html)>

The modalities the model may return. Empty leaves it unset, and the SDK then asks for audio on a live connection, as unset does in ADK Python. A value set here is sent as is, as in ADK Python, so a modality the model cannot answer in fails the connection.

[sessionResumption](session-resumption.html)

Link copied to clipboard

common

val [sessionResumption](session-resumption.html): [SessionResumptionConfig](../../com.google.adk.kt.types/-session-resumption-config/index.html)?

Configuration of the session resumption mechanism.

[speechConfig](speech-config.html)

Link copied to clipboard

common

val [speechConfig](speech-config.html): [SpeechConfig](../../com.google.adk.kt.types/-speech-config/index.html)?

The speech generation configuration.

[streamingMode](streaming-mode.html)

Link copied to clipboard

common

val [streamingMode](streaming-mode.html): [StreamingMode](../-streaming-mode/index.html)

Streaming mode, NONE, SSE or BIDI.

[translationConfig](translation-config.html)

Link copied to clipboard

common

val [translationConfig](translation-config.html): [TranslationConfig](../../com.google.adk.kt.types/-translation-config/index.html)?

Real-time speech-to-speech translation. Only translation models support it.

## Functions

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [RunConfig.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
