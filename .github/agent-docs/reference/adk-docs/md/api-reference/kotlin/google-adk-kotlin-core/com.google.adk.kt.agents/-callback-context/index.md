[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/CallbackContext

# CallbackContext

common

class [CallbackContext](index.html)(invocationContext: [InvocationContext](../-invocation-context/index.html), eventActions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)? = null) : [Context](../-context/index.html)

Context passed to agent and model callbacks.

This subclass is kept for backward compatibility. Prefer [Context](../-context/index.html) in new code.

A callback context is not a node activation, so the node-only members inherited from [Context](../-context/index.html) (such as [Context.output](../-context/output.html) and [Context.routes](../-context/routes.html)) throw [IllegalStateException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-state-exception/index.html) here.

Members

## Constructors

[CallbackContext](-callback-context.html)

Link copied to clipboard

common

constructor(invocationContext: [InvocationContext](../-invocation-context/index.html), eventActions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)? = null)

## Properties

[actions](../-context/actions.html)

Link copied to clipboard

common

var [actions](../-context/actions.html): [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)

The event actions for the current context, holding state deltas and control-flow signals to be attached to emitted events.

[agent](../-context/agent.html)

Link copied to clipboard

common

val [agent](../-context/agent.html): [BaseAgent](../-base-agent/index.html)

[agentName](../-context/agent-name.html)

Link copied to clipboard

common

override val [agentName](../-context/agent-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The name of the agent that is being invoked.

[artifactService](../-context/artifact-service.html)

Link copied to clipboard

common

override val [artifactService](../-context/artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?

The ArtifactService instance.

[attemptCount](../-context/attempt-count.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [attemptCount](../-context/attempt-count.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

1-based attempt number, which a retry increments. 1 off-graph.

[branch](../-context/branch.html)

Link copied to clipboard

common

override val [branch](../-context/branch.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The branch of the invocation context.

[callbackContextData](../-context/callback-context-data.html)

Link copied to clipboard

common

val [callbackContextData](../-context/callback-context-data.html): [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

Per-invocation scratch data; see [ContextFrameworkData.callbackContextData](../-context-framework-data/callback-context-data.html).

[context](../-context/context.html)

Link copied to clipboard

common

override val [context](../-context/context.html): [ReadonlyContext](../-readonly-context/index.html)

The readonly invocation context.

[eventActions](../-context/event-actions.html)

Link copied to clipboard

common

val [eventActions](../-context/event-actions.html): [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)

The same [EventActions](../../com.google.adk.kt.events/-event-actions/index.html) instance as [actions](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html), under the property name used by callbacks.

[eventAuthor](../-context/event-author.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [eventAuthor](../-context/event-author.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The author stamped on events this node emits.

[eventId](../-context/event-id.html)

Link copied to clipboard

common

override val [eventId](../-context/event-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The unique ID of the event that triggered this tool call.

[functionCallId](../-context/function-call-id.html)

Link copied to clipboard

common

override val [functionCallId](../-context/function-call-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The unique ID of the function call.

[hasProducedOutput](../-context/has-produced-output.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [hasProducedOutput](../-context/has-produced-output.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether an output has been produced, by this node or by a `useAsOutput` delegate.

[interruptIds](../-context/interrupt-ids.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [interruptIds](../-context/interrupt-ids.html): [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>

Interrupt IDs this node activation is waiting on.

[invocationContext](../-context/invocation-context.html)

Link copied to clipboard

common

val [invocationContext](../-context/invocation-context.html): [InvocationContext](../-invocation-context/index.html)

[invocationId](../-context/invocation-id.html)

Link copied to clipboard

common

override val [invocationId](../-context/invocation-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The unique ID of this invocation.

[memoryService](../-context/memory-service.html)

Link copied to clipboard

common

override val [memoryService](../-context/memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?

The MemoryService instance.

[node](../-context/node.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [node](../-context/node.html): [Node](../../com.google.adk.kt.workflow/-node/index.html)

The node this context is an activation of.

[nodePath](../-context/node-path.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [nodePath](../-context/node-path.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

This activation's path: `name@runId` segments joined by `/`, rooted at the outermost node.

[output](../-context/output.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [output](../-context/output.html): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

The node's output value. Can be set at most once per activation. Assigning `null` before any output is a no-op.

[parent](../-context/parent.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [parent](../-context/parent.html): [Context](../-context/index.html)?

The context of the node that scheduled this one, or null at the root or off-graph.

[resumeInputs](../-context/resume-inputs.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [resumeInputs](../-context/resume-inputs.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>

Answers to this node's interrupts, keyed by interrupt id. Empty off-graph.

[routes](../-context/routes.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [routes](../-context/routes.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Route](../../com.google.adk.kt.workflow/-route/index.html)>?

The routes this node selected, read by the scheduler to pick the outgoing edges.

[runConfig](../-context/run-config.html)

Link copied to clipboard

common

override val [runConfig](../-context/run-config.html): [RunConfig](../-run-config/index.html)?

The run configuration for this invocation.

[runId](../-context/run-id.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [runId](../-context/run-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

This activation's id within its node, counting from "1". It is a string because it forms the `name@runId` segment of a node path. "1" off-graph.

[session](../-context/session.html)

Link copied to clipboard

common

override val [session](../-context/session.html): [Session](../../com.google.adk.kt.sessions/-session/index.html)

The session that this invocation is a part of.

[state](../-context/state.html)

Link copied to clipboard

common

override val [state](../-context/state.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

The delta-aware state of the current session: committed session state merged with pending [actions](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html) `stateDelta` writes and this activation's transient writes, with removed keys filtered out.

[toolConfirmation](../-context/tool-confirmation.html)

Link copied to clipboard

common

val [toolConfirmation](../-context/tool-confirmation.html): [ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html)?

The tool confirmation of the current tool call.

[userContent](../-context/user-content.html)

Link copied to clipboard

common

override val [userContent](../-context/user-content.html): [Content](../../com.google.adk.kt.types/-content/index.html)?

The user content that this invocation is processing.

[userId](../-context/user-id.html)

Link copied to clipboard

common

override val [userId](../-context/user-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The user ID of the user that initiated the session.

## Functions

[addEventsToMemory](../-context/add-events-to-memory.html)

Link copied to clipboard

common

suspend fun [addEventsToMemory](../-context/add-events-to-memory.html)(events: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null)

Adds an explicit list of [events](../-context/add-events-to-memory.html) to the memory service, scoped to the current session's app/user/session ids.

[addMemory](../-context/add-memory.html)

Link copied to clipboard

common

suspend fun [addMemory](../-context/add-memory.html)(memories: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[MemoryEntry](../../com.google.adk.kt.memory/-memory-entry/index.html)>, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null)

Adds explicit [memories](../-context/add-memory.html) directly to the memory service, scoped to the current session's app/user ids.

[addSessionToMemory](../-context/add-session-to-memory.html)

Link copied to clipboard

common

suspend fun [addSessionToMemory](../-context/add-session-to-memory.html)()

Triggers memory generation for the current session.

[endInvocation](../-context/end-invocation.html)

Link copied to clipboard

common

fun [endInvocation](../-context/end-invocation.html)()

Requests the current LLM agent to stop after the current step completes.

[getEvents](../-context/get-events.html)

Link copied to clipboard

common

suspend override fun [getEvents](../-context/get-events.html)(currentInvocation: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, currentBranch: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Returns the events from the current session.

[listArtifacts](../-context/list-artifacts.html)

Link copied to clipboard

common

suspend override fun [listArtifacts](../-context/list-artifacts.html)(): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>

Lists the filenames of the artifacts attached to the current session. Returns an empty list if no artifact service is configured.

[loadArtifact](../-context/load-artifact.html)

Link copied to clipboard

common

suspend override fun [loadArtifact](../-context/load-artifact.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null): [Part](../../com.google.adk.kt.types/-part/index.html)?

Loads an artifact attached to the current session by [name](../-context/load-artifact.html). Returns `null` if no artifact service is configured or the artifact is not found.

[mergeEventActions](../-context/merge-event-actions.html)

Link copied to clipboard

common

fun [mergeEventActions](../-context/merge-event-actions.html)(actions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html))

Merges the given event actions into the current event actions, replacing [actions](../-context/merge-event-actions.html) with the merged result, after checking their state delta against the state schema in force here. Any reference to [actions](../-context/merge-event-actions.html) taken before the merge will not receive subsequent writes.

[requestConfirmation](../-context/request-confirmation.html)

Link copied to clipboard

common

fun [requestConfirmation](../-context/request-confirmation.html)(hint: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, payload: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null)

Requests confirmation for the current tool call. Only a tool call has a [functionCallId](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html), so this can only be called in a tool context.

[runNode](../-context/run-node.html)

Link copied to clipboard

common

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

suspend fun [runNode](../-context/run-node.html)(node: [Node](../../com.google.adk.kt.workflow/-node/index.html), nodeInput: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, runId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, useAsOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, useSubBranch: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, overrideBranch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, raiseOnWait: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Executes [node](../-context/run-node.html) as a child of this node activation and returns its output.

[saveArtifact](../-context/save-artifact.html)

Link copied to clipboard

common

suspend fun [saveArtifact](../-context/save-artifact.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), artifact: [Part](../../com.google.adk.kt.types/-part/index.html)): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

Saves [artifact](../-context/save-artifact.html) under [name](../-context/save-artifact.html) in the current session, records the new version in [actions](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html)' `artifactDelta`, and returns the saved version number.

[updateState](../-context/update-state.html)

Link copied to clipboard

common

fun [updateState](../-context/update-state.html)(key: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), value: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html))

Records a state change so it shows up in [state](../-context/state.html) and, on a callback or tool context, flushes on the next event as a delta.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
