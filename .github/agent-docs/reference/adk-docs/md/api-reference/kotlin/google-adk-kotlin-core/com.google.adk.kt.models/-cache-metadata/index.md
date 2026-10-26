[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.models](../index.html)/CacheMetadata

# CacheMetadata

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [CacheMetadata](index.html)(val fingerprint: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val contentsCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), val cacheName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val expireTime: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val invocationsUsed: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val createdAt: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null)

Metadata for the context cache associated with LLM responses.

This stores cache identification, usage tracking, and lifecycle information for a particular cache instance. It can be in one of two states:

  1. **Active cache state:** [cacheName](../../../google-adk-kotlin-core/com.google.adk.kt.models/-cache-metadata/--root--.html) is set and [expireTime](../../../google-adk-kotlin-core/com.google.adk.kt.models/-cache-metadata/--root--.html), [invocationsUsed](../../../google-adk-kotlin-core/com.google.adk.kt.models/-cache-metadata/--root--.html), and [createdAt](../../../google-adk-kotlin-core/com.google.adk.kt.models/-cache-metadata/--root--.html) are populated.

  2. **Fingerprint-only state:** [cacheName](../../../google-adk-kotlin-core/com.google.adk.kt.models/-cache-metadata/--root--.html) is `null` and only [fingerprint](../../../google-adk-kotlin-core/com.google.adk.kt.models/-cache-metadata/--root--.html) and [contentsCount](../../../google-adk-kotlin-core/com.google.adk.kt.models/-cache-metadata/--root--.html) are set, used for prefix matching before a cache exists.




Token counts (cached and total) are available in [LlmResponse.usageMetadata](../-llm-response/usage-metadata.html) and should be accessed from there to avoid duplication.

Members

## Constructors

[CacheMetadata](-cache-metadata.html)

Link copied to clipboard

common

constructor(fingerprint: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), contentsCount: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html), cacheName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, expireTime: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, invocationsUsed: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, createdAt: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [CacheMetadata](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[cacheName](cache-name.html)

Link copied to clipboard

common

val [cacheName](cache-name.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

Full resource name of the cached content (e.g. `projects/123/locations/us-central1/cachedContents/456`). `null` when no active cache exists.

[contentsCount](contents-count.html)

Link copied to clipboard

common

val [contentsCount](contents-count.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

Number of contents. When an active cache exists this is the count of cached contents; otherwise it is the count of the cacheable content prefix used for fingerprinting. Must be non-negative.

[createdAt](created-at.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [LenientEpochMillisSerializer::class](../../../google-adk-kotlin-core/com.google.adk.kt.serialization/-lenient-epoch-millis-serializer/index.html))

val [createdAt](created-at.html): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?

Epoch milliseconds when the cache was created. `null` when no active cache exists. Also reads ADK Python's fractional epoch seconds.

[expireSoon](expire-soon.html)

Link copied to clipboard

common

val [expireSoon](expire-soon.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether the cache will expire within [EXPIRY_BUFFER](../../../google-adk-kotlin-core/com.google.adk.kt.models/-cache-metadata/-companion/-e-x-p-i-r-y_-b-u-f-f-e-r.html). Always `false` for fingerprint-only metadata (which has no [expireTime](../../../google-adk-kotlin-core/com.google.adk.kt.models/-cache-metadata/--root--.html)).

[expireTime](expire-time.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [LenientEpochMillisSerializer::class](../../../google-adk-kotlin-core/com.google.adk.kt.serialization/-lenient-epoch-millis-serializer/index.html))

val [expireTime](expire-time.html): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?

Epoch milliseconds when the cache expires. `null` when no active cache exists. Also reads ADK Python's fractional epoch seconds.

[fingerprint](fingerprint.html)

Link copied to clipboard

common

val [fingerprint](fingerprint.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Hash of the cacheable contents (system instruction + tools + contents). Always present for prefix matching.

[invocationsUsed](invocations-used.html)

Link copied to clipboard

common

val [invocationsUsed](invocations-used.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)?

Number of invocations this cache has been used for. `null` when no active cache exists. Must be non-negative when set.

[isActive](is-active.html)

Link copied to clipboard

common

val [isActive](is-active.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether this metadata refers to an active cache, as opposed to a fingerprint-only state.

## Functions

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [CacheMetadata.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

[toString](to-string.html)

Link copied to clipboard

common

open override fun [toString](to-string.html)(): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
