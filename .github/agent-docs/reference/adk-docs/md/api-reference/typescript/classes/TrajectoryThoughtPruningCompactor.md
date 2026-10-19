[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [TrajectoryThoughtPruningCompactor]()



# Class TrajectoryThoughtPruningCompactor

A context compactor that prunes thought parts from older events in the session history. Preserves the causal history (actions and observations) while reducing token usage.

#### Implements

  * [BaseContextCompactor](../interfaces/BaseContextCompactor.html)



  * Defined in [core/src/context/trajectory_thought_pruning_compactor.ts:27](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/trajectory_thought_pruning_compactor.ts#L27)



## Constructors

### constructor

  * new TrajectoryThoughtPruningCompactor(  
options: [TrajectoryThoughtPruningCompactorOptions](../interfaces/TrajectoryThoughtPruningCompactorOptions.html),  
): [TrajectoryThoughtPruningCompactor]()

#### Parameters

    * options: [TrajectoryThoughtPruningCompactorOptions](../interfaces/TrajectoryThoughtPruningCompactorOptions.html)

#### Returns [TrajectoryThoughtPruningCompactor]()

    * Defined in [core/src/context/trajectory_thought_pruning_compactor.ts:30](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/trajectory_thought_pruning_compactor.ts#L30)




## Methods

### compact

  * compact(invocationContext: [InvocationContext](InvocationContext.html)): void | Promise<void>

Compacts the context in place.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns void | Promise<void>

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[compact](../interfaces/BaseContextCompactor.html#compact)

    * Defined in [core/src/context/trajectory_thought_pruning_compactor.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/trajectory_thought_pruning_compactor.ts#L56)




### shouldCompact

  * shouldCompact(invocationContext: [InvocationContext](InvocationContext.html)): boolean | Promise<boolean>

Determines whether the context should be compacted.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns boolean | Promise<boolean>

A boolean or a promise resolving to a boolean indicating if compaction should occur.

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[shouldCompact](../interfaces/BaseContextCompactor.html#shouldcompact)

    * Defined in [core/src/context/trajectory_thought_pruning_compactor.ts:37](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/trajectory_thought_pruning_compactor.ts#L37)




Constructors

constructor

Methods

compactshouldCompact

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


