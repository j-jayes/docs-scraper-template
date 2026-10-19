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




  * Defined in [core/src/a2a/a2a_remote_agent.ts:58](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/a2a/a2a_remote_agent.ts#L58)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


