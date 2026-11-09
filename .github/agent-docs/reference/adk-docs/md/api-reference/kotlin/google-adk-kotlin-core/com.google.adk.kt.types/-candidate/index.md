[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.5.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.types](../index.html)/Candidate

# Candidate

common

data class [Candidate](index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val content: [Content](../-content/index.html), val finishReason: [FinishReason](../-finish-reason/index.html)? = null, val finishMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](../-citation-metadata/index.html)? = null, val groundingMetadata: [GroundingMetadata](../-grounding-metadata/index.html)? = null, val avgLogprobs: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, val logprobsResult: [LogprobsResult](../-logprobs-result/index.html)? = null, val continuationToken: [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html)? = null)

Represents a possible response from the model.

Members

## Constructors

[Candidate](-candidate.html)

Link copied to clipboard

common

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

constructor(content: [Content](../-content/index.html), finishReason: [FinishReason](../-finish-reason/index.html)? = null, finishMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, citationMetadata: [CitationMetadata](../-citation-metadata/index.html)? = null, groundingMetadata: [GroundingMetadata](../-grounding-metadata/index.html)? = null, avgLogprobs: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, logprobsResult: [LogprobsResult](../-logprobs-result/index.html)? = null, continuationToken: [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [Candidate](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[avgLogprobs](avg-logprobs.html)

Link copied to clipboard

common

val [avgLogprobs](avg-logprobs.html): [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)?

The average log probability of the candidate's tokens.

[citationMetadata](citation-metadata.html)

Link copied to clipboard

common

val [citationMetadata](citation-metadata.html): [CitationMetadata](../-citation-metadata/index.html)?

The citation metadata associated with the candidate.

[content](content.html)

Link copied to clipboard

common

val [content](content.html): [Content](../-content/index.html)

The content of the candidate.

[continuationToken](continuation-token.html)

Link copied to clipboard

common

val [continuationToken](continuation-token.html): [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html)?

An opaque token that resumes generation when [finishReason](../../../google-adk-kotlin-core/com.google.adk.kt.types/-candidate/--root--.html) is [FinishReason.CONTINUATION](../-finish-reason/-c-o-n-t-i-n-u-a-t-i-o-n/index.html).

[finishMessage](finish-message.html)

Link copied to clipboard

common

val [finishMessage](finish-message.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The message associated with the finish reason.

[finishReason](finish-reason.html)

Link copied to clipboard

common

val [finishReason](finish-reason.html): [FinishReason](../-finish-reason/index.html)?

The reason why the model stopped generating content.

[groundingMetadata](grounding-metadata.html)

Link copied to clipboard

common

val [groundingMetadata](grounding-metadata.html): [GroundingMetadata](../-grounding-metadata/index.html)?

The grounding metadata associated with the candidate.

[logprobsResult](logprobs-result.html)

Link copied to clipboard

common

val [logprobsResult](logprobs-result.html): [LogprobsResult](../-logprobs-result/index.html)?

Detailed log probabilities for the chosen and top candidate tokens.

## Functions

[equals](equals.html)

Link copied to clipboard

common

open operator override fun [equals](equals.html)(other: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

[hashCode](hash-code.html)

Link copied to clipboard

common

open override fun [hashCode](hash-code.html)(): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [Candidate.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
