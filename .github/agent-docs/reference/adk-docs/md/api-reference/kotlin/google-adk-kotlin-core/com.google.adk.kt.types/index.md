[ google-adk-kotlin ](../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../index.html)/com.google.adk.kt.types

# Package-level declarations

Types

## Types

[ActivityHandling](-activity-handling/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [ActivityHandling](-activity-handling/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[ActivityHandling](-activity-handling/index.html)>

How the start of user activity affects an in-flight model response.

[AudioTranscriptionConfig](-audio-transcription-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [AudioTranscriptionConfig](-audio-transcription-config/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val languageCodes: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val customVocabulary: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val diarization: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val wordTimestamp: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val mode: [AudioTranscriptionConfigMode](-audio-transcription-config-mode/index.html)? = null)

Configures transcription of audio on a live connection.

[AudioTranscriptionConfigMode](-audio-transcription-config-mode/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [AudioTranscriptionConfigMode](-audio-transcription-config-mode/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[AudioTranscriptionConfigMode](-audio-transcription-config-mode/index.html)>

How [AudioTranscriptionConfig](-audio-transcription-config/index.html) transcribes speech; defaults to [VERBATIM](-audio-transcription-config-mode/-v-e-r-b-a-t-i-m/index.html) when unspecified.

[AutomaticActivityDetection](-automatic-activity-detection/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [AutomaticActivityDetection](-automatic-activity-detection/index.html)(val disabled: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val startOfSpeechSensitivity: [StartSensitivity](-start-sensitivity/index.html)? = null, val endOfSpeechSensitivity: [EndSensitivity](-end-sensitivity/index.html)? = null, val prefixPaddingMs: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val silenceDurationMs: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null)

Configures server-side detection of user activity (voice activity detection).

[Blob](-blob/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Blob](-blob/index.html)(val mimeType: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val displayName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val data: [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html)? = null)

Represents binary data.

[BlockedReason](-blocked-reason/index.html)

Link copied to clipboard

common

enum [BlockedReason](-blocked-reason/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[BlockedReason](-blocked-reason/index.html)>

The reason why the prompt was blocked.

[Candidate](-candidate/index.html)

Link copied to clipboard

common

data class [Candidate](-candidate/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val content: [Content](-content/index.html), val finishReason: [FinishReason](-finish-reason/index.html)? = null, val finishMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](-citation-metadata/index.html)? = null, val groundingMetadata: [GroundingMetadata](-grounding-metadata/index.html)? = null, val avgLogprobs: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, val logprobsResult: [LogprobsResult](-logprobs-result/index.html)? = null, val continuationToken: [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html)? = null)

Represents a possible response from the model.

[Citation](-citation/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Citation](-citation/index.html)(val title: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val uri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val startIndex: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val endIndex: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null)

Represents a citation to a source.

[CitationMetadata](-citation-metadata/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [CitationMetadata](-citation-metadata/index.html)(val citationSources: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Citation](-citation/index.html)> = emptyList())

Metadata about citations associated with the candidate.

[CodeExecutionResult](-code-execution-result/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [CodeExecutionResult](-code-execution-result/index.html)(val outcome: [Outcome](-outcome/index.html)? = null, val output: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val id: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

The result of executing an [ExecutableCode](-executable-code/index.html). Produced when the code-execution tool is used.

[Content](-content/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Content](-content/index.html)(val role: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val parts: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Part](-part/index.html)> = emptyList())

Represents the content of a response, including its role and parts.

[ContextWindowCompressionConfig](-context-window-compression-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [ContextWindowCompressionConfig](-context-window-compression-config/index.html)(val triggerTokens: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val slidingWindow: [SlidingWindow](-sliding-window/index.html)? = null)

Enables context window compression, which keeps a live session's context below a given length so a long conversation does not exhaust it.

[EndSensitivity](-end-sensitivity/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [EndSensitivity](-end-sensitivity/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[EndSensitivity](-end-sensitivity/index.html)>

How readily the model treats a pause as the end of speech.

[ExecutableCode](-executable-code/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [ExecutableCode](-executable-code/index.html)(val code: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val language: [Language](-language/index.html)? = null, val id: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Code generated by the model to be executed. Produced when the code-execution tool is used, alongside a matching [CodeExecutionResult](-code-execution-result/index.html).

[FileData](-file-data/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [FileData](-file-data/index.html)(val mimeType: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val displayName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val fileUri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Represents file data.

[FinishReason](-finish-reason/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [FinishReasonSerializer::class](../../google-adk-kotlin-core/com.google.adk.kt.types/-finish-reason-serializer/index.html))

enum [FinishReason](-finish-reason/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[FinishReason](-finish-reason/index.html)>

The reason why the generation finished.

[FunctionCall](-function-call/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [FunctionCall](-function-call/index.html)(val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val args: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?> = emptyMap(), val id: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val partialArgs: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[PartialArg](-partial-arg/index.html)>? = null, val willContinue: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Represents a function call in a generation response.

[FunctionCallingConfig](-function-calling-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [FunctionCallingConfig](-function-calling-config/index.html)(val allowedFunctionNames: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val streamFunctionCallArguments: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val mode: [FunctionCallingConfigMode](-function-calling-config-mode/index.html)? = null)

Configuration for how the model uses the provided function declarations.

[FunctionCallingConfigMode](-function-calling-config-mode/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [FunctionCallingConfigMode](-function-calling-config-mode/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[FunctionCallingConfigMode](-function-calling-config-mode/index.html)>

The mode controlling how the model chooses whether to emit function calls.

[FunctionDeclaration](-function-declaration/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [FunctionDeclaration](-function-declaration/index.html)(val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val parameters: [Schema](-schema/index.html)? = null, val response: [Schema](-schema/index.html)? = null)

Represents a function declaration for tool calling.

[FunctionResponse](-function-response/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [FunctionResponse](-function-response/index.html)(val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val response: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?> = emptyMap(), val id: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Represents a function response.

[GenerateContentConfig](-generate-content-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GenerateContentConfig](-generate-content-config/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val tools: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Tool](-tool/index.html)>? = null, val labels: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val systemInstruction: [Content](-content/index.html)? = null, val temperature: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null, val topP: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null, val topK: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val candidateCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val maxOutputTokens: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val stopSequences: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val responseMimeType: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val responseSchema: [Schema](-schema/index.html)? = null, val thinkingConfig: [ThinkingConfig](-thinking-config/index.html)? = null, val toolConfig: [ToolConfig](-tool-config/index.html)? = null, val safetySettings: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[SafetySetting](-safety-setting/index.html)>? = null, val mediaResolution: [MediaResolution](-media-resolution/index.html)? = null, val serviceTier: [ServiceTier](-service-tier/index.html)? = null, val presencePenalty: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null, val frequencyPenalty: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null, val responseLogprobs: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val routingConfig: [GenerationConfigRoutingConfig](-generation-config-routing-config/index.html)? = null, val cachedContent: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val responseModalities: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val seed: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val continuationToken: [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html)? = null)

Configuration for generating content.

[GenerateContentResponse](-generate-content-response/index.html)

Link copied to clipboard

common

data class [GenerateContentResponse](-generate-content-response/index.html)(val candidates: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Candidate](-candidate/index.html)> = emptyList(), val promptFeedback: [PromptFeedback](-prompt-feedback/index.html)? = null, val usageMetadata: [UsageMetadata](-usage-metadata/index.html)? = null, val modelVersion: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Response from the generate content request.

[GenerationConfigRoutingConfig](-generation-config-routing-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GenerationConfigRoutingConfig](-generation-config-routing-config/index.html)(val autoMode: [GenerationConfigRoutingConfigAutoRoutingMode](-generation-config-routing-config-auto-routing-mode/index.html)? = null, val manualMode: [GenerationConfigRoutingConfigManualRoutingMode](-generation-config-routing-config-manual-routing-mode/index.html)? = null)

Configuration for routing a request to a specific model, either automatically via [autoMode](../../google-adk-kotlin-core/com.google.adk.kt.types/-generation-config-routing-config/--root--.html) or manually via [manualMode](../../google-adk-kotlin-core/com.google.adk.kt.types/-generation-config-routing-config/--root--.html). Not supported in the Gemini API.

[GenerationConfigRoutingConfigAutoRoutingMode](-generation-config-routing-config-auto-routing-mode/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GenerationConfigRoutingConfigAutoRoutingMode](-generation-config-routing-config-auto-routing-mode/index.html)(val modelRoutingPreference: [ModelRoutingPreference](-model-routing-preference/index.html)? = null)

Configuration for automated routing, where the model is selected by the pretrained routing model and the customer-provided [modelRoutingPreference](../../google-adk-kotlin-core/com.google.adk.kt.types/-generation-config-routing-config-auto-routing-mode/--root--.html). Not supported in the Gemini API.

[GenerationConfigRoutingConfigManualRoutingMode](-generation-config-routing-config-manual-routing-mode/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GenerationConfigRoutingConfigManualRoutingMode](-generation-config-routing-config-manual-routing-mode/index.html)(val modelName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Configuration for manual routing, where the model is selected by the given [modelName](../../google-adk-kotlin-core/com.google.adk.kt.types/-generation-config-routing-config-manual-routing-mode/--root--.html). Only public LLM models are accepted. Not supported in the Gemini API.

[GoogleMaps](-google-maps/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GoogleMaps](-google-maps/index.html)(val enableWidget: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Tool to retrieve knowledge from Google Maps.

[GoogleSearch](-google-search/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GoogleSearch](-google-search/index.html)(val excludeDomains: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)> = emptyList())

Represents a Google Search tool.

[GroundingChunk](-grounding-chunk/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GroundingChunk](-grounding-chunk/index.html)(val web: [GroundingChunkWeb](-grounding-chunk-web/index.html)? = null, val retrievedContext: [GroundingChunkRetrievedContext](-grounding-chunk-retrieved-context/index.html)? = null, val maps: [GroundingChunkMaps](-grounding-chunk-maps/index.html)? = null)

A single cited source chunk that grounds part of the model's response.

[GroundingChunkMaps](-grounding-chunk-maps/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GroundingChunkMaps](-grounding-chunk-maps/index.html)(val uri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val title: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val placeId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val text: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

A grounding chunk sourced from Google Maps.

[GroundingChunkRetrievedContext](-grounding-chunk-retrieved-context/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GroundingChunkRetrievedContext](-grounding-chunk-retrieved-context/index.html)(val uri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val title: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val text: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

A grounding chunk sourced from a retrieval (RAG) context.

[GroundingChunkWeb](-grounding-chunk-web/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GroundingChunkWeb](-grounding-chunk-web/index.html)(val uri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val title: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val domain: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

A grounding chunk sourced from the open web.

[GroundingMetadata](-grounding-metadata/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GroundingMetadata](-grounding-metadata/index.html)(val imageSearchQueries: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val groundingChunks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[GroundingChunk](-grounding-chunk/index.html)>? = null, val groundingSupports: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[GroundingSupport](-grounding-support/index.html)>? = null, val webSearchQueries: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val retrievalQueries: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val searchEntryPoint: [SearchEntryPoint](-search-entry-point/index.html)? = null, val retrievalMetadata: [RetrievalMetadata](-retrieval-metadata/index.html)? = null)

Metadata returned to client when grounding is enabled.

[GroundingSupport](-grounding-support/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [GroundingSupport](-grounding-support/index.html)(val segment: [Segment](-segment/index.html)? = null, val groundingChunkIndices: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)>? = null, val confidenceScores: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)>? = null)

Maps a [Segment](-segment/index.html) of the response to the grounding chunks that support it.

[HarmBlockMethod](-harm-block-method/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [HarmBlockMethod](-harm-block-method/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[HarmBlockMethod](-harm-block-method/index.html)>

The method used to block content for a [HarmCategory](-harm-category/index.html). Not supported by the Gemini API.

[HarmBlockThreshold](-harm-block-threshold/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [HarmBlockThreshold](-harm-block-threshold/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[HarmBlockThreshold](-harm-block-threshold/index.html)>

The probability threshold at or above which content is blocked for a [HarmCategory](-harm-category/index.html).

[HarmCategory](-harm-category/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [HarmCategory](-harm-category/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[HarmCategory](-harm-category/index.html)>

The category of a harm that a [SafetySetting](-safety-setting/index.html) applies to.

[HttpOptions](-http-options/index.html)

Link copied to clipboard

common

data class [HttpOptions](-http-options/index.html)(val baseUrl: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val apiVersion: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val headers: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val timeout: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)? = null)

ADK-owned HTTP transport options for calls a [com.google.adk.kt.models.Model](../com.google.adk.kt.models/-model/index.html) makes to its backend.

[InteractionStatus](-interaction-status/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [InteractionStatusSerializer::class](../../google-adk-kotlin-core/com.google.adk.kt.types/-interaction-status-serializer/index.html))

enum [InteractionStatus](-interaction-status/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[InteractionStatus](-interaction-status/index.html)>

Whether the model is still working on the user's prompt.

[Language](-language/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [Language](-language/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[Language](-language/index.html)>

The programming language of an [ExecutableCode](-executable-code/index.html) part.

[LiveConnectConfig](-live-connect-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [LiveConnectConfig](-live-connect-config/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val responseModalities: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Modality](-modality/index.html)>? = null, val temperature: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null, val topP: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null, val topK: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val maxOutputTokens: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val mediaResolution: [MediaResolution](-media-resolution/index.html)? = null, val seed: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val speechConfig: [SpeechConfig](-speech-config/index.html)? = null, val thinkingConfig: [ThinkingConfig](-thinking-config/index.html)? = null, val enableAffectiveDialog: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val systemInstruction: [Content](-content/index.html)? = null, val tools: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Tool](-tool/index.html)>? = null, val sessionResumption: [SessionResumptionConfig](-session-resumption-config/index.html)? = null, val inputAudioTranscription: [AudioTranscriptionConfig](-audio-transcription-config/index.html)? = null, val outputAudioTranscription: [AudioTranscriptionConfig](-audio-transcription-config/index.html)? = null, val realtimeInputConfig: [RealtimeInputConfig](-realtime-input-config/index.html)? = null, val contextWindowCompression: [ContextWindowCompressionConfig](-context-window-compression-config/index.html)? = null, val proactivity: [ProactivityConfig](-proactivity-config/index.html)? = null, val safetySettings: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[SafetySetting](-safety-setting/index.html)>? = null, val explicitVadSignal: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val translationConfig: [TranslationConfig](-translation-config/index.html)? = null)

Configuration for a live (bidirectional streaming) model connection.

[LiveServerGoAway](-live-server-go-away/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [LiveServerGoAway](-live-server-go-away/index.html)(val timeLeft: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)? = null)

Warning that the server will stop serving this connection shortly.

[LiveServerSessionResumptionUpdate](-live-server-session-resumption-update/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [LiveServerSessionResumptionUpdate](-live-server-session-resumption-update/index.html)(val newHandle: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val resumable: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val lastConsumedClientMessageIndex: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null)

A handle for resuming this session on a later connection.

[LogprobsResult](-logprobs-result/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [LogprobsResult](-logprobs-result/index.html)(val chosenCandidates: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[LogprobsResultCandidate](-logprobs-result-candidate/index.html)>? = null, val topCandidates: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[LogprobsResultTopCandidates](-logprobs-result-top-candidates/index.html)>? = null, val logProbabilitySum: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null)

Detailed log probabilities for the chosen and top candidate tokens.

[LogprobsResultCandidate](-logprobs-result-candidate/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [LogprobsResultCandidate](-logprobs-result-candidate/index.html)(val token: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val tokenId: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val logProbability: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null)

A single token candidate and its log probability.

[LogprobsResultTopCandidates](-logprobs-result-top-candidates/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [LogprobsResultTopCandidates](-logprobs-result-top-candidates/index.html)(val candidates: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[LogprobsResultCandidate](-logprobs-result-candidate/index.html)>? = null)

The top token candidates at a single decoding step.

[MediaModality](-media-modality/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [MediaModality](-media-modality/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[MediaModality](-media-modality/index.html)>

The modality that a token count applies to.

[MediaResolution](-media-resolution/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [MediaResolution](-media-resolution/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[MediaResolution](-media-resolution/index.html)>

The resolution used when processing media inputs.

[Modality](-modality/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [Modality](-modality/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[Modality](-modality/index.html)>

A modality the model can return in a response.

[ModalityTokenCount](-modality-token-count/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [ModalityTokenCount](-modality-token-count/index.html)(val modality: [MediaModality](-media-modality/index.html)? = null, val tokenCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null)

A breakdown of token usage by modality.

[ModelRoutingPreference](-model-routing-preference/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [ModelRoutingPreference](-model-routing-preference/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[ModelRoutingPreference](-model-routing-preference/index.html)>

The model routing preference for automated routing.

[MultiSpeakerVoiceConfig](-multi-speaker-voice-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [MultiSpeakerVoiceConfig](-multi-speaker-voice-config/index.html)(val speakerVoiceConfigs: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[SpeakerVoiceConfig](-speaker-voice-config/index.html)>? = null)

Configuration for a multi-speaker text-to-speech request.

[Outcome](-outcome/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [Outcome](-outcome/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[Outcome](-outcome/index.html)>

The outcome of executing an [ExecutableCode](-executable-code/index.html) part.

[Part](-part/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

class [Part](-part/index.html)(val text: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val inlineData: [Blob](-blob/index.html)? = null, val fileData: [FileData](-file-data/index.html)? = null, val functionCall: [FunctionCall](-function-call/index.html)? = null, val functionResponse: [FunctionResponse](-function-response/index.html)? = null, val thought: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val thoughtSignature: [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html)? = null, val videoMetadata: [VideoMetadata](-video-metadata/index.html)? = null, val toolCall: [ToolCall](-tool-call/index.html)? = null, val toolResponse: [ToolResponse](-tool-response/index.html)? = null, val partMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null, val executableCode: [ExecutableCode](-executable-code/index.html)? = null, val codeExecutionResult: [CodeExecutionResult](-code-execution-result/index.html)? = null, val mediaResolution: [PartMediaResolution](-part-media-resolution/index.html)? = null)

A part of a multi-modal prompt or response.

[PartialArg](-partial-arg/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [PartialArg](-partial-arg/index.html)(val value: [PartialArgValue](-partial-arg-value/index.html)? = null, val jsonPath: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val willContinue: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Partial argument value of the function call.

[PartialArgValue](-partial-arg-value/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

sealed interface [PartialArgValue](-partial-arg-value/index.html)

Represents one of the possible values within a [PartialArg](-partial-arg/index.html).

[PartMediaResolution](-part-media-resolution/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [PartMediaResolution](-part-media-resolution/index.html)(val level: [PartMediaResolutionLevel](-part-media-resolution-level/index.html)? = null, val numTokens: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null)

The media resolution applied to a [Part](-part/index.html)'s media input.

[PartMediaResolutionLevel](-part-media-resolution-level/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [PartMediaResolutionLevel](-part-media-resolution-level/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[PartMediaResolutionLevel](-part-media-resolution-level/index.html)>

The tokenization quality used for a [Part](-part/index.html)'s media, set via [PartMediaResolution](-part-media-resolution/index.html).

[PrebuiltVoiceConfig](-prebuilt-voice-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [PrebuiltVoiceConfig](-prebuilt-voice-config/index.html)(val voiceName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Configuration for a prebuilt voice.

[ProactivityConfig](-proactivity-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [ProactivityConfig](-proactivity-config/index.html)(val proactiveAudio: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Config for proactivity features.

[PromptFeedback](-prompt-feedback/index.html)

Link copied to clipboard

common

data class [PromptFeedback](-prompt-feedback/index.html)(val blockReason: [BlockedReason](-blocked-reason/index.html)? = null, val blockReasonMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Feedback received from the prompt.

[RealtimeInputConfig](-realtime-input-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [RealtimeInputConfig](-realtime-input-config/index.html)(val automaticActivityDetection: [AutomaticActivityDetection](-automatic-activity-detection/index.html)? = null, val activityHandling: [ActivityHandling](-activity-handling/index.html)? = null, val turnCoverage: [TurnCoverage](-turn-coverage/index.html)? = null)

Configures how realtime input is interpreted as conversational turns.

[ReplicatedVoiceConfig](-replicated-voice-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [ReplicatedVoiceConfig](-replicated-voice-config/index.html)(val mimeType: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val voiceSampleAudio: [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html)? = null, val consentAudio: [ByteArray](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-byte-array/index.html)? = null, val voiceConsentSignature: [VoiceConsentSignature](-voice-consent-signature/index.html)? = null)

Configuration for a replicated (cloned) voice.

[Retrieval](-retrieval/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Retrieval](-retrieval/index.html)(val vertexAiSearch: [VertexAISearch](-vertex-a-i-search/index.html)? = null, val vertexRagStore: [VertexRagStore](-vertex-rag-store/index.html)? = null)

Defines a retrieval tool that model can call to access external knowledge.

[RetrievalMetadata](-retrieval-metadata/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [RetrievalMetadata](-retrieval-metadata/index.html)(val googleSearchDynamicRetrievalScore: [Float](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html)? = null)

Metadata about the retrieval step performed for a grounded response.

[Role](-role/index.html)

Link copied to clipboard

common

object [Role](-role/index.html)

Standard roles for content and events.

[SafetySetting](-safety-setting/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [SafetySetting](-safety-setting/index.html)(val category: [HarmCategory](-harm-category/index.html)? = null, val threshold: [HarmBlockThreshold](-harm-block-threshold/index.html)? = null, val method: [HarmBlockMethod](-harm-block-method/index.html)? = null)

A per-request safety setting controlling the block threshold for a single [HarmCategory](-harm-category/index.html).

[Schema](-schema/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Schema](-schema/index.html)(val type: [Type](-type/index.html)? = null, val properties: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Schema](-schema/index.html)>? = null, val items: [Schema](-schema/index.html)? = null, val required: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val enum: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val format: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val nullable: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val default: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, val anyOf: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Schema](-schema/index.html)>? = null, val title: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val pattern: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val minimum: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, val maximum: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, val minLength: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val maxLength: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val minItems: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val maxItems: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val minProperties: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val maxProperties: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null)

Schema is used to define the format of input/output data.

[SearchEntryPoint](-search-entry-point/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [SearchEntryPoint](-search-entry-point/index.html)(val renderedContent: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

The Google Search entry point used to render search suggestions for grounded responses.

[Segment](-segment/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Segment](-segment/index.html)(val startIndex: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val endIndex: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val partIndex: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val text: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

A contiguous segment of the response content that a [GroundingSupport](-grounding-support/index.html) refers to.

[ServiceTier](-service-tier/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [ServiceTier](-service-tier/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[ServiceTier](-service-tier/index.html)>

The service tier requested for a generate content request.

[SessionResumptionConfig](-session-resumption-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [SessionResumptionConfig](-session-resumption-config/index.html)(val handle: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val transparent: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Configures the session resumption mechanism.

[SlidingWindow](-sliding-window/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [SlidingWindow](-sliding-window/index.html)(val targetTokens: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null)

Sliding-window context compression: the oldest turns are dropped once the window is exceeded.

[SpeakerVoiceConfig](-speaker-voice-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [SpeakerVoiceConfig](-speaker-voice-config/index.html)(val speaker: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val voiceConfig: [VoiceConfig](-voice-config/index.html)? = null)

Configuration for a single speaker in a multi-speaker setup.

[SpeechConfig](-speech-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [SpeechConfig](-speech-config/index.html)(val voiceConfig: [VoiceConfig](-voice-config/index.html)? = null, val languageCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val multiSpeakerVoiceConfig: [MultiSpeakerVoiceConfig](-multi-speaker-voice-config/index.html)? = null)

Config for speech generation and transcription.

[StartSensitivity](-start-sensitivity/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [StartSensitivity](-start-sensitivity/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[StartSensitivity](-start-sensitivity/index.html)>

How readily the model treats incoming audio as the start of speech.

[ThinkingConfig](-thinking-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [ThinkingConfig](-thinking-config/index.html)(val includeThoughts: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val thinkingBudget: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val thinkingLevel: [ThinkingLevel](-thinking-level/index.html)? = null)

The thinking features configuration.

[ThinkingLevel](-thinking-level/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [ThinkingLevel](-thinking-level/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[ThinkingLevel](-thinking-level/index.html)>

The number of thoughts tokens that the model should generate.

[Tool](-tool/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Tool](-tool/index.html)(val functionDeclarations: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[FunctionDeclaration](-function-declaration/index.html)>? = null, val googleSearch: [GoogleSearch](-google-search/index.html)? = null, val googleMaps: [GoogleMaps](-google-maps/index.html)? = null, val retrieval: [Retrieval](-retrieval/index.html)? = null, val urlContext: [UrlContext](-url-context/index.html)? = null)

Represents a GenAI tool definition.

[ToolCall](-tool-call/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [ToolCall](-tool-call/index.html)(val id: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val toolType: [ToolType](-tool-type/index.html)? = null, val args: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null)

A tool call the model runs on its own server side.

[ToolConfig](-tool-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [ToolConfig](-tool-config/index.html)(val functionCallingConfig: [FunctionCallingConfig](-function-calling-config/index.html)? = null)

Configuration shared across all tools provided in a request.

[ToolResponse](-tool-response/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [ToolResponse](-tool-response/index.html)(val id: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val toolType: [ToolType](-tool-type/index.html)? = null, val response: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null)

The output of a server-side [ToolCall](-tool-call/index.html) the model ran itself.

[ToolType](-tool-type/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

@[JvmInline](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-inline/index.html)

value class [ToolType](-tool-type/index.html)(val value: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html))

The type of tool a server-side [ToolCall](-tool-call/index.html) invoked.

[Transcription](-transcription/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Transcription](-transcription/index.html)(val text: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val finished: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val languageCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val speakerLabel: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val words: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[WordInfo](-word-info/index.html)>? = null)

A transcription of audio, either the user's input or the model's output.

[TranslationConfig](-translation-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [TranslationConfig](-translation-config/index.html)(val targetLanguageCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val echoTargetLanguage: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null)

Configuration for real-time speech-to-speech translation.

[TurnCompleteReason](-turn-complete-reason/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [TurnCompleteReasonSerializer::class](../../google-adk-kotlin-core/com.google.adk.kt.types/-turn-complete-reason-serializer/index.html))

enum [TurnCompleteReason](-turn-complete-reason/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[TurnCompleteReason](-turn-complete-reason/index.html)>

Why a live turn ended.

[TurnCoverage](-turn-coverage/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [TurnCoverage](-turn-coverage/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[TurnCoverage](-turn-coverage/index.html)>

Which realtime input counts towards the user's turn.

[Type](-type/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

enum [Type](-type/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[Type](-type/index.html)>

The value type of the schema.

[UrlContext](-url-context/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

class [UrlContext](-url-context/index.html)

Tool to support URL context retrieval.

[UsageMetadata](-usage-metadata/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [UsageMetadata](-usage-metadata/index.html)(val promptTokenCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val candidatesTokenCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val totalTokenCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val thoughtsTokenCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val toolUsePromptTokenCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val cachedContentTokenCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val promptTokensDetails: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](-modality-token-count/index.html)>? = null, val candidatesTokensDetails: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](-modality-token-count/index.html)>? = null, val toolUsePromptTokensDetails: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](-modality-token-count/index.html)>? = null, val trafficType: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Usage metadata for a generate content request.

[VertexAISearch](-vertex-a-i-search/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [VertexAISearch](-vertex-a-i-search/index.html)(val dataStoreSpecs: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[VertexAISearchDataStoreSpec](-vertex-a-i-search-data-store-spec/index.html)>? = null, val datastore: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val engine: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val filter: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val maxResults: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null)

Retrieve from Vertex AI Search datastore or engine for grounding. datastore and engine are mutually exclusive.

[VertexAISearchDataStoreSpec](-vertex-a-i-search-data-store-spec/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [VertexAISearchDataStoreSpec](-vertex-a-i-search-data-store-spec/index.html)(val dataStore: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val filter: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Define data stores within engine to filter on in a search call and configurations for those data stores.

[VertexRagStore](-vertex-rag-store/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [VertexRagStore](-vertex-rag-store/index.html)(val ragCorpora: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val ragResources: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[VertexRagStoreRagResource](-vertex-rag-store-rag-resource/index.html)>? = null, val similarityTopK: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val vectorDistanceThreshold: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null)

Retrieve from a Vertex RAG store for grounding.

[VertexRagStoreRagResource](-vertex-rag-store-rag-resource/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [VertexRagStoreRagResource](-vertex-rag-store-rag-resource/index.html)(val ragCorpus: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val ragFileIds: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null)

The representation of a RAG source for a [VertexRagStore](-vertex-rag-store/index.html).

[VideoMetadata](-video-metadata/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [VideoMetadata](-video-metadata/index.html)(val startOffset: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)? = null, val endOffset: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)? = null, val fps: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null)

Metadata describing how to interpret a video [Part](-part/index.html).

[VoiceActivity](-voice-activity/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [VoiceActivity](-voice-activity/index.html)(val voiceActivityType: [VoiceActivityType](-voice-activity-type/index.html)? = null, val audioOffset: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)? = null)

A server-detected change in whether the user is speaking.

[VoiceActivityType](-voice-activity-type/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [VoiceActivityTypeSerializer::class](../../google-adk-kotlin-core/com.google.adk.kt.types/-voice-activity-type-serializer/index.html))

enum [VoiceActivityType](-voice-activity-type/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[VoiceActivityType](-voice-activity-type/index.html)>

Which edge of a stretch of user speech the server detected.

[VoiceConfig](-voice-config/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [VoiceConfig](-voice-config/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val replicatedVoiceConfig: [ReplicatedVoiceConfig](-replicated-voice-config/index.html)? = null, val prebuiltVoiceConfig: [PrebuiltVoiceConfig](-prebuilt-voice-config/index.html)? = null, val voice: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

The configuration for the voice to use.

[VoiceConsentSignature](-voice-consent-signature/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [VoiceConsentSignature](-voice-consent-signature/index.html)(val signature: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

A server-issued signature attesting that voice consent was already verified.

[WordInfo](-word-info/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [WordInfo](-word-info/index.html)(val word: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val startOffset: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val endOffset: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

A single transcribed word and where it falls in the audio.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
