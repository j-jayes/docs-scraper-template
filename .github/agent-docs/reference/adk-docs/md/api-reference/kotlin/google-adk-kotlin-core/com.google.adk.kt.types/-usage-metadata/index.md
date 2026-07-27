toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.types](../index.html)/UsageMetadata

# UsageMetadata

@Serializable

data class [UsageMetadata](index.html)(val promptTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val candidatesTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val totalTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val thoughtsTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val toolUsePromptTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val cachedContentTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val promptTokensDetails: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](../-modality-token-count/index.html)>? = null, val candidatesTokensDetails: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](../-modality-token-count/index.html)>? = null)

Usage metadata for a generate content request.

Members

## Constructors

[UsageMetadata](-usage-metadata.html)

Link copied to clipboard

constructor(promptTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, candidatesTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, totalTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, thoughtsTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, toolUsePromptTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, cachedContentTokenCount: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, promptTokensDetails: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](../-modality-token-count/index.html)>? = null, candidatesTokensDetails: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](../-modality-token-count/index.html)>? = null)

## Properties

[cachedContentTokenCount](cached-content-token-count.html)

Link copied to clipboard

val [cachedContentTokenCount](cached-content-token-count.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null

The number of tokens served from the cached content (cache read).

[candidatesTokenCount](candidates-token-count.html)

Link copied to clipboard

val [candidatesTokenCount](candidates-token-count.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null

The number of tokens in the candidates.

[candidatesTokensDetails](candidates-tokens-details.html)

Link copied to clipboard

val [candidatesTokensDetails](candidates-tokens-details.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](../-modality-token-count/index.html)>? = null

A per-modality breakdown of the candidates token count.

[promptTokenCount](prompt-token-count.html)

Link copied to clipboard

val [promptTokenCount](prompt-token-count.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null

The number of tokens in the prompt.

[promptTokensDetails](prompt-tokens-details.html)

Link copied to clipboard

val [promptTokensDetails](prompt-tokens-details.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[ModalityTokenCount](../-modality-token-count/index.html)>? = null

A per-modality breakdown of the prompt token count.

[thoughtsTokenCount](thoughts-token-count.html)

Link copied to clipboard

val [thoughtsTokenCount](thoughts-token-count.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null

The number of tokens that were part of the model's "thoughts" output, for thinking models.

[toolUsePromptTokenCount](tool-use-prompt-token-count.html)

Link copied to clipboard

val [toolUsePromptTokenCount](tool-use-prompt-token-count.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null

The number of tokens in tool-execution results provided back to the model as input.

[totalTokenCount](total-token-count.html)

Link copied to clipboard

val [totalTokenCount](total-token-count.html): [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null

The total number of tokens.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
