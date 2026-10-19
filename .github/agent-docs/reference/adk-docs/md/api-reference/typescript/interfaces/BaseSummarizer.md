[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseSummarizer]()



# Interface BaseSummarizer

Interface for summarizing a list of events into a single CompactedEvent.

interface BaseSummarizer {  
summarize(events: [Event](Event.html)[]): Promise<[CompactedEvent](CompactedEvent.html)>;  
}

#### Implemented by

  * [LlmSummarizer](../classes/LlmSummarizer.html)



  * Defined in [core/src/context/summarizers/base_summarizer.ts:14](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/summarizers/base_summarizer.ts#L14)



## Methods

### summarize

  * summarize(events: [Event](Event.html)[]): Promise<[CompactedEvent](CompactedEvent.html)>

Summarizes the given events into a CompactedEvent.

#### Parameters

    * events: [Event](Event.html)[]

The events to summarize.

#### Returns Promise<[CompactedEvent](CompactedEvent.html)>

A promise resolving to the CompactedEvent representation of the events.

    * Defined in [core/src/context/summarizers/base_summarizer.ts:21](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/summarizers/base_summarizer.ts#L21)




Methods

summarize

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


