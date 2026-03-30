[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LoopAgentConfig]()



# Interface LoopAgentConfig

The configuration options for creating a loop agent.

interface LoopAgentConfig {  
afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html);  
beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html);  
description?: string;  
maxIterations?: number;  
name: string;  
parentAgent?: [BaseAgent](../classes/BaseAgent.html);  
subAgents?: [BaseAgent](../classes/BaseAgent.html)[];  
}

#### Hierarchy ([View Summary](../hierarchy.html#LoopAgentConfig))

  * [BaseAgentConfig](BaseAgentConfig.html)
    * LoopAgentConfig



  * Defined in [agents/loop_agent.ts:15](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/loop_agent.ts#L15)



## Properties

### `Optional`afterAgentCallback

afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[afterAgentCallback](BaseAgentConfig.html#afteragentcallback)

  * Defined in [agents/base_agent.ts:48](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L48)



### `Optional`beforeAgentCallback

beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[beforeAgentCallback](BaseAgentConfig.html#beforeagentcallback)

  * Defined in [agents/base_agent.ts:47](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L47)



### `Optional`description

description?: string

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[description](BaseAgentConfig.html#description)

  * Defined in [agents/base_agent.ts:44](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L44)



### `Optional`maxIterations

maxIterations?: number

The maximum number of iterations the loop agent will run.

If not provided, the loop agent will run indefinitely.

  * Defined in [agents/loop_agent.ts:21](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/loop_agent.ts#L21)



### name

name: string

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[name](BaseAgentConfig.html#name)

  * Defined in [agents/base_agent.ts:43](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L43)



### `Optional`parentAgent

parentAgent?: [BaseAgent](../classes/BaseAgent.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[parentAgent](BaseAgentConfig.html#parentagent)

  * Defined in [agents/base_agent.ts:45](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L45)



### `Optional`subAgents

subAgents?: [BaseAgent](../classes/BaseAgent.html)[]

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[subAgents](BaseAgentConfig.html#subagents)

  * Defined in [agents/base_agent.ts:46](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L46)



Properties

afterAgentCallbackbeforeAgentCallbackdescriptionmaxIterationsnameparentAgentsubAgents

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


