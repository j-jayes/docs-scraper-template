[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.5.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.workflow](../index.html)/NodeInfo

# NodeInfo

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [NodeInfo](index.html)(val path: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val outputFor: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val messageAsOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Identifies the workflow-node activation that emitted an [com.google.adk.kt.events.Event](../../com.google.adk.kt.events/-event/index.html); `null` outside a workflow.

Members

## Constructors

[NodeInfo](-node-info.html)

Link copied to clipboard

common

constructor(path: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", outputFor: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, messageAsOutput: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [NodeInfo](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[messageAsOutput](message-as-output.html)

Link copied to clipboard

common

val [messageAsOutput](message-as-output.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

When true this event's content _is_ the node's output, so no separate output event follows.

[name](name.html)

Link copied to clipboard

common

val [name](name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The emitting node's name: the last segment of [path](../../../google-adk-kotlin-core/com.google.adk.kt.workflow/-node-info/--root--.html) without its run ID, such as `a` for `wf@1/a@2`, or null when [path](../../../google-adk-kotlin-core/com.google.adk.kt.workflow/-node-info/--root--.html) is empty. Mirrors ADK Python's `NodeInfo.name`, which returns an empty string instead of null.

[outputFor](output-for.html)

Link copied to clipboard

common

val [outputFor](output-for.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?

The node paths this event's output counts for within its invocation: the emitter's own path, then each ancestor linked to it by `useAsOutput` (a `runNode` caller, or the workflow of a terminal node). Set on an event carrying the node's output, in `output` or as message-as-output content.

[parentRunId](parent-run-id.html)

Link copied to clipboard

common

val [parentRunId](parent-run-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The run ID of the emitting node's parent: the part of [path](../../../google-adk-kotlin-core/com.google.adk.kt.workflow/-node-info/--root--.html)'s second-to-last segment after `@`, such as `1` for `wf@1/a@2`. Returns null when [path](../../../google-adk-kotlin-core/com.google.adk.kt.workflow/-node-info/--root--.html) has no parent segment or the segment has no run ID. Mirrors ADK Python's `NodeInfo.parent_run_id`.

[path](path.html)

Link copied to clipboard

common

val [path](path.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The emitting node's path. Segments are `/`-separated and each is `name@runId`, so a node of workflow `wf` reads `wf@1/a@1`. An empty path denotes the workflow's top-level node.

[runId](run-id.html)

Link copied to clipboard

common

val [runId](run-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The emitting node's run ID: the part of [path](../../../google-adk-kotlin-core/com.google.adk.kt.workflow/-node-info/--root--.html)'s last segment after `@`, such as `2` for `wf@1/a@2`, or null when the segment has none. Mirrors ADK Python's `NodeInfo.run_id`, which returns an empty string instead of null.

## Functions

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [NodeInfo.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
