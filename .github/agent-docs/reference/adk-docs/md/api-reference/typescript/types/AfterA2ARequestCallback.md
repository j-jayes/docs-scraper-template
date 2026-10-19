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




  * Defined in [core/src/a2a/a2a_remote_agent.ts:74](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/a2a/a2a_remote_agent.ts#L74)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


