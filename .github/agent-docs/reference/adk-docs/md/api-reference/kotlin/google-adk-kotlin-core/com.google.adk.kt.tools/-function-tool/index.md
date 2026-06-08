toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.tools](../index.html)/FunctionTool

# FunctionTool

abstract class [FunctionTool](index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val isLongRunning: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap(), requiresConfirmation: ([Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>) -> [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = { false }) : [BaseTool](../-base-tool/index.html)

Represents a compile-time generated tool that wraps a function annotated with [com.google.adk.kt.annotations.Tool](../../com.google.adk.kt.annotations/-tool/index.html).

The optional confirmation gate (set via the `requiresConfirmation` constructor parameter) makes an invocation pause for human approval before the underlying function runs:

  * On the first call the tool records a confirmation request via [ToolContext.requestConfirmation](../-tool-context/request-confirmation.html) and returns a placeholder error response without invoking the underlying function.

  * Once the user supplies a [com.google.adk.kt.events.ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html), the tool is re-executed: if the user confirmed it runs normally; otherwise it returns a rejection error response.




The gate has two forms:

  * Per-call predicate (the primary constructor): a `(args) -> Boolean` is invoked on every call with the function's `args` and decides whether to gate this invocation, e.g. `requiresConfirmation = { args -> (args["amount"] as Int) > 1000 }`. The default value `{ false }` disables the gate entirely.

  * Boolean (the secondary constructor): a constant flag that gates either every invocation (`true`) or none (`false`). It is a thin wrapper that lifts the Boolean into a constant predicate `{ value }`.




Members

## Constructors

[FunctionTool](-function-tool.html)

Link copied to clipboard

constructor(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), isLongRunning: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap(), requiresConfirmation: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html))

Boolean convenience constructor: pass `true` to gate every invocation, `false` to skip the gate entirely. Equivalent to passing `{ requiresConfirmation }` to the primary constructor.

constructor(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), isLongRunning: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap(), requiresConfirmation: ([Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>) -> [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = { false })

## Types

[Companion](-companion/index.html)

Link copied to clipboard

object [Companion](-companion/index.html)

## Properties

[customMetadata](../-base-tool/custom-metadata.html)

Link copied to clipboard

val [customMetadata](../-base-tool/custom-metadata.html): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>

The custom metadata of the tool.

[description](../-base-tool/description.html)

Link copied to clipboard

val [description](../-base-tool/description.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The description of the tool.

[isLongRunning](../-base-tool/is-long-running.html)

Link copied to clipboard

val [isLongRunning](../-base-tool/is-long-running.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

Whether the tool's final result will be delivered out-of-band. When `true`, the framework marks the call as long-running and uses the tool's return value as the function-response payload (or suppresses the response entirely if the tool returns `Unit`).

[name](../-base-tool/name.html)

Link copied to clipboard

val [name](../-base-tool/name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The name of the tool.

## Functions

[close](../-base-tool/close.html)

Link copied to clipboard

open override fun [close](../-base-tool/close.html)()

[declaration](../-base-tool/declaration.html)

Link copied to clipboard

abstract fun [declaration](../-base-tool/declaration.html)(): [FunctionDeclaration](../../com.google.adk.kt.types/-function-declaration/index.html)?

Returns the underlying function declaration.

[execute](execute.html)

Link copied to clipboard

abstract suspend fun [execute](execute.html)(context: [ToolContext](../-tool-context/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)

Executes the function with the provided [args](execute.html), optionally utilizing the [context](execute.html).

[processLlmRequest](../-base-tool/process-llm-request.html)

Link copied to clipboard

open suspend fun [processLlmRequest](../-base-tool/process-llm-request.html)(toolContext: [ToolContext](../-tool-context/index.html), llmRequest: [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)): [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)

Processes the LLM request before it is sent.

[run](run.html)

Link copied to clipboard

suspend override fun [run](run.html)(context: [ToolContext](../-tool-context/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)

Executes the tool. This overrides the generic base method to apply the optional confirmation gate before delegating to [execute](execute.html).

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
