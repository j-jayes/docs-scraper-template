[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.sessions](../index.html)/State

# State

common

class [State](index.html)(initialState: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap(), initialDelta: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap()) : [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

A thread-safe state map that maintains the current value and tracks modifications.

This class implements [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html) to provide a read-only view of the state, while exposing specific mutation methods ([set](set.html), [putAll](put-all.html)).

Members

## Constructors

[State](-state.html)

Link copied to clipboard

common

constructor(initialState: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap(), initialDelta: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap())

## Types

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[entries](entries.html)

Link copied to clipboard

common

open override val [entries](entries.html): [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html)<[Map.Entry](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/-entry/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>>

[hasDelta](has-delta.html)

Link copied to clipboard

common

val [hasDelta](has-delta.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether the state has pending delta.

[keys](keys.html)

Link copied to clipboard

common

open override val [keys](keys.html): [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>

[size](size.html)

Link copied to clipboard

common

open override val [size](size.html): [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)

[values](values.html)

Link copied to clipboard

common

open override val [values](values.html): [Collection](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-collection/index.html)<[Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

## Functions

[applyDelta](apply-delta.html)

Link copied to clipboard

common

fun [applyDelta](apply-delta.html)(delta: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>)

Applies the non-`temp:` entries of [delta](apply-delta.html) to the state, tracking them in the delta map.

[applyTempDelta](apply-temp-delta.html)

Link copied to clipboard

common

fun [applyTempDelta](apply-temp-delta.html)(delta: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>)

Applies only the `temp:`-prefixed entries of [delta](apply-temp-delta.html) to the state, tracking them in the delta map; the complement of [applyDelta](apply-delta.html).

[clear](clear.html)

Link copied to clipboard

common

fun [clear](clear.html)()

Clears the state and delta maps.

[containsKey](contains-key.html)

Link copied to clipboard

common

open override fun [containsKey](contains-key.html)(key: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

[containsValue](contains-value.html)

Link copied to clipboard

common

open override fun [containsValue](contains-value.html)(value: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

[get](get.html)

Link copied to clipboard

common

open operator override fun [get](get.html)(key: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

[isEmpty](is-empty.html)

Link copied to clipboard

common

open override fun [isEmpty](is-empty.html)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

[putAll](put-all.html)

Link copied to clipboard

common

fun [putAll](put-all.html)(from: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<out [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>)

Updates the state with all entries from the given map.

[remove](remove.html)

Link copied to clipboard

common

fun [remove](remove.html)(key: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

[set](set.html)

Link copied to clipboard

common

operator fun [set](set.html)(key: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), value: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

Sets the value for the given key.

[toString](to-string.html)

Link copied to clipboard

common

open override fun [toString](to-string.html)(): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
