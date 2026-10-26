[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.workflow](../index.html)/EdgesBuilder

# EdgesBuilder

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

class [EdgesBuilder](index.html)

The receiver that collects the edges declared in an [edges](../edges.html) or [workflow](../workflow.html) block. A node is identified by its instance, so create each node once and reuse it. To add a tool as a step, convert it once with [asNode](../as-node.html) and reuse that node.

Members

## Functions

[anyOf](any-of.html)

Link copied to clipboard

common

fun [anyOf](any-of.html)(first: [Route](../-route/index.html), second: [Route](../-route/index.html), vararg rest: [Route](../-route/index.html)): [RouteSet](../-route-set/index.html)

Groups routes for [on](on.html), so one edge fires on any of them.

fun [anyOf](any-of.html)(first: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), second: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), vararg rest: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): [RouteSet](../-route-set/index.html)

Groups number routes for [on](on.html), so one edge fires on any of them.

fun [anyOf](any-of.html)(first: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), second: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), vararg rest: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [RouteSet](../-route-set/index.html)

Groups string routes for [on](on.html), so one edge fires on any of them.

[chain](chain.html)

Link copied to clipboard

common

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

fun [chain](chain.html)(first: [Node](../-node/index.html), second: [Node](../-node/index.html), vararg rest: [Node](../-node/index.html)): [Node](../-node/index.html)

Connects [first](chain.html), [second](chain.html), and each node in [rest](chain.html) in order by adding an edge from each node to the next. Returns the last node so the chain can continue from it: `chain(Start, a, b)` is short for `Start.then(a).then(b)`.

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

fun [Node](../-node/index.html).[chain](chain.html)(first: [Node](../-node/index.html), second: [Node](../-node/index.html), vararg rest: [Node](../-node/index.html)): [Node](../-node/index.html)

Connects this node to [first](chain.html), [second](chain.html), and each node in [rest](chain.html) in order by adding an edge from each node to the next, and returns the last node. `a.chain(b, c)` is short for `a.then(b).then(c)`. Unlike the `chain` overload that takes the first node as an argument, this form can continue a fluent chain, such as after [joinTo](join-to.html).

[from](from.html)

Link copied to clipboard

common

fun [from](from.html)(node: [Node](../-node/index.html)): [EdgeChain](../-edge-chain/index.html)

Starts a chain of edges at [node](from.html) for Java callers. Its calls add the same edges as the Kotlin calls of the same names: `g.from(a).then(b).then(c)`.

fun [from](from.html)(group: [NodeGroup](../-node-group/index.html)): [NodeGroupChain](../-node-group-chain/index.html)

Starts a chain of edges at [group](from.html) (such as one built with [nodes](nodes.html)) for Java callers so the group can join without a fan-out.

fun [from](from.html)(nodes: [Collection](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html)<[Node](../-node/index.html)>): [NodeGroupChain](../-node-group-chain/index.html)

Starts a chain of edges at [nodes](from.html) (such as a computed list) for Java callers so the nodes can join without a fan-out. For a fixed set of nodes, the `g.from(a, b)` overload is shorter.

fun [from](from.html)(first: [Node](../-node/index.html), second: [Node](../-node/index.html), vararg rest: [Node](../-node/index.html)): [NodeGroupChain](../-node-group-chain/index.html)

Starts a chain of edges at [first](from.html), [second](from.html), and each node in [rest](from.html) for Java callers so they can join without a fan-out: `g.from(a, b).joinTo(join)`.

[fromStart](from-start.html)

Link copied to clipboard

common

fun [fromStart](from-start.html)(): [EdgeChain](../-edge-chain/index.html)

Starts a chain of edges at [Start](../-start/index.html) for Java callers: `g.fromStart().then(a)` instead of `g.from(Start.INSTANCE).then(a)`.

[joinFrom](join-from.html)

Link copied to clipboard

common

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

fun [JoinNode](../-join-node/index.html).[joinFrom](join-from.html)(first: [Node](../-node/index.html), vararg rest: [Node](../-node/index.html)): [Node](../-node/index.html)

Fans in: connects [first](join-from.html) and each of [rest](join-from.html) to this join, which runs once all of them complete. Returns the join, so a chain continues from it.

[joinTo](join-to.html)

Link copied to clipboard

common

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

infix fun [NodeGroup](../-node-group/index.html).[joinTo](join-to.html)(join: [JoinNode](../-join-node/index.html)): [Node](../-node/index.html)

Fans in by connecting each node of this group to [join](join-to.html), which runs once all of them complete. Returns [join](join-to.html) so the chain continues from it: `a.then(b, c).joinTo(join).then(d)`.

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

infix fun [Collection](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html)<[Node](../-node/index.html)>.[joinTo](join-to.html)(join: [JoinNode](../-join-node/index.html)): [Node](../-node/index.html)

Fans in by connecting each node in this collection, such as a computed list, to [join](join-to.html), like `nodes(...).joinTo(join)`. Returns [join](join-to.html) so the chain continues from it. An empty collection adds no edges.

[nodes](nodes.html)

Link copied to clipboard

common

fun [nodes](nodes.html)(vararg nodes: [Node](../-node/index.html)): [NodeGroup](../-node-group/index.html)

Groups [nodes](nodes.html) without connecting them, as in `a then nodes(b, c)` for an infix fan-out or `nodes(b, c).joinTo(join)` for a join. Prefer this over `listOf(b, c)` for fan-outs and joins because `listOf` infers the nodes' closest common supertype. For some built-in nodes of different types, such as a [Workflow](../-workflow/index.html) and a [JoinNode](../-join-node/index.html), that supertype is the framework-internal `BaseNode`, so the call fails to compile.

[on](on.html)

Link copied to clipboard

common

infix fun [Node](../-node/index.html).[on](on.html)(route: [Route](../-route/index.html)): [PendingEdge](../-pending-edge/index.html)

Starts an edge that fires when this node emits [route](on.html); [then](then.html) completes it.

infix fun [Node](../-node/index.html).[on](on.html)(routes: [RouteSet](../-route-set/index.html)): [PendingEdge](../-pending-edge/index.html)

Starts one edge that fires once when this node emits any of [routes](on.html) (built with [anyOf](any-of.html)); [then](then.html) completes it.

infix fun [Node](../-node/index.html).[on](on.html)(route: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)): [PendingEdge](../-pending-edge/index.html)

Starts an edge that fires when this node emits [route](on.html) as a [Route.Flag](../-route/-flag/index.html); [then](then.html) completes it.

infix fun [Node](../-node/index.html).[on](on.html)(route: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)): [PendingEdge](../-pending-edge/index.html)

Starts an edge that fires when this node emits [route](on.html) as a [Route.Num](../-route/-num/index.html); [then](then.html) completes it.

infix fun [Node](../-node/index.html).[on](on.html)(route: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [PendingEdge](../-pending-edge/index.html)

Starts an edge that fires when this node emits [route](on.html) as a [Route.Tag](../-route/-tag/index.html); [then](then.html) completes it.

[route](route.html)

Link copied to clipboard

common

infix fun [Node](../-node/index.html).[route](route.html)(block: [EdgesDslBlock](../-edges-dsl-block/index.html)<[RouteMapBuilder](../-route-map-builder/index.html)>)

Adds this node's routing map, with an edge for each route [block](route.html) maps to a node. A routing map ends the statement; connect its targets onward in separate statements. An empty map throws [IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html), and an entry not completed with `then` throws [IllegalStateException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-state-exception/index.html).

[then](then.html)

Link copied to clipboard

common

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

infix fun [Node](../-node/index.html).[then](then.html)(node: [Node](../-node/index.html)): [Node](../-node/index.html)

Connects this node to [node](then.html) and returns [node](then.html), so a chain continues from it.

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

infix fun [Node](../-node/index.html).[then](then.html)(targets: [NodeGroup](../-node-group/index.html)): [NodeGroup](../-node-group/index.html)

Fans out to each node in [targets](then.html) so they run concurrently, as in `a then nodes(b, c)`. Returns [targets](then.html), which [joinTo](join-to.html) connects to a [JoinNode](../-join-node/index.html) to continue once they all complete.

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

infix fun [Node](../-node/index.html).[then](then.html)(targets: [Collection](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html)<[Node](../-node/index.html)>): [NodeGroup](../-node-group/index.html)

Fans out by connecting this node to each of [targets](then.html), such as a computed list, and returns them as a [NodeGroup](../-node-group/index.html), like `then(nodes(...))`. An empty collection adds no edges.

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

infix fun [PendingEdge](../-pending-edge/index.html).[then](then.html)(node: [Node](../-node/index.html)): [Node](../-node/index.html)

Completes this routed edge at [node](then.html) and returns [node](then.html), so a chain continues from it.

@[CanIgnoreReturnValue](https://javadoc.io/doc/com.google.errorprone/error_prone_annotations/latest/com/google/errorprone/annotations/CanIgnoreReturnValue.html)

fun [Node](../-node/index.html).[then](then.html)(first: [Node](../-node/index.html), second: [Node](../-node/index.html), vararg rest: [Node](../-node/index.html)): [NodeGroup](../-node-group/index.html)

Fans out by connecting this node to [first](then.html), [second](then.html), and each node in [rest](then.html) so they run concurrently, as in `a.then(b, c)`. Returns them as a [NodeGroup](../-node-group/index.html) for [joinTo](join-to.html). Infix chains still need `a then nodes(b, c)` because an infix call takes one argument.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
