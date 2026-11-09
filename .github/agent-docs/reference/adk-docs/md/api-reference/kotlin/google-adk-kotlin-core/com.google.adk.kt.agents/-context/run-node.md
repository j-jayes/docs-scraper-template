[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.5.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/[Context](index.html)/runNode

# runNode

common

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

suspend fun [runNode](run-node.html)(node: [Node](../../com.google.adk.kt.workflow/-node/index.html), nodeInput: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, runId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, useAsOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, useSubBranch: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, overrideBranch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, overrideIsolationScope: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, raiseOnWait: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Executes [node](run-node.html) as a child of this node activation and returns its output. When [node](run-node.html) is an agent that hands off with `transfer_to_agent`, the handoffs are followed and the last agent's output is returned.

Child events are recorded under `<thisNodePath>/<node.name>@<runId>`. If [node](run-node.html) fails, this call throws [DynamicNodeFailedException](../../com.google.adk.kt.workflow/-dynamic-node-failed-exception/index.html), which fails this node unless the caller catches it. If [node](run-node.html) pauses for input, this call throws an internal [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html) that is not an [Exception](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-exception/index.html), so the runtime can mark this node as waiting; do not catch it with `runCatching` or `catch (t: Throwable)`.

#### Parameters

 _node_

Child node to execute.

_node Input_

Input passed to [node](run-node.html), or `null` if none.

_run Id_

Explicit run ID for [node](run-node.html): at least one non-digit, and no `'/'`, `'@'`, or `'.'`. A child that already recorded an output under the same ID, in this activation, an earlier attempt, or an earlier turn, returns it without running again; one that finished without an output may run again. When `null` or empty, the child gets the next number for its name, which follows call order, so concurrent children need explicit IDs.

_use AsOutput_

When `true`, delegates this node's output to [node](run-node.html). The first output this node produces afterwards (such as returning [node](run-node.html)'s result) is dropped, even if [node](run-node.html) produces none. A second output fails this node. The claim is released only if [node](run-node.html) fails before emitting an output, so a caller that catches the failure may fall back to its own output. Once [node](run-node.html) has emitted, its output is this node's output and successors receive it. A `node {}` outputs it encoded under its output type, as if it had returned it, and fails if it does not decode.

_use SubBranch_

When `true`, runs [node](run-node.html) on a sub-branch `<branch>.<node.name>@<runId>`.

_override Branch_

Branch for [node](run-node.html) to run on instead of this node's branch.

_override IsolationScope_

Isolation scope for [node](run-node.html) to run in instead of this node's scope. When `null`, an [AgentMode.TASK](../-agent-mode/-t-a-s-k/index.html) child of a node activation runs in a scope named by its own node path.

_raise OnWait_

When `true` and [node](run-node.html) is a [Workflow](../../com.google.adk.kt.workflow/-workflow/index.html) or sets [Node.waitForOutput](../../com.google.adk.kt.workflow/-node/wait-for-output.html) but finishes without an output, aborts this node's run like an interrupt, without recording one: this node completes with any output it already produced, or else waits only if it sets [Node.waitForOutput](../../com.google.adk.kt.workflow/-node/wait-for-output.html).

#### Throws

[IllegalStateException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-state-exception/index.html)

if called outside a node activation, if this node does not set `rerunOnResume = true`, or if this node already produced or delegated its output and [useAsOutput](run-node.html) is `true`.

[IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)

if [node](run-node.html)'s name or [runId](run-node.html) is invalid, if [nodeInput](run-node.html) fails [node](run-node.html)'s input schema, or if a handoff can't be followed: a node that is not an agent requests one, or an agent requests one to itself, to an agent its transfer flags forbid, to a task or single-turn agent, or to an agent that is not its child, parent or peer. A [node](../../com.google.adk.kt.workflow/node.html) child's input check throws [NodeInputValidationException](../../com.google.adk.kt.workflow/-node-input-validation-exception/index.html) instead. A [parallelNode](../../com.google.adk.kt.workflow/parallel-node.html) checks each item instead, and a rejected item fails it.

[DynamicNodeFailedException](../../com.google.adk.kt.workflow/-dynamic-node-failed-exception/index.html)

if [node](run-node.html) fails; its `error` is the child's failure.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
