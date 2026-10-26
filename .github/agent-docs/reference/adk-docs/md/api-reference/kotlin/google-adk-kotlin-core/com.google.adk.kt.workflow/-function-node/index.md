[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.workflow](../index.html)/FunctionNode

# FunctionNode

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [FunctionNode](index.html)<[I](index.html), [O](index.html)> : [BaseNode](../-base-node/index.html)

A workflow [Node](../-node/index.html) backed by a suspending function that may emit progress [Event](../../com.google.adk.kt.events/-event/index.html)s and returns an output of type [O](index.html). Its schemas inferred from [I](index.html) and [O](index.html) only describe it; an explicit schema passed to [node](../node.html) is also enforced.

Inline workflow steps use [node](../node.html) or [parallelNode](../parallel-node.html).

#### Type Parameters

 _I_

Expected type of `nodeInput` from predecessor nodes.

_O_

Type of output value this node returns (`Unit`/`null` emits no output event; [Event](../../com.google.adk.kt.events/-event/index.html) passes through directly; a [Content](../../com.google.adk.kt.types/-content/index.html) becomes a message event with no node output; any other value becomes the node's output on an [Event](../../com.google.adk.kt.events/-event/index.html)).

Members

## Properties

[config](../-base-node/config.html)

Link copied to clipboard

common

open override val [config](../-base-node/config.html): [NodeConfig](../-node-config/index.html)

The node's retry policy and execution timeout.

[description](../-base-node/description.html)

Link copied to clipboard

common

open override val [description](../-base-node/description.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

What the node does, for humans and for a model that may call it.

[inputSchema](../-base-node/input-schema.html)

Link copied to clipboard

common

open override val [inputSchema](../-base-node/input-schema.html): [Schema](../../com.google.adk.kt.types/-schema/index.html)?

Validates the node's input before it runs.

[name](../-base-node/name.html)

Link copied to clipboard

common

override val [name](../-base-node/name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Identifies the node within its graph.

[outputSchema](../-base-node/output-schema.html)

Link copied to clipboard

common

open override val [outputSchema](../-base-node/output-schema.html): [Schema](../../com.google.adk.kt.types/-schema/index.html)?

Validates the output value the node emits. A value assigned to `Context.output` and a message-as-output event's content are not checked.

[requiresAllPredecessors](../-base-node/requires-all-predecessors.html)

Link copied to clipboard

common

open override val [requiresAllPredecessors](../-base-node/requires-all-predecessors.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether the node runs only once every predecessor has completed, receiving all their outputs keyed by node name. A fan-in node overrides this to true.

[rerunOnResume](../-base-node/rerun-on-resume.html)

Link copied to clipboard

common

open override val [rerunOnResume](../-base-node/rerun-on-resume.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

On resume, whether to run the node again from scratch rather than completing it with the resuming answer as its output.

[stateSchema](../-base-node/state-schema.html)

Link copied to clipboard

common

open override val [stateSchema](../-base-node/state-schema.html): [Schema](../../com.google.adk.kt.types/-schema/index.html)?

Declares the state keys the node uses. Child nodes inherit it unless they declare their own.

[waitForOutput](../-base-node/wait-for-output.html)

Link copied to clipboard

common

open override val [waitForOutput](../-base-node/wait-for-output.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether the node stays re-triggerable until it produces an output or a route, instead of completing when [runNode](../-node/run-node.html) returns. A node that never produces either then waits forever, which is a graph-authoring error.

## Functions

[run](../-base-node/run.html)

Link copied to clipboard

common

fun [run](../-base-node/run.html)(context: [Context](../../com.google.adk.kt.agents/-context/index.html), nodeInput: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Runs the node and normalizes each raw emission of [runNode](../-node/run-node.html) into an [Event](../../com.google.adk.kt.events/-event/index.html): `null` and `Unit` are skipped, a [RequestInput](../-request-input/index.html) becomes an `adk_request_input` interrupt event, an [Event](../../com.google.adk.kt.events/-event/index.html) keeps its content and has its `output` validated, and any other value becomes the output.

[runNode](run-node.html)

Link copied to clipboard

common

open override fun [runNode](run-node.html)(context: [Context](../../com.google.adk.kt.agents/-context/index.html), nodeInput: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)<[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>

The user-facing implementation of the node's execution logic.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
