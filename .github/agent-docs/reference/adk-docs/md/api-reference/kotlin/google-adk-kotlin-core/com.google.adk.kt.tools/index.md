[ google-adk-kotlin ](../../index.html) Toggle table of contents 

1.4.0 

commonJvmAndroid common jvm

Target filter __

    * commonJvmAndroid 
    * common 
    * jvm 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../index.html)/com.google.adk.kt.tools

# Package-level declarations

TypesFunctions

## Types

[AgentTool](-agent-tool/index.html)

Link copied to clipboard

common

open class [AgentTool](-agent-tool/index.html)(val agent: [BaseAgent](../com.google.adk.kt.agents/-base-agent/index.html), val skipSummarization: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val includePlugins: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = true, val propagateGroundingMetadata: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false) : [BaseTool](-base-tool/index.html)

A tool that wraps a [BaseAgent](../com.google.adk.kt.agents/-base-agent/index.html).

[BaseRetrievalTool](-base-retrieval-tool/index.html)

Link copied to clipboard

common

abstract class [BaseRetrievalTool](-base-retrieval-tool/index.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), isLongRunning: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false) : [BaseTool](-base-tool/index.html)

Base class for retrieval tools.

[BaseTool](-base-tool/index.html)

Link copied to clipboard

common

abstract class [BaseTool](-base-tool/index.html)(val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val isLongRunning: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap()) : [AutoCloseable](https://developer.android.com/reference/kotlin/java/lang/AutoCloseable.html)

Abstract base class for defining and executing tools.

[ExitLoopTool](-exit-loop-tool/index.html)

Link copied to clipboard

common

class [ExitLoopTool](-exit-loop-tool/index.html) : [BaseTool](-base-tool/index.html)

A tool that allows an agent to exit a loop.

[FunctionTool](-function-tool/index.html)

Link copied to clipboard

common

abstract class [FunctionTool](-function-tool/index.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), isLongRunning: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap(), requiresConfirmation: ([Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>) -> [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = { false }) : [BaseTool](-base-tool/index.html)

Represents a compile-time generated tool that wraps a function annotated with [com.google.adk.kt.annotations.Tool](../com.google.adk.kt.annotations/-tool/index.html).

[GetUserChoiceTool](-get-user-choice-tool/index.html)

Link copied to clipboard

common

class [GetUserChoiceTool](-get-user-choice-tool/index.html) : [BaseTool](-base-tool/index.html)

Built-in long-running tool that presents a list of options and pauses the invocation until the user picks one.

[GoogleMapsTool](-google-maps-tool/index.html)

Link copied to clipboard

common

class [GoogleMapsTool](-google-maps-tool/index.html) : [BaseTool](-base-tool/index.html)

A built-in tool that is automatically invoked by Gemini 2 models to retrieve search results from Google Maps.

[GoogleSearchTool](-google-search-tool/index.html)

Link copied to clipboard

common

class [GoogleSearchTool](-google-search-tool/index.html)(val bypassMultiToolsLimit: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false) : [BaseTool](-base-tool/index.html)

A built-in tool that is automatically invoked by Gemini 2 and 3 models to retrieve search results from Google Search.

[LoadArtifactsTool](-load-artifacts-tool/index.html)

Link copied to clipboard

common

class [LoadArtifactsTool](-load-artifacts-tool/index.html) : [BaseTool](-base-tool/index.html)

A tool that loads artifacts and adds them to the session.

[LoadMemoryTool](-load-memory-tool/index.html)

Link copied to clipboard

common

class [LoadMemoryTool](-load-memory-tool/index.html) : [BaseTool](-base-tool/index.html)

A tool that loads the memory for the current user.

[PreloadMemoryTool](-preload-memory-tool/index.html)

Link copied to clipboard

common

class [PreloadMemoryTool](-preload-memory-tool/index.html) : [BaseTool](-base-tool/index.html)

A tool that preloads the memory for the current user.

[ReadonlyToolContext](-readonly-tool-context/index.html)

Link copied to clipboard

common

interface [ReadonlyToolContext](-readonly-tool-context/index.html)

A readonly view of the tool context.

[RequestInputTool](-request-input-tool/index.html)

Link copied to clipboard

common

class [RequestInputTool](-request-input-tool/index.html) : [BaseTool](-base-tool/index.html)

Built-in long-running tool that asks the user a question and pauses the invocation until they respond.

[Schema](-schema/index.html)

Link copied to clipboard

common

@[Target](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [[AnnotationTarget.FUNCTION](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html), [AnnotationTarget.VALUE_PARAMETER](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.annotation/-annotation-target/-v-a-l-u-e_-p-a-r-a-m-e-t-e-r/index.html)])

annotation class [Schema](-schema/index.html)(val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val optional: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false)

The annotation for binding the 'Schema' input.

[SkillToolset](-skill-toolset/index.html)

Link copied to clipboard

common

class [SkillToolset](-skill-toolset/index.html) @[ExperimentalEnvironmentApi](../com.google.adk.kt.annotations/-experimental-environment-api/index.html) constructor(source: [SkillSource](../com.google.adk.kt.skills/-skill-source/index.html), environment: [Environment](../com.google.adk.kt.environment/-environment/index.html)?, scriptTimeout: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) = DEFAULT_SCRIPT_TIMEOUT) : [Toolset](-toolset/index.html)

Toolset exposing the skills a [SkillSource](../com.google.adk.kt.skills/-skill-source/index.html) provides. When [environment](../../google-adk-kotlin-core/com.google.adk.kt.tools/-skill-toolset/--root--.html) is set, it also exposes `run_skill_script`, which copies the skill into `skills/<skill_name>/` in the environment and runs the model's command there.

[ToolContext](-tool-context/index.html)

Link copied to clipboard

common

class [ToolContext](-tool-context/index.html)(invocationContext: [InvocationContext](../com.google.adk.kt.agents/-invocation-context/index.html), actions: [EventActions](../com.google.adk.kt.events/-event-actions/index.html) = EventActions(), functionCallId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, toolConfirmation: [ToolConfirmation](../com.google.adk.kt.events/-tool-confirmation/index.html)? = null, eventId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null) : [Context](../com.google.adk.kt.agents/-context/index.html)

Context passed to tool executions.

[ToolFilter](-tool-filter/index.html)

Link copied to clipboard

common

sealed interface [ToolFilter](-tool-filter/index.html)

Selects which tools a [Toolset](-toolset/index.html) exposes to the LLM.

[ToolPredicate](-tool-predicate/index.html)

Link copied to clipboard

common

fun interface [ToolPredicate](-tool-predicate/index.html)

Decides whether a [BaseTool](-base-tool/index.html) should be exposed to the LLM under the current context.

[Toolset](-toolset/index.html)

Link copied to clipboard

common

interface [Toolset](-toolset/index.html) : [AutoCloseable](https://developer.android.com/reference/kotlin/java/lang/AutoCloseable.html)

Base interface for toolsets.

[UrlContextTool](-url-context-tool/index.html)

Link copied to clipboard

common

class [UrlContextTool](-url-context-tool/index.html) : [BaseTool](-base-tool/index.html)

A built-in tool that is automatically invoked by Gemini models to retrieve content from the given URLs and use that content to inform and shape its response.

[VertexAiRagClientTool](-vertex-ai-rag-client-tool/index.html)

Link copied to clipboard

jvm

class [VertexAiRagClientTool](-vertex-ai-rag-client-tool/index.html) : [BaseRetrievalTool](-base-retrieval-tool/index.html)

A client-side retrieval tool that fetches context from a Vertex AI RAG corpus.

[VertexAiRagRetrieval](-vertex-ai-rag-retrieval/index.html)

Link copied to clipboard

common

class [VertexAiRagRetrieval](-vertex-ai-rag-retrieval/index.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val ragCorpora: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val ragResources: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[VertexRagStoreRagResource](../com.google.adk.kt.types/-vertex-rag-store-rag-resource/index.html)>? = null, val similarityTopK: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val vectorDistanceThreshold: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null) : [BaseTool](-base-tool/index.html)

A built-in tool that uses Vertex AI RAG (Retrieval-Augmented Generation) to retrieve data.

[VertexAiSearchTool](-vertex-ai-search-tool/index.html)

Link copied to clipboard

common

class [VertexAiSearchTool](-vertex-ai-search-tool/index.html)(val dataStoreId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val dataStoreSpecs: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[VertexAISearchDataStoreSpec](../com.google.adk.kt.types/-vertex-a-i-search-data-store-spec/index.html)>? = null, val searchEngineId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val filter: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val maxResults: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val bypassMultiToolsLimit: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false) : [BaseTool](-base-tool/index.html)

A built-in tool using Vertex AI Search.

## Functions

[isToolSelected](is-tool-selected.html)

Link copied to clipboard

common

fun [ToolFilter](-tool-filter/index.html)?.[isToolSelected](is-tool-selected.html)(tool: [BaseTool](-base-tool/index.html), readonlyContext: [ReadonlyContext](../com.google.adk.kt.agents/-readonly-context/index.html)? = null): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Returns whether [tool](is-tool-selected.html) is selected by this filter under [readonlyContext](is-tool-selected.html).

[toJsonSchema](to-json-schema.html)

Link copied to clipboard

commonJvmAndroid

fun [Schema](../com.google.adk.kt.types/-schema/index.html).[toJsonSchema](to-json-schema.html)(): [JsonObject](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html)

Renders this [Schema](../com.google.adk.kt.types/-schema/index.html) as a JSON Schema [JsonObject](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html), the same shape used in prompt tool descriptions. Exposed so an adapter can hand a tool's parameter schema to another framework rather than forking this conversion.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
