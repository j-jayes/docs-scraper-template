[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

commonJvmAndroid

Target filter __

    * commonJvmAndroid 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.interop](../index.html)/BasePublisherNode

# BasePublisherNode

commonJvmAndroid

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

abstract class [BasePublisherNode](index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", rerunOnResume: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, waitForOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, config: [NodeConfig](../../com.google.adk.kt.workflow/-node-config/index.html) = NodeConfig(), inputSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null, outputSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null, stateSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null) : [BaseNode](../../com.google.adk.kt.workflow/-base-node/index.html)

Java-friendly base for implementing a workflow node. A Java subclass overrides [runNodeJava](../../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-publisher-node/run-node-java.html) to set routes or state on the context and return a Reactive Streams [Publisher](https://www.reactive-streams.org/reactive-streams-1.0.4-javadoc/org/reactivestreams/Publisher.html) of node outputs, which this base adapts to the `Flow`-returning [runNode](run-node.html).

Members

## Constructors

[BasePublisherNode](-base-publisher-node.html)

Link copied to clipboard

commonJvmAndroid

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", rerunOnResume: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, waitForOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, config: [NodeConfig](../../com.google.adk.kt.workflow/-node-config/index.html) = NodeConfig(), inputSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null, outputSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null, stateSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null)

constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), config: [NodeConfig](../../com.google.adk.kt.workflow/-node-config/index.html))

Creates a node with [config](../../../google-adk-kotlin-core/com.google.adk.kt.interop/-base-publisher-node/--root--.html) and every other property at its default.

## Properties

[config](../../com.google.adk.kt.workflow/-base-node/config.html)

Link copied to clipboard

commonJvmAndroid

open override val [config](../../com.google.adk.kt.workflow/-base-node/config.html): [NodeConfig](../../com.google.adk.kt.workflow/-node-config/index.html)

The node's retry policy and execution timeout.

[description](../../com.google.adk.kt.workflow/-base-node/description.html)

Link copied to clipboard

commonJvmAndroid

open override val [description](../../com.google.adk.kt.workflow/-base-node/description.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

What the node does, for humans and for a model that may call it.

[inputSchema](../../com.google.adk.kt.workflow/-base-node/input-schema.html)

Link copied to clipboard

commonJvmAndroid

open override val [inputSchema](../../com.google.adk.kt.workflow/-base-node/input-schema.html): [Schema](../../com.google.adk.kt.types/-schema/index.html)?

Validates the node's input before it runs.

[name](../../com.google.adk.kt.workflow/-base-node/name.html)

Link copied to clipboard

commonJvmAndroid

override val [name](../../com.google.adk.kt.workflow/-base-node/name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Identifies the node within its graph.

[outputSchema](../../com.google.adk.kt.workflow/-base-node/output-schema.html)

Link copied to clipboard

commonJvmAndroid

open override val [outputSchema](../../com.google.adk.kt.workflow/-base-node/output-schema.html): [Schema](../../com.google.adk.kt.types/-schema/index.html)?

Validates the output value the node emits. A value assigned to `Context.output` and a message-as-output event's content are not checked.

[requiresAllPredecessors](../../com.google.adk.kt.workflow/-base-node/requires-all-predecessors.html)

Link copied to clipboard

commonJvmAndroid

open override val [requiresAllPredecessors](../../com.google.adk.kt.workflow/-base-node/requires-all-predecessors.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether the node runs only once every predecessor has completed, receiving all their outputs keyed by node name. A fan-in node overrides this to true.

[rerunOnResume](../../com.google.adk.kt.workflow/-base-node/rerun-on-resume.html)

Link copied to clipboard

commonJvmAndroid

open override val [rerunOnResume](../../com.google.adk.kt.workflow/-base-node/rerun-on-resume.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

On resume, whether to run the node again from scratch rather than completing it with the resuming answer as its output.

[stateSchema](../../com.google.adk.kt.workflow/-base-node/state-schema.html)

Link copied to clipboard

commonJvmAndroid

open override val [stateSchema](../../com.google.adk.kt.workflow/-base-node/state-schema.html): [Schema](../../com.google.adk.kt.types/-schema/index.html)?

Declares the state keys the node uses. Child nodes inherit it unless they declare their own.

[waitForOutput](../../com.google.adk.kt.workflow/-base-node/wait-for-output.html)

Link copied to clipboard

commonJvmAndroid

open override val [waitForOutput](../../com.google.adk.kt.workflow/-base-node/wait-for-output.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether the node stays re-triggerable until it produces an output or a route, instead of completing when [runNode](../../com.google.adk.kt.workflow/-node/run-node.html) returns. A node that never produces either then waits forever, which is a graph-authoring error.

## Functions

[run](../../com.google.adk.kt.workflow/-base-node/run.html)

Link copied to clipboard

commonJvmAndroid

fun [run](../../com.google.adk.kt.workflow/-base-node/run.html)(context: [Context](../../com.google.adk.kt.agents/-context/index.html), nodeInput: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Runs the node and normalizes each raw emission of [runNode](../../com.google.adk.kt.workflow/-node/run-node.html) into an [Event](../../com.google.adk.kt.events/-event/index.html): `null` and `Unit` are skipped, a [RequestInput](../../com.google.adk.kt.workflow/-request-input/index.html) becomes an `adk_request_input` interrupt event, an [Event](../../com.google.adk.kt.events/-event/index.html) keeps its content and has its `output` validated, and any other value becomes the output.

[runNode](run-node.html)

Link copied to clipboard

commonJvmAndroid

override fun [runNode](run-node.html)(context: [Context](../../com.google.adk.kt.agents/-context/index.html), nodeInput: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Flow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/index.html)<[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>

The user-facing implementation of the node's execution logic.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
