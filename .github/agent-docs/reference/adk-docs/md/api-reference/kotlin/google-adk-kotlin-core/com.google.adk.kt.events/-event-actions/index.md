[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.events](../index.html)/EventActions

# EventActions

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [EventActions](index.html)(var skipSummarization: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val stateDelta: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = concurrentMutableMapOf(), val artifactDelta: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)> = concurrentMutableMapOf(), var transferToAgent: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, var escalate: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, var endOfAgent: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val requestedToolConfirmations: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [ToolConfirmation](../-tool-confirmation/index.html)> = concurrentMutableMapOf(), var rewindBeforeInvocationId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, var route: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Route](../../com.google.adk.kt.workflow/-route/index.html)>? = null, var agentState: [TypedData](../../com.google.adk.kt.agents/-typed-data/index.html)? = null, var compaction: [EventCompaction](../-event-compaction/index.html)? = null)

Represents the actions attached to an event.

Members

## Constructors

[EventActions](-event-actions.html)

Link copied to clipboard

common

constructor(skipSummarization: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, stateDelta: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = concurrentMutableMapOf(), artifactDelta: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)> = concurrentMutableMapOf(), transferToAgent: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, escalate: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, endOfAgent: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, requestedToolConfirmations: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [ToolConfirmation](../-tool-confirmation/index.html)> = concurrentMutableMapOf(), rewindBeforeInvocationId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, route: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Route](../../com.google.adk.kt.workflow/-route/index.html)>? = null, agentState: [TypedData](../../com.google.adk.kt.agents/-typed-data/index.html)? = null, compaction: [EventCompaction](../-event-compaction/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [EventActions](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[agentState](agent-state.html)

Link copied to clipboard

common

var [agentState](agent-state.html): [TypedData](../../com.google.adk.kt.agents/-typed-data/index.html)?

The state of the agent for resumability.

[artifactDelta](artifact-delta.html)

Link copied to clipboard

common

val [artifactDelta](artifact-delta.html): [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)>

Indicates that the event is updating an artifact. The key is the filename, and the value is the version.

[compaction](compaction.html)

Link copied to clipboard

common

var [compaction](compaction.html): [EventCompaction](../-event-compaction/index.html)?

If set, this event carries a context-compaction summary that replaces the compacted range of events when the next LLM prompt is built. See [EventCompaction](../-event-compaction/index.html).

[endOfAgent](end-of-agent.html)

Link copied to clipboard

common

var [endOfAgent](end-of-agent.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

If true, the current agent has finished its current run. Note that there can be multiple events with [endOfAgent](../../../google-adk-kotlin-core/com.google.adk.kt.events/-event-actions/--root--.html) set to `true` for the same agent within one invocation when there is a loop. The ADK workflow sets this when an agent's run completes naturally. In addition, tools and callbacks may set this on an event they produce to request the current LLM agent's per-step loop to stop after the current step, mirroring Java ADK's `EventActions.setEndInvocation(true)` / `setEndOfAgent(true)`. Note: this only stops the current LLM agent's step loop; it does not terminate an enclosing workflow agent (`SequentialAgent`, `LoopAgent`, `ParallelAgent`). To break out of a `LoopAgent`, set [escalate](../../../google-adk-kotlin-core/com.google.adk.kt.events/-event-actions/--root--.html) instead. `CallbackContext.endInvocation()` / `ToolContext.endInvocation()` are convenience helpers for the same per-agent stop signal via [InvocationContext.isEndOfInvocation](../../com.google.adk.kt.agents/-invocation-context/is-end-of-invocation.html).

[escalate](escalate.html)

Link copied to clipboard

common

var [escalate](escalate.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

The agent is escalating to a higher level agent.

[requestedToolConfirmations](requested-tool-confirmations.html)

Link copied to clipboard

common

val [requestedToolConfirmations](requested-tool-confirmations.html): [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [ToolConfirmation](../-tool-confirmation/index.html)>

A map of tool confirmations requested by this event, keyed by function call ID.

[rewindBeforeInvocationId](rewind-before-invocation-id.html)

Link copied to clipboard

common

var [rewindBeforeInvocationId](rewind-before-invocation-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

If set, the agent will rewind history before the specified invocation ID.

[route](route.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [RouteListSerializer::class](../../../google-adk-kotlin-core/com.google.adk.kt.workflow/-route-list-serializer/index.html))

var [route](route.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Route](../../com.google.adk.kt.workflow/-route/index.html)>?

For a workflow node, the routes this event selects; an edge is followed when it carries one.

[skipSummarization](skip-summarization.html)

Link copied to clipboard

common

var [skipSummarization](skip-summarization.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

If true, it won't call the model to summarize the function response. Only used for a function response event.

[stateDelta](state-delta.html)

Link copied to clipboard

common

val [stateDelta](state-delta.html): [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

Indicates that the event is updating the state with the given delta.

[transferToAgent](transfer-to-agent.html)

Link copied to clipboard

common

var [transferToAgent](transfer-to-agent.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

If set, the event transfers to the specified agent.

## Functions

[mergeWith](merge-with.html)

Link copied to clipboard

common

fun [mergeWith](merge-with.html)(other: [EventActions](index.html)): [EventActions](index.html)

Merges this [EventActions](index.html) with another one.

[removeStateByKey](remove-state-by-key.html)

Link copied to clipboard

common

fun [removeStateByKey](remove-state-by-key.html)(key: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html))

Removes a key from the state delta.

[removeTempKeys](remove-temp-keys.html)

Link copied to clipboard

common

fun [removeTempKeys](remove-temp-keys.html)()

Deletes the `temp:`-prefixed entries from [stateDelta](../../../google-adk-kotlin-core/com.google.adk.kt.events/-event-actions/--root--.html) in place, so they are never persisted.

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [EventActions.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added. The mutable maps are copied, not shared.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
