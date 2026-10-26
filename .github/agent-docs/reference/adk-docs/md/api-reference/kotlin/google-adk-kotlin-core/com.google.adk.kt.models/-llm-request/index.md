[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.models](../index.html)/LlmRequest

# LlmRequest

common

data class [LlmRequest](index.html)(val model: [Model](../-model/index.html)? = null, val contents: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Content](../../com.google.adk.kt.types/-content/index.html)> = emptyList(), val config: [GenerateContentConfig](../../com.google.adk.kt.types/-generate-content-config/index.html) = GenerateContentConfig(), toolsDict: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)> = emptyList(), val cacheConfig: [ContextCacheConfig](../../com.google.adk.kt.agents/-context-cache-config/index.html)? = null, val cacheMetadata: [CacheMetadata](../-cache-metadata/index.html)? = null, val cacheableContentsTokenCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val liveConnectConfig: [LiveConnectConfig](../../com.google.adk.kt.types/-live-connect-config/index.html) = LiveConnectConfig())

LlmRequest represents a request to an LLM.

Members

## Constructors

[LlmRequest](-llm-request.html)

Link copied to clipboard

common

constructor(model: [Model](../-model/index.html)? = null, contents: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Content](../../com.google.adk.kt.types/-content/index.html)> = emptyList(), config: [GenerateContentConfig](../../com.google.adk.kt.types/-generate-content-config/index.html) = GenerateContentConfig(), toolsDict: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)> = emptyList(), cacheConfig: [ContextCacheConfig](../../com.google.adk.kt.agents/-context-cache-config/index.html)? = null, cacheMetadata: [CacheMetadata](../-cache-metadata/index.html)? = null, cacheableContentsTokenCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, liveConnectConfig: [LiveConnectConfig](../../com.google.adk.kt.types/-live-connect-config/index.html) = LiveConnectConfig())

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [LlmRequest](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor. The internal `toolsDict` is request-processing state populated by [appendTools](append-tools.html), not a caller input, so it has no public setter; [LlmRequest.toBuilder](to-builder.html) carries it over.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[cacheableContentsTokenCount](cacheable-contents-token-count.html)

Link copied to clipboard

common

val [cacheableContentsTokenCount](cacheable-contents-token-count.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)?

Prompt token count from the previous request, used to gate cache creation on a minimum size.

[cacheConfig](cache-config.html)

Link copied to clipboard

common

val [cacheConfig](cache-config.html): [ContextCacheConfig](../../com.google.adk.kt.agents/-context-cache-config/index.html)?

Context cache configuration for this request. When `null`, context caching is disabled for the request.

[cacheMetadata](cache-metadata.html)

Link copied to clipboard

common

val [cacheMetadata](cache-metadata.html): [CacheMetadata](../-cache-metadata/index.html)?

Cache metadata carried over from previous requests, used to validate and reuse an existing cache.

[config](config.html)

Link copied to clipboard

common

val [config](config.html): [GenerateContentConfig](../../com.google.adk.kt.types/-generate-content-config/index.html)

The configuration for generating content.

[contents](contents.html)

Link copied to clipboard

common

val [contents](contents.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Content](../../com.google.adk.kt.types/-content/index.html)>

The contents of the request.

[liveConnectConfig](live-connect-config.html)

Link copied to clipboard

common

val [liveConnectConfig](live-connect-config.html): [LiveConnectConfig](../../com.google.adk.kt.types/-live-connect-config/index.html)

The configuration used when opening a live connection. Ignored by [Model.generateContent](../-model/generate-content.html); it applies only to [Model.connect](../-model/connect.html). The agent's instruction, tools, and thinking settings win over this config's, while this config's sampling and safety settings win over the agent's.

[model](model.html)

Link copied to clipboard

common

val [model](model.html): [Model](../-model/index.html)?

The model to use for the request.

## Functions

[appendContent](append-content.html)

Link copied to clipboard

common

fun [appendContent](append-content.html)(content: [Content](../../com.google.adk.kt.types/-content/index.html)): [LlmRequest](index.html)

Appends a content block to the request.

[appendInstructions](append-instructions.html)

Link copied to clipboard

common

fun [appendInstructions](append-instructions.html)(instructions: [Content](../../com.google.adk.kt.types/-content/index.html)): [LlmRequest](index.html)

Appends instructions to the system instruction.

[appendTools](append-tools.html)

Link copied to clipboard

common

fun [appendTools](append-tools.html)(tools: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)>): [LlmRequest](index.html)

Appends tools to the request and merges any new function declarations.

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [LlmRequest.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
