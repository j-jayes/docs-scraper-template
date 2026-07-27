toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.tools](../index.html)/AgentTool

# AgentTool

open class [AgentTool](index.html)(val agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), val skipSummarization: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val includePlugins: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = true, val propagateGroundingMetadata: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false) : [BaseTool](../-base-tool/index.html)

A tool that wraps a [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html).

This tool allows an agent to be called as a tool within a larger application. The agent's input schema is used to define the tool's input parameters, and the agent's output is returned as the tool's result.

Members

## Constructors

[AgentTool](-agent-tool.html)

Link copied to clipboard

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), skipSummarization: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, includePlugins: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = true, propagateGroundingMetadata: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

## Types

[Companion](-companion/index.html)

Link copied to clipboard

object [Companion](-companion/index.html)

## Properties

[agent](agent.html)

Link copied to clipboard

val [agent](agent.html): [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html)

The agent to wrap.

[customMetadata](../-base-tool/custom-metadata.html)

Link copied to clipboard

val [customMetadata](../-base-tool/custom-metadata.html): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>

The custom metadata of the tool.

[description](../-base-tool/description.html)

Link copied to clipboard

val [description](../-base-tool/description.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The description of the tool.

[includePlugins](include-plugins.html)

Link copied to clipboard

val [includePlugins](include-plugins.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = true

Whether the parent runner's plugins should be propagated to the wrapped agent's runner. When `true` (the default), the wrapped agent observes the same plugins as the parent (their plugin callbacks fire for the child invocation). When `false`, the wrapped agent runs with no plugins.

[isLongRunning](../-base-tool/is-long-running.html)

Link copied to clipboard

val [isLongRunning](../-base-tool/is-long-running.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

Whether the tool's final result will be delivered out-of-band. When `true`, the framework marks the call as long-running and uses the tool's return value as the function-response payload. Returning `Unit` means "no response yet": the FR event is suppressed so the function-call event (which carries the call id in `longRunningToolIds` and is thus the turn's final response) ends the turn without re-invoking the model. A non-`Unit` return -- including an explicit empty `Map` \-- is treated as a real response and emitted. (`Unit` suppression aligns with Python; Java instead always emits `{}`.) The `longRunningToolIds` id also drives the resumable-mode pause gate so the invocation can be resumed later via a user-injected function-response.

[name](../-base-tool/name.html)

Link copied to clipboard

val [name](../-base-tool/name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The name of the tool.

[propagateGroundingMetadata](propagate-grounding-metadata.html)

Link copied to clipboard

val [propagateGroundingMetadata](propagate-grounding-metadata.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

Whether grounding metadata produced by the wrapped agent should be propagated back to the parent invocation. Used by the built-in-tool workaround (e.g. [GoogleSearchAgentTool](../../../google-adk-kotlin-core/com.google.adk.kt.tools/-google-search-agent-tool/index.html)) so the parent still surfaces the sub-agent's grounding metadata.

[skipSummarization](skip-summarization.html)

Link copied to clipboard

val [skipSummarization](skip-summarization.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

Whether to skip summarization of the agent output in the parent agent.

## Functions

[close](../-base-tool/close.html)

Link copied to clipboard

open fun [close](../-base-tool/close.html)()

[declaration](declaration.html)

Link copied to clipboard

open override fun [declaration](declaration.html)(): [FunctionDeclaration](../../com.google.adk.kt.types/-function-declaration/index.html)

Returns the underlying function declaration.

[processLlmRequest](../-base-tool/process-llm-request.html)

Link copied to clipboard

open suspend fun [processLlmRequest](../-base-tool/process-llm-request.html)(toolContext: [ToolContext](../-tool-context/index.html), llmRequest: [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)): [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)

Processes the LLM request before it is sent.

[run](run.html)

Link copied to clipboard

open suspend override fun [run](run.html)(context: [ToolContext](../-tool-context/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

Executes the tool and returns its result.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
