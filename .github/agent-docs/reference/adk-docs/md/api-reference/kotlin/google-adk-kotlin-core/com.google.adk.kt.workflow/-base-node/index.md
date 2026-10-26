[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.workflow](../index.html)/BaseNode

# BaseNode

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

abstract class [BaseNode](index.html)(val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val rerunOnResume: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val waitForOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val config: [NodeConfig](../-node-config/index.html) = NodeConfig(), val inputSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null, val outputSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null, val stateSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null) : [Node](../-node/index.html)

The base class for units of work in a workflow graph. A `Workflow` is itself a node, so graphs nest, and every agent is one too.

Public only so that `BaseAgent`, `Workflow`, `JoinNode` and the Java interop base `BasePublisherNode` can extend it. It is framework plumbing: write a node by implementing [Node](../-node/index.html), or from Java by extending `BasePublisherNode`.

Subclasses implement [runNode](../-node/run-node.html) and emit raw values; [run](run.html) normalizes each into an [Event](../../com.google.adk.kt.events/-event/index.html). Node names must be unique within a graph, since the scheduler keys on them.

#### Inheritors

[BasePublisherNode](../../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-publisher-node/index.html)

[BaseAgent](../../com.google.adk.kt.agents/-base-agent/index.html)

[FunctionNode](../-function-node/index.html)

[JoinNode](../-join-node/index.html)

[Workflow](../-workflow/index.html)

Members

## Constructors

[BaseNode](-base-node.html)

Link copied to clipboard

common

constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", rerunOnResume: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, waitForOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, config: [NodeConfig](../-node-config/index.html) = NodeConfig(), inputSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null, outputSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null, stateSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null)

## Properties

[config](config.html)

Link copied to clipboard

common

open override val [config](config.html): [NodeConfig](../-node-config/index.html)

The node's retry policy and execution timeout.

[description](description.html)

Link copied to clipboard

common

open override val [description](description.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

What the node does, for humans and for a model that may call it.

[inputSchema](input-schema.html)

Link copied to clipboard

common

open override val [inputSchema](input-schema.html): [Schema](../../com.google.adk.kt.types/-schema/index.html)?

Validates the node's input before it runs.

[name](name.html)

Link copied to clipboard

common

override val [name](name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Identifies the node within its graph.

[outputSchema](output-schema.html)

Link copied to clipboard

common

open override val [outputSchema](output-schema.html): [Schema](../../com.google.adk.kt.types/-schema/index.html)?

Validates the output value the node emits. A value assigned to `Context.output` and a message-as-output event's content are not checked.

[requiresAllPredecessors](requires-all-predecessors.html)

Link copied to clipboard

common

open override val [requiresAllPredecessors](requires-all-predecessors.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether the node runs only once every predecessor has completed, receiving all their outputs keyed by node name. A fan-in node overrides this to true.

[rerunOnResume](rerun-on-resume.html)

Link copied to clipboard

common

open override val [rerunOnResume](rerun-on-resume.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

On resume, whether to run the node again from scratch rather than completing it with the resuming answer as its output.

[stateSchema](state-schema.html)

Link copied to clipboard

common

open override val [stateSchema](state-schema.html): [Schema](../../com.google.adk.kt.types/-schema/index.html)?

Declares the state keys the node uses. Child nodes inherit it unless they declare their own.

[waitForOutput](wait-for-output.html)

Link copied to clipboard

common

open override val [waitForOutput](wait-for-output.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether the node stays re-triggerable until it produces an output or a route, instead of completing when [runNode](../-node/run-node.html) returns. A node that never produces either then waits forever, which is a graph-authoring error.

## Functions

[run](run.html)

Link copied to clipboard

common

fun [run](run.html)(context: [Context](../../com.google.adk.kt.agents/-context/index.html), nodeInput: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Runs the node and normalizes each raw emission of [runNode](../-node/run-node.html) into an [Event](../../com.google.adk.kt.events/-event/index.html): `null` and `Unit` are skipped, a [RequestInput](../-request-input/index.html) becomes an `adk_request_input` interrupt event, an [Event](../../com.google.adk.kt.events/-event/index.html) keeps its content and has its `output` validated, and any other value becomes the output.

[runNode](../-node/run-node.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

abstract fun [runNode](../-node/run-node.html)(context: [Context](../../com.google.adk.kt.agents/-context/index.html), nodeInput: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)<[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>

The user-facing implementation of the node's execution logic.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
