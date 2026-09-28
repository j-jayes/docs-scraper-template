[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [A2AAgentExecutor]()



# Class A2AAgentExecutor

AgentExecutor invokes an ADK agent and translates session events to A2A events.

#### Implements

  * AgentExecutor



  * Defined in [core/src/a2a/agent_executor.ts:83](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_executor.ts#L83)



## Constructors

### constructor

  * new A2AAgentExecutor(config: [AgentExecutorConfig](../interfaces/AgentExecutorConfig.html)): [A2AAgentExecutor]()

#### Parameters

    * config: [AgentExecutorConfig](../interfaces/AgentExecutorConfig.html)

#### Returns [A2AAgentExecutor]()

    * Defined in [core/src/a2a/agent_executor.ts:86](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_executor.ts#L86)




## Methods

### cancelTask

  * cancelTask(_taskId: string): Promise<void>

Method to explicitly cancel a running task. The implementation should handle the logic of stopping the execution and publishing the final 'canceled' status event on the provided event bus.

#### Parameters

    * _taskId: string

#### Returns Promise<void>

Implementation of AgentExecutor.cancelTask

    * Defined in [core/src/a2a/agent_executor.ts:200](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_executor.ts#L200)




### execute

  * execute(ctx: RequestContext, eventBus: ExecutionEventBus): Promise<void>

Executes the agent logic based on the request context and publishes events.

#### Parameters

    * ctx: RequestContext
    * eventBus: ExecutionEventBus

The bus to publish execution events to.

#### Returns Promise<void>

Implementation of AgentExecutor.execute

    * Defined in [core/src/a2a/agent_executor.ts:88](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_executor.ts#L88)




Constructors

constructor

Methods

cancelTaskexecute

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


