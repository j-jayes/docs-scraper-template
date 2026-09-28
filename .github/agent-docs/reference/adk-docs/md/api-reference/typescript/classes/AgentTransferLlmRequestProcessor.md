[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AgentTransferLlmRequestProcessor]()



# Class AgentTransferLlmRequestProcessor

Augments the [LlmRequest](../interfaces/LlmRequest.html) to support agent transfer. When the current agent has reachable transfer targets (sub-agents, peer agents, or a parent agent), this processor registers a `transfer_to_agent` function tool and appends instructions describing each candidate so the model can choose to hand off control.

#### Hierarchy ([View Summary](../hierarchy.html#AgentTransferLlmRequestProcessor))

  * [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html)
    * AgentTransferLlmRequestProcessor



  * Defined in [core/src/agents/processors/agent_transfer_llm_request_processor.ts:24](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/processors/agent_transfer_llm_request_processor.ts#L24)



## Constructors

### constructor

  * new AgentTransferLlmRequestProcessor(): [AgentTransferLlmRequestProcessor]()

#### Returns [AgentTransferLlmRequestProcessor]()

Inherited from [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html).[constructor](BaseLlmRequestProcessor.html#constructor)




## Methods

### runAsync

  * runAsync(  
invocationContext: [InvocationContext](InvocationContext.html),  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Appends transfer instructions and registers the `transfer_to_agent` tool when the agent has reachable transfer targets.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The request to augment with transfer instructions and the transfer tool.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Overrides [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html).[runAsync](BaseLlmRequestProcessor.html#runasync)

    * Defined in [core/src/agents/processors/agent_transfer_llm_request_processor.ts:50](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/processors/agent_transfer_llm_request_processor.ts#L50)




Constructors

constructor

Methods

runAsync

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


