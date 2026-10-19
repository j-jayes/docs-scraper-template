[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SingleAfterModelCallback]()



# Type Alias SingleAfterModelCallback

SingleAfterModelCallback: (  
params: { context: [Context](../classes/Context.html); response: [LlmResponse](../interfaces/LlmResponse.html) },  
) => [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

A callback that runs after a response is received from the model.

#### Type Declaration

  *     * (  
params: { context: [Context](../classes/Context.html); response: [LlmResponse](../interfaces/LlmResponse.html) },  
): [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>
    * #### Parameters

      * params: { context: [Context](../classes/Context.html); response: [LlmResponse](../interfaces/LlmResponse.html) }
        * ##### context: [Context](../classes/Context.html)

The current callback context.

        * ##### response: [LlmResponse](../interfaces/LlmResponse.html)

The actual model response.

#### Returns [LlmResponse](../interfaces/LlmResponse.html) | undefined | Promise<[LlmResponse](../interfaces/LlmResponse.html) | undefined>

The content to return to the user. When present, the actual model response will be ignored and the provided content will be returned to user.




  * Defined in [core/src/agents/llm_agent.ts:214](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L214)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


