[ google-adk-kotlin ](../../index.html) Toggle table of contents 

1.4.0 

commonJvmAndroid common

Target filter __

    * commonJvmAndroid 
    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../index.html)/com.google.adk.kt.models

# Package-level declarations

Types

## Types

[CacheMetadata](-cache-metadata/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [CacheMetadata](-cache-metadata/index.html)(val fingerprint: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val contentsCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), val cacheName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val expireTime: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val invocationsUsed: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val createdAt: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null)

Metadata for the context cache associated with LLM responses.

[ContentInput](-content-input/index.html)

Link copied to clipboard

common

@[ExperimentalLiveApi](../com.google.adk.kt.annotations/-experimental-live-api/index.html)

data class [ContentInput](-content-input/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val content: [Content](../com.google.adk.kt.types/-content/index.html), val partial: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false) : [LiveInput](-live-input/index.html)

A user turn, or the function responses that answer the model's calls.

[Gemini](-gemini/index.html)

Link copied to clipboard

common

class [Gemini](-gemini/index.html) : [Model](-model/index.html)

Implementation of [Model](-model/index.html) that interacts with Google Gemini models using the GenAI SDK.

[GoogleCredentials](-google-credentials/index.html)

Link copied to clipboard

commonJvmAndroidcommon

actual typealias [GoogleCredentials](-google-credentials/index.html) = [com.google.auth.oauth2.GoogleCredentials](https://javadoc.io/doc/com.google.auth/google-auth-library-oauth2-http/1.48.0/com/google/auth/oauth2/GoogleCredentials.html)

typealias [GoogleCredentials](-google-credentials/index.html) = [com.google.auth.oauth2.GoogleCredentials](https://javadoc.io/doc/com.google.auth/google-auth-library-oauth2-http/1.48.0/com/google/auth/oauth2/GoogleCredentials.html)

On JVM and Android, ADK credentials are the Java Auth Library's `GoogleCredentials`.

expect class [GoogleCredentials](-google-credentials/index.html)

ADK-owned handle to Google Cloud credentials for Vertex AI (see [VertexCredentials](-vertex-credentials/index.html)). On JVM and Android it is a `typealias` for `com.google.auth.oauth2.GoogleCredentials`; [toGenaiSdk](../../google-adk-kotlin-core/com.google.adk.kt.models/index.html) bridges it to the GenAI SDK.

[LiveConnection](-live-connection/index.html)

Link copied to clipboard

common

@[ExperimentalLiveApi](../com.google.adk.kt.annotations/-experimental-live-api/index.html)

interface [LiveConnection](-live-connection/index.html) : [AutoCloseable](https://developer.android.com/reference/kotlin/java/lang/AutoCloseable.html)

An open bidirectional (live) connection to a model, obtained from [Model.connect](-model/connect.html).

[LiveInput](-live-input/index.html)

Link copied to clipboard

common

@[ExperimentalLiveApi](../com.google.adk.kt.annotations/-experimental-live-api/index.html)

sealed interface [LiveInput](-live-input/index.html)

What one live request sends to the model: a [ContentInput](-content-input/index.html) turn or a [RealtimeInput](-realtime-input/index.html).

[LlmRequest](-llm-request/index.html)

Link copied to clipboard

common

data class [LlmRequest](-llm-request/index.html)(val model: [Model](-model/index.html)? = null, val contents: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Content](../com.google.adk.kt.types/-content/index.html)> = emptyList(), val config: [GenerateContentConfig](../com.google.adk.kt.types/-generate-content-config/index.html) = GenerateContentConfig(), toolsDict: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseTool](../com.google.adk.kt.tools/-base-tool/index.html)> = emptyList(), val cacheConfig: [ContextCacheConfig](../com.google.adk.kt.agents/-context-cache-config/index.html)? = null, val cacheMetadata: [CacheMetadata](-cache-metadata/index.html)? = null, val cacheableContentsTokenCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val liveConnectConfig: [LiveConnectConfig](../com.google.adk.kt.types/-live-connect-config/index.html) = LiveConnectConfig())

LlmRequest represents a request to an LLM.

[LlmResponse](-llm-response/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [LlmResponse](-llm-response/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val content: [Content](../com.google.adk.kt.types/-content/index.html)? = null, val usageMetadata: [UsageMetadata](../com.google.adk.kt.types/-usage-metadata/index.html)? = null, val finishReason: [FinishReason](../com.google.adk.kt.types/-finish-reason/index.html)? = null, val errorMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val partial: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val interrupted: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val modelVersion: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](../com.google.adk.kt.types/-citation-metadata/index.html)? = null, val groundingMetadata: [GroundingMetadata](../com.google.adk.kt.types/-grounding-metadata/index.html)? = null, val errorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null, val avgLogprobs: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, val logprobsResult: [LogprobsResult](../com.google.adk.kt.types/-logprobs-result/index.html)? = null, val cacheMetadata: [CacheMetadata](-cache-metadata/index.html)? = null, val turnComplete: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val turnCompleteReason: [TurnCompleteReason](../com.google.adk.kt.types/-turn-complete-reason/index.html)? = null, val interactionStatus: [InteractionStatus](../com.google.adk.kt.types/-interaction-status/index.html)? = null, val inputTranscription: [Transcription](../com.google.adk.kt.types/-transcription/index.html)? = null, val outputTranscription: [Transcription](../com.google.adk.kt.types/-transcription/index.html)? = null, val liveSessionId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val liveSessionResumptionUpdate: [LiveServerSessionResumptionUpdate](../com.google.adk.kt.types/-live-server-session-resumption-update/index.html)? = null, val goAway: [LiveServerGoAway](../com.google.adk.kt.types/-live-server-go-away/index.html)? = null, val voiceActivity: [VoiceActivity](../com.google.adk.kt.types/-voice-activity/index.html)? = null)

LLM response class that provides the first candidate response from the model if available. Otherwise, contains the error code and message.

[Model](-model/index.html)

Link copied to clipboard

common

interface [Model](-model/index.html)

Interface that provides a common interface for interacting with different LLMs.

[RealtimeInput](-realtime-input/index.html)

Link copied to clipboard

common

@[ExperimentalLiveApi](../com.google.adk.kt.annotations/-experimental-live-api/index.html)

sealed interface [RealtimeInput](-realtime-input/index.html) : [LiveInput](-live-input/index.html)

Input streamed to a live model outside the turn-by-turn content exchange.

[StreamingResponseAggregator](-streaming-response-aggregator/index.html)

Link copied to clipboard

common

class [StreamingResponseAggregator](-streaming-response-aggregator/index.html)

Aggregates partial streaming responses into a single, cohesive response.

[VertexCredentials](-vertex-credentials/index.html)

Link copied to clipboard

common

data class [VertexCredentials](-vertex-credentials/index.html)(val project: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val location: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val credentials: [GoogleCredentials](-google-credentials/index.html)? = null)

Config for authenticating to Vertex AI when constructing a [Gemini](-gemini/index.html) model.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
