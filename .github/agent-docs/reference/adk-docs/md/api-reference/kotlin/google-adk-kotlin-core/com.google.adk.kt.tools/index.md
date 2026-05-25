toggle menu

[ google-adk-kotlin ](../../index.html)

0.1.0 

commonJvmAndroid common jvm

switch theme

search in API

[google-adk-kotlin-core](../index.html)/com.google.adk.kt.tools

# Package-level declarations

Types

## Types

[AgentTool](-agent-tool/index.html)

Link copied to clipboard

class [AgentTool](-agent-tool/index.html)(val agent: [BaseAgent](../com.google.adk.kt.agents/-base-agent/index.html), val skipSummarization: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false) : [BaseTool](-base-tool/index.html)

A tool that wraps a [BaseAgent](../com.google.adk.kt.agents/-base-agent/index.html).

[BaseTool](-base-tool/index.html)

Link copied to clipboard

abstract class [BaseTool](-base-tool/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val isLongRunning: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap()) : [AutoCloseable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-auto-closeable/index.html)

Abstract base class for defining and executing tools.

[ExitLoopTool](-exit-loop-tool/index.html)

Link copied to clipboard

class [ExitLoopTool](-exit-loop-tool/index.html) : [BaseTool](-base-tool/index.html)

A tool that allows an agent to exit a loop.

[FunctionTool](-function-tool/index.html)

Link copied to clipboard

abstract class [FunctionTool](-function-tool/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val isLongRunning: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap(), requiresConfirmation: ([Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>) -> [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = { false }) : [BaseTool](-base-tool/index.html)

Represents a compile-time generated tool that wraps a function annotated with [com.google.adk.kt.annotations.Tool](../com.google.adk.kt.annotations/-tool/index.html).

[GoogleMapsTool](-google-maps-tool/index.html)

Link copied to clipboard

jvm

class [GoogleMapsTool](-google-maps-tool/index.html)(val model: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null) : [BaseTool](-base-tool/index.html)

A built-in tool that is automatically invoked by Gemini 2 models to retrieve search results from Google Maps.

[GoogleSearchTool](-google-search-tool/index.html)

Link copied to clipboard

jvm

class [GoogleSearchTool](-google-search-tool/index.html)(val bypassMultiToolsLimit: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val model: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null) : [BaseTool](-base-tool/index.html)

A built-in tool that is automatically invoked by Gemini 2 and 3 models to retrieve search results from Google Search.

[LoadArtifactsTool](-load-artifacts-tool/index.html)

Link copied to clipboard

class [LoadArtifactsTool](-load-artifacts-tool/index.html) : [BaseTool](-base-tool/index.html)

A tool that loads artifacts and adds them to the session.

[LoadMemoryTool](-load-memory-tool/index.html)

Link copied to clipboard

class [LoadMemoryTool](-load-memory-tool/index.html) : [BaseTool](-base-tool/index.html)

A tool that loads the memory for the current user.

[PreloadMemoryTool](-preload-memory-tool/index.html)

Link copied to clipboard

class [PreloadMemoryTool](-preload-memory-tool/index.html) : [BaseTool](-base-tool/index.html)

A tool that preloads the memory for the current user.

[PromptFormat](-prompt-format/index.html)

Link copied to clipboard

commonJvmAndroid

enum [PromptFormat](-prompt-format/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[PromptFormat](-prompt-format/index.html)>

The format to use when rendering prompt descriptions of tools.

[ReadonlyToolContext](-readonly-tool-context/index.html)

Link copied to clipboard

interface [ReadonlyToolContext](-readonly-tool-context/index.html)

A readonly view of the tool context.

[Schema](-schema/index.html)

Link copied to clipboard

@[Target](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.annotation/-target/index.html)(allowedTargets = [[AnnotationTarget.FUNCTION](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.annotation/-annotation-target/-f-u-n-c-t-i-o-n/index.html), [AnnotationTarget.VALUE_PARAMETER](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.annotation/-annotation-target/-v-a-l-u-e_-p-a-r-a-m-e-t-e-r/index.html)])

annotation class [Schema](-schema/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val optional: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

The annotation for binding the 'Schema' input.

[SkillToolset](-skill-toolset/index.html)

Link copied to clipboard

class [SkillToolset](-skill-toolset/index.html)(source: [SkillSource](../com.google.adk.kt.skills/-skill-source/index.html)) : [Toolset](-toolset/index.html)

Toolset that manages and provides access to a collection of Skills.

[ToolContext](-tool-context/index.html)

Link copied to clipboard

class [ToolContext](-tool-context/index.html)(val invocationContext: [InvocationContext](../com.google.adk.kt.agents/-invocation-context/index.html), val actions: [EventActions](../com.google.adk.kt.events/-event-actions/index.html) = EventActions(), val functionCallId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val toolConfirmation: [ToolConfirmation](../com.google.adk.kt.events/-tool-confirmation/index.html)? = null, val eventId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null) : [ReadonlyToolContext](-readonly-tool-context/index.html)

ToolContext provides a structured context for executing tools or functions.

[Toolset](-toolset/index.html)

Link copied to clipboard

interface [Toolset](-toolset/index.html) : [AutoCloseable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-auto-closeable/index.html)

Base interface for toolsets.

[VertexAiSearchTool](-vertex-ai-search-tool/index.html)

Link copied to clipboard

jvm

class [VertexAiSearchTool](-vertex-ai-search-tool/index.html)(val dataStoreId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val dataStoreSpecs: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[VertexAISearchDataStoreSpec](../com.google.adk.kt.types/-vertex-a-i-search-data-store-spec/index.html)>? = null, val searchEngineId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val filter: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val maxResults: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val model: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null) : [BaseTool](-base-tool/index.html)

A built-in tool using Vertex AI Search.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
