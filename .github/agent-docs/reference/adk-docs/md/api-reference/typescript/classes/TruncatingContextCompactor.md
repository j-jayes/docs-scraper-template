[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [TruncatingContextCompactor]()



# Class TruncatingContextCompactor

A simple context compactor that truncates the oldest events to get under the given threshold limit.

#### Implements

  * [BaseContextCompactor](../interfaces/BaseContextCompactor.html)



  * Defined in [core/src/context/truncating_context_compactor.ts:21](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/truncating_context_compactor.ts#L21)



## Constructors

### constructor

  * new TruncatingContextCompactor(  
options: [TruncatingContextCompactorOptions](../interfaces/TruncatingContextCompactorOptions.html),  
): [TruncatingContextCompactor]()

#### Parameters

    * options: [TruncatingContextCompactorOptions](../interfaces/TruncatingContextCompactorOptions.html)

#### Returns [TruncatingContextCompactor]()

    * Defined in [core/src/context/truncating_context_compactor.ts:25](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/truncating_context_compactor.ts#L25)




## Methods

### compact

  * compact(invocationContext: [InvocationContext](InvocationContext.html)): void

Compacts the context in place.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns void

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[compact](../interfaces/BaseContextCompactor.html#compact)

    * Defined in [core/src/context/truncating_context_compactor.ts:37](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/truncating_context_compactor.ts#L37)




### shouldCompact

  * shouldCompact(invocationContext: [InvocationContext](InvocationContext.html)): boolean

Determines whether the context should be compacted.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns boolean

A boolean or a promise resolving to a boolean indicating if compaction should occur.

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[shouldCompact](../interfaces/BaseContextCompactor.html#shouldcompact)

    * Defined in [core/src/context/truncating_context_compactor.ts:30](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/truncating_context_compactor.ts#L30)




Constructors

constructor

Methods

compactshouldCompact

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


