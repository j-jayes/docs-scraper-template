[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.workflow](../index.html)/RetryConfig

# RetryConfig

common

@[ExperimentalWorkflowApi](../../com.google.adk.kt.annotations/-experimental-workflow-api/index.html)

data class [RetryConfig](index.html)(val maxAttempts: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = DEFAULT_MAX_ATTEMPTS, val initialDelay: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) = DEFAULT_INITIAL_DELAY, val maxDelay: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) = DEFAULT_MAX_DELAY, val backoffFactor: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html) = DEFAULT_BACKOFF_FACTOR, val jitter: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html) = DEFAULT_JITTER, val exceptions: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null)

How a node is retried when it raises.

Members

## Constructors

[RetryConfig](-retry-config.html)

Link copied to clipboard

common

constructor(maxAttempts: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = DEFAULT_MAX_ATTEMPTS, initialDelay: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) = DEFAULT_INITIAL_DELAY, maxDelay: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) = DEFAULT_MAX_DELAY, backoffFactor: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html) = DEFAULT_BACKOFF_FACTOR, jitter: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html) = DEFAULT_JITTER, exceptions: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [RetryConfig](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[backoffFactor](backoff-factor.html)

Link copied to clipboard

common

val [backoffFactor](backoff-factor.html): [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)

Multiplier applied to the delay after each attempt.

[exceptions](exceptions.html)

Link copied to clipboard

common

val [exceptions](exceptions.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?

Reported type names to retry on, matched exactly with no subclass match. The reported name is the failure's own simple name, or for a [NodeExecutionException](../-node-execution-exception/index.html) the wrapped failure's type name -- so list e.g. "RuntimeError", not "NodeExecutionException". Null retries any failure; an empty list retries none.

[initialDelay](initial-delay.html)

Link copied to clipboard

common

val [initialDelay](initial-delay.html): [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)

Delay before the first retry.

[jitter](jitter.html)

Link copied to clipboard

common

val [jitter](jitter.html): [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)

Randomness factor, not a duration: the delay is spread over `delay * (1 +/- jitter)`. Zero removes randomness.

[maxAttempts](max-attempts.html)

Link copied to clipboard

common

val [maxAttempts](max-attempts.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

Attempts including the first, so 0 or 1 means no retry.

[maxDelay](max-delay.html)

Link copied to clipboard

common

val [maxDelay](max-delay.html): [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)

Ceiling on any single delay.

## Functions

[initialDelayMillis](initial-delay-millis.html)

Link copied to clipboard

common

fun [initialDelayMillis](initial-delay-millis.html)(): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)

Returns [initialDelay](../../../google-adk-kotlin-core/com.google.adk.kt.workflow/-retry-config/--root--.html) in whole milliseconds. Java cannot read it (mangled).

[maxDelayMillis](max-delay-millis.html)

Link copied to clipboard

common

fun [maxDelayMillis](max-delay-millis.html)(): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)

Returns [maxDelay](../../../google-adk-kotlin-core/com.google.adk.kt.workflow/-retry-config/--root--.html) in whole milliseconds. Java cannot read it (mangled).

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [RetryConfig.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
