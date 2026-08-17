[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [TrajectoryThoughtPruningCompactor]()



# Class TrajectoryThoughtPruningCompactor

A context compactor that prunes thought parts from older events in the session history. Preserves the causal history (actions and observations) while reducing token usage.

#### Implements

  * [BaseContextCompactor](../interfaces/BaseContextCompactor.html)



  * Defined in [core/src/context/trajectory_thought_pruning_compactor.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/trajectory_thought_pruning_compactor.ts#L26)



## Constructors

### constructor

  * new TrajectoryThoughtPruningCompactor(  
options: [TrajectoryThoughtPruningCompactorOptions](../interfaces/TrajectoryThoughtPruningCompactorOptions.html),  
): [TrajectoryThoughtPruningCompactor]()

#### Parameters

    * options: [TrajectoryThoughtPruningCompactorOptions](../interfaces/TrajectoryThoughtPruningCompactorOptions.html)

#### Returns [TrajectoryThoughtPruningCompactor]()

    * Defined in [core/src/context/trajectory_thought_pruning_compactor.ts:29](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/trajectory_thought_pruning_compactor.ts#L29)




## Methods

### compact

  * compact(invocationContext: [InvocationContext](InvocationContext.html)): void | Promise<void>

Compacts the context in place.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns void | Promise<void>

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[compact](../interfaces/BaseContextCompactor.html#compact)

    * Defined in [core/src/context/trajectory_thought_pruning_compactor.ts:51](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/trajectory_thought_pruning_compactor.ts#L51)




### shouldCompact

  * shouldCompact(invocationContext: [InvocationContext](InvocationContext.html)): boolean | Promise<boolean>

Determines whether the context should be compacted.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns boolean | Promise<boolean>

A boolean or a promise resolving to a boolean indicating if compaction should occur.

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[shouldCompact](../interfaces/BaseContextCompactor.html#shouldcompact)

    * Defined in [core/src/context/trajectory_thought_pruning_compactor.ts:36](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/trajectory_thought_pruning_compactor.ts#L36)




Constructors

constructor

Methods

compactshouldCompact

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


