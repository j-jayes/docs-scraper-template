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
parentAgent?: [BaseAgent](../classes/BaseAgent.html);  
subAgents?: [BaseAgent](../classes/BaseAgent.html)[];  
}

#### Hierarchy ([View Summary](../hierarchy.html#BaseAgentConfig))

  * BaseAgentConfig
    * [LlmAgentConfig](LlmAgentConfig.html)
    * [LoopAgentConfig](LoopAgentConfig.html)



  * Defined in [agents/base_agent.ts:42](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L42)



## Properties

### `Optional`afterAgentCallback

afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html)

  * Defined in [agents/base_agent.ts:48](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L48)



### `Optional`beforeAgentCallback

beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html)

  * Defined in [agents/base_agent.ts:47](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L47)



### `Optional`description

description?: string

  * Defined in [agents/base_agent.ts:44](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L44)



### name

name: string

  * Defined in [agents/base_agent.ts:43](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L43)



### `Optional`parentAgent

parentAgent?: [BaseAgent](../classes/BaseAgent.html)

  * Defined in [agents/base_agent.ts:45](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L45)



### `Optional`subAgents

subAgents?: [BaseAgent](../classes/BaseAgent.html)[]

  * Defined in [agents/base_agent.ts:46](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L46)



Properties

afterAgentCallbackbeforeAgentCallbackdescriptionnameparentAgentsubAgents

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


