[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LlmAgentConfig]()



# Interface LlmAgentConfig

The configuration options for creating an LLM-based agent.

interface LlmAgentConfig {  
afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html);  
afterModelCallback?: [AfterModelCallback](../types/AfterModelCallback.html);  
afterToolCallback?: [AfterToolCallback](../types/AfterToolCallback.html);  
beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html);  
beforeModelCallback?: [BeforeModelCallback](../types/BeforeModelCallback.html);  
beforeToolCallback?: [BeforeToolCallback](../types/BeforeToolCallback.html);  
codeExecutor?: [BaseCodeExecutor](../classes/BaseCodeExecutor.html);  
contextCompactors?: [BaseContextCompactor](BaseContextCompactor.html)[];  
description?: string;  
disallowTransferToParent?: boolean;  
disallowTransferToPeers?: boolean;  
generateContentConfig?: GenerateContentConfig;  
globalInstruction?: string | [InstructionProvider](../types/InstructionProvider.html);  
includeContents?: "default" | "none";  
inputSchema?: [LlmAgentSchema](../types/LlmAgentSchema.html);  
instruction?: string | [InstructionProvider](../types/InstructionProvider.html);  
isolationScope?: string | true;  
mode?: "single_turn" | "task";  
model?: string | [BaseLlm](../classes/BaseLlm.html);  
name: string;  
outputKey?: string;  
outputSchema?: [LlmAgentSchema](../types/LlmAgentSchema.html);  
parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>;  
planner?: [BasePlanner](../classes/BasePlanner.html);  
requestProcessors?: [BaseLlmRequestProcessor](../classes/BaseLlmRequestProcessor.html)[];  
rerunOnResume?: boolean;  
responseProcessors?: [BaseLlmResponseProcessor](../classes/BaseLlmResponseProcessor.html)[];  
retryConfig?: [RetryConfig](RetryConfig.html);  
stateSchema?: [SchemaLike](../types/SchemaLike.html);  
subAgents?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>[];  
timeout?: number;  
tools?: [ToolUnion](../types/ToolUnion.html)[];  
waitForOutput?: boolean;  
}

#### Hierarchy ([View Summary](../hierarchy.html#LlmAgentConfig))

  * [BaseAgentConfig](BaseAgentConfig.html)
    * LlmAgentConfig



  * Defined in [core/src/agents/llm_agent.ts:297](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L297)



## Properties

### `Optional`afterAgentCallback

afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[afterAgentCallback](BaseAgentConfig.html#afteragentcallback)

  * Defined in [core/src/agents/base_agent.ts:55](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L55)



### `Optional`afterModelCallback

afterModelCallback?: [AfterModelCallback](../types/AfterModelCallback.html)

Callbacks to be called after calling the LLM.

  * Defined in [core/src/agents/llm_agent.ts:393](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L393)



### `Optional`afterToolCallback

afterToolCallback?: [AfterToolCallback](../types/AfterToolCallback.html)

Callbacks to be called after calling the tool.

  * Defined in [core/src/agents/llm_agent.ts:403](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L403)



### `Optional`beforeAgentCallback

beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[beforeAgentCallback](BaseAgentConfig.html#beforeagentcallback)

  * Defined in [core/src/agents/base_agent.ts:54](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L54)



### `Optional`beforeModelCallback

beforeModelCallback?: [BeforeModelCallback](../types/BeforeModelCallback.html)

Callbacks to be called before calling the LLM.

  * Defined in [core/src/agents/llm_agent.ts:388](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L388)



### `Optional`beforeToolCallback

beforeToolCallback?: [BeforeToolCallback](../types/BeforeToolCallback.html)

Callbacks to be called before calling the tool.

  * Defined in [core/src/agents/llm_agent.ts:398](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L398)



### `Optional`codeExecutor

codeExecutor?: [BaseCodeExecutor](../classes/BaseCodeExecutor.html)

Instructs the agent to make a plan and execute it step by step.

  * Defined in [core/src/agents/llm_agent.ts:424](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L424)



### `Optional`contextCompactors

contextCompactors?: [BaseContextCompactor](BaseContextCompactor.html)[]

A list of context compactors to evaluate in priority order. Modifies the session history to keep context overhead within limits.

  * Defined in [core/src/agents/llm_agent.ts:419](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L419)



### `Optional`description

description?: string

Human-readable description (used when a node is exposed as a tool).

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[description](BaseAgentConfig.html#description)

  * Defined in [core/src/agents/base_agent.ts:51](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L51)



### `Optional`disallowTransferToParent

disallowTransferToParent?: boolean

Disallows LLM-controlled transferring to the parent agent.

NOTE: Setting this to `true` also prevents this agent to continue reply to the end-user. This behavior prevents one-way transfer, in which end-user may be stuck with one agent that cannot transfer to other agents in the agent tree.

  * Defined in [core/src/agents/llm_agent.ts:344](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L344)



### `Optional`disallowTransferToPeers

disallowTransferToPeers?: boolean

Disallows LLM-controlled transferring to the peer agents.

  * Defined in [core/src/agents/llm_agent.ts:347](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L347)



### `Optional`generateContentConfig

generateContentConfig?: GenerateContentConfig

The additional content generation configurations.

Three fields are rejected by the constructor, because the agent owns them: `tools` (set them through `tools`), `systemInstruction` (through `instruction`) and `responseSchema` (through `outputSchema`). Every other field is forwarded to the model as given. That includes `thinkingConfig`, unless `planner` is a `BuiltInPlanner` with its own `thinkingConfig`: the planner's `thinkingConfig` then takes precedence.

For example: use this config to adjust model temperature, configure safety settings, etc.

  * Defined in [core/src/agents/llm_agent.ts:334](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L334)



### `Optional`globalInstruction

globalInstruction?: string | [InstructionProvider](../types/InstructionProvider.html)

Instructions for all the agents in the entire agent tree.

ONLY the globalInstruction in root agent will take effect.

For example: use globalInstruction to make all agents have a stable identity or personality.

#### Deprecated

Use GlobalInstructionPlugin instead.

  * Defined in [core/src/agents/llm_agent.ts:316](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L316)



### `Optional`includeContents

includeContents?: "default" | "none"

Controls content inclusion in model requests.

Options: default: Model receives relevant conversation history none: Model receives no prior history, operates solely on current instruction and input

  * Defined in [core/src/agents/llm_agent.ts:358](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L358)



### `Optional`inputSchema

inputSchema?: [LlmAgentSchema](../types/LlmAgentSchema.html)

The input schema when agent is used as a tool.

Overrides [BaseAgentConfig](BaseAgentConfig.html).[inputSchema](BaseAgentConfig.html#inputschema)

  * Defined in [core/src/agents/llm_agent.ts:371](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L371)



### `Optional`instruction

instruction?: string | [InstructionProvider](../types/InstructionProvider.html)

Instructions for the LLM model, guiding the agent's behavior.

  * Defined in [core/src/agents/llm_agent.ts:304](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L304)



### `Optional`isolationScope

isolationScope?: string | true

Runs this node's subtree in an isolated conversation scope: an agent inside it sees only session events carrying the same scope, plus untagged ones. `true` derives a scope per node run; a string is an explicit shared tag.

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[isolationScope](BaseAgentConfig.html#isolationscope)

  * Defined in [core/src/workflow/base_node.ts:75](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L75)



### `Optional`mode

mode?: "single_turn" | "task"

The agent's execution mode when run as a workflow node.

  * `single_turn` (default): the agent runs once against the node input.
  * `task`: the agent is given a `finish_task` tool and runs a multi-round loop until it calls `finish_task`, whose arguments (conforming to `outputSchema`) become the node output. Mirrors Python's `Agent(mode=...)`.



  * Defined in [core/src/agents/llm_agent.ts:368](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L368)



### `Optional`model

model?: string | [BaseLlm](../classes/BaseLlm.html)

The model to use for the agent.

  * Defined in [core/src/agents/llm_agent.ts:301](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L301)



### name

name: string

Canonical, unique-within-a-graph node name.

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[name](BaseAgentConfig.html#name)

  * Defined in [core/src/agents/base_agent.ts:50](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L50)



### `Optional`outputKey

outputKey?: string

The key in session state to store the output of the agent.

Typically use cases:

  * Extracts agent reply for later use, such as in tools, callbacks, etc.
  * Connects agents to coordinate with each other.



  * Defined in [core/src/agents/llm_agent.ts:383](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L383)



### `Optional`outputSchema

outputSchema?: [LlmAgentSchema](../types/LlmAgentSchema.html)

The output schema when agent replies.

Overrides [BaseAgentConfig](BaseAgentConfig.html).[outputSchema](BaseAgentConfig.html#outputschema)

  * Defined in [core/src/agents/llm_agent.ts:374](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L374)



### `Optional`parentAgent

parentAgent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[parentAgent](BaseAgentConfig.html#parentagent)

  * Defined in [core/src/agents/base_agent.ts:52](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L52)



### `Optional`planner

planner?: [BasePlanner](../classes/BasePlanner.html)

Instructs the agent to make a plan and execute it step by step.

NOTE: to use the model's built-in thinking features, set `thinkingConfig` on a `BuiltInPlanner`.

  * Defined in [core/src/agents/llm_agent.ts:432](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L432)



### `Optional`requestProcessors

requestProcessors?: [BaseLlmRequestProcessor](../classes/BaseLlmRequestProcessor.html)[]

Processors to run before the LLM request is sent.

  * Defined in [core/src/agents/llm_agent.ts:408](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L408)



### `Optional`rerunOnResume

rerunOnResume?: boolean

If true, the node re-executes when a workflow resumes even if it already completed in a prior turn. Default false.

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[rerunOnResume](BaseAgentConfig.html#rerunonresume)

  * Defined in [core/src/workflow/base_node.ts:47](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L47)



### `Optional`responseProcessors

responseProcessors?: [BaseLlmResponseProcessor](../classes/BaseLlmResponseProcessor.html)[]

Processors to run after the LLM response is received.

  * Defined in [core/src/agents/llm_agent.ts:413](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L413)



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



### `Optional`tools

tools?: [ToolUnion](../types/ToolUnion.html)[]

Tools available to this agent.

  * Defined in [core/src/agents/llm_agent.ts:319](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L319)



### `Optional`waitForOutput

waitForOutput?: boolean

If true, the node only produces its output once all of its predecessors have triggered it (fan-in / join semantics). Default false.

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[waitForOutput](BaseAgentConfig.html#waitforoutput)

  * Defined in [core/src/workflow/base_node.ts:53](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L53)



Properties

afterAgentCallbackafterModelCallbackafterToolCallbackbeforeAgentCallbackbeforeModelCallbackbeforeToolCallbackcodeExecutorcontextCompactorsdescriptiondisallowTransferToParentdisallowTransferToPeersgenerateContentConfigglobalInstructionincludeContentsinputSchemainstructionisolationScopemodemodelnameoutputKeyoutputSchemaparentAgentplannerrequestProcessorsrerunOnResumeresponseProcessorsretryConfigstateSchemasubAgentstimeouttoolswaitForOutput

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


