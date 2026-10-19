[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LlmRouter]()



# Type Alias LlmRouter

LlmRouter: (  
models: Readonly<Record<string, [BaseLlm](../classes/BaseLlm.html)>>,  
request: [LlmRequest](../interfaces/LlmRequest.html),  
errorContext?: { failedKeys: ReadonlySet<string>; lastError: unknown },  
) => Promise<string | undefined> | string | undefined

Type definition for a function that selects a model based on the request.

#### Type Declaration

  *     * (  
models: Readonly<Record<string, [BaseLlm](../classes/BaseLlm.html)>>,  
request: [LlmRequest](../interfaces/LlmRequest.html),  
errorContext?: { failedKeys: ReadonlySet<string>; lastError: unknown },  
): Promise<string | undefined> | string | undefined
    * #### Parameters

      * models: Readonly<Record<string, [BaseLlm](../classes/BaseLlm.html)>>
      * request: [LlmRequest](../interfaces/LlmRequest.html)
      * `Optional`errorContext: { failedKeys: ReadonlySet<string>; lastError: unknown }

#### Returns Promise<string | undefined> | string | undefined




  * Defined in [core/src/models/routed_llm.ts:18](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/routed_llm.ts#L18)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


