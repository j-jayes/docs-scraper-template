[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ContextCompactorRequestProcessor]()



# Class ContextCompactorRequestProcessor

A processor that evaluates a set of compactors to optionally compact the conversation history (events) prior to generating an LLM request.

It evaluates each compactor in priority order. The first one that indicates it should compact will perform the compaction and iteration stops.

#### Implements

  * [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html)



  * Defined in [core/src/agents/processors/context_compactor_request_processor.ts:21](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/processors/context_compactor_request_processor.ts#L21)



## Constructors

### constructor

  * new ContextCompactorRequestProcessor(  
compactors: [BaseContextCompactor](../interfaces/BaseContextCompactor.html)[],  
): [ContextCompactorRequestProcessor]()

#### Parameters

    * compactors: [BaseContextCompactor](../interfaces/BaseContextCompactor.html)[]

Ordered list of compactors to evaluate; the first one that reports it should compact will perform the compaction.

#### Returns [ContextCompactorRequestProcessor]()

    * Defined in [core/src/agents/processors/context_compactor_request_processor.ts:28](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/processors/context_compactor_request_processor.ts#L28)




## Methods

### runAsync

  * runAsync(  
invocationContext: [InvocationContext](InvocationContext.html),  
_llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Evaluates compactors in priority order. The first compactor that indicates it should compact will compact the session history, fire plugin hooks, and yield any newly generated events. Iteration stops after one compaction.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

    * _llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

Unused; present to satisfy the [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html) interface.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Implementation of [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html).[runAsync](BaseLlmRequestProcessor.html#runasync)

    * Defined in [core/src/agents/processors/context_compactor_request_processor.ts:40](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/processors/context_compactor_request_processor.ts#L40)




Constructors

constructor

Methods

runAsync

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


