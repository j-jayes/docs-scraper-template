[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseLlm]()



# Class BaseLlm`Abstract`

The BaseLLM class.

#### Hierarchy ([View Summary](../hierarchy.html#BaseLlm))

  * BaseLlm
    * [Gemini](Gemini.html)



  * Defined in [core/src/models/base_llm.ts:14](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/base_llm.ts#L14)



## Constructors

### constructor

  * new BaseLlm(params: { model: string }): [BaseLlm]()

Creates an instance of BaseLLM.

#### Parameters

    * params: { model: string }

The parameters for creating a BaseLlm instance.

      * ##### model: string

The name of the LLM, e.g. gemini-1.5-flash or gemini-1.5-flash-001.

#### Returns [BaseLlm]()

    * Defined in [core/src/models/base_llm.ts:23](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/base_llm.ts#L23)




## Properties

### `Readonly`model

model: string

  * Defined in [core/src/models/base_llm.ts:15](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/base_llm.ts#L15)



### `Static` `Readonly`supportedModels

supportedModels: (string | RegExp)[] = []

List of supported models in regex for LlmRegistry.

  * Defined in [core/src/models/base_llm.ts:30](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/base_llm.ts#L30)



## Methods

### `Abstract`connect

  * connect(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): Promise<[BaseLlmConnection](../interfaces/BaseLlmConnection.html)>

Creates a live connection to the LLM.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

#### Returns Promise<[BaseLlmConnection](../interfaces/BaseLlmConnection.html)>

A live connection to the LLM.

    * Defined in [core/src/models/base_llm.ts:49](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/base_llm.ts#L49)




### `Abstract`generateContentAsync

  * generateContentAsync(  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
stream?: boolean,  
): AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

Generates one content from the given contents and tools.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

    * `Optional`stream: boolean

whether to do streaming call. For non-streaming call, it will only yield one Content.

#### Returns AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

A generator of LlmResponse.

    * Defined in [core/src/models/base_llm.ts:40](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/base_llm.ts#L40)




### maybeAppendUserContent

  * maybeAppendUserContent(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): void

Appends a user content, so that model can continue to output.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

#### Returns void

    * Defined in [core/src/models/base_llm.ts:56](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/base_llm.ts#L56)




Constructors

constructor

Properties

modelsupportedModels

Methods

connectgenerateContentAsyncmaybeAppendUserContent

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


