[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SingleBeforeModelCallback]()



# Type Alias SingleBeforeModelCallback

SingleBeforeModelCallback: (  
params: { context: [CallbackContext](../classes/CallbackContext.html); request: [LlmRequest](../interfaces/LlmRequest.html) },  
) => [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

A callback that runs before a request is sent to the model.

#### Type Declaration

  *     * (  
params: { context: [CallbackContext](../classes/CallbackContext.html); request: [LlmRequest](../interfaces/LlmRequest.html) },  
): [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>
    * #### Parameters

      * params: { context: [CallbackContext](../classes/CallbackContext.html); request: [LlmRequest](../interfaces/LlmRequest.html) }

#### Returns [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

The content to return to the user. When present, the model call will be skipped and the provided content will be returned to user.




  * Defined in [core/src/agents/llm_agent.ts:47](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L47)



[ADK for TypeScript: API Reference](../index.html)

  * Loading...


