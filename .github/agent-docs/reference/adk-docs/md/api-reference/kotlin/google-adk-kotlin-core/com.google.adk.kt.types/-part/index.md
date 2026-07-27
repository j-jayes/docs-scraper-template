toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.types](../index.html)/Part

# Part

@Serializable

class [Part](index.html) constructor(val text: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val inlineData: [Blob](../-blob/index.html)? = null, val fileData: [FileData](../-file-data/index.html)? = null, val functionCall: [FunctionCall](../-function-call/index.html)? = null, val functionResponse: [FunctionResponse](../-function-response/index.html)? = null, val thought: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val thoughtSignature: [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html)? = null, val videoMetadata: [VideoMetadata](../-video-metadata/index.html)? = null, val partMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?>? = null, val opaqueData: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)? = null)

A part of a multi-modal prompt or response.

A Part can contain one of the following:

  * text: Plain text.

  * inlineData: Binary data (e.g., image, audio).

  * fileData: Data from a file.

  * functionCall: A call to a function.

  * functionResponse: The response from a function call.




Members

## Constructors

[Part](-part.html)

Link copied to clipboard

constructor(text: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, inlineData: [Blob](../-blob/index.html)? = null, fileData: [FileData](../-file-data/index.html)? = null, functionCall: [FunctionCall](../-function-call/index.html)? = null, functionResponse: [FunctionResponse](../-function-response/index.html)? = null, thought: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null, thoughtSignature: [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html)? = null, videoMetadata: [VideoMetadata](../-video-metadata/index.html)? = null, partMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?>? = null)

constructor(text: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, inlineData: [Blob](../-blob/index.html)? = null, fileData: [FileData](../-file-data/index.html)? = null, functionCall: [FunctionCall](../-function-call/index.html)? = null, functionResponse: [FunctionResponse](../-function-response/index.html)? = null, thought: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null, thoughtSignature: [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html)? = null, videoMetadata: [VideoMetadata](../-video-metadata/index.html)? = null, partMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?>? = null, opaqueData: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)? = null)

## Properties

[fileData](file-data.html)

Link copied to clipboard

val [fileData](file-data.html): [FileData](../-file-data/index.html)? = null

Data from a file.

[functionCall](function-call.html)

Link copied to clipboard

val [functionCall](function-call.html): [FunctionCall](../-function-call/index.html)? = null

A call to a function.

[functionResponse](function-response.html)

Link copied to clipboard

val [functionResponse](function-response.html): [FunctionResponse](../-function-response/index.html)? = null

The response from a function call.

[inlineData](inline-data.html)

Link copied to clipboard

val [inlineData](inline-data.html): [Blob](../-blob/index.html)? = null

Binary data (e.g., image, audio).

[opaqueData](opaque-data.html)

Link copied to clipboard

@Transient

val [opaqueData](opaque-data.html): [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)? = null

Other opaque data associated with the part to be interpreted by the agent. Reserved for ADK internal use. Users should not set this field.

[partMetadata](part-metadata.html)

Link copied to clipboard

val [partMetadata](part-metadata.html): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?>? = null

Arbitrary key-value metadata associated with this part. The map must be JSON serializable.

[text](text.html)

Link copied to clipboard

val [text](text.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

Plain text.

[thought](thought.html)

Link copied to clipboard

val [thought](thought.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = null

Indicates whether the part represents the model's thought process.

[thoughtSignature](thought-signature.html)

Link copied to clipboard

val [thoughtSignature](thought-signature.html): [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html)? = null

An opaque signature for the thought.

[videoMetadata](video-metadata.html)

Link copied to clipboard

val [videoMetadata](video-metadata.html): [VideoMetadata](../-video-metadata/index.html)? = null

Metadata for a video part (segment offsets and frame rate).

## Functions

[copy](copy.html)

Link copied to clipboard

fun [copy](copy.html)(text: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = this.text, inlineData: [Blob](../-blob/index.html)? = this.inlineData, fileData: [FileData](../-file-data/index.html)? = this.fileData, functionCall: [FunctionCall](../-function-call/index.html)? = this.functionCall, functionResponse: [FunctionResponse](../-function-response/index.html)? = this.functionResponse, thought: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = this.thought, thoughtSignature: [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html)? = this.thoughtSignature, videoMetadata: [VideoMetadata](../-video-metadata/index.html)? = this.videoMetadata, partMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?>? = this.partMetadata): [Part](index.html)

fun [copy](copy.html)(text: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = this.text, inlineData: [Blob](../-blob/index.html)? = this.inlineData, fileData: [FileData](../-file-data/index.html)? = this.fileData, functionCall: [FunctionCall](../-function-call/index.html)? = this.functionCall, functionResponse: [FunctionResponse](../-function-response/index.html)? = this.functionResponse, thought: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)? = this.thought, thoughtSignature: [ByteArray](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-byte-array/index.html)? = this.thoughtSignature, videoMetadata: [VideoMetadata](../-video-metadata/index.html)? = this.videoMetadata, partMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?>? = this.partMetadata, opaqueData: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?): [Part](index.html)

[equals](equals.html)

Link copied to clipboard

open operator override fun [equals](equals.html)(other: [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)?): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)

[hashCode](hash-code.html)

Link copied to clipboard

open override fun [hashCode](hash-code.html)(): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)

[toString](to-string.html)

Link copied to clipboard

open override fun [toString](to-string.html)(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

[toStringInternal](to-string-internal.html)

Link copied to clipboard

fun [toStringInternal](to-string-internal.html)(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
