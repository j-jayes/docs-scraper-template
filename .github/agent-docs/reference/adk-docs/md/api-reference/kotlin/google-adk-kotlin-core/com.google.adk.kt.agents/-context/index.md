[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/Context

# Context

common

open class [Context](index.html)(val invocationContext: [InvocationContext](../-invocation-context/index.html), actions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)? = null, val functionCallId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val toolConfirmation: [ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html)? = null, val eventId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null) : [ReadonlyContext](../-readonly-context/index.html), [ReadonlyToolContext](../../com.google.adk.kt.tools/-readonly-tool-context/index.html)

Execution context passed to agent callbacks, model callbacks, tools, and workflow nodes during an invocation.

Provides read access to invocation metadata and session state, along with methods to record state deltas, artifacts, and control-flow signals. Tool-specific operations such as [requestConfirmation](request-confirmation.html) require a [functionCallId](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html), which is only populated during a tool call. The node-only members (such as [output](output.html) and [routes](routes.html)) throw [IllegalStateException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-state-exception/index.html) unless this context was created for a workflow node; a callback, model-callback, or tool context is not a node activation and so has none of them.

A context is created in one of two ways: the public constructor is used for callbacks and tools, while the internal constructor is used for workflow node activations. Only the internal constructor populates node execution state (such as [node](node.html) and [parent](parent.html)); contexts created with the public constructor leave that state empty, causing node-only members to throw.

[CallbackContext](../-callback-context/index.html) and [com.google.adk.kt.tools.ToolContext](../../com.google.adk.kt.tools/-tool-context/index.html) are thin subclasses kept for backward compatibility. Prefer [Context](index.html) in new code.

This class is `open` only so those two subclasses can exist as distinct JVM types that Java callers can reference. Every member is `final` so subclasses only forward constructor arguments without changing behavior.

#### Inheritors

[ToolContext](../../com.google.adk.kt.tools/-tool-context/index.html)

[CallbackContext](../-callback-context/index.html)

Members

## Constructors

[Context](-context.html)

Link copied to clipboard

common

constructor(invocationContext: [InvocationContext](../-invocation-context/index.html), actions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)? = null, functionCallId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, toolConfirmation: [ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html)? = null, eventId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

## Types

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[actions](actions.html)

Link copied to clipboard

common

var [actions](actions.html): [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)

The event actions for the current context, holding state deltas and control-flow signals to be attached to emitted events.

[agent](agent.html)

Link copied to clipboard

common

val [agent](agent.html): [BaseAgent](../-base-agent/index.html)

[agentName](agent-name.html)

Link copied to clipboard

common

override val [agentName](agent-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The name of the agent that is being invoked.

[artifactService](artifact-service.html)

Link copied to clipboard

common

override val [artifactService](artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?

The ArtifactService instance.

[attemptCount](attempt-count.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [attemptCount](attempt-count.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

1-based attempt number, which a retry increments. 1 off-graph.

[branch](branch.html)

Link copied to clipboard

common

override val [branch](branch.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The branch of the invocation context.

[callbackContextData](callback-context-data.html)

Link copied to clipboard

common

val [callbackContextData](callback-context-data.html): [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

Per-invocation scratch data; see [ContextFrameworkData.callbackContextData](../-context-framework-data/callback-context-data.html).

[context](context.html)

Link copied to clipboard

common

override val [context](context.html): [ReadonlyContext](../-readonly-context/index.html)

The readonly invocation context.

[eventActions](event-actions.html)

Link copied to clipboard

common

val [eventActions](event-actions.html): [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)

The same [EventActions](../../com.google.adk.kt.events/-event-actions/index.html) instance as [actions](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html), under the property name used by callbacks.

[eventAuthor](event-author.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [eventAuthor](event-author.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The author stamped on events this node emits.

[eventId](event-id.html)

Link copied to clipboard

common

override val [eventId](event-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The unique ID of the event that triggered this tool call.

[functionCallId](function-call-id.html)

Link copied to clipboard

common

override val [functionCallId](function-call-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The unique ID of the function call.

[hasProducedOutput](has-produced-output.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [hasProducedOutput](has-produced-output.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether an output has been produced, by this node or by a `useAsOutput` delegate.

[interruptIds](interrupt-ids.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [interruptIds](interrupt-ids.html): [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>

Interrupt IDs this node activation is waiting on.

[invocationContext](invocation-context.html)

Link copied to clipboard

common

val [invocationContext](invocation-context.html): [InvocationContext](../-invocation-context/index.html)

[invocationId](invocation-id.html)

Link copied to clipboard

common

override val [invocationId](invocation-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The unique ID of this invocation.

[memoryService](memory-service.html)

Link copied to clipboard

common

override val [memoryService](memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?

The MemoryService instance.

[node](node.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [node](node.html): [Node](../../com.google.adk.kt.workflow/-node/index.html)

The node this context is an activation of.

[nodePath](node-path.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [nodePath](node-path.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

This activation's path: `name@runId` segments joined by `/`, rooted at the outermost node.

[output](output.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [output](output.html): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

The node's output value. Can be set at most once per activation. Assigning `null` before any output is a no-op.

[parent](parent.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [parent](parent.html): [Context](index.html)?

The context of the node that scheduled this one, or null at the root or off-graph.

[resumeInputs](resume-inputs.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [resumeInputs](resume-inputs.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>

Answers to this node's interrupts, keyed by interrupt id. Empty off-graph.

[routes](routes.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [routes](routes.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Route](../../com.google.adk.kt.workflow/-route/index.html)>?

The routes this node selected, read by the scheduler to pick the outgoing edges.

[runConfig](run-config.html)

Link copied to clipboard

common

override val [runConfig](run-config.html): [RunConfig](../-run-config/index.html)?

The run configuration for this invocation.

[runId](run-id.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [runId](run-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

This activation's id within its node, counting from "1". It is a string because it forms the `name@runId` segment of a node path. "1" off-graph.

[session](session.html)

Link copied to clipboard

common

override val [session](session.html): [Session](../../com.google.adk.kt.sessions/-session/index.html)

The session that this invocation is a part of.

[state](state.html)

Link copied to clipboard

common

override val [state](state.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

The delta-aware state of the current session: committed session state merged with pending [actions](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html) `stateDelta` writes and this activation's transient writes, with removed keys filtered out.

[toolConfirmation](tool-confirmation.html)

Link copied to clipboard

common

val [toolConfirmation](tool-confirmation.html): [ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html)?

The tool confirmation of the current tool call.

[userContent](user-content.html)

Link copied to clipboard

common

override val [userContent](user-content.html): [Content](../../com.google.adk.kt.types/-content/index.html)?

The user content that this invocation is processing.

[userId](user-id.html)

Link copied to clipboard

common

override val [userId](user-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The user ID of the user that initiated the session.

## Functions

[addEventsToMemory](add-events-to-memory.html)

Link copied to clipboard

common

suspend fun [addEventsToMemory](add-events-to-memory.html)(events: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null)

Adds an explicit list of [events](add-events-to-memory.html) to the memory service, scoped to the current session's app/user/session ids.

[addMemory](add-memory.html)

Link copied to clipboard

common

suspend fun [addMemory](add-memory.html)(memories: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[MemoryEntry](../../com.google.adk.kt.memory/-memory-entry/index.html)>, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null)

Adds explicit [memories](add-memory.html) directly to the memory service, scoped to the current session's app/user ids.

[addSessionToMemory](add-session-to-memory.html)

Link copied to clipboard

common

suspend fun [addSessionToMemory](add-session-to-memory.html)()

Triggers memory generation for the current session.

[endInvocation](end-invocation.html)

Link copied to clipboard

common

fun [endInvocation](end-invocation.html)()

Requests the current LLM agent to stop after the current step completes.

[getEvents](get-events.html)

Link copied to clipboard

common

suspend override fun [getEvents](get-events.html)(currentInvocation: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, currentBranch: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Returns the events from the current session.

[listArtifacts](list-artifacts.html)

Link copied to clipboard

common

suspend override fun [listArtifacts](list-artifacts.html)(): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>

Lists the filenames of the artifacts attached to the current session. Returns an empty list if no artifact service is configured.

[loadArtifact](load-artifact.html)

Link copied to clipboard

common

suspend override fun [loadArtifact](load-artifact.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null): [Part](../../com.google.adk.kt.types/-part/index.html)?

Loads an artifact attached to the current session by [name](load-artifact.html). Returns `null` if no artifact service is configured or the artifact is not found.

[mergeEventActions](merge-event-actions.html)

Link copied to clipboard

common

fun [mergeEventActions](merge-event-actions.html)(actions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html))

Merges the given event actions into the current event actions, replacing [actions](merge-event-actions.html) with the merged result, after checking their state delta against the state schema in force here. Any reference to [actions](merge-event-actions.html) taken before the merge will not receive subsequent writes.

[requestConfirmation](request-confirmation.html)

Link copied to clipboard

common

fun [requestConfirmation](request-confirmation.html)(hint: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, payload: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null)

Requests confirmation for the current tool call. Only a tool call has a [functionCallId](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html), so this can only be called in a tool context.

[runNode](run-node.html)

Link copied to clipboard

common

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

suspend fun [runNode](run-node.html)(node: [Node](../../com.google.adk.kt.workflow/-node/index.html), nodeInput: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, runId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, useAsOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, useSubBranch: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, overrideBranch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, raiseOnWait: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Executes [node](run-node.html) as a child of this node activation and returns its output.

[saveArtifact](save-artifact.html)

Link copied to clipboard

common

suspend fun [saveArtifact](save-artifact.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), artifact: [Part](../../com.google.adk.kt.types/-part/index.html)): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

Saves [artifact](save-artifact.html) under [name](save-artifact.html) in the current session, records the new version in [actions](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html)' `artifactDelta`, and returns the saved version number.

[updateState](update-state.html)

Link copied to clipboard

common

fun [updateState](update-state.html)(key: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), value: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html))

Records a state change so it shows up in [state](state.html) and, on a callback or tool context, flushes on the next event as a delta.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
