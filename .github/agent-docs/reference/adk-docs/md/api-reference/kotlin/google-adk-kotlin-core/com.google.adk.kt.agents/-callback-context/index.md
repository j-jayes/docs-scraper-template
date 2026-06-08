toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

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

[getEvents](../-readonly-context/get-events.html)

Link copied to clipboard

open suspend override fun [getEvents](../-readonly-context/get-events.html)(currentInvocation: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html), currentBranch: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Returns the events from the current session.

[mergeEventActions](merge-event-actions.html)

Link copied to clipboard

fun [mergeEventActions](merge-event-actions.html)(actions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html))

Merges the given event actions into the current event actions.

[updateState](update-state.html)

Link copied to clipboard

fun [updateState](update-state.html)(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), value: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html))

Updates the state delta in the event actions.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
