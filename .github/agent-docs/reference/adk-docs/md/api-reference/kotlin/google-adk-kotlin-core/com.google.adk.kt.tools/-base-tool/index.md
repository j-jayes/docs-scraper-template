toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.tools](../index.html)/BaseTool

# BaseTool

abstract class [BaseTool](index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val isLongRunning: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap()) : [AutoCloseable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-auto-closeable/index.html)

Abstract base class for defining and executing tools.

#### Inheritors

[AgentTool](../-agent-tool/index.html)

[ExitLoopTool](../-exit-loop-tool/index.html)

[FunctionTool](../-function-tool/index.html)

[GoogleMapsTool](../-google-maps-tool/index.html)

[GoogleSearchTool](../-google-search-tool/index.html)

[LoadArtifactsTool](../-load-artifacts-tool/index.html)

[LoadMemoryTool](../-load-memory-tool/index.html)

[PreloadMemoryTool](../-preload-memory-tool/index.html)

[VertexAiSearchTool](../-vertex-ai-search-tool/index.html)

[McpTool](../../../google-adk-kotlin-core/com.google.adk.kt.tools.mcp/-mcp-tool/index.html)

Members

## Constructors

[BaseTool](-base-tool.html)

Link copied to clipboard

constructor(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), isLongRunning: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap())

## Types

[Companion](-companion/index.html)

Link copied to clipboard

object [Companion](-companion/index.html)

## Properties

[customMetadata](custom-metadata.html)

Link copied to clipboard

val [customMetadata](custom-metadata.html): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>

The custom metadata of the tool.

[description](description.html)

Link copied to clipboard

val [description](description.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The description of the tool.

[isLongRunning](is-long-running.html)

Link copied to clipboard

val [isLongRunning](is-long-running.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

Whether the tool's final result will be delivered out-of-band. When `true`, the framework marks the call as long-running and uses the tool's return value as the function-response payload (or suppresses the response entirely if the tool returns `Unit`).

[name](name.html)

Link copied to clipboard

val [name](name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The name of the tool.

## Functions

[close](close.html)

Link copied to clipboard

open override fun [close](close.html)()

[declaration](declaration.html)

Link copied to clipboard

abstract fun [declaration](declaration.html)(): [FunctionDeclaration](../../com.google.adk.kt.types/-function-declaration/index.html)?

Returns the underlying function declaration.

[processLlmRequest](process-llm-request.html)

Link copied to clipboard

open suspend fun [processLlmRequest](process-llm-request.html)(toolContext: [ToolContext](../-tool-context/index.html), llmRequest: [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)): [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)

Processes the LLM request before it is sent.

[run](run.html)

Link copied to clipboard

abstract suspend fun [run](run.html)(context: [ToolContext](../-tool-context/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)

Executes the tool.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
