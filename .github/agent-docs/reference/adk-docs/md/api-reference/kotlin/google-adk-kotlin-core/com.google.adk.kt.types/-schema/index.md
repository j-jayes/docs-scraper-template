[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

commonJvmAndroid common

Target filter __

    * commonJvmAndroid 
    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.types](../index.html)/Schema

# Schema

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Schema](index.html)(val type: [Type](../-type/index.html)? = null, val properties: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Schema](index.html)>? = null, val items: [Schema](index.html)? = null, val required: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val enum: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val format: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val nullable: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val default: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, val anyOf: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Schema](index.html)>? = null, val title: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val pattern: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val minimum: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, val maximum: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, val minLength: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val maxLength: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val minItems: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val maxItems: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val minProperties: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, val maxProperties: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null)

Schema is used to define the format of input/output data.

Represents a select subset of an [OpenAPI 3.0 schema object](https://spec.openapis.org/oas/v3.0.3#schema-object).

MembersMembers & Extensions

## Constructors

[Schema](-schema.html)

Link copied to clipboard

common

constructor(type: [Type](../-type/index.html)? = null, properties: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Schema](index.html)>? = null, items: [Schema](index.html)? = null, required: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, enum: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, format: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, nullable: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, default: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, anyOf: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Schema](index.html)>? = null, title: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, pattern: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, minimum: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, maximum: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, minLength: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, maxLength: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, minItems: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, maxItems: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, minProperties: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null, maxProperties: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [Schema](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[anyOf](any-of.html)

Link copied to clipboard

common

val [anyOf](any-of.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Schema](index.html)>?

The value must validate against at least one of these subschemas.

[default](default.html)

Link copied to clipboard

common

val [default](default.html): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

The value to assume when the property is absent. Must be JSON-native -- a `String`, number, `Boolean`, `Map` or `List` \-- since anything else fails to serialize. Serializing a [Schema](index.html) that sets this needs a `Json` whose `serializersModule` carries a contextual serializer for `Any`; a plain `Json` throws. JSON also has a single number type, so a numeric default that crosses a JSON boundary comes back as whatever Kotlin type the reader picks, not necessarily the one it was written as.

[description](description.html)

Link copied to clipboard

common

val [description](description.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

A human-readable description of the schema.

[enum](enum.html)

Link copied to clipboard

common

val [enum](enum.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?

Restricts a value to a fixed set of values.

[format](format.html)

Link copied to clipboard

common

val [format](format.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The format of the data, refining [type](../../../google-adk-kotlin-core/com.google.adk.kt.types/-schema/--root--.html). The field is free-form, but Gemini accepts only `int32` or `int64` for [Type.INTEGER](../-type/-i-n-t-e-g-e-r/index.html) and [Type.NUMBER](../-type/-n-u-m-b-e-r/index.html), and `enum` or `date-time` for [Type.STRING](../-type/-s-t-r-i-n-g/index.html); it rejects a declaration carrying any other value.

[items](items.html)

Link copied to clipboard

common

val [items](items.html): [Schema](index.html)?

Describes the schema of items in an array. Applicable only if `type` is [Type.ARRAY](../-type/-a-r-r-a-y/index.html).

[maximum](maximum.html)

Link copied to clipboard

common

val [maximum](maximum.html): [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)?

The largest allowed value. Applicable only if `type` is [Type.INTEGER](../-type/-i-n-t-e-g-e-r/index.html) or [Type.NUMBER](../-type/-n-u-m-b-e-r/index.html).

[maxItems](max-items.html)

Link copied to clipboard

common

val [maxItems](max-items.html): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?

The most allowed items. Applicable only if `type` is [Type.ARRAY](../-type/-a-r-r-a-y/index.html).

[maxLength](max-length.html)

Link copied to clipboard

common

val [maxLength](max-length.html): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?

The longest allowed string. Applicable only if `type` is [Type.STRING](../-type/-s-t-r-i-n-g/index.html).

[maxProperties](max-properties.html)

Link copied to clipboard

common

val [maxProperties](max-properties.html): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?

The most allowed properties. Applicable only if `type` is [Type.OBJECT](../-type/-o-b-j-e-c-t/index.html).

[minimum](minimum.html)

Link copied to clipboard

common

val [minimum](minimum.html): [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)?

The smallest allowed value. Applicable only if `type` is [Type.INTEGER](../-type/-i-n-t-e-g-e-r/index.html) or [Type.NUMBER](../-type/-n-u-m-b-e-r/index.html).

[minItems](min-items.html)

Link copied to clipboard

common

val [minItems](min-items.html): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?

The fewest allowed items. Applicable only if `type` is [Type.ARRAY](../-type/-a-r-r-a-y/index.html).

[minLength](min-length.html)

Link copied to clipboard

common

val [minLength](min-length.html): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?

The shortest allowed string. Applicable only if `type` is [Type.STRING](../-type/-s-t-r-i-n-g/index.html).

[minProperties](min-properties.html)

Link copied to clipboard

common

val [minProperties](min-properties.html): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)?

The fewest allowed properties. Applicable only if `type` is [Type.OBJECT](../-type/-o-b-j-e-c-t/index.html).

[nullable](nullable.html)

Link copied to clipboard

common

val [nullable](nullable.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)?

Whether the value may be null.

[pattern](pattern.html)

Link copied to clipboard

common

val [pattern](pattern.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

A regular expression the value must match. Applicable only if `type` is [Type.STRING](../-type/-s-t-r-i-n-g/index.html).

[properties](properties.html)

Link copied to clipboard

common

val [properties](properties.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Schema](index.html)>?

Describes the properties of an object. The keys are property names and values are schemas for corresponding properties. Applicable only if `type` is [Type.OBJECT](../-type/-o-b-j-e-c-t/index.html).

[required](required.html)

Link copied to clipboard

common

val [required](required.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?

A list of required property names. Applicable only if `type` is [Type.OBJECT](../-type/-o-b-j-e-c-t/index.html).

[title](title.html)

Link copied to clipboard

common

val [title](title.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

A title for the schema.

[type](type.html)

Link copied to clipboard

common

val [type](type.html): [Type](../-type/index.html)?

Data type of the schema.

## Functions

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [Schema.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

[toJsonSchema](../../com.google.adk.kt.tools/to-json-schema.html)

Link copied to clipboard

commonJvmAndroid

fun [Schema](index.html).[toJsonSchema](../../com.google.adk.kt.tools/to-json-schema.html)(): [JsonObject](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html)

Renders this [Schema](index.html) as a JSON Schema [JsonObject](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/index.html), the same shape used in prompt tool descriptions. Exposed so an adapter can hand a tool's parameter schema to another framework rather than forking this conversion.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
