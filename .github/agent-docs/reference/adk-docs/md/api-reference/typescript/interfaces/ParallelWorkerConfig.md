[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ParallelWorkerConfig]()



# Interface ParallelWorkerConfig

Options for a [ParallelWorker](../classes/ParallelWorker.html).

interface ParallelWorkerConfig {  
maxParallelWorkers?: number;  
}

  * Defined in [core/src/workflow/nodes/parallel_worker.ts:22](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/parallel_worker.ts#L22)



## Properties

### `Optional`maxParallelWorkers

maxParallelWorkers?: number

Maximum number of items processed concurrently. Defaults to `DEFAULT_MAX_PARALLEL_WORKERS` (8); pass `Infinity` for unbounded.

  * Defined in [core/src/workflow/nodes/parallel_worker.ts:27](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/parallel_worker.ts#L27)



Properties

maxParallelWorkers

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


