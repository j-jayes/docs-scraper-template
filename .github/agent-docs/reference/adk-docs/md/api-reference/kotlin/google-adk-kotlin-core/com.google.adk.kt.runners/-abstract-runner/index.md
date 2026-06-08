toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.runners](../index.html)/AbstractRunner

# AbstractRunner

abstract class [AbstractRunner](index.html)(val appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), val sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html), val artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?, val memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?, val pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html), val resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html) = ResumabilityConfig()) : [Runner](../-runner/index.html)

An abstract base class for [Runner](../-runner/index.html) implementations that provides common orchestration logic.

#### Inheritors

[InMemoryRunner](../-in-memory-runner/index.html)

Members

## Constructors

[AbstractRunner](-abstract-runner.html)

Link copied to clipboard

constructor(appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?, memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?, pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html), resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html) = ResumabilityConfig())

## Properties

[agent](agent.html)

Link copied to clipboard

open override val [agent](agent.html): [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html)

[appName](app-name.html)

Link copied to clipboard

open override val [appName](app-name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

[artifactService](artifact-service.html)

Link copied to clipboard

open override val [artifactService](artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?

[memoryService](memory-service.html)

Link copied to clipboard

open override val [memoryService](memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?

[pluginManager](plugin-manager.html)

Link copied to clipboard

open override val [pluginManager](plugin-manager.html): [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html)

[resumabilityConfig](resumability-config.html)

Link copied to clipboard

open override val [resumabilityConfig](resumability-config.html): [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html)

[sessionService](session-service.html)

Link copied to clipboard

open override val [sessionService](session-service.html): [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)

## Functions

[applyStateDelta](apply-state-delta.html)

Link copied to clipboard

fun [applyStateDelta](apply-state-delta.html)(event: [Event](../../com.google.adk.kt.events/-event/index.html), stateDelta: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?)

Applies the provided [stateDelta](apply-state-delta.html) to the given [event](apply-state-delta.html).

[run](run.html)

Link copied to clipboard

open override fun [run](run.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), newMessage: [Content](../../com.google.adk.kt.types/-content/index.html), runConfig: [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?): [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-iterator/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Sync interface for local testing and convenience purpose.

[runAsync](run-async.html)

Link copied to clipboard

open override fun [runAsync](run-async.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)?, newMessage: [Content](../../com.google.adk.kt.types/-content/index.html)?, stateDelta: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?, runConfig: [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?): Flow<[Event](../../com.google.adk.kt.events/-event/index.html)>

Main entry method to run the agent in this runner.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
