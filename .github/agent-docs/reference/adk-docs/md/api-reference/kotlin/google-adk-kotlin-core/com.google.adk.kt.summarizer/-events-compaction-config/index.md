[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.summarizer](../index.html)/EventsCompactionConfig

# EventsCompactionConfig

common

data class [EventsCompactionConfig](index.html)(val compactionInterval: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val overlapSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val summarizer: [EventSummarizer](../-event-summarizer/index.html)? = null, val tokenThreshold: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val eventRetentionSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null)

Configuration for event compaction.

Members

## Constructors

[EventsCompactionConfig](-events-compaction-config.html)

Link copied to clipboard

common

constructor(compactionInterval: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, overlapSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, summarizer: [EventSummarizer](../-event-summarizer/index.html)? = null, tokenThreshold: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, eventRetentionSize: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [EventsCompactionConfig](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[compactionInterval](compaction-interval.html)

Link copied to clipboard

common

val [compactionInterval](compaction-interval.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)?

The number of _new_ user-initiated invocations that, once fully represented in the session's events, will trigger a sliding-window compaction. Must be strictly positive when set.

[eventRetentionSize](event-retention-size.html)

Link copied to clipboard

common

val [eventRetentionSize](event-retention-size.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)?

The number of most recent events kept raw (un-compacted) when token-threshold compaction fires; the older events are summarized into a single event. Must be non-negative when set, and must be set together with [tokenThreshold](../../../google-adk-kotlin-core/com.google.adk.kt.summarizer/-events-compaction-config/--root--.html).

[overlapSize](overlap-size.html)

Link copied to clipboard

common

val [overlapSize](overlap-size.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)?

The number of preceding invocations to include from the end of the last compacted range when forming the next sliding-window compaction window. Creates an overlap between consecutive summaries for context continuity. Must be non-negative when set.

[summarizer](summarizer.html)

Link copied to clipboard

common

val [summarizer](summarizer.html): [EventSummarizer](../-event-summarizer/index.html)?

The [EventSummarizer](../-event-summarizer/index.html) used to produce the compaction summary. When `null`, the runner defaults it to an [LlmEventSummarizer](../-llm-event-summarizer/index.html) backed by the root agent's model, requiring the root to be an `LlmAgent` (otherwise it throws at construction).

[tokenThreshold](token-threshold.html)

Link copied to clipboard

common

val [tokenThreshold](token-threshold.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)?

The most recent prompt token count that triggers intra-invocation token-threshold (tail-retention) compaction before an LLM call. Must be strictly positive when set, and must be set together with [eventRetentionSize](../../../google-adk-kotlin-core/com.google.adk.kt.summarizer/-events-compaction-config/--root--.html).

## Functions

[hasSlidingWindowConfig](has-sliding-window-config.html)

Link copied to clipboard

common

fun [hasSlidingWindowConfig](has-sliding-window-config.html)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Returns true when sliding-window compaction is fully configured.

[hasTokenThresholdConfig](has-token-threshold-config.html)

Link copied to clipboard

common

fun [hasTokenThresholdConfig](has-token-threshold-config.html)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Returns true when token-threshold compaction is fully configured.

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [EventsCompactionConfig.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
