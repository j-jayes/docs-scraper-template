[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AfterEventCallback]()



# Type Alias AfterEventCallback

AfterEventCallback: (  
ctx: [ExecutorContext](../interfaces/ExecutorContext.html),  
adkEvent: [Event](../interfaces/Event.html),  
a2aEvent?: TaskArtifactUpdateEvent,  
) => Promise<void>

Callback called after an ADK event is converted to an A2A event.

#### Type Declaration

  *     * (  
ctx: [ExecutorContext](../interfaces/ExecutorContext.html),  
adkEvent: [Event](../interfaces/Event.html),  
a2aEvent?: TaskArtifactUpdateEvent,  
): Promise<void>
    * #### Parameters

      * ctx: [ExecutorContext](../interfaces/ExecutorContext.html)
      * adkEvent: [Event](../interfaces/Event.html)
      * `Optional`a2aEvent: TaskArtifactUpdateEvent

#### Returns Promise<void>




  * Defined in [core/src/a2a/agent_executor.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_executor.ts#L54)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


