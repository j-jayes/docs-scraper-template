[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [Task]()



# Class Task<T>

Represents a runtime task wrapping a promise, allowing status check and cancellation.

#### Type Parameters

  * T = void



  * Defined in [core/src/utils/task.ts:12](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/utils/task.ts#L12)



## Constructors

### constructor

  * new Task<T = void>(executable: [TaskExecutable](../types/TaskExecutable.html)<T>): [Task]()<T>

#### Type Parameters

    * T = void

#### Parameters

    * executable: [TaskExecutable](../types/TaskExecutable.html)<T>

#### Returns [Task]()<T>

    * Defined in [core/src/utils/task.ts:17](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/utils/task.ts#L17)




## Properties

### executable

executable: [TaskExecutable](../types/TaskExecutable.html)<T>

  * Defined in [core/src/utils/task.ts:17](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/utils/task.ts#L17)



### promise

promise: Promise<T>

  * Defined in [core/src/utils/task.ts:15](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/utils/task.ts#L15)



## Methods

### cancel

  * cancel(): void

Cancels the task execution.

#### Returns void

    * Defined in [core/src/utils/task.ts:29](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/utils/task.ts#L29)




### done

  * done(): boolean

Returns true if the task has completed (either resolved or rejected).

#### Returns boolean

    * Defined in [core/src/utils/task.ts:36](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/utils/task.ts#L36)




Constructors

constructor

Properties

executablepromise

Methods

canceldone

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


