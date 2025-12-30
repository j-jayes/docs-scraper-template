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



  * Defined in [core/src/models/google_llm.ts:58](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L58)



## Constructors

### constructor

  * new Gemini(params: [GeminiParams](../interfaces/GeminiParams.html)): [Gemini]()

#### Parameters

    * params: [GeminiParams](../interfaces/GeminiParams.html)

The parameters for creating a Gemini instance.

#### Returns [Gemini]()

Overrides [BaseLlm](BaseLlm.html).[constructor](BaseLlm.html#constructor)

    * Defined in [core/src/models/google_llm.ts:68](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L68)




## Properties

### `Readonly`model

model: string

Inherited from [BaseLlm](BaseLlm.html).[model](BaseLlm.html#model)

  * Defined in [core/src/models/base_llm.ts:15](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/base_llm.ts#L15)



### `Static` `Readonly`supportedModels

supportedModels: (string | RegExp)[] = ...

A list of model name patterns that are supported by this LLM.

#### Returns

A list of supported models.

Overrides [BaseLlm](BaseLlm.html).[supportedModels](BaseLlm.html#supportedmodels)

  * Defined in [core/src/models/google_llm.ts:130](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L130)



## Accessors

### apiBackend

  * get apiBackend(): GoogleLLMVariant

#### Returns GoogleLLMVariant

    * Defined in [core/src/models/google_llm.ts:271](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L271)




### apiClient

  * get apiClient(): GoogleGenAI

#### Returns GoogleGenAI

    * Defined in [core/src/models/google_llm.ts:244](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L244)




### liveApiClient

  * get liveApiClient(): GoogleGenAI

#### Returns GoogleGenAI

    * Defined in [core/src/models/google_llm.ts:309](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L309)




### liveApiVersion

  * get liveApiVersion(): string

#### Returns string

    * Defined in [core/src/models/google_llm.ts:300](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L300)




### trackingHeaders

  * get trackingHeaders(): Record<string, string>

#### Returns Record<string, string>

    * Defined in [core/src/models/google_llm.ts:279](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L279)




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

    * Defined in [core/src/models/google_llm.ts:328](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L328)




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

    * Defined in [core/src/models/google_llm.ts:152](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L152)




### maybeAppendUserContent

  * maybeAppendUserContent(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): void

Appends a user content, so that model can continue to output.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

#### Returns void

Inherited from [BaseLlm](BaseLlm.html).[maybeAppendUserContent](BaseLlm.html#maybeappendusercontent)

    * Defined in [core/src/models/base_llm.ts:56](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/base_llm.ts#L56)




Constructors

constructor

Properties

modelsupportedModels

Accessors

apiBackendapiClientliveApiClientliveApiVersiontrackingHeaders

Methods

connectgenerateContentAsyncmaybeAppendUserContent

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


