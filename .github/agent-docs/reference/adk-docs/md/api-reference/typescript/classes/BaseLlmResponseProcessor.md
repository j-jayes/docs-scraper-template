[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseLlmResponseProcessor]()



# Class BaseLlmResponseProcessor`Abstract`

Base class for LLM response processors. Implementations inspect or transform the [LlmResponse](../interfaces/LlmResponse.html) after it is received from the model.

  * Defined in [core/src/agents/processors/base_llm_processor.ts:33](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/processors/base_llm_processor.ts#L33)



## Constructors

### constructor

  * new BaseLlmResponseProcessor(): [BaseLlmResponseProcessor]()

#### Returns [BaseLlmResponseProcessor]()




## Methods

### `Abstract`runAsync

  * runAsync(  
invocationContext: [InvocationContext](InvocationContext.html),  
llmResponse: [LlmResponse](../interfaces/LlmResponse.html),  
): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Runs the processor, optionally yielding intermediate [Event](../interfaces/Event.html)s.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

    * llmResponse: [LlmResponse](../interfaces/LlmResponse.html)

The response received from the model.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

    * Defined in [core/src/agents/processors/base_llm_processor.ts:40](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/processors/base_llm_processor.ts#L40)




Constructors

constructor

Methods

runAsync

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


