toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

commonJvmAndroid

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.runners](../index.html)/ReplRunner

# ReplRunner

commonJvmAndroid

open class [ReplRunner](index.html)(val agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html)) : [InMemoryRunner](../-in-memory-runner/index.html)

A runner for Kotlin agents that provides a simple REPL for debugging.

Members

## Constructors

[ReplRunner](-repl-runner.html)

Link copied to clipboard

commonJvmAndroid

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html))

## Types

[Companion](-companion/index.html)

Link copied to clipboard

commonJvmAndroid

object [Companion](-companion/index.html)

## Properties

[agent](../-abstract-runner/agent.html)

Link copied to clipboard

commonJvmAndroid

open override val [agent](../-abstract-runner/agent.html): [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html)

[appName](../-abstract-runner/app-name.html)

Link copied to clipboard

commonJvmAndroid

open override val [appName](../-abstract-runner/app-name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

[artifactService](../-abstract-runner/artifact-service.html)

Link copied to clipboard

commonJvmAndroid

open override val [artifactService](../-abstract-runner/artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?

[memoryService](../-abstract-runner/memory-service.html)

Link copied to clipboard

commonJvmAndroid

open override val [memoryService](../-abstract-runner/memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?

[pluginManager](../-abstract-runner/plugin-manager.html)

Link copied to clipboard

commonJvmAndroid

open override val [pluginManager](../-abstract-runner/plugin-manager.html): [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html)

[resumabilityConfig](../-abstract-runner/resumability-config.html)

Link copied to clipboard

commonJvmAndroid

open override val [resumabilityConfig](../-abstract-runner/resumability-config.html): [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html)

[sessionService](../-abstract-runner/session-service.html)

Link copied to clipboard

commonJvmAndroid

open override val [sessionService](../-abstract-runner/session-service.html): [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)

## Functions

[applyStateDelta](../-abstract-runner/apply-state-delta.html)

Link copied to clipboard

commonJvmAndroid

fun [applyStateDelta](../-abstract-runner/apply-state-delta.html)(event: [Event](../../com.google.adk.kt.events/-event/index.html), stateDelta: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?)

Applies the provided [stateDelta](../-abstract-runner/apply-state-delta.html) to the given [event](../-abstract-runner/apply-state-delta.html).

[run](../-abstract-runner/run.html)

Link copied to clipboard

commonJvmAndroid

open override fun [run](../-abstract-runner/run.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), newMessage: [Content](../../com.google.adk.kt.types/-content/index.html), runConfig: [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?): [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-iterator/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Sync interface for local testing and convenience purpose.

[runAsync](../-abstract-runner/run-async.html)

Link copied to clipboard

commonJvmAndroid

open override fun [runAsync](../-abstract-runner/run-async.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)?, newMessage: [Content](../../com.google.adk.kt.types/-content/index.html)?, stateDelta: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?, runConfig: [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?): Flow<[Event](../../com.google.adk.kt.events/-event/index.html)>

Main entry method to run the agent in this runner.

[start](start.html)

Link copied to clipboard

commonJvmAndroid

fun [start](start.html)()

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
