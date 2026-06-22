toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.tools](../index.html)/VertexAiSearchTool

# VertexAiSearchTool

class [VertexAiSearchTool](index.html)(val dataStoreId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val dataStoreSpecs: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[VertexAISearchDataStoreSpec](../../com.google.adk.kt.types/-vertex-a-i-search-data-store-spec/index.html)>? = null, val searchEngineId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val filter: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val maxResults: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val model: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null) : [BaseTool](../-base-tool/index.html)

A built-in tool using Vertex AI Search.

This tool can be configured with either a [dataStoreId](data-store-id.html) (the Vertex AI search data store resource ID) or a [searchEngineId](search-engine-id.html) (the Vertex AI search engine resource ID).

Members

## Constructors

[VertexAiSearchTool](-vertex-ai-search-tool.html)

Link copied to clipboard

constructor(dataStoreId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, dataStoreSpecs: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[VertexAISearchDataStoreSpec](../../com.google.adk.kt.types/-vertex-a-i-search-data-store-spec/index.html)>? = null, searchEngineId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, filter: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, maxResults: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, model: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

## Properties

[customMetadata](../-base-tool/custom-metadata.html)

Link copied to clipboard

val [customMetadata](../-base-tool/custom-metadata.html): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>

The custom metadata of the tool.

[dataStoreId](data-store-id.html)

Link copied to clipboard

val [dataStoreId](data-store-id.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

The Vertex AI search data store resource ID in the format of `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`.

[dataStoreSpecs](data-store-specs.html)

Link copied to clipboard

val [dataStoreSpecs](data-store-specs.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[VertexAISearchDataStoreSpec](../../com.google.adk.kt.types/-vertex-a-i-search-data-store-spec/index.html)>? = null

Specifications that define the specific DataStores to be searched. It should only be set if engine is used.

[description](../-base-tool/description.html)

Link copied to clipboard

val [description](../-base-tool/description.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The description of the tool.

[filter](filter.html)

Link copied to clipboard

val [filter](filter.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

The filter to apply to the search results.

[isLongRunning](../-base-tool/is-long-running.html)

Link copied to clipboard

val [isLongRunning](../-base-tool/is-long-running.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

Whether the tool's final result will be delivered out-of-band. When `true`, the framework marks the call as long-running and uses the tool's return value as the function-response payload (or suppresses the response entirely if the tool returns `Unit`).

[maxResults](max-results.html)

Link copied to clipboard

val [maxResults](max-results.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null

The maximum number of results to return.

[model](model.html)

Link copied to clipboard

val [model](model.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

The model name to use, overriding the one in [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html).

[name](../-base-tool/name.html)

Link copied to clipboard

val [name](../-base-tool/name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The name of the tool.

[searchEngineId](search-engine-id.html)

Link copied to clipboard

val [searchEngineId](search-engine-id.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

The Vertex AI search engine resource ID in the format of `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`.

## Functions

[close](../-base-tool/close.html)

Link copied to clipboard

open override fun [close](../-base-tool/close.html)()

[declaration](declaration.html)

Link copied to clipboard

open override fun [declaration](declaration.html)(): [FunctionDeclaration](../../com.google.adk.kt.types/-function-declaration/index.html)?

Returns the underlying function declaration.

[processLlmRequest](process-llm-request.html)

Link copied to clipboard

open suspend override fun [processLlmRequest](process-llm-request.html)(toolContext: [ToolContext](../-tool-context/index.html), llmRequest: [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)): [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)

Processes the LLM request before it is sent.

[run](run.html)

Link copied to clipboard

open suspend override fun [run](run.html)(context: [ToolContext](../-tool-context/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)

Executes the tool.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
