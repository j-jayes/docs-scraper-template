toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.models](../index.html)/LlmResponse

# LlmResponse

data class [LlmResponse](index.html)(val content: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, val usageMetadata: [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)? = null, val finishReason: [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)? = null, val errorMessage: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val partial: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val interrupted: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val modelVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)? = null, val groundingMetadata: [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)? = null)

LLM response class that provides the first candidate response from the model if available. Otherwise, contains the error code and message.

Members

## Constructors

[LlmResponse](-llm-response.html)

Link copied to clipboard

constructor(content: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, usageMetadata: [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)? = null, finishReason: [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)? = null, errorMessage: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, partial: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, interrupted: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, modelVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, citationMetadata: [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)? = null, groundingMetadata: [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)? = null)

## Types

[Companion](-companion/index.html)

Link copied to clipboard

object [Companion](-companion/index.html)

## Properties

[citationMetadata](citation-metadata.html)

Link copied to clipboard

val [citationMetadata](citation-metadata.html): [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)? = null

The citation metadata of the response.

[content](content.html)

Link copied to clipboard

val [content](content.html): [Content](../../com.google.adk.kt.types/-content/index.html)? = null

The generative content of the response. This should only contain content from the user or the model, and not any framework or system-generated data.

[errorMessage](error-message.html)

Link copied to clipboard

val [errorMessage](error-message.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

Error message if the response is an error.

[finishReason](finish-reason.html)

Link copied to clipboard

val [finishReason](finish-reason.html): [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)? = null

The finish reason of the response.

[groundingMetadata](grounding-metadata.html)

Link copied to clipboard

val [groundingMetadata](grounding-metadata.html): [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)? = null

The grounding metadata of the response.

[interrupted](interrupted.html)

Link copied to clipboard

val [interrupted](interrupted.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

Flag indicating that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

[modelVersion](model-version.html)

Link copied to clipboard

val [modelVersion](model-version.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

The model version used to generate the response.

[partial](partial.html)

Link copied to clipboard

val [partial](partial.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

Indicates whether the text content is part of an unfinished text stream. Only used for streaming mode and when the content is plain text.

[usageMetadata](usage-metadata.html)

Link copied to clipboard

val [usageMetadata](usage-metadata.html): [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)? = null

The usage metadata of the LlmResponse.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
