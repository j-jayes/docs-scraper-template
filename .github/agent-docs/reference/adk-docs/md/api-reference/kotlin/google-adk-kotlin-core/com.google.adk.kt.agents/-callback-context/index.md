toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/CallbackContext

# CallbackContext

class [CallbackContext](index.html)(invocationContext: [InvocationContext](../-invocation-context/index.html), eventActions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)? = null) : [ReadonlyContext](../-readonly-context/index.html)

The context provided to agents and tools during a callback, such as when a tool is run.

It provides access to the current invocation context, event actions, and state.

Members

## Constructors

[CallbackContext](-callback-context.html)

Link copied to clipboard

constructor(invocationContext: [InvocationContext](../-invocation-context/index.html), eventActions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)? = null)

## Properties

[agent](agent.html)

Link copied to clipboard

val [agent](agent.html): [BaseAgent](../-base-agent/index.html)

[agentName](../-readonly-context/agent-name.html)

Link copied to clipboard

open override val [agentName](../-readonly-context/agent-name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The name of the agent that is being invoked.

[artifactService](../-readonly-context/artifact-service.html)

Link copied to clipboard

open override val [artifactService](../-readonly-context/artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?

The ArtifactService instance.

[branch](../-readonly-context/branch.html)

Link copied to clipboard

open override val [branch](../-readonly-context/branch.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)?

The branch of the invocation context.

[eventActions](event-actions.html)

Link copied to clipboard

var [eventActions](event-actions.html): [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)

[invocationId](../-readonly-context/invocation-id.html)

Link copied to clipboard

open override val [invocationId](../-readonly-context/invocation-id.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The unique ID of this invocation.

[memoryService](../-readonly-context/memory-service.html)

Link copied to clipboard

open override val [memoryService](../-readonly-context/memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?

The MemoryService instance.

[runConfig](../-readonly-context/run-config.html)

Link copied to clipboard

open override val [runConfig](../-readonly-context/run-config.html): [RunConfig](../-run-config/index.html)?

The run configuration for this invocation.

[session](../-readonly-context/session.html)

Link copied to clipboard

open override val [session](../-readonly-context/session.html): [Session](../../com.google.adk.kt.sessions/-session/index.html)

The session that this invocation is a part of.

[state](state.html)

Link copied to clipboard

open override val [state](state.html): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>

The state of the session.

[userContent](../-readonly-context/user-content.html)

Link copied to clipboard

open override val [userContent](../-readonly-context/user-content.html): [Content](../../com.google.adk.kt.types/-content/index.html)?

The user content that this invocation is processing.

[userId](../-readonly-context/user-id.html)

Link copied to clipboard

open override val [userId](../-readonly-context/user-id.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The user ID of the user that initiated the session.

## Functions

[addSessionToMemory](add-session-to-memory.html)

Link copied to clipboard

suspend fun [addSessionToMemory](add-session-to-memory.html)()

Triggers memory generation for the current session.

[endInvocation](end-invocation.html)

Link copied to clipboard

fun [endInvocation](end-invocation.html)()

Requests the current LLM agent to stop after the current step completes.

[getEvents](../-readonly-context/get-events.html)

Link copied to clipboard

open suspend override fun [getEvents](../-readonly-context/get-events.html)(currentInvocation: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html), currentBranch: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Returns the events from the current session.

[listArtifacts](list-artifacts.html)

Link copied to clipboard

suspend fun [listArtifacts](list-artifacts.html)(): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>

Lists the artifact names visible to this invocation. Returns an empty list if no artifact service is configured.

[loadArtifact](load-artifact.html)

Link copied to clipboard

suspend fun [loadArtifact](load-artifact.html)(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null): [Part](../../com.google.adk.kt.types/-part/index.html)?

Loads an artifact by [name](load-artifact.html) from the invocation's [com.google.adk.kt.artifacts.ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html). Returns `null` if no artifact service is configured or the artifact is not found.

[mergeEventActions](merge-event-actions.html)

Link copied to clipboard

fun [mergeEventActions](merge-event-actions.html)(actions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html))

Merges the given event actions into the current event actions.

[saveArtifact](save-artifact.html)

Link copied to clipboard

suspend fun [saveArtifact](save-artifact.html)(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), artifact: [Part](../../com.google.adk.kt.types/-part/index.html)): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)

Saves [artifact](save-artifact.html) under [name](save-artifact.html) on the invocation's [com.google.adk.kt.artifacts.ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html), records the new version into [eventActions](event-actions.html)' `artifactDelta`, and returns the version.

[updateState](update-state.html)

Link copied to clipboard

fun [updateState](update-state.html)(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), value: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html))

Updates the state delta in the event actions.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
