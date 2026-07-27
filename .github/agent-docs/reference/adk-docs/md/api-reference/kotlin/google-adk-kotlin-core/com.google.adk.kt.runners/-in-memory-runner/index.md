toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.runners](../index.html)/InMemoryRunner

# InMemoryRunner

open class [InMemoryRunner](index.html) : [AbstractRunner](../-abstract-runner/index.html)

An in-memory implementation of a [Runner](../-runner/index.html) that manages the lifecycle of a [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html) execution.

It provides default in-memory implementations for session, artifact, and memory services. It can be constructed either directly from a root agent or from an [App](../../com.google.adk.kt.apps/-app/index.html).

#### Inheritors

[ReplRunner](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-repl-runner/index.html)

Members

## Constructors

[InMemoryRunner](-in-memory-runner.html)

Link copied to clipboard

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "InMemoryRunner", sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService())

Creates an [InMemoryRunner](index.html) from a root [agent](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-in-memory-runner/\[60\]init\[62\].html) and default in-memory services.

constructor(app: [App](../../com.google.adk.kt.apps/-app/index.html), sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService(), skipClosingPlugins: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Creates an [InMemoryRunner](index.html) from an [App](../../com.google.adk.kt.apps/-app/index.html), deriving its [App.appName](../../com.google.adk.kt.apps/-app/app-name.html), [App.rootAgent](../../com.google.adk.kt.apps/-app/root-agent.html), [App.plugins](../../com.google.adk.kt.apps/-app/plugins.html), and [App.resumabilityConfig](../../com.google.adk.kt.apps/-app/resumability-config.html).

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "InMemoryRunner", sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService(), pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html))

Creates an [InMemoryRunner](index.html) with an explicit [pluginManager](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-in-memory-runner/\[60\]init\[62\].html).

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "InMemoryRunner", sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService(), resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html))

Creates an [InMemoryRunner](index.html) with an explicit [resumabilityConfig](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-in-memory-runner/\[60\]init\[62\].html).

constructor(agent: [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html), appName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "InMemoryRunner", sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html) = InMemorySessionService(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = InMemoryArtifactService(), memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = InMemoryMemoryService(), pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html), resumabilityConfig: [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html))

Creates an [InMemoryRunner](index.html) with both an explicit [pluginManager](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-in-memory-runner/\[60\]init\[62\].html) and [resumabilityConfig](../../../google-adk-kotlin-core/com.google.adk.kt.runners/-in-memory-runner/\[60\]init\[62\].html).

## Properties

[agent](../-abstract-runner/agent.html)

Link copied to clipboard

override val [agent](../-abstract-runner/agent.html): [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html)

[app](../-abstract-runner/app.html)

Link copied to clipboard

val [app](../-abstract-runner/app.html): [App](../../com.google.adk.kt.apps/-app/index.html)?

[appName](../-abstract-runner/app-name.html)

Link copied to clipboard

override val [appName](../-abstract-runner/app-name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

[artifactService](../-abstract-runner/artifact-service.html)

Link copied to clipboard

override val [artifactService](../-abstract-runner/artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?

[memoryService](../-abstract-runner/memory-service.html)

Link copied to clipboard

override val [memoryService](../-abstract-runner/memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?

[pluginManager](../-abstract-runner/plugin-manager.html)

Link copied to clipboard

override val [pluginManager](../-abstract-runner/plugin-manager.html): [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html)

[resumabilityConfig](../-abstract-runner/resumability-config.html)

Link copied to clipboard

override val [resumabilityConfig](../-abstract-runner/resumability-config.html): [ResumabilityConfig](../../com.google.adk.kt.agents/-resumability-config/index.html)

[sessionService](../-abstract-runner/session-service.html)

Link copied to clipboard

override val [sessionService](../-abstract-runner/session-service.html): [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)

## Functions

[applyStateDelta](../-abstract-runner/apply-state-delta.html)

Link copied to clipboard

fun [applyStateDelta](../-abstract-runner/apply-state-delta.html)(event: [Event](../../com.google.adk.kt.events/-event/index.html), stateDelta: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?)

Applies the provided [stateDelta](../-abstract-runner/apply-state-delta.html) to the given [event](../-abstract-runner/apply-state-delta.html).

[rewindAsync](../-abstract-runner/rewind-async.html)

Link copied to clipboard

open suspend override fun [rewindAsync](../-abstract-runner/rewind-async.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), rewindBeforeInvocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html))

Rewinds the session to before the specified invocation.

[run](../-abstract-runner/run.html)

Link copied to clipboard

open override fun [run](../-abstract-runner/run.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), newMessage: [Content](../../com.google.adk.kt.types/-content/index.html), runConfig: [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?): [Iterator](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-iterator/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Sync interface for local testing and convenience purpose.

[runAsync](../-abstract-runner/run-async.html)

Link copied to clipboard

open override fun [runAsync](../-abstract-runner/run-async.html)(userId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), sessionId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)?, newMessage: [Content](../../com.google.adk.kt.types/-content/index.html)?, stateDelta: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>?, runConfig: [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?): Flow<[Event](../../com.google.adk.kt.events/-event/index.html)>

Main entry method to run the agent in this runner.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
