toggle menu

[ google-adk-kotlin ](../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../index.html)/com.google.adk.kt.events

# Package-level declarations

Types

## Types

[Event](-event/index.html)

Link copied to clipboard

@Serializable

data class [Event](-event/index.html)(val id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = Uuid.random(), val invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val author: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val content: [Content](../com.google.adk.kt.types/-content/index.html)? = null, val actions: [EventActions](-event-actions/index.html) = EventActions(), val longRunningToolIds: [Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)> = emptySet(), val partial: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val turnComplete: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val errorCode: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val errorMessage: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val finishReason: [FinishReason](../com.google.adk.kt.types/-finish-reason/index.html)? = null, val usageMetadata: [UsageMetadata](../com.google.adk.kt.types/-usage-metadata/index.html)? = null, val avgLogProbs: [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html)? = null, val interrupted: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val branch: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val groundingMetadata: [GroundingMetadata](../com.google.adk.kt.types/-grounding-metadata/index.html)? = null, val modelVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](../com.google.adk.kt.types/-citation-metadata/index.html)? = null, val customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>? = null, val timestamp: [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-long/index.html) = Clock.System.now().toEpochMilliseconds())

Represents an event in a session.

[EventActions](-event-actions/index.html)

Link copied to clipboard

@Serializable

data class [EventActions](-event-actions/index.html)(var skipSummarization: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val stateDelta: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)> = concurrentMutableMapOf(), val artifactDelta: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)> = concurrentMutableMapOf(), var transferToAgent: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, var escalate: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, var endOfAgent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val requestedToolConfirmations: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [ToolConfirmation](-tool-confirmation/index.html)> = concurrentMutableMapOf(), var rewindBeforeInvocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, var agentState: [TypedData](../com.google.adk.kt.agents/-typed-data/index.html)? = null, var compaction: [EventCompaction](-event-compaction/index.html)? = null)

Represents the actions attached to an event.

[EventCompaction](-event-compaction/index.html)

Link copied to clipboard

@Serializable

data class [EventCompaction](-event-compaction/index.html)(val startTimestamp: [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-long/index.html), val endTimestamp: [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-long/index.html), val compactedContent: [Content](../com.google.adk.kt.types/-content/index.html))

A record that a continuous range of session [Event](-event/index.html)s has been replaced by a single piece of [compactedContent](-event-compaction/compacted-content.html) (typically a model-generated summary).

[ToolConfirmation](-tool-confirmation/index.html)

Link copied to clipboard

@Serializable

data class [ToolConfirmation](-tool-confirmation/index.html)(val confirmed: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html), val payload: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)? = null, val hint: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null)

Represents a tool confirmation configuration.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
