[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/ContextCacheConfig

# ContextCacheConfig

common

data class [ContextCacheConfig](index.html) @[ExperimentalContextCachingFeature](../../com.google.adk.kt.annotations/-experimental-context-caching-feature/index.html) constructor(val cacheIntervals: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 10, val ttl: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) = 1800.seconds, val minTokens: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 0, val createHttpOptions: [HttpOptions](../../com.google.adk.kt.types/-http-options/index.html)? = null)

Configuration for context caching across all agents in an app.

When this config is present on an app, context caching is enabled for all agents. When absent (`null`), context caching is disabled.

Context caching can significantly reduce costs and improve response times by reusing previously processed context across multiple requests.

Constructing this type requires `@OptIn(ExperimentalContextCachingFeature::class)`.

Members

## Constructors

[ContextCacheConfig](-context-cache-config.html)

Link copied to clipboard

common

@[ExperimentalContextCachingFeature](../../com.google.adk.kt.annotations/-experimental-context-caching-feature/index.html)

constructor(cacheIntervals: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 10, ttl: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) = 1800.seconds, minTokens: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 0, createHttpOptions: [HttpOptions](../../com.google.adk.kt.types/-http-options/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

@[ExperimentalContextCachingFeature](../../com.google.adk.kt.annotations/-experimental-context-caching-feature/index.html)

class [Builder](-builder/index.html)

Fluent builder for [ContextCacheConfig](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[cacheIntervals](cache-intervals.html)

Link copied to clipboard

common

val [cacheIntervals](cache-intervals.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

Maximum number of invocations to reuse the same cache before refreshing it. Must be in the range `1..100`. Defaults to 10.

[createHttpOptions](create-http-options.html)

Link copied to clipboard

common

val [createHttpOptions](create-http-options.html): [HttpOptions](../../com.google.adk.kt.types/-http-options/index.html)?

Optional HTTP options for the cache-creation call. Set this to add a timeout on `CachedContent.create()` calls (e.g. `HttpOptions(timeout = 10.seconds)`). When the cache creation call exceeds the timeout, it fails and the request proceeds without caching. `null` uses the model backend's default HTTP options.

[minTokens](min-tokens.html)

Link copied to clipboard

common

val [minTokens](min-tokens.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

Minimum prior-request tokens required to enable caching. This gates on the previous request's actual prompt token count (from the model's usage metadata), not an estimate of the current request. Gemini enforces a hard 4096-token minimum that always applies, so values below 4096 have no additional effect. No cache is created on the first request of a session; caching begins on the second turn once a previous token count is known. Context cache storage may have a cost, so set this higher to avoid caching small requests where the overhead may exceed the benefits. Must be non-negative. Defaults to 0.

[ttl](ttl.html)

Link copied to clipboard

common

val [ttl](ttl.html): [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)

Time-to-live for the cache. Must be strictly positive. Defaults to 30 minutes.

[ttlString](ttl-string.html)

Link copied to clipboard

common

val [ttlString](ttl-string.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Returns the TTL in the string format used for cache creation, e.g. `"1800s"`.

## Functions

[toBuilder](to-builder.html)

Link copied to clipboard

common

@[ExperimentalContextCachingFeature](../../com.google.adk.kt.annotations/-experimental-context-caching-feature/index.html)

fun [toBuilder](to-builder.html)(): [ContextCacheConfig.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
