[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [TruncatingContextCompactor]()



# Class TruncatingContextCompactor

A simple context compactor that truncates the oldest events to get under the given threshold limit.

#### Implements

  * [BaseContextCompactor](../interfaces/BaseContextCompactor.html)



  * Defined in [core/src/context/truncating_context_compactor.ts:22](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/truncating_context_compactor.ts#L22)



## Constructors

### constructor

  * new TruncatingContextCompactor(  
options: [TruncatingContextCompactorOptions](../interfaces/TruncatingContextCompactorOptions.html),  
): [TruncatingContextCompactor]()

#### Parameters

    * options: [TruncatingContextCompactorOptions](../interfaces/TruncatingContextCompactorOptions.html)

#### Returns [TruncatingContextCompactor]()

    * Defined in [core/src/context/truncating_context_compactor.ts:26](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/truncating_context_compactor.ts#L26)




## Methods

### compact

  * compact(invocationContext: [InvocationContext](InvocationContext.html)): void

Compacts the context in place.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns void

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[compact](../interfaces/BaseContextCompactor.html#compact)

    * Defined in [core/src/context/truncating_context_compactor.ts:42](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/truncating_context_compactor.ts#L42)




### shouldCompact

  * shouldCompact(invocationContext: [InvocationContext](InvocationContext.html)): boolean

Determines whether the context should be compacted.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns boolean

A boolean or a promise resolving to a boolean indicating if compaction should occur.

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[shouldCompact](../interfaces/BaseContextCompactor.html#shouldcompact)

    * Defined in [core/src/context/truncating_context_compactor.ts:31](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/truncating_context_compactor.ts#L31)




Constructors

constructor

Methods

compactshouldCompact

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


