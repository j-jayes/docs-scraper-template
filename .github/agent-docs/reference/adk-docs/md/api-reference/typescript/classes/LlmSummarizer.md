[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LlmSummarizer]()



# Class LlmSummarizer

A summarizer that uses an LLM to generate a compacted representation of existing events.

#### Implements

  * [BaseSummarizer](../interfaces/BaseSummarizer.html)



  * Defined in [core/src/context/summarizers/llm_summarizer.ts:37](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/summarizers/llm_summarizer.ts#L37)



## Constructors

### constructor

  * new LlmSummarizer(options: [LlmSummarizerOptions](../interfaces/LlmSummarizerOptions.html)): [LlmSummarizer]()

#### Parameters

    * options: [LlmSummarizerOptions](../interfaces/LlmSummarizerOptions.html)

Configuration specifying the LLM and optional prompt.

#### Returns [LlmSummarizer]()

    * Defined in [core/src/context/summarizers/llm_summarizer.ts:44](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/summarizers/llm_summarizer.ts#L44)




## Methods

### summarize

  * summarize(events: [Event](../interfaces/Event.html)[]): Promise<[CompactedEvent](../interfaces/CompactedEvent.html)>

Summarizes a list of events into a single [CompactedEvent](../interfaces/CompactedEvent.html) using the configured LLM.

#### Parameters

    * events: [Event](../interfaces/Event.html)[]

The events to summarize. Must be non-empty.

#### Returns Promise<[CompactedEvent](../interfaces/CompactedEvent.html)>

A promise resolving to the compacted representation.

#### Throws

If `events` is empty or the LLM returns no content.

Implementation of [BaseSummarizer](../interfaces/BaseSummarizer.html).[summarize](../interfaces/BaseSummarizer.html#summarize)

    * Defined in [core/src/context/summarizers/llm_summarizer.ts:57](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/summarizers/llm_summarizer.ts#L57)




Constructors

constructor

Methods

summarize

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


