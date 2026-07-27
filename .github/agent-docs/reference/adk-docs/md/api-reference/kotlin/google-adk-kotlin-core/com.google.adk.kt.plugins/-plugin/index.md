toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.plugins](../index.html)/Plugin

# Plugin

interface [Plugin](index.html)

Interface for creating plugins.

Plugins provide a structured way to intercept and modify agent, tool, and LLM behaviors at critical execution points in a callback manner.

#### Inheritors

[LoggingPlugin](../-logging-plugin/index.html)

Members

## Properties

[name](name.html)

Link copied to clipboard

abstract val [name](name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The unique name of the plugin.

## Functions

[afterAgent](after-agent.html)

Link copied to clipboard

open suspend fun [afterAgent](after-agent.html)(context: [CallbackContext](../../com.google.adk.kt.agents/-callback-context/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-unit/index.html), [Content](../../com.google.adk.kt.types/-content/index.html)>

Callback executed after a specific agent finishes its processing.

[afterModel](after-model.html)

Link copied to clipboard

open suspend fun [afterModel](after-model.html)(context: [CallbackContext](../../com.google.adk.kt.agents/-callback-context/index.html), response: [LlmResponse](../../com.google.adk.kt.models/-llm-response/index.html)): [LlmResponse](../../com.google.adk.kt.models/-llm-response/index.html)

Callback executed after an LLM response is received.

[afterRun](after-run.html)

Link copied to clipboard

open suspend fun [afterRun](after-run.html)(invocationContext: [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html))

Callback executed after the ADK runner completes its execution.

[afterTool](after-tool.html)

Link copied to clipboard

open suspend fun [afterTool](after-tool.html)(context: [ToolContext](../../com.google.adk.kt.tools/-tool-context/index.html), tool: [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>, result: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>

Callback executed after a tool finishes its execution.

[beforeAgent](before-agent.html)

Link copied to clipboard

open suspend fun [beforeAgent](before-agent.html)(context: [CallbackContext](../../com.google.adk.kt.agents/-callback-context/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[EventActions](../../com.google.adk.kt.events/-event-actions/index.html), [Content](../../com.google.adk.kt.types/-content/index.html)>

Callback executed before a specific agent starts processing.

[beforeModel](before-model.html)

Link copied to clipboard

open suspend fun [beforeModel](before-model.html)(context: [CallbackContext](../../com.google.adk.kt.agents/-callback-context/index.html), request: [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html), [LlmResponse](../../com.google.adk.kt.models/-llm-response/index.html)>

Callback executed before an LLM request is sent.

[beforeRun](before-run.html)

Link copied to clipboard

open suspend fun [beforeRun](before-run.html)(invocationContext: [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-unit/index.html), [Content](../../com.google.adk.kt.types/-content/index.html)>

Callback executed before the ADK runner starts the main execution loop.

[beforeTool](before-tool.html)

Link copied to clipboard

open suspend fun [beforeTool](before-tool.html)(context: [ToolContext](../../com.google.adk.kt.tools/-tool-context/index.html), tool: [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>, [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>>

Callback executed before a tool is invoked.

[close](close.html)

Link copied to clipboard

open suspend fun [close](close.html)()

Method executed when the runner is closed.

[onEvent](on-event.html)

Link copied to clipboard

open suspend fun [onEvent](on-event.html)(invocationContext: [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html), event: [Event](../../com.google.adk.kt.events/-event/index.html)): [Event](../../com.google.adk.kt.events/-event/index.html)

Callback executed when an event is yielded by an agent during execution.

[onModelError](on-model-error.html)

Link copied to clipboard

open suspend fun [onModelError](on-model-error.html)(context: [CallbackContext](../../com.google.adk.kt.agents/-callback-context/index.html), request: [LlmRequest](../../com.google.adk.kt.models/-llm-request/index.html), error: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-unit/index.html), [LlmResponse](../../com.google.adk.kt.models/-llm-response/index.html)>

Callback executed when an error occurs during an LLM interaction.

[onToolError](on-tool-error.html)

Link copied to clipboard

open suspend fun [onToolError](on-tool-error.html)(context: [ToolContext](../../com.google.adk.kt.tools/-tool-context/index.html), tool: [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html), args: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>, error: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)): [CallbackChoice](../../com.google.adk.kt.callbacks/-callback-choice/index.html)<[Unit](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-unit/index.html), [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>>

Callback executed when an error occurs during a tool invocation.

[onUserMessage](on-user-message.html)

Link copied to clipboard

open suspend fun [onUserMessage](on-user-message.html)(invocationContext: [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html), userMessage: [Content](../../com.google.adk.kt.types/-content/index.html)): [Content](../../com.google.adk.kt.types/-content/index.html)

Callback executed when a user message is received before an invocation starts.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
