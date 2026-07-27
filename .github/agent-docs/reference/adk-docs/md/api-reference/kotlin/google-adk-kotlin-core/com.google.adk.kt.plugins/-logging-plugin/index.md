toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.plugins](../index.html)/LoggingPlugin

# LoggingPlugin

class [LoggingPlugin](index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "logging_plugin") : [Plugin](../-plugin/index.html)

A plugin that logs a high volume of requests and responses handled by the agent at each callback point.

This plugin is primarily intended for ADK development and debugging purposes, helping to print all critical events in the console.

**CAUTION** : The plugin logs raw requests / responses, including user prompts. Be mindful of sensitive data disclosure.

Members

## Constructors

[LoggingPlugin](-logging-plugin.html)

Link copied to clipboard

constructor(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "logging_plugin")

## Types

[Companion](-companion/index.html)

Link copied to clipboard

object [Companion](-companion/index.html)

## Properties

[name](name.html)

Link copied to clipboard

open override val [name](name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The unique name of the plugin.

## Functions

[afterAgent](after-agent.html)

Link copied to clipboard

open suspend override fun [afterAgent](after-agent.html)(context: [CallbackContext](../../com.google.adk.kt.agents/-callback-context/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-unit/index.html), [Content](../../com.google.adk.kt.types/-content/index.html)>

Callback executed after a specific agent finishes its processing.

[afterModel](after-model.html)

Link copied to clipboard

open suspend override fun [afterModel](after-model.html)(context: [CallbackContext](../../com.google.adk.kt.agents/-callback-context/index.html), response: [LlmResponse](../../com.google.adk.kt.models/-llm-response/index.html)): [LlmResponse](../../com.google.adk.kt.models/-llm-response/index.html)

Callback executed after an LLM response is received.

[afterRun](after-run.html)

Link copied to clipboard

open suspend override fun [afterRun](after-run.html)(invocationContext: [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html))

Callback executed after the ADK runner completes its execution.

[afterTool](after-tool.html)

Link copied to clipboard

open suspend override fun [afterTool](after-tool.html)(context: [ToolContext](../../com.google.adk.kt.tools/-tool-context/index.html), tool: [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>, result: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>

Callback executed after a tool finishes its execution.

[beforeAgent](before-agent.html)

Link copied to clipboard

open suspend override fun [beforeAgent](before-agent.html)(context: [CallbackContext](../../com.google.adk.kt.agents/-callback-context/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[EventActions](../../com.google.adk.kt.events/-event-actions/index.html), [Content](../../com.google.adk.kt.types/-content/index.html)>

Callback executed before a specific agent starts processing.

[beforeModel](before-model.html)

Link copied to clipboard

open suspend override fun [beforeModel](before-model.html)(context: [CallbackContext](../../com.google.adk.kt.agents/-callback-context/index.html), request: [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html), [LlmResponse](../../com.google.adk.kt.models/-llm-response/index.html)>

Callback executed before an LLM request is sent.

[beforeRun](before-run.html)

Link copied to clipboard

open suspend override fun [beforeRun](before-run.html)(invocationContext: [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-unit/index.html), [Content](../../com.google.adk.kt.types/-content/index.html)>

Callback executed before the ADK runner starts the main execution loop.

[beforeTool](before-tool.html)

Link copied to clipboard

open suspend override fun [beforeTool](before-tool.html)(context: [ToolContext](../../com.google.adk.kt.tools/-tool-context/index.html), tool: [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>, [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>>

Callback executed before a tool is invoked.

[close](../-plugin/close.html)

Link copied to clipboard

open suspend fun [close](../-plugin/close.html)()

Method executed when the runner is closed.

[formatArgs](format-args.html)

Link copied to clipboard

fun [formatArgs](format-args.html)(args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

[formatContent](format-content.html)

Link copied to clipboard

fun [formatContent](format-content.html)(content: [Content](../../com.google.adk.kt.types/-content/index.html)?): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

[onEvent](on-event.html)

Link copied to clipboard

open suspend override fun [onEvent](on-event.html)(invocationContext: [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html), event: [Event](../../com.google.adk.kt.events/-event/index.html)): [Event](../../com.google.adk.kt.events/-event/index.html)

Callback executed when an event is yielded by an agent during execution.

[onModelError](on-model-error.html)

Link copied to clipboard

open suspend override fun [onModelError](on-model-error.html)(context: [CallbackContext](../../com.google.adk.kt.agents/-callback-context/index.html), request: [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html), error: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-unit/index.html), [LlmResponse](../../com.google.adk.kt.models/-llm-response/index.html)>

Callback executed when an error occurs during an LLM interaction.

[onToolError](on-tool-error.html)

Link copied to clipboard

open suspend override fun [onToolError](on-tool-error.html)(context: [ToolContext](../../com.google.adk.kt.tools/-tool-context/index.html), tool: [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>, error: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-unit/index.html), [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>>

Callback executed when an error occurs during a tool invocation.

[onUserMessage](on-user-message.html)

Link copied to clipboard

open suspend override fun [onUserMessage](on-user-message.html)(invocationContext: [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html), userMessage: [Content](../../com.google.adk.kt.types/-content/index.html)): [Content](../../com.google.adk.kt.types/-content/index.html)

Callback executed when a user message is received before an invocation starts.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
