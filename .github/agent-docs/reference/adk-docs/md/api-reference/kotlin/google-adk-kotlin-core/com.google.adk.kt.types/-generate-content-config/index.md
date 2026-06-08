toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.types](../index.html)/GenerateContentConfig

# GenerateContentConfig

data class [GenerateContentConfig](index.html)(val tools: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Tool](../-tool/index.html)>? = null, val labels: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, val systemInstruction: [Content](../-content/index.html)? = null, val temperature: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null, val topP: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null, val topK: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val candidateCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val maxOutputTokens: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val stopSequences: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, val responseMimeType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val thinkingConfig: [ThinkingConfig](../-thinking-config/index.html)? = null)

Configuration for generating content.

Members

## Constructors

[GenerateContentConfig](-generate-content-config.html)

Link copied to clipboard

constructor(tools: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Tool](../-tool/index.html)>? = null, labels: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, systemInstruction: [Content](../-content/index.html)? = null, temperature: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null, topP: [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null, topK: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, candidateCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, maxOutputTokens: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, stopSequences: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null, responseMimeType: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, thinkingConfig: [ThinkingConfig](../-thinking-config/index.html)? = null)

## Properties

[candidateCount](candidate-count.html)

Link copied to clipboard

val [candidateCount](candidate-count.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null

[labels](labels.html)

Link copied to clipboard

val [labels](labels.html): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null

[maxOutputTokens](max-output-tokens.html)

Link copied to clipboard

val [maxOutputTokens](max-output-tokens.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null

[responseMimeType](response-mime-type.html)

Link copied to clipboard

val [responseMimeType](response-mime-type.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

[stopSequences](stop-sequences.html)

Link copied to clipboard

val [stopSequences](stop-sequences.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>? = null

[systemInstruction](system-instruction.html)

Link copied to clipboard

val [systemInstruction](system-instruction.html): [Content](../-content/index.html)? = null

[temperature](temperature.html)

Link copied to clipboard

val [temperature](temperature.html): [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null

[thinkingConfig](thinking-config.html)

Link copied to clipboard

val [thinkingConfig](thinking-config.html): [ThinkingConfig](../-thinking-config/index.html)? = null

[tools](tools.html)

Link copied to clipboard

val [tools](tools.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Tool](../-tool/index.html)>? = null

[topK](top-k.html)

Link copied to clipboard

val [topK](top-k.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null

[topP](top-p.html)

Link copied to clipboard

val [topP](top-p.html): [Float](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-float/index.html)? = null

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
