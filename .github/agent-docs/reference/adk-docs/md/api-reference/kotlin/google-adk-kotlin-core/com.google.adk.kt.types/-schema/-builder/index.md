[ google-adk-kotlin ](../../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../../index.html)/[com.google.adk.kt.types](../../index.html)/[Schema](../index.html)/Builder

# Builder

common

class [Builder](index.html)

Fluent builder for [Schema](../index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

Members

## Constructors

[Builder](-builder.html)

Link copied to clipboard

common

constructor()

## Functions

[anyOf](any-of.html)

Link copied to clipboard

common

fun [anyOf](any-of.html)(anyOf: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Schema](../index.html)>?): [Schema.Builder](index.html)

fun [anyOf](any-of.html)(vararg anyOf: [Schema](../index.html)): [Schema.Builder](index.html)

[build](build.html)

Link copied to clipboard

common

fun [build](build.html)(): [Schema](../index.html)

[defaultValue](default-value.html)

Link copied to clipboard

common

fun [defaultValue](default-value.html)(defaultValue: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?): [Schema.Builder](index.html)

Sets [Schema.default](../default.html); named [defaultValue](default-value.html) because `default` is a reserved word in Java.

[description](description.html)

Link copied to clipboard

common

fun [description](description.html)(description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?): [Schema.Builder](index.html)

[enum](enum.html)

Link copied to clipboard

common

fun [enum](enum.html)(enum: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?): [Schema.Builder](index.html)

fun [enum](enum.html)(vararg enum: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [Schema.Builder](index.html)

[enumValues](enum-values.html)

Link copied to clipboard

common

fun [enumValues](enum-values.html)(enumValues: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?): [Schema.Builder](index.html)

fun [enumValues](enum-values.html)(vararg enumValues: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [Schema.Builder](index.html)

Sets [enum](enum.html). Java callers need this because `enum` is a reserved word in Java.

[format](format.html)

Link copied to clipboard

common

fun [format](format.html)(format: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?): [Schema.Builder](index.html)

[items](items.html)

Link copied to clipboard

common

fun [items](items.html)(items: [Schema](../index.html)?): [Schema.Builder](index.html)

[maximum](maximum.html)

Link copied to clipboard

common

fun [maximum](maximum.html)(maximum: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)?): [Schema.Builder](index.html)

[maxItems](max-items.html)

Link copied to clipboard

common

fun [maxItems](max-items.html)(maxItems: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?): [Schema.Builder](index.html)

[maxLength](max-length.html)

Link copied to clipboard

common

fun [maxLength](max-length.html)(maxLength: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?): [Schema.Builder](index.html)

[maxProperties](max-properties.html)

Link copied to clipboard

common

fun [maxProperties](max-properties.html)(maxProperties: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?): [Schema.Builder](index.html)

[minimum](minimum.html)

Link copied to clipboard

common

fun [minimum](minimum.html)(minimum: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)?): [Schema.Builder](index.html)

[minItems](min-items.html)

Link copied to clipboard

common

fun [minItems](min-items.html)(minItems: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?): [Schema.Builder](index.html)

[minLength](min-length.html)

Link copied to clipboard

common

fun [minLength](min-length.html)(minLength: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?): [Schema.Builder](index.html)

[minProperties](min-properties.html)

Link copied to clipboard

common

fun [minProperties](min-properties.html)(minProperties: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?): [Schema.Builder](index.html)

[nullable](nullable.html)

Link copied to clipboard

common

fun [nullable](nullable.html)(nullable: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)?): [Schema.Builder](index.html)

[pattern](pattern.html)

Link copied to clipboard

common

fun [pattern](pattern.html)(pattern: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?): [Schema.Builder](index.html)

[properties](properties.html)

Link copied to clipboard

common

fun [properties](properties.html)(properties: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Schema](../index.html)>?): [Schema.Builder](index.html)

[required](required.html)

Link copied to clipboard

common

fun [required](required.html)(required: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?): [Schema.Builder](index.html)

fun [required](required.html)(vararg required: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [Schema.Builder](index.html)

[title](title.html)

Link copied to clipboard

common

fun [title](title.html)(title: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?): [Schema.Builder](index.html)

[type](type.html)

Link copied to clipboard

common

fun [type](type.html)(type: [Type](../../-type/index.html)?): [Schema.Builder](index.html)

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
