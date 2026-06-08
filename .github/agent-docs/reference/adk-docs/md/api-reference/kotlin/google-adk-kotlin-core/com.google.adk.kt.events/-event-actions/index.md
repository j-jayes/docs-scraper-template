toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.events](../index.html)/EventActions

# EventActions

data class [EventActions](index.html)(var skipSummarization: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val stateDelta: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)> = concurrentMutableMapOf(), val artifactDelta: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)> = concurrentMutableMapOf(), var transferToAgent: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, var escalate: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, var endOfAgent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val requestedToolConfirmations: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [ToolConfirmation](../-tool-confirmation/index.html)> = concurrentMutableMapOf(), var rewindBeforeInvocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, var agentState: [TypedData](../../com.google.adk.kt.agents/-typed-data/index.html)? = null)

Represents the actions attached to an event.

Members

## Constructors

[EventActions](-event-actions.html)

Link copied to clipboard

constructor(skipSummarization: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, stateDelta: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)> = concurrentMutableMapOf(), artifactDelta: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)> = concurrentMutableMapOf(), transferToAgent: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, escalate: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, endOfAgent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, requestedToolConfirmations: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [ToolConfirmation](../-tool-confirmation/index.html)> = concurrentMutableMapOf(), rewindBeforeInvocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, agentState: [TypedData](../../com.google.adk.kt.agents/-typed-data/index.html)? = null)

## Properties

[agentState](agent-state.html)

Link copied to clipboard

var [agentState](agent-state.html): [TypedData](../../com.google.adk.kt.agents/-typed-data/index.html)?

The state of the agent for resumability.

[artifactDelta](artifact-delta.html)

Link copied to clipboard

val [artifactDelta](artifact-delta.html): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)>

Indicates that the event is updating an artifact. The key is the filename, and the value is the version.

[endOfAgent](end-of-agent.html)

Link copied to clipboard

var [endOfAgent](end-of-agent.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)

If true, the current agent has finished its current run. Note that there can be multiple events with [endOfAgent](end-of-agent.html) set to `true` for the same agent within one invocation when there is a loop. This should only be set by the ADK workflow.

[escalate](escalate.html)

Link copied to clipboard

var [escalate](escalate.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)

The agent is escalating to a higher level agent.

[requestedToolConfirmations](requested-tool-confirmations.html)

Link copied to clipboard

val [requestedToolConfirmations](requested-tool-confirmations.html): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [ToolConfirmation](../-tool-confirmation/index.html)>

A map of tool confirmations requested by this event, keyed by function call ID.

[rewindBeforeInvocationId](rewind-before-invocation-id.html)

Link copied to clipboard

var [rewindBeforeInvocationId](rewind-before-invocation-id.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)?

If set, the agent will rewind history before the specified invocation ID.

[skipSummarization](skip-summarization.html)

Link copied to clipboard

var [skipSummarization](skip-summarization.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)

If true, it won't call the model to summarize the function response. Only used for a function response event.

[stateDelta](state-delta.html)

Link copied to clipboard

val [stateDelta](state-delta.html): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>

Indicates that the event is updating the state with the given delta.

[transferToAgent](transfer-to-agent.html)

Link copied to clipboard

var [transferToAgent](transfer-to-agent.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)?

If set, the event transfers to the specified agent.

## Functions

[mergeWith](merge-with.html)

Link copied to clipboard

fun [mergeWith](merge-with.html)(other: [EventActions](index.html)): [EventActions](index.html)

Merges this [EventActions](index.html) with another one.

[removeStateByKey](remove-state-by-key.html)

Link copied to clipboard

fun [removeStateByKey](remove-state-by-key.html)(key: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html))

Removes a key from the state delta.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
