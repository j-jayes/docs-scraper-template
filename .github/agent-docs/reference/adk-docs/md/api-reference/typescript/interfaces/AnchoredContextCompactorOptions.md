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

  * Defined in [core/src/context/anchored_context_compactor.ts:17](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/anchored_context_compactor.ts#L17)



## Properties

### eventRetentionSize

eventRetentionSize: number

The minimum number of raw events to keep at the end of the session. Compaction will not affect these tail events (unless needed for tool splits).

  * Defined in [core/src/context/anchored_context_compactor.ts:24](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/anchored_context_compactor.ts#L24)



### summarizer

summarizer: [BaseSummarizer](BaseSummarizer.html)

The summarizer used to create the compacted event content.

  * Defined in [core/src/context/anchored_context_compactor.ts:26](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/anchored_context_compactor.ts#L26)



### tokenThreshold

tokenThreshold: number

The maximum number of tokens to retain in the session history before compaction.

  * Defined in [core/src/context/anchored_context_compactor.ts:19](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/anchored_context_compactor.ts#L19)



Properties

eventRetentionSizesummarizertokenThreshold

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


