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
inputSchema?: [SchemaLike](../types/SchemaLike.html);  
isolationScope?: string | true;  
name: string;  
outputSchema?: [SchemaLike](../types/SchemaLike.html);  
parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>;  
rerunOnResume?: boolean;  
retryConfig?: [RetryConfig](RetryConfig.html);  
router: [AgentRouter](../types/AgentRouter.html);  
stateSchema?: [SchemaLike](../types/SchemaLike.html);  
subAgents?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[];  
timeout?: number;  
waitForOutput?: boolean;  
}

#### Hierarchy ([View Summary](../hierarchy.html#RoutedAgentConfig))

  * [BaseAgentConfig](BaseAgentConfig.html)
    * RoutedAgentConfig



  * Defined in [core/src/agents/routed_agent.ts:45](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/routed_agent.ts#L45)



## Properties

### `Optional`afterAgentCallback

afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[afterAgentCallback](BaseAgentConfig.html#afteragentcallback)

  * Defined in [core/src/agents/base_agent.ts:55](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L55)



### agents

agents:  
| [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[]  
| Readonly<Record<string, [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>>>

The set of agents to route to. Can be an array of agents or a Record of keys to agents. If an array is provided, the agent names will be used as keys.

  * Defined in [core/src/agents/routed_agent.ts:50](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/routed_agent.ts#L50)



### `Optional`beforeAgentCallback

beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[beforeAgentCallback](BaseAgentConfig.html#beforeagentcallback)

  * Defined in [core/src/agents/base_agent.ts:54](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L54)



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



### router

router: [AgentRouter](../types/AgentRouter.html)

The function to select which agent to run.

  * Defined in [core/src/agents/routed_agent.ts:55](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/routed_agent.ts#L55)



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

afterAgentCallbackagentsbeforeAgentCallbackdescriptioninputSchemaisolationScopenameoutputSchemaparentAgentrerunOnResumeretryConfigrouterstateSchemasubAgentstimeoutwaitForOutput

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


