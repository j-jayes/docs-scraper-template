[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SingleAfterModelCallback]()



# Type Alias SingleAfterModelCallback

SingleAfterModelCallback: (  
params: { context: [CallbackContext](../classes/CallbackContext.html); response: [LlmResponse](../interfaces/LlmResponse.html) },  
) => [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

A callback that runs after a response is received from the model.

#### Type Declaration

  *     * (  
params: { context: [CallbackContext](../classes/CallbackContext.html); response: [LlmResponse](../interfaces/LlmResponse.html) },  
): [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>
    * #### Parameters

      * params: { context: [CallbackContext](../classes/CallbackContext.html); response: [LlmResponse](../interfaces/LlmResponse.html) }

#### Returns [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

The content to return to the user. When present, the actual model response will be ignored and the provided content will be returned to user.




  * Defined in [core/src/agents/llm_agent.ts:69](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L69)



[ADK for TypeScript: API Reference](../index.html)

  * Loading...


