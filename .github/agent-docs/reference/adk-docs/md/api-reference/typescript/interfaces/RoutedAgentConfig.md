[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [RoutedAgentConfig]()



# Interface RoutedAgentConfig

Configuration for the RoutingAgent.

interface RoutedAgentConfig {  
afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html);  
agents:  
| [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[]  
| Readonly<Record<string, [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>>>;  
beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html);  
description?: string;  
name: string;  
parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>;  
router: [AgentRouter](../types/AgentRouter.html);  
subAgents?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[];  
}

#### Hierarchy ([View Summary](../hierarchy.html#RoutedAgentConfig))

  * [BaseAgentConfig](BaseAgentConfig.html)
    * RoutedAgentConfig



  * Defined in [core/src/agents/routed_agent.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/routed_agent.ts#L46)



## Properties

### `Optional`afterAgentCallback

afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[afterAgentCallback](BaseAgentConfig.html#afteragentcallback)

  * Defined in [core/src/agents/base_agent.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L48)



### agents

agents:  
| [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[]  
| Readonly<Record<string, [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>>>

The set of agents to route to. Can be an array of agents or a Record of keys to agents. If an array is provided, the agent names will be used as keys.

  * Defined in [core/src/agents/routed_agent.ts:51](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/routed_agent.ts#L51)



### `Optional`beforeAgentCallback

beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[beforeAgentCallback](BaseAgentConfig.html#beforeagentcallback)

  * Defined in [core/src/agents/base_agent.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L47)



### `Optional`description

description?: string

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[description](BaseAgentConfig.html#description)

  * Defined in [core/src/agents/base_agent.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L44)



### name

name: string

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[name](BaseAgentConfig.html#name)

  * Defined in [core/src/agents/base_agent.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L43)



### `Optional`parentAgent

parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[parentAgent](BaseAgentConfig.html#parentagent)

  * Defined in [core/src/agents/base_agent.ts:45](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L45)



### router

router: [AgentRouter](../types/AgentRouter.html)

The function to select which agent to run.

  * Defined in [core/src/agents/routed_agent.ts:56](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/routed_agent.ts#L56)



### `Optional`subAgents

subAgents?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[]

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[subAgents](BaseAgentConfig.html#subagents)

  * Defined in [core/src/agents/base_agent.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L46)



Properties

afterAgentCallbackagentsbeforeAgentCallbackdescriptionnameparentAgentroutersubAgents

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


