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



  * Defined in [core/src/models/google_llm.ts:84](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L84)



## Constructors

### constructor

  * new Gemini(params: [GeminiParams](../interfaces/GeminiParams.html)): [Gemini]()

#### Parameters

    * params: [GeminiParams](../interfaces/GeminiParams.html)

The parameters for creating a Gemini instance.

#### Returns [Gemini]()

Overrides [BaseLlm](BaseLlm.html).[constructor](BaseLlm.html#constructor)

    * Defined in [core/src/models/google_llm.ts:96](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L96)




## Properties

### `Readonly`[BASE_MODEL_SYMBOL]

"[BASE_MODEL_SYMBOL]": true

A unique symbol to identify BaseLlm classes.

Inherited from [BaseLlm](BaseLlm.html).[[BASE_MODEL_SYMBOL]](BaseLlm.html#base_model_symbol)

  * Defined in [core/src/models/base_llm.ts:40](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm.ts#L40)



### `Readonly`[GEMINI_MODEL_SYMBOL]

"[GEMINI_MODEL_SYMBOL]": true

  * Defined in [core/src/models/google_llm.ts:85](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L85)



### `Readonly`model

model: string

Inherited from [BaseLlm](BaseLlm.html).[model](BaseLlm.html#model)

  * Defined in [core/src/models/base_llm.ts:42](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm.ts#L42)



### `Readonly`useInteractionsApi

useInteractionsApi: boolean

  * Defined in [core/src/models/google_llm.ts:91](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L91)



### `Protected` `Readonly`vertexai

vertexai: boolean

  * Defined in [core/src/models/google_llm.ts:87](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L87)



### `Static` `Readonly`supportedModels

supportedModels: (string | RegExp)[] = ...

A list of model name patterns that are supported by this LLM.

#### Returns

A list of supported models.

Overrides [BaseLlm](BaseLlm.html).[supportedModels](BaseLlm.html#supportedmodels)

  * Defined in [core/src/models/google_llm.ts:136](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L136)



## Accessors

### apiBackend

  * get apiBackend(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

    * Defined in [core/src/models/google_llm.ts:239](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L239)




### apiClient

  * get apiClient(): GoogleGenAI

#### Returns GoogleGenAI

    * Defined in [core/src/models/google_llm.ts:218](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L218)




### liveApiClient

  * get liveApiClient(): GoogleGenAI

#### Returns GoogleGenAI

    * Defined in [core/src/models/google_llm.ts:263](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L263)




### liveApiVersion

  * get liveApiVersion(): string

#### Returns string

    * Defined in [core/src/models/google_llm.ts:248](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L248)




### `Protected`trackingHeaders

  * get trackingHeaders(): Record<string, string>

#### Returns Record<string, string>

Inherited from BaseLlm.trackingHeaders

    * Defined in [core/src/models/base_llm.ts:81](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm.ts#L81)




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

    * Defined in [core/src/models/google_llm.ts:288](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L288)




### generateContentAsync

  * generateContentAsync(  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
stream?: boolean,  
abortSignal?: AbortSignal,  
): AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

Sends a request to the Gemini model.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the Gemini model.

    * stream: boolean = false

bool = false, whether to do streaming call.

    * `Optional`abortSignal: AbortSignal

#### Returns AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

#### Yields

LlmResponse: The model response.

Overrides [BaseLlm](BaseLlm.html).[generateContentAsync](BaseLlm.html#generatecontentasync)

    * Defined in [core/src/models/google_llm.ts:157](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L157)




### `Protected`getHttpOptions

  * getHttpOptions(): HttpOptions

#### Returns HttpOptions

    * Defined in [core/src/models/google_llm.ts:214](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L214)




### `Protected`getLiveHttpOptions

  * getLiveHttpOptions(): HttpOptions

#### Returns HttpOptions

    * Defined in [core/src/models/google_llm.ts:256](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L256)




### maybeAppendUserContent

  * maybeAppendUserContent(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): void

Appends a user content, so that model can continue to output.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

#### Returns void

Inherited from [BaseLlm](BaseLlm.html).[maybeAppendUserContent](BaseLlm.html#maybeappendusercontent)

    * Defined in [core/src/models/base_llm.ts:95](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/base_llm.ts#L95)




Constructors

constructor

Properties

[BASE_MODEL_SYMBOL][GEMINI_MODEL_SYMBOL]modeluseInteractionsApivertexaisupportedModels

Accessors

apiBackendapiClientliveApiClientliveApiVersiontrackingHeaders

Methods

connectgenerateContentAsyncgetHttpOptionsgetLiveHttpOptionsmaybeAppendUserContent

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


