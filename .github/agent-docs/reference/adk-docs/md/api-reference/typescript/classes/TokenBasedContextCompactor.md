[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [TokenBasedContextCompactor]()



# Class TokenBasedContextCompactor

A context compactor that uses token count to determine when to compact events. Oldest events are summarized into a CompactedEvent when the session history exceeds the token threshold.

#### Implements

  * [BaseContextCompactor](../interfaces/BaseContextCompactor.html)



  * Defined in [core/src/context/token_based_context_compactor.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/token_based_context_compactor.ts#L43)



## Constructors

### constructor

  * new TokenBasedContextCompactor(  
options: [TokenBasedContextCompactorOptions](../interfaces/TokenBasedContextCompactorOptions.html),  
): [TokenBasedContextCompactor]()

#### Parameters

    * options: [TokenBasedContextCompactorOptions](../interfaces/TokenBasedContextCompactorOptions.html)

#### Returns [TokenBasedContextCompactor]()

    * Defined in [core/src/context/token_based_context_compactor.ts:48](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/token_based_context_compactor.ts#L48)




## Methods

### compact

  * compact(invocationContext: [InvocationContext](InvocationContext.html)): Promise<void>

Compacts the context in place.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns Promise<void>

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[compact](../interfaces/BaseContextCompactor.html#compact)

    * Defined in [core/src/context/token_based_context_compactor.ts:87](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/token_based_context_compactor.ts#L87)




### shouldCompact

  * shouldCompact(invocationContext: [InvocationContext](InvocationContext.html)): boolean | Promise<boolean>

Determines whether the context should be compacted.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns boolean | Promise<boolean>

A boolean or a promise resolving to a boolean indicating if compaction should occur.

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[shouldCompact](../interfaces/BaseContextCompactor.html#shouldcompact)

    * Defined in [core/src/context/token_based_context_compactor.ts:54](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/token_based_context_compactor.ts#L54)




Constructors

constructor

Methods

compactshouldCompact

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


