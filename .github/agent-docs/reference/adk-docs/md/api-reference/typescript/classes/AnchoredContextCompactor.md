[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AnchoredContextCompactor]()



# Class AnchoredContextCompactor

A context compactor that maintains a single persistent 'Scratchpad' or 'State Tracker' event at the top of the context history.

When compaction is triggered, it merges new raw events into the existing Scratchpad event and discards them from the active history view.

#### Implements

  * [BaseContextCompactor](../interfaces/BaseContextCompactor.html)



  * Defined in [core/src/context/anchored_context_compactor.ts:36](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/anchored_context_compactor.ts#L36)



## Constructors

### constructor

  * new AnchoredContextCompactor(  
options: [AnchoredContextCompactorOptions](../interfaces/AnchoredContextCompactorOptions.html),  
): [AnchoredContextCompactor]()

#### Parameters

    * options: [AnchoredContextCompactorOptions](../interfaces/AnchoredContextCompactorOptions.html)

#### Returns [AnchoredContextCompactor]()

    * Defined in [core/src/context/anchored_context_compactor.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/anchored_context_compactor.ts#L41)




## Methods

### compact

  * compact(invocationContext: [InvocationContext](InvocationContext.html)): Promise<void>

Compacts the context in place.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns Promise<void>

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[compact](../interfaces/BaseContextCompactor.html#compact)

    * Defined in [core/src/context/anchored_context_compactor.ts:107](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/anchored_context_compactor.ts#L107)




### shouldCompact

  * shouldCompact(invocationContext: [InvocationContext](InvocationContext.html)): boolean | Promise<boolean>

Determines whether the context should be compacted.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns boolean | Promise<boolean>

A boolean or a promise resolving to a boolean indicating if compaction should occur.

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[shouldCompact](../interfaces/BaseContextCompactor.html#shouldcompact)

    * Defined in [core/src/context/anchored_context_compactor.ts:75](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/anchored_context_compactor.ts#L75)




Constructors

constructor

Methods

compactshouldCompact

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


