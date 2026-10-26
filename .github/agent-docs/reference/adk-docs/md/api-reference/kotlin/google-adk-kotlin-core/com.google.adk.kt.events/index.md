[ google-adk-kotlin ](../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../index.html)/com.google.adk.kt.events

# Package-level declarations

Types

## Types

[Event](-event/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Event](-event/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val id: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = Uuid.random(), val invocationId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val author: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val content: [Content](../com.google.adk.kt.types/-content/index.html)? = null, val actions: [EventActions](-event-actions/index.html) = EventActions(), val longRunningToolIds: [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)> = emptySet(), val partial: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val turnComplete: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val errorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val errorMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val finishReason: [FinishReason](../com.google.adk.kt.types/-finish-reason/index.html)? = null, val usageMetadata: [UsageMetadata](../com.google.adk.kt.types/-usage-metadata/index.html)? = null, val avgLogProbs: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, val interrupted: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val branch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val groundingMetadata: [GroundingMetadata](../com.google.adk.kt.types/-grounding-metadata/index.html)? = null, val modelVersion: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](../com.google.adk.kt.types/-citation-metadata/index.html)? = null, val cacheMetadata: [CacheMetadata](../com.google.adk.kt.models/-cache-metadata/index.html)? = null, val customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null, val output: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, val nodeInfo: [NodeInfo](../com.google.adk.kt.workflow/-node-info/index.html)? = null, val timestamp: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html) = Clock.System.now().toEpochMilliseconds(), val turnCompleteReason: [TurnCompleteReason](../com.google.adk.kt.types/-turn-complete-reason/index.html)? = null, val interactionStatus: [InteractionStatus](../com.google.adk.kt.types/-interaction-status/index.html)? = null, val inputTranscription: [Transcription](../com.google.adk.kt.types/-transcription/index.html)? = null, val outputTranscription: [Transcription](../com.google.adk.kt.types/-transcription/index.html)? = null, val liveSessionId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val liveSessionResumptionUpdate: [LiveServerSessionResumptionUpdate](../com.google.adk.kt.types/-live-server-session-resumption-update/index.html)? = null, val voiceActivity: [VoiceActivity](../com.google.adk.kt.types/-voice-activity/index.html)? = null)

Represents an event in a session.

[EventActions](-event-actions/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [EventActions](-event-actions/index.html)(var skipSummarization: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val stateDelta: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = concurrentMutableMapOf(), val artifactDelta: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)> = concurrentMutableMapOf(), var transferToAgent: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, var escalate: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, var endOfAgent: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val requestedToolConfirmations: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [ToolConfirmation](-tool-confirmation/index.html)> = concurrentMutableMapOf(), var rewindBeforeInvocationId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, var route: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Route](../com.google.adk.kt.workflow/-route/index.html)>? = null, var agentState: [TypedData](../com.google.adk.kt.agents/-typed-data/index.html)? = null, var compaction: [EventCompaction](-event-compaction/index.html)? = null)

Represents the actions attached to an event.

[EventCompaction](-event-compaction/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [EventCompaction](-event-compaction/index.html)(val startTimestamp: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html), val endTimestamp: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html), val compactedContent: [Content](../com.google.adk.kt.types/-content/index.html))

A record that a continuous range of session [Event](-event/index.html)s has been replaced by a single piece of [compactedContent](../../google-adk-kotlin-core/com.google.adk.kt.events/-event-compaction/--root--.html) (typically a model-generated summary).

[ToolConfirmation](-tool-confirmation/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [ToolConfirmation](-tool-confirmation/index.html)(val confirmed: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html), val payload: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, val hint: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Represents a tool confirmation configuration.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
