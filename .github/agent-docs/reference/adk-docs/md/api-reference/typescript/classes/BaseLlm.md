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



  * Defined in [models/base_llm.ts:36](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L36)



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

    * Defined in [models/base_llm.ts:50](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L50)




## Properties

### `Readonly`[BASE_MODEL_SYMBOL]

"[BASE_MODEL_SYMBOL]": true

A unique symbol to identify BaseLlm classes.

  * Defined in [models/base_llm.ts:40](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L40)



### `Readonly`model

model: string

  * Defined in [models/base_llm.ts:42](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L42)



### `Static` `Readonly`supportedModels

supportedModels: (string | RegExp)[] = []

List of supported models in regex for LlmRegistry.

  * Defined in [models/base_llm.ts:57](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L57)



## Accessors

### `Protected`trackingHeaders

  * get trackingHeaders(): Record<string, string>

#### Returns Record<string, string>

    * Defined in [models/base_llm.ts:80](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L80)




## Methods

### `Abstract`connect

  * connect(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): Promise<[BaseLlmConnection](../interfaces/BaseLlmConnection.html)>

Creates a live connection to the LLM.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

#### Returns Promise<[BaseLlmConnection](../interfaces/BaseLlmConnection.html)>

A live connection to the LLM.

    * Defined in [models/base_llm.ts:78](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L78)




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

    * Defined in [models/base_llm.ts:67](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L67)




### maybeAppendUserContent

  * maybeAppendUserContent(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): void

Appends a user content, so that model can continue to output.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

#### Returns void

    * Defined in [models/base_llm.ts:94](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L94)




Constructors

constructor

Properties

[BASE_MODEL_SYMBOL]modelsupportedModels

Accessors

trackingHeaders

Methods

connectgenerateContentAsyncmaybeAppendUserContent

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


