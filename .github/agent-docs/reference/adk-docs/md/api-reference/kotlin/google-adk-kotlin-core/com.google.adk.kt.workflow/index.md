[ google-adk-kotlin ](../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../index.html)/com.google.adk.kt.workflow

# Package-level declarations

TypesFunctions

## Types

[BaseNode](-base-node/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

abstract class [BaseNode](-base-node/index.html)(val name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val rerunOnResume: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val waitForOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val config: [NodeConfig](-node-config/index.html) = NodeConfig(), val inputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, val outputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, val stateSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null) : [Node](-node/index.html)

The base class for units of work in a workflow graph. A `Workflow` is itself a node, so graphs nest, and every agent is one too.

[DynamicNodeFailedException](-dynamic-node-failed-exception/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [DynamicNodeFailedException](-dynamic-node-failed-exception/index.html) : [RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html)

Thrown by [com.google.adk.kt.agents.Context.runNode](../com.google.adk.kt.agents/-context/run-node.html) when the dispatched child fails: [error](../../google-adk-kotlin-core/com.google.adk.kt.workflow/-dynamic-node-failed-exception/--root--.html) is the child's failure and [errorNodePath](../../google-adk-kotlin-core/com.google.adk.kt.workflow/-dynamic-node-failed-exception/--root--.html) the path of the node that failed.

[Edge](-edge/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

data class [Edge](-edge/index.html)(val from: [Node](-node/index.html), val to: [Node](-node/index.html), val routes: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Route](-route/index.html)> = emptyList())

A connection between two nodes.

[EdgeChain](-edge-chain/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [EdgeChain](-edge-chain/index.html)

A chain of edges for Java callers, positioned at a node. [EdgesBuilder.from](-edges-builder/from.html) starts a chain, and each call adds the same edges as the edges DSL function of the same name and continues from its target.

[EdgesBuilder](-edges-builder/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [EdgesBuilder](-edges-builder/index.html)

The receiver that collects the edges declared in an [edges](edges.html) or [workflow](workflow.html) block. A node is identified by its instance, so create each node once and reuse it. To add a tool as a step, convert it once with [asNode](as-node.html) and reuse that node.

[EdgesDslBlock](-edges-dsl-block/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

fun interface [EdgesDslBlock](-edges-dsl-block/index.html)<in [T](-edges-dsl-block/index.html)>

A block that declares edges or routes on a [T](-edges-dsl-block/index.html) builder. In Kotlin, pass a lambda with the builder as its receiver. In Java, pass a lambda that takes the builder as an argument, with no `Unit` to return.

[FunctionNode](-function-node/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [FunctionNode](-function-node/index.html)<[I](-function-node/index.html), [O](-function-node/index.html)> : [BaseNode](-base-node/index.html)

A workflow [Node](-node/index.html) backed by a suspending function that may emit progress [Event](../com.google.adk.kt.events/-event/index.html)s and returns an output of type [O](-function-node/index.html). Its schemas inferred from [I](-function-node/index.html) and [O](-function-node/index.html) only describe it; an explicit schema passed to [node](node.html) is also enforced.

[GraphValidationException](-graph-validation-exception/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [GraphValidationException](-graph-validation-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : [IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html)

A workflow graph failed validation. Raised when the graph is built, not when it runs.

[JoinNode](-join-node/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [JoinNode](-join-node/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", inputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, outputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null) : [BaseNode](-base-node/index.html)

Waits for every predecessor to complete, then outputs their outputs keyed by predecessor name.

[Node](-node/index.html)

Link copied to clipboard

common

interface [Node](-node/index.html)

A unit of work in a workflow graph.

[NodeConfig](-node-config/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

data class [NodeConfig](-node-config/index.html)(val retryConfig: [RetryConfig](-retry-config/index.html)? = null, val timeout: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)? = null)

Bundles a node's retry policy and execution timeout. A null [timeout](../../google-adk-kotlin-core/com.google.adk.kt.workflow/-node-config/--root--.html) imposes no limit, so an attempt is then bounded only by any ambient deadline. Validation lives here, so every [Node](-node/index.html) implementation inherits it.

[NodeExecutionException](-node-execution-exception/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

open class [NodeExecutionException](-node-execution-exception/index.html)(val typeName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html)

A node failure that reports under a [typeName](../../google-adk-kotlin-core/com.google.adk.kt.workflow/-node-execution-exception/--root--.html) other than this class's own, so a failure raised in one ADK implementation is matched by the same name in another.

[NodeGroup](-node-group/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [NodeGroup](-node-group/index.html)

Nodes grouped by `nodes(...)` or a fan-out `then`, which [EdgesBuilder.joinTo](-edges-builder/join-to.html) connects to a [JoinNode](-join-node/index.html).

[NodeGroupChain](-node-group-chain/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [NodeGroupChain](-node-group-chain/index.html)

A chain of edges for Java callers, positioned at a [NodeGroup](-node-group/index.html) from a fan-out or [EdgesBuilder.from](-edges-builder/from.html).

[NodeInfo](-node-info/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [NodeInfo](-node-info/index.html)(val path: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val outputFor: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val messageAsOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Identifies the workflow-node activation that emitted an [com.google.adk.kt.events.Event](../com.google.adk.kt.events/-event/index.html); `null` outside a workflow.

[NodeInputValidationException](-node-input-validation-exception/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [NodeInputValidationException](-node-input-validation-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [NodeExecutionException](-node-execution-exception/index.html)

Raised when a node's runtime input fails validation. Reports `typeName = "NodeInputValidationError"`.

[NodeTimeoutException](-node-timeout-exception/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [NodeTimeoutException](-node-timeout-exception/index.html)(val nodeName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val timeout: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html), cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [NodeExecutionException](-node-execution-exception/index.html)

A node exceeded its configured timeout. An ordinary exception, so a timed-out node is still eligible for retry.

[PendingEdge](-pending-edge/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [PendingEdge](-pending-edge/index.html)

An edge started by [EdgesBuilder.on](-edges-builder/on.html), which has a source and its routes but no target yet. [EdgesBuilder.then](-edges-builder/then.html) completes it.

[PendingEdgeChain](-pending-edge-chain/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [PendingEdgeChain](-pending-edge-chain/index.html)

A chain of edges for Java callers, positioned at a routed edge started by [EdgeChain.on](-edge-chain/on.html); [then](-pending-edge-chain/then.html) completes it.

[RequestInput](-request-input/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

data class [RequestInput](-request-input/index.html)(val interruptId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = Uuid.random(), val message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val payload: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, val responseSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null)

A node's request for user input, which pauses the workflow until a matching response arrives.

[RetryConfig](-retry-config/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

data class [RetryConfig](-retry-config/index.html)(val maxAttempts: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = DEFAULT_MAX_ATTEMPTS, val initialDelay: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) = DEFAULT_INITIAL_DELAY, val maxDelay: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) = DEFAULT_MAX_DELAY, val backoffFactor: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html) = DEFAULT_BACKOFF_FACTOR, val jitter: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html) = DEFAULT_JITTER, val exceptions: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null)

How a node is retried when it raises.

[Route](-route/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [RouteSerializer::class](../../google-adk-kotlin-core/com.google.adk.kt.workflow/-route-serializer/index.html))

sealed interface [Route](-route/index.html)

A value on a workflow edge, and the value a node emits to select which of its outgoing edges are followed. An edge fires when the value it carries matches one the node emitted.

[RouteMapBuilder](-route-map-builder/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [RouteMapBuilder](-route-map-builder/index.html)

The receiver of an [EdgesBuilder.route](-edges-builder/route.html) block, which maps each route the source node may emit to a target node, written `on("billing") then billing` or `"billing" then billing`. Mapping one route to several nodes fans out on that route.

[RouteMapEntry](-route-map-entry/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [RouteMapEntry](-route-map-entry/index.html)

A routing-map entry started by [RouteMapBuilder.on](-route-map-builder/on.html) whose routes have no target yet. [then](-route-map-entry/then.html) completes it.

[RouteSet](-route-set/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [RouteSet](-route-set/index.html)

Routes that select a single edge, which fires once when its source emits any of them. Separate edges to the same target would fire once each. Build one with `anyOf(...)` in the workflow DSL.

[Start](-start/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

object [Start](-start/index.html) : [Node](-node/index.html)

Marks where a graph starts. Never runs: the scheduler seeds its successors directly.

[Workflow](-workflow/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [Workflow](-workflow/index.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val edges: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Edge](-edge/index.html)> = emptyList(), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val maxConcurrency: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, rerunOnResume: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = true, waitForOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, config: [NodeConfig](-node-config/index.html) = NodeConfig(), inputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, outputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, stateSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null) : [BaseNode](-base-node/index.html)

A graph of nodes, and a [Node](-node/index.html) itself, so graphs nest: a workflow drops into another workflow wherever an ordinary node goes.

[WorkflowConfigurationException](-workflow-configuration-exception/index.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [WorkflowConfigurationException](-workflow-configuration-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : [IllegalArgumentException](https://developer.android.com/reference/kotlin/java/lang/IllegalArgumentException.html)

Thrown when a workflow or node configuration is invalid.

## Functions

[asNode](as-node.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

fun [BaseTool](../com.google.adk.kt.tools/-base-tool/index.html).[asNode](as-node.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = this.name, config: [NodeConfig](-node-config/index.html) = NodeConfig()): [Node](-node/index.html)

Returns a workflow node that runs this tool as a fixed step: the predecessor's output becomes the tool's arguments, and the tool's result becomes the node's output.

[edges](edges.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

fun [edges](edges.html)(block: [EdgesDslBlock](-edges-dsl-block/index.html)<[EdgesBuilder](-edges-builder/index.html)>): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Edge](-edge/index.html)>

Returns the edges declared by [block](edges.html) for a [Workflow](-workflow/index.html); [workflow](workflow.html) builds both in one step.

[node](node.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

inline fun <[I](node.html), [O](node.html)> [node](node.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", rerunOnResume: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, waitForOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, config: [NodeConfig](-node-config/index.html) = NodeConfig(), inputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, outputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, stateSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, crossinline block: suspend [FlowCollector](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow-collector/index.html)<[Event](../com.google.adk.kt.events/-event/index.html)>.(context: [Context](../com.google.adk.kt.agents/-context/index.html), input: [I](node.html)) -> [O](node.html)): [FunctionNode](-function-node/index.html)<[I](node.html), [O](node.html)>

Creates a [FunctionNode](-function-node/index.html) that runs [block](node.html) on an input of type [I](node.html) and returns an output of type [O](node.html), emitting progress [Event](../com.google.adk.kt.events/-event/index.html)s through its [FlowCollector](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow-collector/index.html) receiver. Schemas inferred from [I](node.html) and [O](node.html) describe the node, while an explicit [inputSchema](node.html) or [outputSchema](node.html) is also enforced on every run.

[parallelNode](parallel-node.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

inline fun <[I](parallel-node.html), [O](parallel-node.html)> [parallelNode](parallel-node.html)(node: [FunctionNode](-function-node/index.html)<[I](parallel-node.html), [O](parallel-node.html)>, maxParallelWorkers: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null): [FunctionNode](-function-node/index.html)<[List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[I](parallel-node.html)>, [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[O](parallel-node.html)>>

Wraps [node](parallel-node.html) so it runs concurrently on each item of a list input and returns the results in input order. [node](parallel-node.html)'s configuration applies to each item's run.

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

inline fun <[I](parallel-node.html), [O](parallel-node.html)> [parallelNode](parallel-node.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", rerunOnResume: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, waitForOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, maxParallelWorkers: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, config: [NodeConfig](-node-config/index.html) = NodeConfig(), inputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, outputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, stateSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, crossinline block: suspend [FlowCollector](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow-collector/index.html)<[Event](../com.google.adk.kt.events/-event/index.html)>.(context: [Context](../com.google.adk.kt.agents/-context/index.html), input: [I](parallel-node.html)) -> [O](parallel-node.html)): [FunctionNode](-function-node/index.html)<[List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[I](parallel-node.html)>, [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[O](parallel-node.html)>>

Creates a [FunctionNode](-function-node/index.html) that runs [block](parallel-node.html) concurrently on each item of a list input and returns the results as a [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html) of [O](parallel-node.html) in input order. A non-list input runs as one item.

[workflow](workflow.html)

Link copied to clipboard

common

@[ExperimentalWorkflowApi](../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

fun [workflow](workflow.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", maxConcurrency: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, rerunOnResume: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = true, waitForOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, config: [NodeConfig](-node-config/index.html) = NodeConfig(), inputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, outputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, stateSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, block: [EdgesDslBlock](-edges-dsl-block/index.html)<[EdgesBuilder](-edges-builder/index.html)>): [Workflow](-workflow/index.html)

Builds a [Workflow](-workflow/index.html) from the edges [block](workflow.html) declares.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
