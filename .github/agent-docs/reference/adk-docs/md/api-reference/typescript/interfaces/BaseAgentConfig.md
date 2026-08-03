[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseAgentConfig]()



# Interface BaseAgentConfig

The config of a base agent.

interface BaseAgentConfig {  
afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html);  
beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html);  
description?: string;  
name: string;  
parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig]()>;  
subAgents?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig]()>[];  
}

#### Hierarchy ([View Summary](../hierarchy.html#BaseAgentConfig))

  * BaseAgentConfig
    * [RemoteA2AAgentConfig](RemoteA2AAgentConfig.html)
    * [LlmAgentConfig](LlmAgentConfig.html)
    * [LoopAgentConfig](LoopAgentConfig.html)
    * [RoutedAgentConfig](RoutedAgentConfig.html)



  * Defined in [core/src/agents/base_agent.ts:42](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L42)



## Properties

### `Optional`afterAgentCallback

afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html)

  * Defined in [core/src/agents/base_agent.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L48)



### `Optional`beforeAgentCallback

beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html)

  * Defined in [core/src/agents/base_agent.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L47)



### `Optional`description

description?: string

  * Defined in [core/src/agents/base_agent.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L44)



### name

name: string

  * Defined in [core/src/agents/base_agent.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L43)



### `Optional`parentAgent

parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig]()>

  * Defined in [core/src/agents/base_agent.ts:45](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L45)



### `Optional`subAgents

subAgents?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig]()>[]

  * Defined in [core/src/agents/base_agent.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L46)



Properties

afterAgentCallbackbeforeAgentCallbackdescriptionnameparentAgentsubAgents

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


