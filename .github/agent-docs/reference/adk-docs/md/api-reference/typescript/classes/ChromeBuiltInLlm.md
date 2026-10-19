[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ChromeBuiltInLlm]()



# Class ChromeBuiltInLlm

See the file overview for the design rationale.

#### Hierarchy ([View Summary](../hierarchy.html#ChromeBuiltInLlm))

  * [BaseLlm](BaseLlm.html)
    * ChromeBuiltInLlm



  * Defined in [core/src/models/chrome_prompt_llm.ts:247](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L247)



## Constructors

### constructor

  * new ChromeBuiltInLlm(params?: [ChromeBuiltInLlmParams](../interfaces/ChromeBuiltInLlmParams.html)): [ChromeBuiltInLlm]()

#### Parameters

    * params: [ChromeBuiltInLlmParams](../interfaces/ChromeBuiltInLlmParams.html) = {}

#### Returns [ChromeBuiltInLlm]()

Overrides [BaseLlm](BaseLlm.html).[constructor](BaseLlm.html#constructor)

    * Defined in [core/src/models/chrome_prompt_llm.ts:272](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L272)




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

supportedModels: (string | RegExp)[] = ...

List of supported models in regex for LlmRegistry.

Overrides [BaseLlm](BaseLlm.html).[supportedModels](BaseLlm.html#supportedmodels)

  * Defined in [core/src/models/chrome_prompt_llm.ts:251](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L251)



## Accessors

### `Protected`trackingHeaders

  * get trackingHeaders(): Record<string, string>

#### Returns Record<string, string>

Inherited from BaseLlm.trackingHeaders

    * Defined in [core/src/models/base_llm.ts:81](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/base_llm.ts#L81)




## Methods

### availability

  * availability(): Promise<[ChromeModelAvailability](../types/ChromeModelAvailability.html)>

Reports whether this browser can actually run the model.

#### Returns Promise<[ChromeModelAvailability](../types/ChromeModelAvailability.html)>

    * Defined in [core/src/models/chrome_prompt_llm.ts:287](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L287)




### connect

  * connect(_llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): Promise<[BaseLlmConnection](../interfaces/BaseLlmConnection.html)>

Creates a live connection to the LLM.

#### Parameters

    * _llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

#### Returns Promise<[BaseLlmConnection](../interfaces/BaseLlmConnection.html)>

A live connection to the LLM.

Overrides [BaseLlm](BaseLlm.html).[connect](BaseLlm.html#connect)

    * Defined in [core/src/models/chrome_prompt_llm.ts:588](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L588)




### destroy

  * destroy(): void

Releases the warm base session.

#### Returns void

    * Defined in [core/src/models/chrome_prompt_llm.ts:596](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L596)




### generateContentAsync

  * generateContentAsync(  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
stream?: boolean,  
abortSignal?: AbortSignal,  
): AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

Generates one content from the given contents and tools.

#### Parameters

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

LlmRequest, the request to send to the LLM.

    * stream: boolean = false

whether to do streaming call. For non-streaming call, it will only yield one Content.

    * `Optional`abortSignal: AbortSignal

#### Returns AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void>

A generator of LlmResponse.

Overrides [BaseLlm](BaseLlm.html).[generateContentAsync](BaseLlm.html#generatecontentasync)

    * Defined in [core/src/models/chrome_prompt_llm.ts:403](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L403)




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

availabilityconnectdestroygenerateContentAsyncmaybeAppendUserContent

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


