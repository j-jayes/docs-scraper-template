[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [RoutedLlm]()



# Class RoutedLlm

A BaseLlm implementation that delegates to one of multiple models based on a router function.

#### Hierarchy ([View Summary](../hierarchy.html#RoutedLlm))

  * [BaseLlm](BaseLlm.html)
    * RoutedLlm



  * Defined in [core/src/models/routed_llm.ts:27](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/routed_llm.ts#L27)



## Constructors

### constructor

  * new RoutedLlm(  
__namedParameters: {  
modelName?: string;  
models: Readonly<Record<string, [BaseLlm](BaseLlm.html)>> | [BaseLlm](BaseLlm.html)[];  
router: [LlmRouter](../types/LlmRouter.html);  
},  
): [RoutedLlm]()

#### Parameters

    * __namedParameters: {  
modelName?: string;  
models: Readonly<Record<string, [BaseLlm](BaseLlm.html)>> | [BaseLlm](BaseLlm.html)[];  
router: [LlmRouter](../types/LlmRouter.html);  
}

#### Returns [RoutedLlm]()

Overrides [BaseLlm](BaseLlm.html).[constructor](BaseLlm.html#constructor)

    * Defined in [core/src/models/routed_llm.ts:31](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/routed_llm.ts#L31)




## Properties

### `Readonly`[BASE_MODEL_SYMBOL]

"[BASE_MODEL_SYMBOL]": true

A unique symbol to identify BaseLlm classes.

Inherited from [BaseLlm](BaseLlm.html).[[BASE_MODEL_SYMBOL]](BaseLlm.html#base_model_symbol)

  * Defined in [core/src/models/base_llm.ts:40](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/base_llm.ts#L40)



### `Readonly`model

model: string

Inherited from [BaseLlm](BaseLlm.html).[model](BaseLlm.html#model)

  * Defined in [core/src/models/base_llm.ts:42](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/base_llm.ts#L42)



### `Static` `Readonly`supportedModels

supportedModels: (string | RegExp)[] = []

List of supported models in regex for LlmRegistry.

Inherited from [BaseLlm](BaseLlm.html).[supportedModels](BaseLlm.html#supportedmodels)

  * Defined in [core/src/models/base_llm.ts:57](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/base_llm.ts#L57)



## Accessors

### `Protected`trackingHeaders

  * get trackingHeaders(): Record<string, string>

#### Returns Record<string, string>

Inherited from BaseLlm.trackingHeaders

    * Defined in [core/src/models/base_llm.ts:81](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/base_llm.ts#L81)




## Methods

### connect

  * connect(llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): Promise<[BaseLlmConnection](../interfaces/BaseLlmConnection.html)>

Creates a live connection to the LLM by delegating to the selected model. This live connection cannot be switched mid-stream, it is tied to the model selected at the time of connection.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

#### Returns Promise<[BaseLlmConnection](../interfaces/BaseLlmConnection.html)>

Overrides [BaseLlm](BaseLlm.html).[connect](BaseLlm.html#connect)

    * Defined in [core/src/models/routed_llm.ts:72](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/routed_llm.ts#L72)




### generateContentAsync

  * generateContentAsync(  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
stream?: boolean,  
): AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

Generates content by delegating to the selected model.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)
    * `Optional`stream: boolean

#### Returns AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

Overrides [BaseLlm](BaseLlm.html).[generateContentAsync](BaseLlm.html#generatecontentasync)

    * Defined in [core/src/models/routed_llm.ts:57](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/routed_llm.ts#L57)




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

[BASE_MODEL_SYMBOL]modelsupportedModels

Accessors

trackingHeaders

Methods

connectgenerateContentAsyncmaybeAppendUserContent

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


