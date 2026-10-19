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
inputSchema?: [SchemaLike](../types/SchemaLike.html);  
isolationScope?: string | true;  
messageSendConfig?: MessageSendConfiguration;  
metadata?: Record<string, unknown>;  
name: string;  
outputSchema?: [SchemaLike](../types/SchemaLike.html);  
parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>;  
rerunOnResume?: boolean;  
retryConfig?: [RetryConfig](RetryConfig.html);  
stateSchema?: [SchemaLike](../types/SchemaLike.html);  
subAgents?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[];  
timeout?: number;  
waitForOutput?: boolean;  
}

#### Hierarchy ([View Summary](../hierarchy.html#RemoteA2AAgentConfig))

  * [BaseAgentConfig](BaseAgentConfig.html)
    * RemoteA2AAgentConfig



  * Defined in [core/src/a2a/a2a_remote_agent.ts:82](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/a2a/a2a_remote_agent.ts#L82)



## Properties

### `Optional`afterAgentCallback

afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[afterAgentCallback](BaseAgentConfig.html#afteragentcallback)

  * Defined in [core/src/agents/base_agent.ts:55](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L55)



### `Optional`afterRequestCallbacks

afterRequestCallbacks?: [AfterA2ARequestCallback](../types/AfterA2ARequestCallback.html)[]

Callbacks run after receiving a response chunk or event, before conversion.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:108](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/a2a/a2a_remote_agent.ts#L108)



### `Optional`agentCard

agentCard?: string | AgentCard

Loaded AgentCard or URL to AgentCard.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:86](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/a2a/a2a_remote_agent.ts#L86)



### `Optional`beforeAgentCallback

beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[beforeAgentCallback](BaseAgentConfig.html#beforeagentcallback)

  * Defined in [core/src/agents/base_agent.ts:54](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L54)



### `Optional`beforeRequestCallbacks

beforeRequestCallbacks?: [BeforeA2ARequestCallback](../types/BeforeA2ARequestCallback.html)[]

Callbacks run before the remote request is sent.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:104](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/a2a/a2a_remote_agent.ts#L104)



### `Optional`client

client?: Client

Optional pre-initialized Client for connection pooling.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:91](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/a2a/a2a_remote_agent.ts#L91)



### `Optional`clientFactory

clientFactory?: ClientFactory

Optional ClientFactory for creating the A2A Client.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:96](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/a2a/a2a_remote_agent.ts#L96)



### `Optional`description

description?: string

Human-readable description (used when a node is exposed as a tool).

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[description](BaseAgentConfig.html#description)

  * Defined in [core/src/agents/base_agent.ts:51](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L51)



### `Optional`inputSchema

inputSchema?: [SchemaLike](../types/SchemaLike.html)

Optional schema validating the node input (Zod v3/v4 or genai `Schema`).

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[inputSchema](BaseAgentConfig.html#inputschema)

  * Defined in [core/src/workflow/base_node.ts:62](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L62)



### `Optional`isolationScope

isolationScope?: string | true

Runs this node's subtree in an isolated conversation scope: an agent inside it sees only session events carrying the same scope, plus untagged ones. `true` derives a scope per node run; a string is an explicit shared tag.

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[isolationScope](BaseAgentConfig.html#isolationscope)

  * Defined in [core/src/workflow/base_node.ts:75](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L75)



### `Optional`messageSendConfig

messageSendConfig?: MessageSendConfiguration

Optional default configuration for sending messages.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:100](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/a2a/a2a_remote_agent.ts#L100)



### `Optional`metadata

metadata?: Record<string, unknown>

Optional request-level metadata to include in the A2A message send request. If omitted, defaults to `context.a2aMetadata` from the current invocation context.

  * Defined in [core/src/a2a/a2a_remote_agent.ts:113](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/a2a/a2a_remote_agent.ts#L113)



### name

name: string

Canonical, unique-within-a-graph node name.

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[name](BaseAgentConfig.html#name)

  * Defined in [core/src/agents/base_agent.ts:50](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L50)



### `Optional`outputSchema

outputSchema?: [SchemaLike](../types/SchemaLike.html)

Optional schema validating the node output (Zod v3/v4 or genai `Schema`).

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[outputSchema](BaseAgentConfig.html#outputschema)

  * Defined in [core/src/workflow/base_node.ts:65](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L65)



### `Optional`parentAgent

parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[parentAgent](BaseAgentConfig.html#parentagent)

  * Defined in [core/src/agents/base_agent.ts:52](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L52)



### `Optional`rerunOnResume

rerunOnResume?: boolean

If true, the node re-executes when a workflow resumes even if it already completed in a prior turn. Default false.

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[rerunOnResume](BaseAgentConfig.html#rerunonresume)

  * Defined in [core/src/workflow/base_node.ts:47](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L47)



### `Optional`retryConfig

retryConfig?: [RetryConfig](RetryConfig.html)

Optional retry configuration for transient failures.

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[retryConfig](BaseAgentConfig.html#retryconfig)

  * Defined in [core/src/workflow/base_node.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L56)



### `Optional`stateSchema

stateSchema?: [SchemaLike](../types/SchemaLike.html)

Optional schema validating relevant session state (Zod v3/v4 or genai `Schema`).

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[stateSchema](BaseAgentConfig.html#stateschema)

  * Defined in [core/src/workflow/base_node.ts:68](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L68)



### `Optional`subAgents

subAgents?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[]

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[subAgents](BaseAgentConfig.html#subagents)

  * Defined in [core/src/agents/base_agent.ts:53](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L53)



### `Optional`timeout

timeout?: number

Maximum time, in seconds, for this node to complete.

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[timeout](BaseAgentConfig.html#timeout)

  * Defined in [core/src/workflow/base_node.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L59)



### `Optional`waitForOutput

waitForOutput?: boolean

If true, the node only produces its output once all of its predecessors have triggered it (fan-in / join semantics). Default false.

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[waitForOutput](BaseAgentConfig.html#waitforoutput)

  * Defined in [core/src/workflow/base_node.ts:53](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L53)



Properties

afterAgentCallbackafterRequestCallbacksagentCardbeforeAgentCallbackbeforeRequestCallbacksclientclientFactorydescriptioninputSchemaisolationScopemessageSendConfigmetadatanameoutputSchemaparentAgentrerunOnResumeretryConfigstateSchemasubAgentstimeoutwaitForOutput

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


