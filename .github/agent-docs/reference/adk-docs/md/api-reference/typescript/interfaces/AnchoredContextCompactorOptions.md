[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AnchoredContextCompactorOptions]()



# Interface AnchoredContextCompactorOptions

interface AnchoredContextCompactorOptions {  
eventRetentionSize: number;  
summarizer: [BaseSummarizer](BaseSummarizer.html);  
tokenThreshold: number;  
}

  * Defined in [core/src/context/anchored_context_compactor.ts:14](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/anchored_context_compactor.ts#L14)



## Properties

### eventRetentionSize

eventRetentionSize: number

The minimum number of raw events to keep at the end of the session. Compaction will not affect these tail events (unless needed for tool splits).

  * Defined in [core/src/context/anchored_context_compactor.ts:21](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/anchored_context_compactor.ts#L21)



### summarizer

summarizer: [BaseSummarizer](BaseSummarizer.html)

The summarizer used to create the compacted event content.

  * Defined in [core/src/context/anchored_context_compactor.ts:23](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/anchored_context_compactor.ts#L23)



### tokenThreshold

tokenThreshold: number

The maximum number of tokens to retain in the session history before compaction.

  * Defined in [core/src/context/anchored_context_compactor.ts:16](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/anchored_context_compactor.ts#L16)



Properties

eventRetentionSizesummarizertokenThreshold

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


