toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.plugins](../index.html)/PluginManager

# PluginManager

class [PluginManager](index.html)(val plugins: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Plugin](../-plugin/index.html)> = emptyList(), val skipClosingPlugins: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Manages the pre-aggregation of typed functional callbacks.

Members

## Constructors

[PluginManager](-plugin-manager.html)

Link copied to clipboard

constructor(plugins: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Plugin](../-plugin/index.html)> = emptyList(), skipClosingPlugins: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

## Types

[Companion](-companion/index.html)

Link copied to clipboard

object [Companion](-companion/index.html)

## Properties

[afterAgentCallbacks](after-agent-callbacks.html)

Link copied to clipboard

val [afterAgentCallbacks](after-agent-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../../com.google.adk.kt.callbacks/-after-agent-callback/index.html)>

[afterModelCallbacks](after-model-callbacks.html)

Link copied to clipboard

val [afterModelCallbacks](after-model-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterModelCallback](../../com.google.adk.kt.callbacks/-after-model-callback/index.html)>

[afterRunCallbacks](after-run-callbacks.html)

Link copied to clipboard

val [afterRunCallbacks](after-run-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterRunCallback](../../com.google.adk.kt.callbacks/-after-run-callback/index.html)>

[afterToolCallbacks](after-tool-callbacks.html)

Link copied to clipboard

val [afterToolCallbacks](after-tool-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterToolCallback](../../com.google.adk.kt.callbacks/-after-tool-callback/index.html)>

[beforeAgentCallbacks](before-agent-callbacks.html)

Link copied to clipboard

val [beforeAgentCallbacks](before-agent-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../../com.google.adk.kt.callbacks/-before-agent-callback/index.html)>

[beforeModelCallbacks](before-model-callbacks.html)

Link copied to clipboard

val [beforeModelCallbacks](before-model-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeModelCallback](../../com.google.adk.kt.callbacks/-before-model-callback/index.html)>

[beforeRunCallbacks](before-run-callbacks.html)

Link copied to clipboard

val [beforeRunCallbacks](before-run-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeRunCallback](../../com.google.adk.kt.callbacks/-before-run-callback/index.html)>

[beforeToolCallbacks](before-tool-callbacks.html)

Link copied to clipboard

val [beforeToolCallbacks](before-tool-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeToolCallback](../../com.google.adk.kt.callbacks/-before-tool-callback/index.html)>

[onEventCallbacks](on-event-callbacks.html)

Link copied to clipboard

val [onEventCallbacks](on-event-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnEventCallback](../../com.google.adk.kt.callbacks/-on-event-callback/index.html)>

[onModelErrorCallbacks](on-model-error-callbacks.html)

Link copied to clipboard

val [onModelErrorCallbacks](on-model-error-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnModelErrorCallback](../../com.google.adk.kt.callbacks/-on-model-error-callback/index.html)>

[onToolErrorCallbacks](on-tool-error-callbacks.html)

Link copied to clipboard

val [onToolErrorCallbacks](on-tool-error-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnToolErrorCallback](../../com.google.adk.kt.callbacks/-on-tool-error-callback/index.html)>

[onUserMessageCallbacks](on-user-message-callbacks.html)

Link copied to clipboard

val [onUserMessageCallbacks](on-user-message-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnUserMessageCallback](../../com.google.adk.kt.callbacks/-on-user-message-callback/index.html)>

[plugins](plugins.html)

Link copied to clipboard

val [plugins](plugins.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Plugin](../-plugin/index.html)>

The list of registered plugins managed by this instance.

[skipClosingPlugins](skip-closing-plugins.html)

Link copied to clipboard

val [skipClosingPlugins](skip-closing-plugins.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

When `true`, [close](close.html) becomes a no-op so that plugins owned by another (parent) manager are not torn down by this sub-manager. Intended for cases where a sub-runner shares the parent runner's [Plugin](../-plugin/index.html) instances (e.g. [com.google.adk.kt.tools.AgentTool](../../com.google.adk.kt.tools/-agent-tool/index.html) propagating parent plugins to the wrapped agent's runner): the sub-runner must not close plugins it does not own.

## Functions

[close](close.html)

Link copied to clipboard

suspend fun [close](close.html)()

[getPlugin](get-plugin.html)

Link copied to clipboard

fun [getPlugin](get-plugin.html)(pluginName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)): [Plugin](../-plugin/index.html)?

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
