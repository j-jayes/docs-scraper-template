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

  * Defined in [core/src/context/truncating_context_compactor.ts:10](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/truncating_context_compactor.ts#L10)



## Properties

### `Optional`preserveLeadingEvents

preserveLeadingEvents?: number

Keep the first X events in the history, which often act as the initial grounding prompt.

  * Defined in [core/src/context/truncating_context_compactor.ts:14](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/truncating_context_compactor.ts#L14)



### threshold

threshold: number

The maximum number of events to retain in the session history.

  * Defined in [core/src/context/truncating_context_compactor.ts:12](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/truncating_context_compactor.ts#L12)



Properties

preserveLeadingEventsthreshold

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


