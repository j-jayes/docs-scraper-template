[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AfterExecuteCallback]()



# Type Alias AfterExecuteCallback

AfterExecuteCallback: (  
ctx: [ExecutorContext](../interfaces/ExecutorContext.html),  
finalA2aEvent: TaskStatusUpdateEvent,  
err?: Error,  
) => Promise<void>

Callback called after execution resolved into a completed or failed task.

#### Type Declaration

  *     * (  
ctx: [ExecutorContext](../interfaces/ExecutorContext.html),  
finalA2aEvent: TaskStatusUpdateEvent,  
err?: Error,  
): Promise<void>
    * #### Parameters

      * ctx: [ExecutorContext](../interfaces/ExecutorContext.html)
      * finalA2aEvent: TaskStatusUpdateEvent
      * `Optional`err: Error

#### Returns Promise<void>




  * Defined in [core/src/a2a/agent_executor.ts:63](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_executor.ts#L63)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


