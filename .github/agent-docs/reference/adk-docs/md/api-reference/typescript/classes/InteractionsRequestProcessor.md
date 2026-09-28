[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InteractionsRequestProcessor]()



# Class InteractionsRequestProcessor

Request processor for Gemini Interactions API. Resolves the previous interaction ID from the session history.

#### Implements

  * [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html)



  * Defined in [core/src/agents/processors/interactions_request_processor.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/processors/interactions_request_processor.ts#L18)



## Constructors

### constructor

  * new InteractionsRequestProcessor(): [InteractionsRequestProcessor]()

#### Returns [InteractionsRequestProcessor]()




## Methods

### runAsync

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

Implementation of [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html).[runAsync](BaseLlmRequestProcessor.html#runasync)

    * Defined in [core/src/agents/processors/interactions_request_processor.ts:20](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/processors/interactions_request_processor.ts#L20)




Constructors

constructor

Methods

runAsync

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


