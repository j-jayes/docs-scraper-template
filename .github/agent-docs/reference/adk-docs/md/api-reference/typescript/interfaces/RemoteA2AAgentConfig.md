[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [RemoteA2AAgentConfig]()



# Interface RemoteA2AAgentConfig

Configuration for the A2ARemoteAgent.

interface RemoteA2AAgentConfig {  
afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html);  
afterRequestCallbacks?: [AfterA2ARequestCallback](../types/AfterA2ARequestCallback.html)[];  
agentCard?: string | AgentCard;  
beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html);  
beforeRequestCallbacks?: [BeforeA2ARequestCallback](../types/BeforeA2ARequestCallback.html)[];  
client?: Client;  
clientFactory?: ClientFactory;  
description?: string;  
messageSendConfig?: MessageSendConfiguration;  
name: string;  
parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>;  
subAgents?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[];  
}

#### Hierarchy ([View Summary](../hierarchy.html#RemoteA2AAgentConfig))

  * [BaseAgentConfig](BaseAgentConfig.html)
    * RemoteA2AAgentConfig



  * Defined in [core/src/a2a/a2a_remote_agent.ts:81](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/a2a_remote_agent.ts#L81)



## Properties

### `Optional`afterAgentCallback

afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[afterAgentCallback](BaseAgentConfig.html#afteragentcallback)

  * Defined in [core/src/agents/base_agent.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L48)



### `Optional`afterRequestCallbacks

afterRequestCallbacks?: [AfterA2ARequestCallback](../types/AfterA2ARequestCallback.html)[]

Callbacks run after receiving a response chunk or event, before conversion.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:107](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/a2a_remote_agent.ts#L107)



### `Optional`agentCard

agentCard?: string | AgentCard

Loaded AgentCard or URL to AgentCard.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:85](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/a2a_remote_agent.ts#L85)



### `Optional`beforeAgentCallback

beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[beforeAgentCallback](BaseAgentConfig.html#beforeagentcallback)

  * Defined in [core/src/agents/base_agent.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L47)



### `Optional`beforeRequestCallbacks

beforeRequestCallbacks?: [BeforeA2ARequestCallback](../types/BeforeA2ARequestCallback.html)[]

Callbacks run before the remote request is sent.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:103](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/a2a_remote_agent.ts#L103)



### `Optional`client

client?: Client

Optional pre-initialized Client for connection pooling.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:90](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/a2a_remote_agent.ts#L90)



### `Optional`clientFactory

clientFactory?: ClientFactory

Optional ClientFactory for creating the A2A Client.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:95](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/a2a_remote_agent.ts#L95)



### `Optional`description

description?: string

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[description](BaseAgentConfig.html#description)

  * Defined in [core/src/agents/base_agent.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L44)



### `Optional`messageSendConfig

messageSendConfig?: MessageSendConfiguration

Optional default configuration for sending messages.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:99](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/a2a_remote_agent.ts#L99)



### name

name: string

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[name](BaseAgentConfig.html#name)

  * Defined in [core/src/agents/base_agent.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L43)



### `Optional`parentAgent

parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[parentAgent](BaseAgentConfig.html#parentagent)

  * Defined in [core/src/agents/base_agent.ts:45](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L45)



### `Optional`subAgents

subAgents?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[]

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[subAgents](BaseAgentConfig.html#subagents)

  * Defined in [core/src/agents/base_agent.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L46)



Properties

afterAgentCallbackafterRequestCallbacksagentCardbeforeAgentCallbackbeforeRequestCallbacksclientclientFactorydescriptionmessageSendConfignameparentAgentsubAgents

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


