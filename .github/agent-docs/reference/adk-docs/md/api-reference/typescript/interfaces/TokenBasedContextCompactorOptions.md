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

  * Defined in [core/src/context/token_based_context_compactor.ts:21](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/token_based_context_compactor.ts#L21)



## Properties

### eventRetentionSize

eventRetentionSize: number

The minimum number of raw events to keep at the end of the session. Compaction will not affect these tail events (unless needed for tool splits).

  * Defined in [core/src/context/token_based_context_compactor.ts:33](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/token_based_context_compactor.ts#L33)



### summarizer

summarizer: [BaseSummarizer](BaseSummarizer.html)

The summarizer used to create the compacted event content.

  * Defined in [core/src/context/token_based_context_compactor.ts:35](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/token_based_context_compactor.ts#L35)



### tokenThreshold

tokenThreshold: number

Prompt-size threshold (in tokens) that triggers compaction. Compared against the most recently observed LLM request size (`usageMetadata.promptTokenCount`), falling back to a character-based estimate of the effective contents when no usage metadata is available.

  * Defined in [core/src/context/token_based_context_compactor.ts:28](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/token_based_context_compactor.ts#L28)



Properties

eventRetentionSizesummarizertokenThreshold

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


