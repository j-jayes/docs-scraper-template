[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.5.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.models](../index.html)/Gemini

# Gemini

common

class [Gemini](index.html) : [Model](../-model/index.html)

Implementation of [Model](../-model/index.html) that interacts with Google Gemini models using the GenAI SDK.

This class provides functionality to generate content from Gemini models, supporting both unary and streaming responses. It can be configured to use either a Google AI API key or Vertex AI credentials for authentication.

GenAI SDK based [Gemini](index.html) currently prevents usage of `API_KEY` and `GoogleCredentials` on Android. Use Firebase AI instead.

Members

## Constructors

[Gemini](-gemini.html)

Link copied to clipboard

common

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

constructor(client: Client, name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), speechConfig: [SpeechConfig](../../com.google.adk.kt.types/-speech-config/index.html)? = null)

Creates a [Gemini](-gemini.html) from a preconfigured GenAI SDK Client, for callers that need a custom transport or auth. Each generate request and live connection appends ADK's tracking tag to the client's `user-agent` and `x-goog-api-client` headers. The SDK matches these names exactly, so a client header spelled `User-Agent` replaces the merged value.

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), apiKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, speechConfig: [SpeechConfig](../../com.google.adk.kt.types/-speech-config/index.html)? = null)

Creates a [Gemini](-gemini.html) instance using a Google AI API key for authentication. Its client retries transient failures with the GenAI SDK's default retry options; pass your own Client for other retry settings.

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), vertexCredentials: [VertexCredentials](../-vertex-credentials/index.html), speechConfig: [SpeechConfig](../../com.google.adk.kt.types/-speech-config/index.html)? = null)

Creates a [Gemini](-gemini.html) instance using Vertex AI credentials for authentication. Its client retries transient failures with the GenAI SDK's default retry options; pass your own Client for other retry settings.

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [Gemini](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[name](name.html)

Link copied to clipboard

common

open override val [name](name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The name of the model.

[speechConfig](speech-config.html)

Link copied to clipboard

common

val [speechConfig](speech-config.html): [SpeechConfig](../../com.google.adk.kt.types/-speech-config/index.html)?

The speech config for live sessions opened by this model. When set, it replaces the request's own speech config at connect, as in ADK Python.

## Functions

[connect](connect.html)

Link copied to clipboard

common

@[ExperimentalLiveApi](../../com.google.adk.kt.annotations/-experimental-live-api/index.html)

open suspend override fun [connect](connect.html)(request: [LlmRequest](../-llm-request/index.html)): [LiveConnection](../-live-connection/index.html)

Opens a live session configured by [LlmRequest.liveConnectConfig](../-llm-request/live-connect-config.html) (using `request.model` when set), returning once the server confirms setup and throwing if the server refuses it. If the caller is cancelled while the session opens, the session is closed in the background. Reconnection is not handled here, though a Vertex AI resume with `transparent` unset asks for transparent resumption.

[generateContent](generate-content.html)

Link copied to clipboard

common

open override fun [generateContent](generate-content.html)(request: [LlmRequest](../-llm-request/index.html), stream: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false): [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)<[LlmResponse](../-llm-response/index.html)>

Generates content for the given [LlmRequest](../-llm-request/index.html). This returns a [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html) of [LlmResponse](../-llm-response/index.html)s.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
