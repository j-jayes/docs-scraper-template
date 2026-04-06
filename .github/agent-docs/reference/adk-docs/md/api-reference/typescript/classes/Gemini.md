[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [Gemini]()



# Class Gemini

Integration for Gemini models.

#### Hierarchy ([View Summary](../hierarchy.html#Gemini))

  * [BaseLlm](BaseLlm.html)
    * Gemini
      * [ApigeeLlm](ApigeeLlm.html)



  * Defined in [models/google_llm.ts:63](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L63)



## Constructors

### constructor

  * new Gemini(params: [GeminiParams](../interfaces/GeminiParams.html)): [Gemini]()

#### Parameters

    * params: [GeminiParams](../interfaces/GeminiParams.html)

The parameters for creating a Gemini instance.

#### Returns [Gemini]()

Overrides [BaseLlm](BaseLlm.html).[constructor](BaseLlm.html#constructor)

    * Defined in [models/google_llm.ts:73](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L73)




## Properties

### `Readonly`[BASE_MODEL_SYMBOL]

"[BASE_MODEL_SYMBOL]": true

A unique symbol to identify BaseLlm classes.

Inherited from [BaseLlm](BaseLlm.html).[[BASE_MODEL_SYMBOL]](BaseLlm.html#base_model_symbol)

  * Defined in [models/base_llm.ts:40](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L40)



### `Readonly`model

model: string

Inherited from [BaseLlm](BaseLlm.html).[model](BaseLlm.html#model)

  * Defined in [models/base_llm.ts:42](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L42)



### `Protected` `Readonly`vertexai

vertexai: boolean

  * Defined in [models/google_llm.ts:65](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L65)



### `Static` `Readonly`supportedModels

supportedModels: (string | RegExp)[] = ...

A list of model name patterns that are supported by this LLM.

#### Returns

A list of supported models.

Overrides [BaseLlm](BaseLlm.html).[supportedModels](BaseLlm.html#supportedmodels)

  * Defined in [models/google_llm.ts:111](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L111)



## Accessors

### apiBackend

  * get apiBackend(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

    * Defined in [models/google_llm.ts:252](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L252)




### apiClient

  * get apiClient(): GoogleGenAI

#### Returns GoogleGenAI

    * Defined in [models/google_llm.ts:231](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L231)




### liveApiClient

  * get liveApiClient(): GoogleGenAI

#### Returns GoogleGenAI

    * Defined in [models/google_llm.ts:276](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L276)




### liveApiVersion

  * get liveApiVersion(): string

#### Returns string

    * Defined in [models/google_llm.ts:261](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L261)




### `Protected`trackingHeaders

  * get trackingHeaders(): Record<string, string>

#### Returns Record<string, string>

Inherited from BaseLlm.trackingHeaders

    * Defined in [models/base_llm.ts:80](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L80)




## Methods

### connect

  * connect(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): Promise<[BaseLlmConnection](../interfaces/BaseLlmConnection.html)>

Connects to the Gemini model and returns an llm connection.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the Gemini model.

#### Returns Promise<[BaseLlmConnection](../interfaces/BaseLlmConnection.html)>

BaseLlmConnection, the connection to the Gemini model.

Overrides [BaseLlm](BaseLlm.html).[connect](BaseLlm.html#connect)

    * Defined in [models/google_llm.ts:292](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L292)




### generateContentAsync

  * generateContentAsync(  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
stream?: boolean,  
): AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

Sends a request to the Gemini model.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the Gemini model.

    * stream: boolean = false

bool = false, whether to do streaming call.

#### Returns AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

#### Yields

LlmResponse: The model response.

Overrides [BaseLlm](BaseLlm.html).[generateContentAsync](BaseLlm.html#generatecontentasync)

    * Defined in [models/google_llm.ts:132](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L132)




### `Protected`getHttpOptions

  * getHttpOptions(): HttpOptions

#### Returns HttpOptions

    * Defined in [models/google_llm.ts:227](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L227)




### `Protected`getLiveHttpOptions

  * getLiveHttpOptions(): HttpOptions

#### Returns HttpOptions

    * Defined in [models/google_llm.ts:269](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L269)




### maybeAppendUserContent

  * maybeAppendUserContent(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): void

Appends a user content, so that model can continue to output.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

#### Returns void

Inherited from [BaseLlm](BaseLlm.html).[maybeAppendUserContent](BaseLlm.html#maybeappendusercontent)

    * Defined in [models/base_llm.ts:94](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L94)




Constructors

constructor

Properties

[BASE_MODEL_SYMBOL]modelvertexaisupportedModels

Accessors

apiBackendapiClientliveApiClientliveApiVersiontrackingHeaders

Methods

connectgenerateContentAsyncgetHttpOptionsgetLiveHttpOptionsmaybeAppendUserContent

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


