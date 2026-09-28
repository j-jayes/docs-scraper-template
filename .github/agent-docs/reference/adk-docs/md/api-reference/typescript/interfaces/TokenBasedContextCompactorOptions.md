[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [TokenBasedContextCompactorOptions]()



# Interface TokenBasedContextCompactorOptions

interface TokenBasedContextCompactorOptions {  
eventRetentionSize: number;  
summarizer: [BaseSummarizer](BaseSummarizer.html);  
tokenThreshold: number;  
}

  * Defined in [core/src/context/token_based_context_compactor.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/token_based_context_compactor.ts#L18)



## Properties

### eventRetentionSize

eventRetentionSize: number

The minimum number of raw events to keep at the end of the session. Compaction will not affect these tail events (unless needed for tool splits).

  * Defined in [core/src/context/token_based_context_compactor.ts:30](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/token_based_context_compactor.ts#L30)



### summarizer

summarizer: [BaseSummarizer](BaseSummarizer.html)

The summarizer used to create the compacted event content.

  * Defined in [core/src/context/token_based_context_compactor.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/token_based_context_compactor.ts#L32)



### tokenThreshold

tokenThreshold: number

Prompt-size threshold (in tokens) that triggers compaction. Compared against the most recently observed LLM request size (`usageMetadata.promptTokenCount`), falling back to a character-based estimate of the effective contents when no usage metadata is available.

  * Defined in [core/src/context/token_based_context_compactor.ts:25](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/token_based_context_compactor.ts#L25)



Properties

eventRetentionSizesummarizertokenThreshold

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


