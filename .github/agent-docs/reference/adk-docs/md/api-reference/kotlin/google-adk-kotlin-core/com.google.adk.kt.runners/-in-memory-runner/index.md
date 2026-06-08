toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.runners](../index.html)/InMemoryRunner

# InMemoryRunner

open class [InMemoryRunner](index.html)(val agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), val appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "InMemoryRunner", val sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), val artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), val memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService(), val pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html) = PluginManager(), val resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html) = ResumabilityConfig()) : [AbstractRunner](../-abstract-runner/index.html)

An in-memory implementation of a [Runner](../-runner/index.html) that manages the lifecycle of a [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html) execution.

It provides default in-memory implementations for session, artifact, and memory services.

#### Inheritors

[ReplRunner](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-repl-runner/index.html)

Members

## Constructors

[InMemoryRunner](-in-memory-runner.html)

Link copied to clipboard

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "InMemoryRunner", sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService(), pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html) = PluginManager(), resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html) = ResumabilityConfig())

## Properties

[agent](../-abstract-runner/agent.html)

Link copied to clipboard

open override val [agent](../-abstract-runner/agent.html): [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html)

[appName](../-abstract-runner/app-name.html)

Link copied to clipboard

open override val [appName](../-abstract-runner/app-name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

[artifactService](../-abstract-runner/artifact-service.html)

Link copied to clipboard

open override val [artifactService](../-abstract-runner/artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?

[memoryService](../-abstract-runner/memory-service.html)

Link copied to clipboard

open override val [memoryService](../-abstract-runner/memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?

[pluginManager](../-abstract-runner/plugin-manager.html)

Link copied to clipboard

open override val [pluginManager](../-abstract-runner/plugin-manager.html): [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html)

[resumabilityConfig](../-abstract-runner/resumability-config.html)

Link copied to clipboard

open override val [resumabilityConfig](../-abstract-runner/resumability-config.html): [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html)

[sessionService](../-abstract-runner/session-service.html)

Link copied to clipboard

open override val [sessionService](../-abstract-runner/session-service.html): [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)

## Functions

[applyStateDelta](../-abstract-runner/apply-state-delta.html)

Link copied to clipboard

fun [applyStateDelta](../-abstract-runner/apply-state-delta.html)(event: [Event](../../com.google.adk.kt.events/-event/index.html), stateDelta: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?)

Applies the provided [stateDelta](../-abstract-runner/apply-state-delta.html) to the given [event](../-abstract-runner/apply-state-delta.html).

[run](../-abstract-runner/run.html)

Link copied to clipboard

open override fun [run](../-abstract-runner/run.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), newMessage: [Content](../../com.google.adk.kt.types/-content/index.html), runConfig: [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?): [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-iterator/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Sync interface for local testing and convenience purpose.

[runAsync](../-abstract-runner/run-async.html)

Link copied to clipboard

open override fun [runAsync](../-abstract-runner/run-async.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)?, newMessage: [Content](../../com.google.adk.kt.types/-content/index.html)?, stateDelta: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?, runConfig: [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?): Flow<[Event](../../com.google.adk.kt.events/-event/index.html)>

Main entry method to run the agent in this runner.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
