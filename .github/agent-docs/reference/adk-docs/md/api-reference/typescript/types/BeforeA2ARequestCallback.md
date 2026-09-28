[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BeforeA2ARequestCallback]()



# Type Alias BeforeA2ARequestCallback

BeforeA2ARequestCallback: (  
ctx: [InvocationContext](../classes/InvocationContext.html),  
params: MessageSendParams,  
) => Promise<void> | void

Callback called before sending a request to the remote agent. Allows modifying the request parameters.

#### Type Declaration

  *     * (ctx: [InvocationContext](../classes/InvocationContext.html), params: MessageSendParams): Promise<void> | void
    * #### Parameters

      * ctx: [InvocationContext](../classes/InvocationContext.html)

The current invocation context, providing access to session state, agent metadata, and services.

      * params: MessageSendParams

The A2A message send parameters that will be sent to the remote agent. Mutations to this object are reflected in the outgoing request.

#### Returns Promise<void> | void

A Promise or void. Returning a rejected Promise aborts the request.




  * Defined in [core/src/a2a/a2a_remote_agent.ts:57](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/a2a_remote_agent.ts#L57)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


