toggle menu

[ google-adk-kotlin ](../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../index.html)/com.google.adk.kt.types

# Package-level declarations

Types

## Types

[Blob](-blob/index.html)

Link copied to clipboard

data class [Blob](-blob/index.html)(val mimeType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val displayName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val data: [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html)? = null)

Represents binary data.

[BlockedReason](-blocked-reason/index.html)

Link copied to clipboard

enum [BlockedReason](-blocked-reason/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[BlockedReason](-blocked-reason/index.html)>

The reason why the prompt was blocked.

[Candidate](-candidate/index.html)

Link copied to clipboard

data class [Candidate](-candidate/index.html)(val content: [Content](-content/index.html), val finishReason: [FinishReason](-finish-reason/index.html)? = null, val finishMessage: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](-citation-metadata/index.html)? = null, val groundingMetadata: [GroundingMetadata](-grounding-metadata/index.html)? = null)

Represents a possible response from the model.

[Citation](-citation/index.html)

Link copied to clipboard

data class [Citation](-citation/index.html)(val title: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

Represents a citation to a source.

[CitationMetadata](-citation-metadata/index.html)

Link copied to clipboard

data class [CitationMetadata](-citation-metadata/index.html)(val citationSources: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Citation](-citation/index.html)> = emptyList())

Metadata about citations associated with the candidate.

[Content](-content/index.html)

Link copied to clipboard

data class [Content](-content/index.html)(val role: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val parts: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Part](-part/index.html)> = emptyList())

Represents the content of a response, including its role and parts.

[FileData](-file-data/index.html)

Link copied to clipboard

data class [FileData](-file-data/index.html)(val mimeType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val displayName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val fileUri: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

Represents file data.

[FinishReason](-finish-reason/index.html)

Link copied to clipboard

enum [FinishReason](-finish-reason/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[FinishReason](-finish-reason/index.html)>

The reason why the generation finished.

[FunctionCall](-function-call/index.html)

Link copied to clipboard

data class [FunctionCall](-function-call/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?> = emptyMap(), val id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val partialArgs: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[PartialArg](-partial-arg/index.html)>? = null, val willContinue: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Represents a function call in a generation response.

[FunctionDeclaration](-function-declaration/index.html)

Link copied to clipboard

data class [FunctionDeclaration](-function-declaration/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val parameters: [Schema](-schema/index.html)? = null)

Represents a function declaration for tool calling.

[FunctionResponse](-function-response/index.html)

Link copied to clipboard

data class [FunctionResponse](-function-response/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val response: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?> = emptyMap(), val id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

Represents a function response.

[GenerateContentConfig](-generate-content-config/index.html)

Link copied to clipboard

data class [GenerateContentConfig](-generate-content-config/index.html)(val tools: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Tool](-tool/index.html)>? = null, val labels: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, val systemInstruction: [Content](-content/index.html)? = null, val temperature: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null, val topP: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null, val topK: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val candidateCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val maxOutputTokens: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val stopSequences: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, val responseMimeType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val thinkingConfig: [ThinkingConfig](-thinking-config/index.html)? = null)

Configuration for generating content.

[GenerateContentResponse](-generate-content-response/index.html)

Link copied to clipboard

data class [GenerateContentResponse](-generate-content-response/index.html)(val candidates: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Candidate](-candidate/index.html)> = emptyList(), val promptFeedback: [PromptFeedback](-prompt-feedback/index.html)? = null, val usageMetadata: [UsageMetadata](-usage-metadata/index.html)? = null, val modelVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

Response from the generate content request.

[GoogleMaps](-google-maps/index.html)

Link copied to clipboard

data class [GoogleMaps](-google-maps/index.html)(val enableWidget: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Tool to retrieve knowledge from Google Maps.

[GoogleSearch](-google-search/index.html)

Link copied to clipboard

data class [GoogleSearch](-google-search/index.html)(val excludeDomains: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)> = emptyList())

Represents a Google Search tool.

[GroundingMetadata](-grounding-metadata/index.html)

Link copied to clipboard

data class [GroundingMetadata](-grounding-metadata/index.html)(val imageSearchQueries: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)> = emptyList())

Metadata returned to client when grounding is enabled.

[LlmConstants](-llm-constants/index.html)

Link copied to clipboard

object [LlmConstants](-llm-constants/index.html)

Internal constants for LLM requests and responses.

[Part](-part/index.html)

Link copied to clipboard

class [Part](-part/index.html) constructor(val text: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val inlineData: [Blob](-blob/index.html)? = null, val fileData: [FileData](-file-data/index.html)? = null, val functionCall: [FunctionCall](-function-call/index.html)? = null, val functionResponse: [FunctionResponse](-function-response/index.html)? = null, val thought: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val thoughtSignature: [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html)? = null, val opaqueData: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)? = null)

A part of a multi-modal prompt or response.

[PartialArg](-partial-arg/index.html)

Link copied to clipboard

data class [PartialArg](-partial-arg/index.html)(val value: [PartialArgValue](-partial-arg-value/index.html)? = null, val jsonPath: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val willContinue: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Partial argument value of the function call.

[PartialArgValue](-partial-arg-value/index.html)

Link copied to clipboard

sealed interface [PartialArgValue](-partial-arg-value/index.html)

Represents one of the possible values within a [PartialArg](-partial-arg/index.html).

[PromptFeedback](-prompt-feedback/index.html)

Link copied to clipboard

data class [PromptFeedback](-prompt-feedback/index.html)(val blockReason: [BlockedReason](-blocked-reason/index.html)? = null, val blockReasonMessage: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

Feedback received from the prompt.

[Retrieval](-retrieval/index.html)

Link copied to clipboard

data class [Retrieval](-retrieval/index.html)(val vertexAiSearch: [VertexAISearch](-vertex-a-i-search/index.html)? = null)

Defines a retrieval tool that model can call to access external knowledge.

[Role](-role/index.html)

Link copied to clipboard

object [Role](-role/index.html)

Standard roles for content and events.

[Schema](-schema/index.html)

Link copied to clipboard

data class [Schema](-schema/index.html)(val type: [Type](-type/index.html)? = null, val properties: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Schema](-schema/index.html)>? = null, val items: [Schema](-schema/index.html)? = null, val required: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val enum: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null)

Schema is used to define the format of input/output data.

[ThinkingConfig](-thinking-config/index.html)

Link copied to clipboard

data class [ThinkingConfig](-thinking-config/index.html)(val includeThoughts: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val thinkingBudget: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val thinkingLevel: [ThinkingLevel](-thinking-level/index.html)? = null)

The thinking features configuration.

[ThinkingLevel](-thinking-level/index.html)

Link copied to clipboard

enum [ThinkingLevel](-thinking-level/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[ThinkingLevel](-thinking-level/index.html)>

The number of thoughts tokens that the model should generate.

[Tool](-tool/index.html)

Link copied to clipboard

data class [Tool](-tool/index.html)(val functionDeclarations: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[FunctionDeclaration](-function-declaration/index.html)>? = null, val googleSearch: [GoogleSearch](-google-search/index.html)? = null, val googleMaps: [GoogleMaps](-google-maps/index.html)? = null, val retrieval: [Retrieval](-retrieval/index.html)? = null)

Represents a GenAI tool definition.

[Type](-type/index.html)

Link copied to clipboard

enum [Type](-type/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[Type](-type/index.html)>

The value type of the schema.

[UsageMetadata](-usage-metadata/index.html)

Link copied to clipboard

data class [UsageMetadata](-usage-metadata/index.html)(val promptTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val candidatesTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val totalTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null)

Usage metadata for a generate content request.

[VertexAISearch](-vertex-a-i-search/index.html)

Link copied to clipboard

data class [VertexAISearch](-vertex-a-i-search/index.html)(val dataStoreSpecs: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[VertexAISearchDataStoreSpec](-vertex-a-i-search-data-store-spec/index.html)>? = null, val datastore: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val engine: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val filter: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val maxResults: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null)

Retrieve from Vertex AI Search datastore or engine for grounding. datastore and engine are mutually exclusive.

[VertexAISearchDataStoreSpec](-vertex-a-i-search-data-store-spec/index.html)

Link copied to clipboard

data class [VertexAISearchDataStoreSpec](-vertex-a-i-search-data-store-spec/index.html)(val dataStore: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val filter: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

Define data stores within engine to filter on in a search call and configurations for those data stores.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
