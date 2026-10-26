[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.tools](../index.html)/BaseTool

# BaseTool

common

abstract class [BaseTool](index.html)(val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val isLongRunning: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap()) : [AutoCloseable](https://developer.android.com/reference/kotlin/java/lang/AutoCloseable.html)

Abstract base class for defining and executing tools.

#### Inheritors

[BaseFutureTool](../../com.google.adk.kt.interop/-base-future-tool/index.html#-734085188%2FMain%2F-1855338903)

[AgentTool](../-agent-tool/index.html)

[BaseRetrievalTool](../-base-retrieval-tool/index.html)

[ExitLoopTool](../-exit-loop-tool/index.html)

[FunctionTool](../-function-tool/index.html)

[GetUserChoiceTool](../-get-user-choice-tool/index.html)

[GoogleMapsTool](../-google-maps-tool/index.html)

[GoogleSearchTool](../-google-search-tool/index.html)

[LoadArtifactsTool](../-load-artifacts-tool/index.html)

[LoadMemoryTool](../-load-memory-tool/index.html)

[PreloadMemoryTool](../-preload-memory-tool/index.html)

[RequestInputTool](../-request-input-tool/index.html)

[UrlContextTool](../-url-context-tool/index.html)

[VertexAiRagRetrieval](../-vertex-ai-rag-retrieval/index.html)

[VertexAiSearchTool](../-vertex-ai-search-tool/index.html)

[McpTool](../../com.google.adk.kt.tools.mcp/-mcp-tool/index.html#-1403644802%2FMain%2F-1855338903)

MembersMembers & Extensions

## Constructors

[BaseTool](-base-tool.html)

Link copied to clipboard

common

constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), isLongRunning: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap())

## Types

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[customMetadata](custom-metadata.html)

Link copied to clipboard

common

val [customMetadata](custom-metadata.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

The custom metadata of the tool.

[description](description.html)

Link copied to clipboard

common

val [description](description.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The description of the tool.

[isLongRunning](is-long-running.html)

Link copied to clipboard

common

val [isLongRunning](is-long-running.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether the tool's final result will be delivered out-of-band. When `true`, the framework marks the call as long-running and uses the tool's return value as the function-response payload. Returning `Unit` means "no response yet": the FR event is suppressed so the function-call event (which carries the call id in `longRunningToolIds` and is thus the turn's final response) ends the turn without re-invoking the model. A non-`Unit` return -- including an explicit empty `Map` \-- is treated as a real response and emitted. (`Unit` suppression aligns with Python; Java instead always emits `{}`.) The `longRunningToolIds` id also drives the resumable-mode pause gate so the invocation can be resumed later via a user-injected function-response.

[name](name.html)

Link copied to clipboard

common

val [name](name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The name of the tool.

## Functions

[asNode](../../com.google.adk.kt.workflow/as-node.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

fun [BaseTool](index.html).[asNode](../../com.google.adk.kt.workflow/as-node.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = this.name, config: [NodeConfig](../../com.google.adk.kt.workflow/-node-config/index.html) = NodeConfig()): [Node](../../com.google.adk.kt.workflow/-node/index.html)

Returns a workflow node that runs this tool as a fixed step: the predecessor's output becomes the tool's arguments, and the tool's result becomes the node's output.

[close](close.html)

Link copied to clipboard

common

open override fun [close](close.html)()

[declaration](declaration.html)

Link copied to clipboard

common

abstract fun [declaration](declaration.html)(): [FunctionDeclaration](../../com.google.adk.kt.types/-function-declaration/index.html)?

Returns the underlying function declaration.

[processLlmRequest](process-llm-request.html)

Link copied to clipboard

common

open suspend fun [processLlmRequest](process-llm-request.html)(toolContext: [ToolContext](../-tool-context/index.html), llmRequest: [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)): [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)

Processes the LLM request before it is sent.

[run](run.html)

Link copied to clipboard

common

abstract suspend fun [run](run.html)(context: [ToolContext](../-tool-context/index.html), args: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)

Executes the tool and returns its result.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
