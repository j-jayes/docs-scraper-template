[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AfterA2ARequestCallback]()



# Type Alias AfterA2ARequestCallback

AfterA2ARequestCallback: (  
ctx: [InvocationContext](../classes/InvocationContext.html),  
resp: [A2AStreamEventData](A2AStreamEventData.html),  
) => Promise<void> | void

Callback called after receiving a response from the remote agent. Allows inspecting or modifying the response.

#### Type Declaration

  *     * (ctx: [InvocationContext](../classes/InvocationContext.html), resp: [A2AStreamEventData](A2AStreamEventData.html)): Promise<void> | void
    * #### Parameters

      * ctx: [InvocationContext](../classes/InvocationContext.html)

The current invocation context, providing access to session state, agent metadata, and services.

      * resp: [A2AStreamEventData](A2AStreamEventData.html)

The raw A2A stream event data received from the remote agent, before conversion to an ADK event.

#### Returns Promise<void> | void

A Promise or void. Returning a rejected Promise stops further processing of the response.




  * Defined in [core/src/a2a/a2a_remote_agent.ts:73](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/a2a_remote_agent.ts#L73)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


