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




  * Defined in [core/src/models/routed_llm.ts:19](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/routed_llm.ts#L19)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


