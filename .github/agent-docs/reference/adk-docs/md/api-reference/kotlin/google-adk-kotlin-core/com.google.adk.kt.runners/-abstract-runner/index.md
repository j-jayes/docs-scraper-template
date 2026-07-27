toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.runners](../index.html)/AbstractRunner

# AbstractRunner

abstract class [AbstractRunner](index.html) : [Runner](../-runner/index.html)

An abstract base class for [Runner](../-runner/index.html) implementations that provides common orchestration logic.

#### Inheritors

[InMemoryRunner](../-in-memory-runner/index.html)

Members

## Constructors

[AbstractRunner](-abstract-runner.html)

Link copied to clipboard

constructor(appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?, memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?, pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html), resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html) = ResumabilityConfig())

Creates a runner from explicit fields, not using an [App](../../com.google.adk.kt.apps/-app/index.html).

constructor(app: [App](../../com.google.adk.kt.apps/-app/index.html), sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?, memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?, skipClosingPlugins: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Creates a runner from an [App](../../com.google.adk.kt.apps/-app/index.html), deriving its [App.appName](../../com.google.adk.kt.apps/-app/app-name.html), [App.rootAgent](../../com.google.adk.kt.apps/-app/root-agent.html), [App.plugins](../../com.google.adk.kt.apps/-app/plugins.html), and [App.resumabilityConfig](../../com.google.adk.kt.apps/-app/resumability-config.html).

## Properties

[agent](agent.html)

Link copied to clipboard

override val [agent](agent.html): [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html)

[app](app.html)

Link copied to clipboard

val [app](app.html): [App](../../com.google.adk.kt.apps/-app/index.html)?

[appName](app-name.html)

Link copied to clipboard

override val [appName](app-name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

[artifactService](artifact-service.html)

Link copied to clipboard

override val [artifactService](artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?

[memoryService](memory-service.html)

Link copied to clipboard

override val [memoryService](memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?

[pluginManager](plugin-manager.html)

Link copied to clipboard

override val [pluginManager](plugin-manager.html): [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html)

[resumabilityConfig](resumability-config.html)

Link copied to clipboard

override val [resumabilityConfig](resumability-config.html): [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html)

[sessionService](session-service.html)

Link copied to clipboard

override val [sessionService](session-service.html): [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)

## Functions

[applyStateDelta](apply-state-delta.html)

Link copied to clipboard

fun [applyStateDelta](apply-state-delta.html)(event: [Event](../../com.google.adk.kt.events/-event/index.html), stateDelta: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?)

Applies the provided [stateDelta](apply-state-delta.html) to the given [event](apply-state-delta.html).

[rewindAsync](rewind-async.html)

Link copied to clipboard

open suspend override fun [rewindAsync](rewind-async.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), rewindBeforeInvocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html))

Rewinds the session to before the specified invocation.

[run](run.html)

Link copied to clipboard

open override fun [run](run.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), newMessage: [Content](../../com.google.adk.kt.types/-content/index.html), runConfig: [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?): [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-iterator/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Sync interface for local testing and convenience purpose.

[runAsync](run-async.html)

Link copied to clipboard

open override fun [runAsync](run-async.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)?, newMessage: [Content](../../com.google.adk.kt.types/-content/index.html)?, stateDelta: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?, runConfig: [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?): Flow<[Event](../../com.google.adk.kt.events/-event/index.html)>

Main entry method to run the agent in this runner.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
