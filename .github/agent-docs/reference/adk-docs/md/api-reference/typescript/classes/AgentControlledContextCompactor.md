[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AgentControlledContextCompactor]()



# Class AgentControlledContextCompactor

A context compactor that triggers compaction when the agent explicitly requests it via the `ConsolidateContextTool`.

#### Implements

  * [BaseContextCompactor](../interfaces/BaseContextCompactor.html)



  * Defined in [core/src/context/agent_controlled_context_compactor.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/agent_controlled_context_compactor.ts#L18)



## Constructors

### constructor

  * new AgentControlledContextCompactor(  
options: { summarizer: [BaseSummarizer](../interfaces/BaseSummarizer.html) },  
): [AgentControlledContextCompactor]()

#### Parameters

    * options: { summarizer: [BaseSummarizer](../interfaces/BaseSummarizer.html) }

#### Returns [AgentControlledContextCompactor]()

    * Defined in [core/src/context/agent_controlled_context_compactor.ts:22](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/agent_controlled_context_compactor.ts#L22)




## Properties

### `Readonly`trigger

trigger: [AgentControlled](../enums/ContextCompactionTrigger.html#agentcontrolled) = ContextCompactionTrigger.AgentControlled

The trigger associated with this compactor.

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[trigger](../interfaces/BaseContextCompactor.html#trigger)

  * Defined in [core/src/context/agent_controlled_context_compactor.ts:19](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/agent_controlled_context_compactor.ts#L19)



## Methods

### compact

  * compact(invocationContext: [InvocationContext](InvocationContext.html)): Promise<void>

Compacts the context in place.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns Promise<void>

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[compact](../interfaces/BaseContextCompactor.html#compact)

    * Defined in [core/src/context/agent_controlled_context_compactor.ts:30](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/agent_controlled_context_compactor.ts#L30)




### shouldCompact

  * shouldCompact(invocationContext: [InvocationContext](InvocationContext.html)): boolean

Determines whether the context should be compacted.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The current invocation context.

#### Returns boolean

A boolean or a promise resolving to a boolean indicating if compaction should occur.

Implementation of [BaseContextCompactor](../interfaces/BaseContextCompactor.html).[shouldCompact](../interfaces/BaseContextCompactor.html#shouldcompact)

    * Defined in [core/src/context/agent_controlled_context_compactor.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/context/agent_controlled_context_compactor.ts#L26)




Constructors

constructor

Properties

trigger

Methods

compactshouldCompact

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


