[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseLlmResponseProcessor]()



# Class BaseLlmResponseProcessor`Abstract`

Base class for LLM response processor.

  * Defined in [agents/processors/base_llm_processor.ts:28](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/processors/base_llm_processor.ts#L28)



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

Processes the LLM response.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)
    * llmResponse: [LlmResponse](../interfaces/LlmResponse.html)

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

    * Defined in [agents/processors/base_llm_processor.ts:32](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/processors/base_llm_processor.ts#L32)




Constructors

constructor

Methods

runAsync

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


