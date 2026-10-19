[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SingleBeforeModelCallback]()



# Type Alias SingleBeforeModelCallback

SingleBeforeModelCallback: (  
params: { context: [Context](../classes/Context.html); request: [LlmRequest](../interfaces/LlmRequest.html) },  
) => [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

A callback that runs before a request is sent to the model.

#### Type Declaration

  *     * (  
params: { context: [Context](../classes/Context.html); request: [LlmRequest](../interfaces/LlmRequest.html) },  
): [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>
    * #### Parameters

      * params: { context: [Context](../classes/Context.html); request: [LlmRequest](../interfaces/LlmRequest.html) }
        * ##### context: [Context](../classes/Context.html)

The current callback context.

        * ##### request: [LlmRequest](../interfaces/LlmRequest.html)

The raw model request. Callback can mutate the request.

#### Returns [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

The content to return to the user. When present, the model call will be skipped and the provided content will be returned to user.




  * Defined in [core/src/agents/llm_agent.ts:190](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L190)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


