[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.tools](../index.html)/ToolContext

# ToolContext

common

class [ToolContext](index.html)(invocationContext: [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html), actions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html) = EventActions(), functionCallId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, toolConfirmation: [ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html)? = null, eventId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null) : [Context](../../com.google.adk.kt.agents/-context/index.html)

Context passed to tool executions.

This subclass is kept for backward compatibility. Prefer [Context](../../com.google.adk.kt.agents/-context/index.html) in new code.

A tool context is not a node activation, so the node-only members inherited from [Context](../../com.google.adk.kt.agents/-context/index.html) (such as [Context.output](../../com.google.adk.kt.agents/-context/output.html) and [Context.routes](../../com.google.adk.kt.agents/-context/routes.html)) throw [IllegalStateException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-state-exception/index.html) here.

Members

## Constructors

[ToolContext](-tool-context.html)

Link copied to clipboard

common

constructor(invocationContext: [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html), actions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html) = EventActions(), functionCallId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, toolConfirmation: [ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html)? = null, eventId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

## Properties

[actions](../../com.google.adk.kt.agents/-context/actions.html)

Link copied to clipboard

common

var [actions](../../com.google.adk.kt.agents/-context/actions.html): [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)

The event actions for the current context, holding state deltas and control-flow signals to be attached to emitted events.

[agent](../../com.google.adk.kt.agents/-context/agent.html)

Link copied to clipboard

common

val [agent](../../com.google.adk.kt.agents/-context/agent.html): [BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html)

[agentName](../../com.google.adk.kt.agents/-context/agent-name.html)

Link copied to clipboard

common

override val [agentName](../../com.google.adk.kt.agents/-context/agent-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The name of the agent that is being invoked.

[artifactService](../../com.google.adk.kt.agents/-context/artifact-service.html)

Link copied to clipboard

common

override val [artifactService](../../com.google.adk.kt.agents/-context/artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?

The ArtifactService instance.

[attemptCount](../../com.google.adk.kt.agents/-context/attempt-count.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [attemptCount](../../com.google.adk.kt.agents/-context/attempt-count.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

1-based attempt number, which a retry increments. 1 off-graph.

[branch](../../com.google.adk.kt.agents/-context/branch.html)

Link copied to clipboard

common

override val [branch](../../com.google.adk.kt.agents/-context/branch.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The branch of the invocation context.

[callbackContextData](../../com.google.adk.kt.agents/-context/callback-context-data.html)

Link copied to clipboard

common

val [callbackContextData](../../com.google.adk.kt.agents/-context/callback-context-data.html): [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

Per-invocation scratch data; see [ContextFrameworkData.callbackContextData](../../com.google.adk.kt.agents/-context-framework-data/callback-context-data.html).

[context](../../com.google.adk.kt.agents/-context/context.html)

Link copied to clipboard

common

override val [context](../../com.google.adk.kt.agents/-context/context.html): [ReadonlyContext](../../com.google.adk.kt.agents/-readonly-context/index.html)

The readonly invocation context.

[eventActions](../../com.google.adk.kt.agents/-context/event-actions.html)

Link copied to clipboard

common

val [eventActions](../../com.google.adk.kt.agents/-context/event-actions.html): [EventActions](../../com.google.adk.kt.events/-event-actions/index.html)

The same [EventActions](../../com.google.adk.kt.events/-event-actions/index.html) instance as [actions](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html), under the property name used by callbacks.

[eventAuthor](../../com.google.adk.kt.agents/-context/event-author.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [eventAuthor](../../com.google.adk.kt.agents/-context/event-author.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The author stamped on events this node emits.

[eventId](../../com.google.adk.kt.agents/-context/event-id.html)

Link copied to clipboard

common

override val [eventId](../../com.google.adk.kt.agents/-context/event-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The unique ID of the event that triggered this tool call.

[functionCallId](../../com.google.adk.kt.agents/-context/function-call-id.html)

Link copied to clipboard

common

override val [functionCallId](../../com.google.adk.kt.agents/-context/function-call-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The unique ID of the function call.

[hasProducedOutput](../../com.google.adk.kt.agents/-context/has-produced-output.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [hasProducedOutput](../../com.google.adk.kt.agents/-context/has-produced-output.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether an output has been produced, by this node or by a `useAsOutput` delegate.

[interruptIds](../../com.google.adk.kt.agents/-context/interrupt-ids.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [interruptIds](../../com.google.adk.kt.agents/-context/interrupt-ids.html): [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>

Interrupt IDs this node activation is waiting on.

[invocationContext](../../com.google.adk.kt.agents/-context/invocation-context.html)

Link copied to clipboard

common

val [invocationContext](../../com.google.adk.kt.agents/-context/invocation-context.html): [InvocationContext](../../com.google.adk.kt.agents/-invocation-context/index.html)

[invocationId](../../com.google.adk.kt.agents/-context/invocation-id.html)

Link copied to clipboard

common

override val [invocationId](../../com.google.adk.kt.agents/-context/invocation-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The unique ID of this invocation.

[memoryService](../../com.google.adk.kt.agents/-context/memory-service.html)

Link copied to clipboard

common

override val [memoryService](../../com.google.adk.kt.agents/-context/memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?

The MemoryService instance.

[node](../../com.google.adk.kt.agents/-context/node.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [node](../../com.google.adk.kt.agents/-context/node.html): [Node](../../com.google.adk.kt.workflow/-node/index.html)

The node this context is an activation of.

[nodePath](../../com.google.adk.kt.agents/-context/node-path.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

val [nodePath](../../com.google.adk.kt.agents/-context/node-path.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

This activation's path: `name@runId` segments joined by `/`, rooted at the outermost node.

[output](../../com.google.adk.kt.agents/-context/output.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [output](../../com.google.adk.kt.agents/-context/output.html): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

The node's output value. Can be set at most once per activation. Assigning `null` before any output is a no-op.

[parent](../../com.google.adk.kt.agents/-context/parent.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [parent](../../com.google.adk.kt.agents/-context/parent.html): [Context](../../com.google.adk.kt.agents/-context/index.html)?

The context of the node that scheduled this one, or null at the root or off-graph.

[resumeInputs](../../com.google.adk.kt.agents/-context/resume-inputs.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [resumeInputs](../../com.google.adk.kt.agents/-context/resume-inputs.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>

Answers to this node's interrupts, keyed by interrupt id. Empty off-graph.

[routes](../../com.google.adk.kt.agents/-context/routes.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [routes](../../com.google.adk.kt.agents/-context/routes.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Route](../../com.google.adk.kt.workflow/-route/index.html)>?

The routes this node selected, read by the scheduler to pick the outgoing edges.

[runConfig](../../com.google.adk.kt.agents/-context/run-config.html)

Link copied to clipboard

common

override val [runConfig](../../com.google.adk.kt.agents/-context/run-config.html): [RunConfig](../../com.google.adk.kt.agents/-run-config/index.html)?

The run configuration for this invocation.

[runId](../../com.google.adk.kt.agents/-context/run-id.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

var [runId](../../com.google.adk.kt.agents/-context/run-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

This activation's id within its node, counting from "1". It is a string because it forms the `name@runId` segment of a node path. "1" off-graph.

[session](../../com.google.adk.kt.agents/-context/session.html)

Link copied to clipboard

common

override val [session](../../com.google.adk.kt.agents/-context/session.html): [Session](../../com.google.adk.kt.sessions/-session/index.html)

The session that this invocation is a part of.

[state](../../com.google.adk.kt.agents/-context/state.html)

Link copied to clipboard

common

override val [state](../../com.google.adk.kt.agents/-context/state.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

The delta-aware state of the current session: committed session state merged with pending [actions](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html) `stateDelta` writes and this activation's transient writes, with removed keys filtered out.

[toolConfirmation](../../com.google.adk.kt.agents/-context/tool-confirmation.html)

Link copied to clipboard

common

val [toolConfirmation](../../com.google.adk.kt.agents/-context/tool-confirmation.html): [ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html)?

The tool confirmation of the current tool call.

[userContent](../../com.google.adk.kt.agents/-context/user-content.html)

Link copied to clipboard

common

override val [userContent](../../com.google.adk.kt.agents/-context/user-content.html): [Content](../../com.google.adk.kt.types/-content/index.html)?

The user content that this invocation is processing.

[userId](../../com.google.adk.kt.agents/-context/user-id.html)

Link copied to clipboard

common

override val [userId](../../com.google.adk.kt.agents/-context/user-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The user ID of the user that initiated the session.

## Functions

[addEventsToMemory](../../com.google.adk.kt.agents/-context/add-events-to-memory.html)

Link copied to clipboard

common

suspend fun [addEventsToMemory](../../com.google.adk.kt.agents/-context/add-events-to-memory.html)(events: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null)

Adds an explicit list of [events](../../com.google.adk.kt.agents/-context/add-events-to-memory.html) to the memory service, scoped to the current session's app/user/session ids.

[addMemory](../../com.google.adk.kt.agents/-context/add-memory.html)

Link copied to clipboard

common

suspend fun [addMemory](../../com.google.adk.kt.agents/-context/add-memory.html)(memories: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[MemoryEntry](../../com.google.adk.kt.memory/-memory-entry/index.html)>, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null)

Adds explicit [memories](../../com.google.adk.kt.agents/-context/add-memory.html) directly to the memory service, scoped to the current session's app/user ids.

[addSessionToMemory](../../com.google.adk.kt.agents/-context/add-session-to-memory.html)

Link copied to clipboard

common

suspend fun [addSessionToMemory](../../com.google.adk.kt.agents/-context/add-session-to-memory.html)()

Triggers memory generation for the current session.

[endInvocation](../../com.google.adk.kt.agents/-context/end-invocation.html)

Link copied to clipboard

common

fun [endInvocation](../../com.google.adk.kt.agents/-context/end-invocation.html)()

Requests the current LLM agent to stop after the current step completes.

[getEvents](../../com.google.adk.kt.agents/-context/get-events.html)

Link copied to clipboard

common

suspend override fun [getEvents](../../com.google.adk.kt.agents/-context/get-events.html)(currentInvocation: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, currentBranch: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Returns the events from the current session.

[listArtifacts](../../com.google.adk.kt.agents/-context/list-artifacts.html)

Link copied to clipboard

common

suspend override fun [listArtifacts](../../com.google.adk.kt.agents/-context/list-artifacts.html)(): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>

Lists the filenames of the artifacts attached to the current session. Returns an empty list if no artifact service is configured.

[loadArtifact](../../com.google.adk.kt.agents/-context/load-artifact.html)

Link copied to clipboard

common

suspend override fun [loadArtifact](../../com.google.adk.kt.agents/-context/load-artifact.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), version: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null): [Part](../../com.google.adk.kt.types/-part/index.html)?

Loads an artifact attached to the current session by [name](../../com.google.adk.kt.agents/-context/load-artifact.html). Returns `null` if no artifact service is configured or the artifact is not found.

[mergeEventActions](../../com.google.adk.kt.agents/-context/merge-event-actions.html)

Link copied to clipboard

common

fun [mergeEventActions](../../com.google.adk.kt.agents/-context/merge-event-actions.html)(actions: [EventActions](../../com.google.adk.kt.events/-event-actions/index.html))

Merges the given event actions into the current event actions, replacing [actions](../../com.google.adk.kt.agents/-context/merge-event-actions.html) with the merged result, after checking their state delta against the state schema in force here. Any reference to [actions](../../com.google.adk.kt.agents/-context/merge-event-actions.html) taken before the merge will not receive subsequent writes.

[requestConfirmation](../../com.google.adk.kt.agents/-context/request-confirmation.html)

Link copied to clipboard

common

fun [requestConfirmation](../../com.google.adk.kt.agents/-context/request-confirmation.html)(hint: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, payload: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null)

Requests confirmation for the current tool call. Only a tool call has a [functionCallId](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html), so this can only be called in a tool context.

[runNode](../../com.google.adk.kt.agents/-context/run-node.html)

Link copied to clipboard

common

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

suspend fun [runNode](../../com.google.adk.kt.agents/-context/run-node.html)(node: [Node](../../com.google.adk.kt.workflow/-node/index.html), nodeInput: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, runId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, useAsOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, useSubBranch: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, overrideBranch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, raiseOnWait: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Executes [node](../../com.google.adk.kt.agents/-context/run-node.html) as a child of this node activation and returns its output.

[saveArtifact](../../com.google.adk.kt.agents/-context/save-artifact.html)

Link copied to clipboard

common

suspend fun [saveArtifact](../../com.google.adk.kt.agents/-context/save-artifact.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), artifact: [Part](../../com.google.adk.kt.types/-part/index.html)): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

Saves [artifact](../../com.google.adk.kt.agents/-context/save-artifact.html) under [name](../../com.google.adk.kt.agents/-context/save-artifact.html) in the current session, records the new version in [actions](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-context/--root--.html)' `artifactDelta`, and returns the saved version number.

[updateState](../../com.google.adk.kt.agents/-context/update-state.html)

Link copied to clipboard

common

fun [updateState](../../com.google.adk.kt.agents/-context/update-state.html)(key: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), value: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html))

Records a state change so it shows up in [state](../../com.google.adk.kt.agents/-context/state.html) and, on a callback or tool context, flushes on the next event as a delta.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
