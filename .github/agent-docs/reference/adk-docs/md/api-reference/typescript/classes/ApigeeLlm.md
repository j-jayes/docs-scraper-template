[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ApigeeLlm]()



# Class ApigeeLlm

Integration for Gemini models.

#### Hierarchy ([View Summary](../hierarchy.html#ApigeeLlm))

  * [Gemini](Gemini.html)
    * ApigeeLlm



  * Defined in [models/apigee_llm.ts:51](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/apigee_llm.ts#L51)



## Constructors

### constructor

  * new ApigeeLlm(__namedParameters: [ApigeeLlmParams](../interfaces/ApigeeLlmParams.html)): [ApigeeLlm]()

#### Parameters

    * __namedParameters: [ApigeeLlmParams](../interfaces/ApigeeLlmParams.html)

#### Returns [ApigeeLlm]()

Overrides [Gemini](Gemini.html).[constructor](Gemini.html#constructor)

    * Defined in [models/apigee_llm.ts:63](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/apigee_llm.ts#L63)




## Properties

### `Readonly`[BASE_MODEL_SYMBOL]

"[BASE_MODEL_SYMBOL]": true

A unique symbol to identify BaseLlm classes.

Inherited from [Gemini](Gemini.html).[[BASE_MODEL_SYMBOL]](Gemini.html#base_model_symbol)

  * Defined in [models/base_llm.ts:40](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L40)



### `Readonly`model

model: string

Inherited from [Gemini](Gemini.html).[model](Gemini.html#model)

  * Defined in [models/base_llm.ts:42](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/base_llm.ts#L42)



### `Protected` `Readonly`vertexai

vertexai: boolean

Inherited from [Gemini](Gemini.html).[vertexai](Gemini.html#vertexai)

  * Defined in [models/google_llm.ts:65](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L65)



### `Static` `Readonly`supportedModels

supportedModels: (string | RegExp)[] = ...

A list of model name patterns that are supported by this LLM.

#### Returns

A list of supported models.

Overrides [Gemini](Gemini.html).[supportedModels](Gemini.html#supportedmodels)

  * Defined in [models/apigee_llm.ts:59](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/apigee_llm.ts#L59)



## Accessors

### apiBackend

  * get apiBackend(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

Inherited from Gemini.apiBackend

    * Defined in [models/google_llm.ts:252](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L252)




### apiClient

  * get apiClient(): GoogleGenAI

#### Returns GoogleGenAI

Inherited from Gemini.apiClient

    * Defined in [models/google_llm.ts:231](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L231)




### liveApiClient

  * get liveApiClient(): GoogleGenAI

#### Returns GoogleGenAI

Inherited from Gemini.liveApiClient

    * Defined in [models/google_llm.ts:276](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L276)




### liveApiVersion

  * get liveApiVersion(): string

#### Returns string

Overrides Gemini.liveApiVersion

    * Defined in [models/apigee_llm.ts:135](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/apigee_llm.ts#L135)




### `Protected`trackingHeaders

  * get trackingHeaders(): Record<string, string>

#### Returns Record<string, string>

Inherited from Gemini.trackingHeaders

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

Overrides [Gemini](Gemini.html).[connect](Gemini.html#connect)

    * Defined in [models/apigee_llm.ts:151](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/apigee_llm.ts#L151)




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

Overrides [Gemini](Gemini.html).[generateContentAsync](Gemini.html#generatecontentasync)

    * Defined in [models/apigee_llm.ts:142](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/apigee_llm.ts#L142)




### `Protected`getHttpOptions

  * getHttpOptions(): HttpOptions

#### Returns HttpOptions

Overrides [Gemini](Gemini.html).[getHttpOptions](Gemini.html#gethttpoptions)

    * Defined in [models/apigee_llm.ts:98](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/apigee_llm.ts#L98)




### `Protected`getLiveHttpOptions

  * getLiveHttpOptions(): HttpOptions

#### Returns HttpOptions

Overrides [Gemini](Gemini.html).[getLiveHttpOptions](Gemini.html#getlivehttpoptions)

    * Defined in [models/apigee_llm.ts:104](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/apigee_llm.ts#L104)




### maybeAppendUserContent

  * maybeAppendUserContent(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): void

Appends a user content, so that model can continue to output.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

#### Returns void

Inherited from [Gemini](Gemini.html).[maybeAppendUserContent](Gemini.html#maybeappendusercontent)

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


