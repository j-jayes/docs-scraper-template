[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseLlmRequestProcessor]()



# Class BaseLlmRequestProcessor`Abstract`

Base class for LLM request processors. Implementations mutate or augment the [LlmRequest](../interfaces/LlmRequest.html) before it is sent to the model.

#### Hierarchy ([View Summary](../hierarchy.html#BaseLlmRequestProcessor))

  * BaseLlmRequestProcessor
    * [AgentTransferLlmRequestProcessor](AgentTransferLlmRequestProcessor.html)
    * [AuthPreprocessor](AuthPreprocessor.html)



#### Implemented by

  * [ContentRequestProcessor](ContentRequestProcessor.html)
  * [ContextCompactorRequestProcessor](ContextCompactorRequestProcessor.html)
  * [InteractionsRequestProcessor](InteractionsRequestProcessor.html)



  * Defined in [core/src/agents/processors/base_llm_processor.ts:16](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/processors/base_llm_processor.ts#L16)



## Constructors

### constructor

  * new BaseLlmRequestProcessor(): [BaseLlmRequestProcessor]()

#### Returns [BaseLlmRequestProcessor]()




## Methods

### `Abstract`runAsync

  * runAsync(  
invocationContext: [InvocationContext](InvocationContext.html),  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Runs the processor, optionally yielding intermediate [Event](../interfaces/Event.html)s.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The request object to populate or mutate in place.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

    * Defined in [core/src/agents/processors/base_llm_processor.ts:23](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/processors/base_llm_processor.ts#L23)




Constructors

constructor

Methods

runAsync

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


