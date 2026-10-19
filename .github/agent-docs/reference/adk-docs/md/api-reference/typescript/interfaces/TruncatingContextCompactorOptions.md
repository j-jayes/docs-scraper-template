[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [TruncatingContextCompactorOptions]()



# Interface TruncatingContextCompactorOptions

interface TruncatingContextCompactorOptions {  
preserveLeadingEvents?: number;  
threshold: number;  
}

  * Defined in [core/src/context/truncating_context_compactor.ts:11](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/truncating_context_compactor.ts#L11)



## Properties

### `Optional`preserveLeadingEvents

preserveLeadingEvents?: number

Keep the first X events in the history, which often act as the initial grounding prompt.

  * Defined in [core/src/context/truncating_context_compactor.ts:15](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/truncating_context_compactor.ts#L15)



### threshold

threshold: number

The maximum number of events to retain in the session history.

  * Defined in [core/src/context/truncating_context_compactor.ts:13](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/truncating_context_compactor.ts#L13)



Properties

preserveLeadingEventsthreshold

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


