[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InteractionsRequestProcessor]()



# Class InteractionsRequestProcessor

Request processor for Gemini Interactions API. Resolves the previous interaction ID from the session history.

#### Implements

  * [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html)



  * Defined in [core/src/agents/processors/interactions_request_processor.ts:18](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/processors/interactions_request_processor.ts#L18)



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

    * Defined in [core/src/agents/processors/interactions_request_processor.ts:20](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/processors/interactions_request_processor.ts#L20)




Constructors

constructor

Methods

runAsync

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


