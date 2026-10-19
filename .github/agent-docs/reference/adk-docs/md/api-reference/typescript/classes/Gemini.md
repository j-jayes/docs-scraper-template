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



  * Defined in [core/src/models/google_llm.ts:85](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L85)



## Constructors

### constructor

  * new Gemini(params: [GeminiParams](../interfaces/GeminiParams.html)): [Gemini]()

#### Parameters

    * params: [GeminiParams](../interfaces/GeminiParams.html)

The parameters for creating a Gemini instance.

#### Returns [Gemini]()

Overrides [BaseLlm](BaseLlm.html).[constructor](BaseLlm.html#constructor)

    * Defined in [core/src/models/google_llm.ts:97](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L97)




## Properties

### `Readonly`[BASE_MODEL_SYMBOL]

"[BASE_MODEL_SYMBOL]": true

A unique symbol to identify BaseLlm classes.

Inherited from [BaseLlm](BaseLlm.html).[[BASE_MODEL_SYMBOL]](BaseLlm.html#base_model_symbol)

  * Defined in [core/src/models/base_llm.ts:40](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/base_llm.ts#L40)



### `Readonly`[GEMINI_MODEL_SYMBOL]

"[GEMINI_MODEL_SYMBOL]": true

  * Defined in [core/src/models/google_llm.ts:86](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L86)



### `Readonly`model

model: string

Inherited from [BaseLlm](BaseLlm.html).[model](BaseLlm.html#model)

  * Defined in [core/src/models/base_llm.ts:42](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/base_llm.ts#L42)



### `Readonly`useInteractionsApi

useInteractionsApi: boolean

  * Defined in [core/src/models/google_llm.ts:92](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L92)



### `Protected` `Readonly`vertexai

vertexai: boolean

  * Defined in [core/src/models/google_llm.ts:88](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L88)



### `Static` `Readonly`supportedModels

supportedModels: (string | RegExp)[] = ...

A list of model name patterns that are supported by this LLM.

#### Returns

A list of supported models.

Overrides [BaseLlm](BaseLlm.html).[supportedModels](BaseLlm.html#supportedmodels)

  * Defined in [core/src/models/google_llm.ts:137](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L137)



## Accessors

### apiBackend

  * get apiBackend(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

    * Defined in [core/src/models/google_llm.ts:245](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L245)




### apiClient

  * get apiClient(): GoogleGenAI

#### Returns GoogleGenAI

    * Defined in [core/src/models/google_llm.ts:224](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L224)




### liveApiClient

  * get liveApiClient(): GoogleGenAI

#### Returns GoogleGenAI

    * Defined in [core/src/models/google_llm.ts:270](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L270)




### liveApiVersion

  * get liveApiVersion(): string

#### Returns string

    * Defined in [core/src/models/google_llm.ts:254](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L254)




### `Protected`trackingHeaders

  * get trackingHeaders(): Record<string, string>

#### Returns Record<string, string>

Inherited from BaseLlm.trackingHeaders

    * Defined in [core/src/models/base_llm.ts:81](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/base_llm.ts#L81)




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

    * Defined in [core/src/models/google_llm.ts:295](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L295)




### generateContentAsync

  * generateContentAsync(  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
stream?: boolean,  
abortSignal?: AbortSignal,  
): AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

Sends a request to the Gemini model.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The request to send to the Gemini model.

    * stream: boolean = false

Whether to make a streaming call. Defaults to `false`.

    * `Optional`abortSignal: AbortSignal

#### Returns AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

#### Yields

Each [LlmResponse](../interfaces/LlmResponse.html) produced by the model. A non-streaming call yields exactly one; a streaming call yields the partial responses as they arrive, then a final aggregated response whenever the stream carried either content or usage/grounding/citation metadata. A metadata-only stream therefore still ends with one, holding the metadata and no `content`; only a stream with neither ends silently.

Overrides [BaseLlm](BaseLlm.html).[generateContentAsync](BaseLlm.html#generatecontentasync)

    * Defined in [core/src/models/google_llm.ts:163](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L163)




### `Protected`getHttpOptions

  * getHttpOptions(): HttpOptions

#### Returns HttpOptions

    * Defined in [core/src/models/google_llm.ts:220](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L220)




### `Protected`getLiveHttpOptions

  * getLiveHttpOptions(): HttpOptions

#### Returns HttpOptions

    * Defined in [core/src/models/google_llm.ts:263](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L263)




### maybeAppendUserContent

  * maybeAppendUserContent(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): void

Appends a user content, so that model can continue to output.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

#### Returns void

Inherited from [BaseLlm](BaseLlm.html).[maybeAppendUserContent](BaseLlm.html#maybeappendusercontent)

    * Defined in [core/src/models/base_llm.ts:90](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/base_llm.ts#L90)




Constructors

constructor

Properties

[BASE_MODEL_SYMBOL][GEMINI_MODEL_SYMBOL]modeluseInteractionsApivertexaisupportedModels

Accessors

apiBackendapiClientliveApiClientliveApiVersiontrackingHeaders

Methods

connectgenerateContentAsyncgetHttpOptionsgetLiveHttpOptionsmaybeAppendUserContent

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


