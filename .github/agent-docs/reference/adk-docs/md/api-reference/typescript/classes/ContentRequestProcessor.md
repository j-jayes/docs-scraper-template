[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ContentRequestProcessor]()



# Class ContentRequestProcessor

Populates [LlmRequest.contents](../interfaces/LlmRequest.html#contents) from the session event history.

When a [CompactedEvent](../interfaces/CompactedEvent.html) exists in the session, only the most recent compacted event and the raw events that follow it are included, eliding earlier history. The extent of context included depends on the agent's `includeContents` setting: `'default'` sends the full visible history while any other value sends only the current-turn context.

#### Implements

  * [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html)



  * Defined in [core/src/agents/processors/content_request_processor.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/processors/content_request_processor.ts#L27)



## Constructors

### constructor

  * new ContentRequestProcessor(): [ContentRequestProcessor]()

#### Returns [ContentRequestProcessor]()




## Methods

### runAsync

  * runAsync(  
invocationContext: [InvocationContext](InvocationContext.html),  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Fills [LlmRequest.contents](../interfaces/LlmRequest.html#contents) based on the session event history and agent configuration.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The request whose contents field will be populated.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Implementation of [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html).[runAsync](BaseLlmRequestProcessor.html#runasync)

    * Defined in [core/src/agents/processors/content_request_processor.ts:36](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/processors/content_request_processor.ts#L36)




Constructors

constructor

Methods

runAsync

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


