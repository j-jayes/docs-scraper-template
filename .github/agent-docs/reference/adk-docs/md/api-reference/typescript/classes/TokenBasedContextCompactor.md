[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [TokenBasedContextCompactor]()



# Class TokenBasedContextCompactor

A context compactor that uses token count to determine when to compact events. Oldest events are summarized into a CompactedEvent when the session history exceeds the token threshold.

#### Implements

  * [BaseContextCompactor](../interfaces/BaseContextCompactor.html)



  * Defined in [core/src/context/token_based_context_compactor.ts:40](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/token_based_context_compactor.ts#L40)



## Constructors

### constructor

  * new TokenBasedContextCompactor(  
options: [TokenBasedContextCompactorOptions](../interfaces/TokenBasedContextCompactorOptions.html),  
): [TokenBasedContextCompactor]()

#### Parameters

    * options: [TokenBasedContextCompactorOptions](../interfaces/TokenBasedContextCompactorOptions.html)

#### Returns [TokenBasedContextCompactor]()

    * Defined in [core/src/context/token_based_context_compactor.ts:45](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/token_based_context_compactor.ts#L45)




## Methods

### compact

  * compact(invocationContext: [InvocationContext](InvocationContext.html)): Promise<void>

Compacts the context in place.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns Promise<void>

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[compact](../interfaces/BaseContextCompactor.html#compact)

    * Defined in [core/src/context/token_based_context_compactor.ts:105](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/token_based_context_compactor.ts#L105)




### shouldCompact

  * shouldCompact(invocationContext: [InvocationContext](InvocationContext.html)): boolean | Promise<boolean>

Determines whether the context should be compacted.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns boolean | Promise<boolean>

A boolean or a promise resolving to a boolean indicating if compaction should occur.

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[shouldCompact](../interfaces/BaseContextCompactor.html#shouldcompact)

    * Defined in [core/src/context/token_based_context_compactor.ts:75](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/token_based_context_compactor.ts#L75)




Constructors

constructor

Methods

compactshouldCompact

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


