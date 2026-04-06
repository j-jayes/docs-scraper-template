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
description?: string;  
disallowTransferToParent?: boolean;  
disallowTransferToPeers?: boolean;  
generateContentConfig?: GenerateContentConfig;  
globalInstruction?: string | [InstructionProvider](../types/InstructionProvider.html);  
includeContents?: "none" | "default";  
inputSchema?: [LlmAgentSchema](../types/LlmAgentSchema.html);  
instruction?: string | [InstructionProvider](../types/InstructionProvider.html);  
model?: string | [BaseLlm](../classes/BaseLlm.html);  
name: string;  
outputKey?: string;  
outputSchema?: [LlmAgentSchema](../types/LlmAgentSchema.html);  
parentAgent?: [BaseAgent](../classes/BaseAgent.html);  
requestProcessors?: [BaseLlmRequestProcessor](../classes/BaseLlmRequestProcessor.html)[];  
responseProcessors?: [BaseLlmResponseProcessor](../classes/BaseLlmResponseProcessor.html)[];  
subAgents?: [BaseAgent](../classes/BaseAgent.html)[];  
tools?: [ToolUnion](../types/ToolUnion.html)[];  
}

#### Hierarchy ([View Summary](../hierarchy.html#LlmAgentConfig))

  * [BaseAgentConfig](BaseAgentConfig.html)
    * LlmAgentConfig



  * Defined in [agents/llm_agent.ts:195](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L195)



## Properties

### `Optional`afterAgentCallback

afterAgentCallback?: [AfterAgentCallback](../types/AfterAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[afterAgentCallback](BaseAgentConfig.html#afteragentcallback)

  * Defined in [agents/base_agent.ts:48](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L48)



### `Optional`afterModelCallback

afterModelCallback?: [AfterModelCallback](../types/AfterModelCallback.html)

Callbacks to be called after calling the LLM.

  * Defined in [agents/llm_agent.ts:275](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L275)



### `Optional`afterToolCallback

afterToolCallback?: [AfterToolCallback](../types/AfterToolCallback.html)

Callbacks to be called after calling the tool.

  * Defined in [agents/llm_agent.ts:285](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L285)



### `Optional`beforeAgentCallback

beforeAgentCallback?: [BeforeAgentCallback](../types/BeforeAgentCallback.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[beforeAgentCallback](BaseAgentConfig.html#beforeagentcallback)

  * Defined in [agents/base_agent.ts:47](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L47)



### `Optional`beforeModelCallback

beforeModelCallback?: [BeforeModelCallback](../types/BeforeModelCallback.html)

Callbacks to be called before calling the LLM.

  * Defined in [agents/llm_agent.ts:270](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L270)



### `Optional`beforeToolCallback

beforeToolCallback?: [BeforeToolCallback](../types/BeforeToolCallback.html)

Callbacks to be called before calling the tool.

  * Defined in [agents/llm_agent.ts:280](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L280)



### `Optional`codeExecutor

codeExecutor?: [BaseCodeExecutor](../classes/BaseCodeExecutor.html)

Instructs the agent to make a plan and execute it step by step.

  * Defined in [agents/llm_agent.ts:300](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L300)



### `Optional`description

description?: string

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[description](BaseAgentConfig.html#description)

  * Defined in [agents/base_agent.ts:44](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L44)



### `Optional`disallowTransferToParent

disallowTransferToParent?: boolean

Disallows LLM-controlled transferring to the parent agent.

NOTE: Setting this as True also prevents this agent to continue reply to the end-user. This behavior prevents one-way transfer, in which end-user may be stuck with one agent that cannot transfer to other agents in the agent tree.

  * Defined in [agents/llm_agent.ts:236](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L236)



### `Optional`disallowTransferToPeers

disallowTransferToPeers?: boolean

Disallows LLM-controlled transferring to the peer agents.

  * Defined in [agents/llm_agent.ts:239](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L239)



### `Optional`generateContentConfig

generateContentConfig?: GenerateContentConfig

The additional content generation configurations.

NOTE: not all fields are usable, e.g. tools must be configured via `tools`, thinking_config must be configured via `planner` in LlmAgent.

For example: use this config to adjust model temperature, configure safety settings, etc.

  * Defined in [agents/llm_agent.ts:226](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L226)



### `Optional`globalInstruction

globalInstruction?: string | [InstructionProvider](../types/InstructionProvider.html)

Instructions for all the agents in the entire agent tree.

ONLY the globalInstruction in root agent will take effect.

For example: use globalInstruction to make all agents have a stable identity or personality.

  * Defined in [agents/llm_agent.ts:212](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L212)



### `Optional`includeContents

includeContents?: "none" | "default"

Controls content inclusion in model requests.

Options: default: Model receives relevant conversation history none: Model receives no prior history, operates solely on current instruction and input

  * Defined in [agents/llm_agent.ts:250](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L250)



### `Optional`inputSchema

inputSchema?: [LlmAgentSchema](../types/LlmAgentSchema.html)

The input schema when agent is used as a tool.

  * Defined in [agents/llm_agent.ts:253](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L253)



### `Optional`instruction

instruction?: string | [InstructionProvider](../types/InstructionProvider.html)

Instructions for the LLM model, guiding the agent's behavior.

  * Defined in [agents/llm_agent.ts:202](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L202)



### `Optional`model

model?: string | [BaseLlm](../classes/BaseLlm.html)

The model to use for the agent.

  * Defined in [agents/llm_agent.ts:199](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L199)



### name

name: string

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[name](BaseAgentConfig.html#name)

  * Defined in [agents/base_agent.ts:43](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L43)



### `Optional`outputKey

outputKey?: string

The key in session state to store the output of the agent.

Typically use cases:

  * Extracts agent reply for later use, such as in tools, callbacks, etc.
  * Connects agents to coordinate with each other.



  * Defined in [agents/llm_agent.ts:265](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L265)



### `Optional`outputSchema

outputSchema?: [LlmAgentSchema](../types/LlmAgentSchema.html)

The output schema when agent replies.

  * Defined in [agents/llm_agent.ts:256](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L256)



### `Optional`parentAgent

parentAgent?: [BaseAgent](../classes/BaseAgent.html)

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[parentAgent](BaseAgentConfig.html#parentagent)

  * Defined in [agents/base_agent.ts:45](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L45)



### `Optional`requestProcessors

requestProcessors?: [BaseLlmRequestProcessor](../classes/BaseLlmRequestProcessor.html)[]

Processors to run before the LLM request is sent.

  * Defined in [agents/llm_agent.ts:290](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L290)



### `Optional`responseProcessors

responseProcessors?: [BaseLlmResponseProcessor](../classes/BaseLlmResponseProcessor.html)[]

Processors to run after the LLM response is received.

  * Defined in [agents/llm_agent.ts:295](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L295)



### `Optional`subAgents

subAgents?: [BaseAgent](../classes/BaseAgent.html)[]

Inherited from [BaseAgentConfig](BaseAgentConfig.html).[subAgents](BaseAgentConfig.html#subagents)

  * Defined in [agents/base_agent.ts:46](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L46)



### `Optional`tools

tools?: [ToolUnion](../types/ToolUnion.html)[]

Tools available to this agent.

  * Defined in [agents/llm_agent.ts:215](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L215)



Properties

afterAgentCallbackafterModelCallbackafterToolCallbackbeforeAgentCallbackbeforeModelCallbackbeforeToolCallbackcodeExecutordescriptiondisallowTransferToParentdisallowTransferToPeersgenerateContentConfigglobalInstructionincludeContentsinputSchemainstructionmodelnameoutputKeyoutputSchemaparentAgentrequestProcessorsresponseProcessorssubAgentstools

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


