toggle menu

[ google-adk-kotlin ](../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../index.html)/com.google.adk.kt.types

# Package-level declarations

Types

## Types

[Blob](-blob/index.html)

Link copied to clipboard

@Serializable

data class [Blob](-blob/index.html)(val mimeType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val displayName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val data: [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html)? = null)

Represents binary data.

[BlockedReason](-blocked-reason/index.html)

Link copied to clipboard

enum [BlockedReason](-blocked-reason/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[BlockedReason](-blocked-reason/index.html)>

The reason why the prompt was blocked.

[Candidate](-candidate/index.html)

Link copied to clipboard

data class [Candidate](-candidate/index.html)(val content: [Content](-content/index.html), val finishReason: [FinishReason](-finish-reason/index.html)? = null, val finishMessage: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](-citation-metadata/index.html)? = null, val groundingMetadata: [GroundingMetadata](-grounding-metadata/index.html)? = null, val avgLogprobs: [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html)? = null, val logprobsResult: [LogprobsResult](-logprobs-result/index.html)? = null)

Represents a possible response from the model.

[Citation](-citation/index.html)

Link copied to clipboard

@Serializable

data class [Citation](-citation/index.html)(val title: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val uri: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val startIndex: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val endIndex: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null)

Represents a citation to a source.

[CitationMetadata](-citation-metadata/index.html)

Link copied to clipboard

@Serializable

data class [CitationMetadata](-citation-metadata/index.html)(val citationSources: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Citation](-citation/index.html)> = emptyList())

Metadata about citations associated with the candidate.

[Content](-content/index.html)

Link copied to clipboard

@Serializable

data class [Content](-content/index.html)(val role: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val parts: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Part](-part/index.html)> = emptyList())

Represents the content of a response, including its role and parts.

[FileData](-file-data/index.html)

Link copied to clipboard

@Serializable

data class [FileData](-file-data/index.html)(val mimeType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val displayName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val fileUri: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

Represents file data.

[FinishReason](-finish-reason/index.html)

Link copied to clipboard

@Serializable(with = [FinishReasonSerializer::class](../../google-adk-kotlin-core/com.google.adk.kt.types/-finish-reason-serializer/index.html))

enum [FinishReason](-finish-reason/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[FinishReason](-finish-reason/index.html)>

The reason why the generation finished.

[FunctionCall](-function-call/index.html)

Link copied to clipboard

@Serializable

data class [FunctionCall](-function-call/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?> = emptyMap(), val id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val partialArgs: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[PartialArg](-partial-arg/index.html)>? = null, val willContinue: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Represents a function call in a generation response.

[FunctionCallingConfig](-function-calling-config/index.html)

Link copied to clipboard

data class [FunctionCallingConfig](-function-calling-config/index.html)(val allowedFunctionNames: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null)

Configuration for how the model uses the provided function declarations.

[FunctionDeclaration](-function-declaration/index.html)

Link copied to clipboard

data class [FunctionDeclaration](-function-declaration/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val parameters: [Schema](-schema/index.html)? = null)

Represents a function declaration for tool calling.

[FunctionResponse](-function-response/index.html)

Link copied to clipboard

@Serializable

data class [FunctionResponse](-function-response/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val response: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?> = emptyMap(), val id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

Represents a function response.

[GenerateContentConfig](-generate-content-config/index.html)

Link copied to clipboard

data class [GenerateContentConfig](-generate-content-config/index.html)(val tools: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Tool](-tool/index.html)>? = null, val labels: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, val systemInstruction: [Content](-content/index.html)? = null, val temperature: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null, val topP: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null, val topK: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val candidateCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val maxOutputTokens: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val stopSequences: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, val responseMimeType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val responseSchema: [Schema](-schema/index.html)? = null, val thinkingConfig: [ThinkingConfig](-thinking-config/index.html)? = null, val toolConfig: [ToolConfig](-tool-config/index.html)? = null, val safetySettings: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[SafetySetting](-safety-setting/index.html)>? = null, val mediaResolution: [MediaResolution](-media-resolution/index.html)? = null, val serviceTier: [ServiceTier](-service-tier/index.html)? = null, val presencePenalty: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null, val frequencyPenalty: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null, val responseLogprobs: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

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

[GroundingChunk](-grounding-chunk/index.html)

Link copied to clipboard

@Serializable

data class [GroundingChunk](-grounding-chunk/index.html)(val web: [GroundingChunkWeb](-grounding-chunk-web/index.html)? = null, val retrievedContext: [GroundingChunkRetrievedContext](-grounding-chunk-retrieved-context/index.html)? = null)

A single cited source chunk that grounds part of the model's response.

[GroundingChunkRetrievedContext](-grounding-chunk-retrieved-context/index.html)

Link copied to clipboard

@Serializable

data class [GroundingChunkRetrievedContext](-grounding-chunk-retrieved-context/index.html)(val uri: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val title: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val text: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

A grounding chunk sourced from a retrieval (RAG) context.

[GroundingChunkWeb](-grounding-chunk-web/index.html)

Link copied to clipboard

@Serializable

data class [GroundingChunkWeb](-grounding-chunk-web/index.html)(val uri: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val title: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val domain: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

A grounding chunk sourced from the open web.

[GroundingMetadata](-grounding-metadata/index.html)

Link copied to clipboard

@Serializable

data class [GroundingMetadata](-grounding-metadata/index.html)(val imageSearchQueries: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)> = emptyList(), val groundingChunks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[GroundingChunk](-grounding-chunk/index.html)>? = null, val groundingSupports: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[GroundingSupport](-grounding-support/index.html)>? = null, val webSearchQueries: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, val searchEntryPoint: [SearchEntryPoint](-search-entry-point/index.html)? = null, val retrievalMetadata: [RetrievalMetadata](-retrieval-metadata/index.html)? = null)

Metadata returned to client when grounding is enabled.

[GroundingSupport](-grounding-support/index.html)

Link copied to clipboard

@Serializable

data class [GroundingSupport](-grounding-support/index.html)(val segment: [Segment](-segment/index.html)? = null, val groundingChunkIndices: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)>? = null, val confidenceScores: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)>? = null)

Maps a [Segment](-segment/index.html) of the response to the grounding chunks that support it.

[HarmBlockThreshold](-harm-block-threshold/index.html)

Link copied to clipboard

enum [HarmBlockThreshold](-harm-block-threshold/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[HarmBlockThreshold](-harm-block-threshold/index.html)>

The probability threshold at or above which content is blocked for a [HarmCategory](-harm-category/index.html).

[HarmCategory](-harm-category/index.html)

Link copied to clipboard

enum [HarmCategory](-harm-category/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[HarmCategory](-harm-category/index.html)>

The category of a harm that a [SafetySetting](-safety-setting/index.html) applies to.

[LlmConstants](-llm-constants/index.html)

Link copied to clipboard

object [LlmConstants](-llm-constants/index.html)

Internal constants for LLM requests and responses.

[LogprobsResult](-logprobs-result/index.html)

Link copied to clipboard

@Serializable

data class [LogprobsResult](-logprobs-result/index.html)(val chosenCandidates: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[LogprobsResultCandidate](-logprobs-result-candidate/index.html)>? = null, val topCandidates: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[LogprobsResultTopCandidates](-logprobs-result-top-candidates/index.html)>? = null, val logProbabilitySum: [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html)? = null)

Detailed log probabilities for the chosen and top candidate tokens.

[LogprobsResultCandidate](-logprobs-result-candidate/index.html)

Link copied to clipboard

@Serializable

data class [LogprobsResultCandidate](-logprobs-result-candidate/index.html)(val token: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val tokenId: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val logProbability: [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html)? = null)

A single token candidate and its log probability.

[LogprobsResultTopCandidates](-logprobs-result-top-candidates/index.html)

Link copied to clipboard

@Serializable

data class [LogprobsResultTopCandidates](-logprobs-result-top-candidates/index.html)(val candidates: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[LogprobsResultCandidate](-logprobs-result-candidate/index.html)>? = null)

The top token candidates at a single decoding step.

[MediaModality](-media-modality/index.html)

Link copied to clipboard

@Serializable

enum [MediaModality](-media-modality/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[MediaModality](-media-modality/index.html)>

The modality that a token count applies to.

[MediaResolution](-media-resolution/index.html)

Link copied to clipboard

enum [MediaResolution](-media-resolution/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[MediaResolution](-media-resolution/index.html)>

The resolution used when processing media inputs.

[ModalityTokenCount](-modality-token-count/index.html)

Link copied to clipboard

@Serializable

data class [ModalityTokenCount](-modality-token-count/index.html)(val modality: [MediaModality](-media-modality/index.html)? = null, val tokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null)

A breakdown of token usage by modality.

[Part](-part/index.html)

Link copied to clipboard

@Serializable

class [Part](-part/index.html) constructor(val text: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val inlineData: [Blob](-blob/index.html)? = null, val fileData: [FileData](-file-data/index.html)? = null, val functionCall: [FunctionCall](-function-call/index.html)? = null, val functionResponse: [FunctionResponse](-function-response/index.html)? = null, val thought: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val thoughtSignature: [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html)? = null, val videoMetadata: [VideoMetadata](-video-metadata/index.html)? = null, val partMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?>? = null, val opaqueData: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)? = null)

A part of a multi-modal prompt or response.

[PartialArg](-partial-arg/index.html)

Link copied to clipboard

@Serializable

data class [PartialArg](-partial-arg/index.html)(val value: [PartialArgValue](-partial-arg-value/index.html)? = null, val jsonPath: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val willContinue: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Partial argument value of the function call.

[PartialArgValue](-partial-arg-value/index.html)

Link copied to clipboard

@Serializable

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

[RetrievalMetadata](-retrieval-metadata/index.html)

Link copied to clipboard

@Serializable

data class [RetrievalMetadata](-retrieval-metadata/index.html)(val googleSearchDynamicRetrievalScore: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null)

Metadata about the retrieval step performed for a grounded response.

[Role](-role/index.html)

Link copied to clipboard

object [Role](-role/index.html)

Standard roles for content and events.

[SafetySetting](-safety-setting/index.html)

Link copied to clipboard

data class [SafetySetting](-safety-setting/index.html)(val category: [HarmCategory](-harm-category/index.html)? = null, val threshold: [HarmBlockThreshold](-harm-block-threshold/index.html)? = null)

A per-request safety setting controlling the block threshold for a single [HarmCategory](-harm-category/index.html).

[Schema](-schema/index.html)

Link copied to clipboard

data class [Schema](-schema/index.html)(val type: [Type](-type/index.html)? = null, val properties: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Schema](-schema/index.html)>? = null, val items: [Schema](-schema/index.html)? = null, val required: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val enum: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null)

Schema is used to define the format of input/output data.

[SearchEntryPoint](-search-entry-point/index.html)

Link copied to clipboard

@Serializable

data class [SearchEntryPoint](-search-entry-point/index.html)(val renderedContent: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

The Google Search entry point used to render search suggestions for grounded responses.

[Segment](-segment/index.html)

Link copied to clipboard

@Serializable

data class [Segment](-segment/index.html)(val startIndex: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val endIndex: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val partIndex: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val text: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

A contiguous segment of the response content that a [GroundingSupport](-grounding-support/index.html) refers to.

[ServiceTier](-service-tier/index.html)

Link copied to clipboard

enum [ServiceTier](-service-tier/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[ServiceTier](-service-tier/index.html)>

The service tier requested for a generate content request.

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

data class [Tool](-tool/index.html)(val functionDeclarations: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[FunctionDeclaration](-function-declaration/index.html)>? = null, val googleSearch: [GoogleSearch](-google-search/index.html)? = null, val googleMaps: [GoogleMaps](-google-maps/index.html)? = null, val retrieval: [Retrieval](-retrieval/index.html)? = null, val urlContext: [UrlContext](-url-context/index.html)? = null)

Represents a GenAI tool definition.

[ToolConfig](-tool-config/index.html)

Link copied to clipboard

data class [ToolConfig](-tool-config/index.html)(val functionCallingConfig: [FunctionCallingConfig](-function-calling-config/index.html)? = null)

Configuration shared across all tools provided in a request.

[Type](-type/index.html)

Link copied to clipboard

enum [Type](-type/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[Type](-type/index.html)>

The value type of the schema.

[UrlContext](-url-context/index.html)

Link copied to clipboard

class [UrlContext](-url-context/index.html)

Tool to support URL context retrieval.

[UsageMetadata](-usage-metadata/index.html)

Link copied to clipboard

@Serializable

data class [UsageMetadata](-usage-metadata/index.html)(val promptTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val candidatesTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val totalTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val thoughtsTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val toolUsePromptTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val cachedContentTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val promptTokensDetails: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](-modality-token-count/index.html)>? = null, val candidatesTokensDetails: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](-modality-token-count/index.html)>? = null)

Usage metadata for a generate content request.

[VertexAISearch](-vertex-a-i-search/index.html)

Link copied to clipboard

data class [VertexAISearch](-vertex-a-i-search/index.html)(val dataStoreSpecs: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[VertexAISearchDataStoreSpec](-vertex-a-i-search-data-store-spec/index.html)>? = null, val datastore: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val engine: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val filter: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val maxResults: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null)

Retrieve from Vertex AI Search datastore or engine for grounding. datastore and engine are mutually exclusive.

[VertexAISearchDataStoreSpec](-vertex-a-i-search-data-store-spec/index.html)

Link copied to clipboard

data class [VertexAISearchDataStoreSpec](-vertex-a-i-search-data-store-spec/index.html)(val dataStore: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val filter: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

Define data stores within engine to filter on in a search call and configurations for those data stores.

[VideoMetadata](-video-metadata/index.html)

Link copied to clipboard

@Serializable

data class [VideoMetadata](-video-metadata/index.html)(val startOffset: <Error class: unknown class>? = null, val endOffset: <Error class: unknown class>? = null, val fps: [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html)? = null)

Metadata describing how to interpret a video [Part](-part/index.html).

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
