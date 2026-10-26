[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.types](../index.html)/GroundingMetadata

# GroundingMetadata

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GroundingMetadata](index.html)(val imageSearchQueries: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val groundingChunks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[GroundingChunk](../-grounding-chunk/index.html)>? = null, val groundingSupports: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[GroundingSupport](../-grounding-support/index.html)>? = null, val webSearchQueries: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val retrievalQueries: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val searchEntryPoint: [SearchEntryPoint](../-search-entry-point/index.html)? = null, val retrievalMetadata: [RetrievalMetadata](../-retrieval-metadata/index.html)? = null)

Metadata returned to client when grounding is enabled.

Members

## Constructors

[GroundingMetadata](-grounding-metadata.html)

Link copied to clipboard

common

constructor(imageSearchQueries: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, groundingChunks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[GroundingChunk](../-grounding-chunk/index.html)>? = null, groundingSupports: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[GroundingSupport](../-grounding-support/index.html)>? = null, webSearchQueries: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, retrievalQueries: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, searchEntryPoint: [SearchEntryPoint](../-search-entry-point/index.html)? = null, retrievalMetadata: [RetrievalMetadata](../-retrieval-metadata/index.html)? = null)

## Properties

[groundingChunks](grounding-chunks.html)

Link copied to clipboard

common

val [groundingChunks](grounding-chunks.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[GroundingChunk](../-grounding-chunk/index.html)>?

The cited source chunks that ground the response.

[groundingSupports](grounding-supports.html)

Link copied to clipboard

common

val [groundingSupports](grounding-supports.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[GroundingSupport](../-grounding-support/index.html)>?

Maps response segments to the grounding chunks that support them.

[imageSearchQueries](image-search-queries.html)

Link copied to clipboard

common

val [imageSearchQueries](image-search-queries.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?

The image search queries used to retrieve grounding sources.

[retrievalMetadata](retrieval-metadata.html)

Link copied to clipboard

common

val [retrievalMetadata](retrieval-metadata.html): [RetrievalMetadata](../-retrieval-metadata/index.html)?

Metadata about the retrieval step.

[retrievalQueries](retrieval-queries.html)

Link copied to clipboard

common

val [retrievalQueries](retrieval-queries.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?

The retrieval queries used to retrieve grounding sources.

[searchEntryPoint](search-entry-point.html)

Link copied to clipboard

common

val [searchEntryPoint](search-entry-point.html): [SearchEntryPoint](../-search-entry-point/index.html)?

The Google Search entry point for rendering search suggestions.

[webSearchQueries](web-search-queries.html)

Link copied to clipboard

common

val [webSearchQueries](web-search-queries.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?

The web search queries used to retrieve grounding sources.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
