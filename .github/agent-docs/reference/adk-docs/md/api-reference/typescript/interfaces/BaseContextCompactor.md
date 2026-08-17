[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseContextCompactor]()



# Interface BaseContextCompactor

Interface for compacting the context history in an agent session.

interface BaseContextCompactor {  
trigger?: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html);  
compact(invocationContext: [InvocationContext](../classes/InvocationContext.html)): void | Promise<void>;  
shouldCompact(  
invocationContext: [InvocationContext](../classes/InvocationContext.html),  
): boolean | Promise<boolean>;  
}

#### Implemented by

  * [AgentControlledContextCompactor](../classes/AgentControlledContextCompactor.html)
  * [AnchoredContextCompactor](../classes/AnchoredContextCompactor.html)
  * [TokenBasedContextCompactor](../classes/TokenBasedContextCompactor.html)
  * [TrajectoryThoughtPruningCompactor](../classes/TrajectoryThoughtPruningCompactor.html)
  * [TruncatingContextCompactor](../classes/TruncatingContextCompactor.html)



  * Defined in [core/src/context/base_context_compactor.ts:13](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/base_context_compactor.ts#L13)



## Properties

### `Optional` `Readonly`trigger

trigger?: [ContextCompactionTrigger](../enums/ContextCompactionTrigger.html)

The trigger associated with this compactor.

  * Defined in [core/src/context/base_context_compactor.ts:15](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/base_context_compactor.ts#L15)



## Methods

### compact

  * compact(invocationContext: [InvocationContext](../classes/InvocationContext.html)): void | Promise<void>

Compacts the context in place.

#### Parameters

    * invocationContext: [InvocationContext](../classes/InvocationContext.html)

The current invocation context.

#### Returns void | Promise<void>

    * Defined in [core/src/context/base_context_compactor.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/base_context_compactor.ts#L32)




### shouldCompact

  * shouldCompact(invocationContext: [InvocationContext](../classes/InvocationContext.html)): boolean | Promise<boolean>

Determines whether the context should be compacted.

#### Parameters

    * invocationContext: [InvocationContext](../classes/InvocationContext.html)

The current invocation context.

#### Returns boolean | Promise<boolean>

A boolean or a promise resolving to a boolean indicating if compaction should occur.

    * Defined in [core/src/context/base_context_compactor.ts:23](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/base_context_compactor.ts#L23)




Properties

trigger

Methods

compactshouldCompact

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


