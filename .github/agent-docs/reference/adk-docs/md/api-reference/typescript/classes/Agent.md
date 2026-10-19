[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [Agent]()



# Class Agent

An agent that uses a large language model to generate responses.

#### Hierarchy ([View Summary](../hierarchy.html#Agent))

  * [BaseAgent](BaseAgent.html)<[LlmAgentConfig](../interfaces/LlmAgentConfig.html)>
    * Agent



  * Defined in [core/src/agents/llm_agent.ts:473](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L473)



## Constructors

### constructor

  * new Agent(config: [LlmAgentConfig](../interfaces/LlmAgentConfig.html)): [Agent]()

#### Parameters

    * config: [LlmAgentConfig](../interfaces/LlmAgentConfig.html)

#### Returns [Agent]()

Overrides [BaseAgent](BaseAgent.html).[constructor](BaseAgent.html#constructor)

    * Defined in [core/src/agents/llm_agent.ts:524](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L524)




## Properties

### `Readonly`[BASE_AGENT_SIGNATURE_SYMBOL]

"[BASE_AGENT_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK agent classes.

Inherited from [BaseAgent](BaseAgent.html).[[BASE_AGENT_SIGNATURE_SYMBOL]](BaseAgent.html#base_agent_signature_symbol)

  * Defined in [core/src/agents/base_agent.ts:96](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L96)



### `Readonly`[BASE_NODE_SIGNATURE_SYMBOL]

"[BASE_NODE_SIGNATURE_SYMBOL]": true

Brand identifying this object as a [BaseNode](BaseNode.html) (see `isBaseNode`).

Inherited from [BaseAgent](BaseAgent.html).[[BASE_NODE_SIGNATURE_SYMBOL]](BaseAgent.html#base_node_signature_symbol)

  * Defined in [core/src/workflow/base_node.ts:88](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L88)



### `Readonly`[LLM_AGENT_SIGNATURE_SYMBOL]

"[LLM_AGENT_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK LLM agent class.

  * Defined in [core/src/agents/llm_agent.ts:475](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L475)



### `Readonly`afterAgentCallback

afterAgentCallback: [SingleAgentCallback](../types/SingleAgentCallback.html)[]

Callback or list of callbacks to be invoked after the agent run.

When a list of callbacks is provided, the callbacks will be called in the order they are listed until a callback does not return undefined.

Each callback takes a single [Context](Context.html) argument. Returning `Content` emits it as the agent's response, appended to the event history; return `undefined` to leave the response as the agent produced it.

Inherited from [BaseAgent](BaseAgent.html).[afterAgentCallback](BaseAgent.html#afteragentcallback)

  * Defined in [core/src/agents/base_agent.ts:174](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L174)



### `Optional`afterModelCallback

afterModelCallback?: [AfterModelCallback](../types/AfterModelCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:516](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L516)



### `Optional`afterToolCallback

afterToolCallback?: [AfterToolCallback](../types/AfterToolCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:518](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L518)



### `Readonly`beforeAgentCallback

beforeAgentCallback: [SingleAgentCallback](../types/SingleAgentCallback.html)[]

Callback or list of callbacks to be invoked before the agent run.

When a list of callbacks is provided, the callbacks will be called in the order they are listed until a callback does not return undefined.

Each callback takes a single [Context](Context.html) argument. Returning `Content` skips this agent's own run — its `runAsyncImpl` body and its `afterAgentCallback` — and emits the returned content as this agent's response; return `undefined` to let the run proceed.

That skip is scoped to this agent. It sets `endInvocation` on the invocation context the agent created for itself, which is a copy of its parent's, so callers above are unaffected: a `SequentialAgent` still runs the remaining sub-agents.

Inherited from [BaseAgent](BaseAgent.html).[beforeAgentCallback](BaseAgent.html#beforeagentcallback)

  * Defined in [core/src/agents/base_agent.ts:162](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L162)



### `Optional`beforeModelCallback

beforeModelCallback?: [BeforeModelCallback](../types/BeforeModelCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:515](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L515)



### `Optional`beforeToolCallback

beforeToolCallback?: [BeforeToolCallback](../types/BeforeToolCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:517](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L517)



### `Optional`codeExecutor

codeExecutor?: [BaseCodeExecutor](BaseCodeExecutor.html)

  * Defined in [core/src/agents/llm_agent.ts:521](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L521)



### `Protected` `Readonly`config

config: [LlmAgentConfig](../interfaces/LlmAgentConfig.html)

The config this agent was constructed from.

Stored so clone can rebuild the agent by re-running the concrete constructor with overrides applied, which re-derives all state correctly instead of copying an already-mutated instance. Shallow-copied so later external mutation of the caller's object does not leak into clones.

Inherited from [BaseAgent](BaseAgent.html).[config](BaseAgent.html#config)

  * Defined in [core/src/agents/base_agent.ts:106](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L106)



### `Readonly`description

description: string

Inherited from [BaseAgent](BaseAgent.html).[description](BaseAgent.html#description)

  * Defined in [core/src/workflow/base_node.ts:91](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L91)



### disallowTransferToParent

disallowTransferToParent: boolean

  * Defined in [core/src/agents/llm_agent.ts:483](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L483)



### disallowTransferToPeers

disallowTransferToPeers: boolean

  * Defined in [core/src/agents/llm_agent.ts:484](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L484)



### `Optional`generateContentConfig

generateContentConfig?: GenerateContentConfig

  * Defined in [core/src/agents/llm_agent.ts:482](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L482)



### globalInstruction

globalInstruction: string | [InstructionProvider](../types/InstructionProvider.html)

#### Deprecated

Use GlobalInstructionPlugin instead.

  * Defined in [core/src/agents/llm_agent.ts:480](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L480)



### includeContents

includeContents: "default" | "none"

  * Defined in [core/src/agents/llm_agent.ts:485](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L485)



### `Readonly`includeContentsExplicit

includeContentsExplicit: boolean

Whether includeContents was set by the caller rather than defaulted.

A workflow node runs its agent for a single turn on the input the graph handed it, so the agent must not also read the surrounding conversation — unless the author asked for it. Mirrors Python checking `'include_contents' in agent.model_fields_set`.

  * Defined in [core/src/agents/llm_agent.ts:495](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L495)



### `Optional`inputSchema

inputSchema?: Schema

Overrides [BaseAgent](BaseAgent.html).[inputSchema](BaseAgent.html#inputschema)

  * Defined in [core/src/agents/llm_agent.ts:497](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L497)



### `Optional` `Readonly`inputSchemaSource

inputSchemaSource?: [SchemaLike](../types/SchemaLike.html)

The input schema exactly as it was supplied, before conversion into the genai dialect.

`inputSchema` is normalized to a genai `Schema` because that is what the model API and function declarations require, but that conversion is lossy: a Zod refinement, transform, or custom error message has no genai equivalent. Validation therefore uses the original, falling back to the converted form when the schema was given in the genai dialect to begin with.

  * Defined in [core/src/agents/llm_agent.ts:510](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L510)



### instruction

instruction: string | [InstructionProvider](../types/InstructionProvider.html)

  * Defined in [core/src/agents/llm_agent.ts:478](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L478)



### `Optional` `Readonly`isolationScope

isolationScope?: string | true

Inherited from [BaseAgent](BaseAgent.html).[isolationScope](BaseAgent.html#isolationscope)

  * Defined in [core/src/workflow/base_node.ts:105](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L105)



### `Optional`mode

mode?: "single_turn" | "task"

  * Defined in [core/src/agents/llm_agent.ts:496](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L496)



### `Optional`model

model?: string | [BaseLlm](BaseLlm.html)

  * Defined in [core/src/agents/llm_agent.ts:477](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L477)



### `Readonly`name

name: string

The agent's name. Agent name must be a JS identifier and unique within the agent tree. Agent name cannot be "user", since it's reserved for end-user's input.

Inherited from [BaseAgent](BaseAgent.html).[name](BaseAgent.html#name)

  * Defined in [core/src/agents/base_agent.ts:113](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L113)



### `Optional`outputKey

outputKey?: string

  * Defined in [core/src/agents/llm_agent.ts:513](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L513)



### `Optional`outputSchema

outputSchema?: Schema

Overrides [BaseAgent](BaseAgent.html).[outputSchema](BaseAgent.html#outputschema)

  * Defined in [core/src/agents/llm_agent.ts:498](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L498)



### `Optional` `Readonly`outputSchemaSource

outputSchemaSource?: [SchemaLike](../types/SchemaLike.html)

The output schema as supplied — see inputSchemaSource.

  * Defined in [core/src/agents/llm_agent.ts:512](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L512)



### `Optional`parentAgent

parentAgent?: [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)>

The parent agent of this agent.

Note that an agent can ONLY be added as sub-agent once.

If you want to add one agent twice as sub-agent, consider to create two agent instances with identical config, but with different name and add them to the agent tree.

The parent agent is the agent that created this agent.

Inherited from [BaseAgent](BaseAgent.html).[parentAgent](BaseAgent.html#parentagent)

  * Defined in [core/src/agents/base_agent.ts:139](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L139)



### `Optional`planner

planner?: [BasePlanner](BasePlanner.html)

  * Defined in [core/src/agents/llm_agent.ts:522](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L522)



### `Optional` `Readonly`preparedRetryConfig

preparedRetryConfig?: [PreparedRetryConfig](../interfaces/PreparedRetryConfig.html)

The retry config with its exception filter normalized once, up front (see [prepareRetryConfig](../functions/prepareRetryConfig.html)). Used by the node runner so the retry hot path never re-normalizes or throws on a malformed config mid-retry.

Inherited from [BaseAgent](BaseAgent.html).[preparedRetryConfig](BaseAgent.html#preparedretryconfig)

  * Defined in [core/src/workflow/base_node.ts:100](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L100)



### requestProcessors

requestProcessors: [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html)[]

  * Defined in [core/src/agents/llm_agent.ts:519](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L519)



### `Readonly`rerunOnResume

rerunOnResume: boolean

Inherited from [BaseAgent](BaseAgent.html).[rerunOnResume](BaseAgent.html#rerunonresume)

  * Defined in [core/src/workflow/base_node.ts:92](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L92)



### responseProcessors

responseProcessors: [BaseLlmResponseProcessor](BaseLlmResponseProcessor.html)[]

  * Defined in [core/src/agents/llm_agent.ts:520](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L520)



### `Optional` `Readonly`retryConfig

retryConfig?: [RetryConfig](../interfaces/RetryConfig.html)

Inherited from [BaseAgent](BaseAgent.html).[retryConfig](BaseAgent.html#retryconfig)

  * Defined in [core/src/workflow/base_node.ts:94](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L94)



### `Optional` `Readonly`stateSchema

stateSchema?: [SchemaLike](../types/SchemaLike.html)

Inherited from [BaseAgent](BaseAgent.html).[stateSchema](BaseAgent.html#stateschema)

  * Defined in [core/src/workflow/base_node.ts:104](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L104)



### `Readonly`subAgents

subAgents: [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)>[]

The sub-agents of this agent.

Inherited from [BaseAgent](BaseAgent.html).[subAgents](BaseAgent.html#subagents)

  * Defined in [core/src/agents/base_agent.ts:144](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L144)



### `Optional` `Readonly`timeout

timeout?: number

Inherited from [BaseAgent](BaseAgent.html).[timeout](BaseAgent.html#timeout)

  * Defined in [core/src/workflow/base_node.ts:101](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L101)



### tools

tools: [ToolUnion](../types/ToolUnion.html)[]

  * Defined in [core/src/agents/llm_agent.ts:481](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L481)



### `Readonly`waitForOutput

waitForOutput: boolean

Inherited from [BaseAgent](BaseAgent.html).[waitForOutput](BaseAgent.html#waitforoutput)

  * Defined in [core/src/workflow/base_node.ts:93](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L93)



## Accessors

### canonicalAfterModelCallbacks

  * get canonicalAfterModelCallbacks(): [SingleAfterModelCallback](../types/SingleAfterModelCallback.html)[]

The resolved afterModelCallback field as a list of SingleAfterModelCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleAfterModelCallback](../types/SingleAfterModelCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:785](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L785)




### canonicalAfterToolCallbacks

  * get canonicalAfterToolCallbacks(): [SingleAfterToolCallback](../types/SingleAfterToolCallback.html)[]

The resolved afterToolCallback field as a list of AfterToolCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleAfterToolCallback](../types/SingleAfterToolCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:804](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L804)




### canonicalBeforeModelCallbacks

  * get canonicalBeforeModelCallbacks(): [SingleBeforeModelCallback](../types/SingleBeforeModelCallback.html)[]

The resolved beforeModelCallback field as a list of SingleBeforeModelCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleBeforeModelCallback](../types/SingleBeforeModelCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:775](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L775)




### canonicalBeforeToolCallbacks

  * get canonicalBeforeToolCallbacks(): [SingleBeforeToolCallback](../types/SingleBeforeToolCallback.html)[]

The resolved beforeToolCallback field as a list of BeforeToolCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleBeforeToolCallback](../types/SingleBeforeToolCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:795](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L795)




### canonicalModel

  * get canonicalModel(): [BaseLlm](BaseLlm.html)

The resolved BaseLlm instance.

When not set, the agent will inherit the model from its ancestor.

#### Returns [BaseLlm](BaseLlm.html)

    * Defined in [core/src/agents/llm_agent.ts:666](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L666)




### finishTaskTool

  * get finishTaskTool(): [FinishTaskTool](FinishTaskTool.html)

The `finish_task` tool for this agent (task mode). Lazily created and cached so its declaration (derived from `outputSchema`) is stable across turns.

#### Returns [FinishTaskTool](FinishTaskTool.html)

    * Defined in [core/src/agents/llm_agent.ts:689](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L689)




### requiresAllPredecessors

  * get requiresAllPredecessors(): boolean

Whether this node must wait for ALL of its predecessors to trigger before it runs (fan-in barrier). Overridden by `JoinNode`.

#### Returns boolean

Inherited from BaseAgent.requiresAllPredecessors

    * Defined in [core/src/workflow/base_node.ts:134](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L134)




### rootAgent

  * get rootAgent(): [BaseAgent](BaseAgent.html)

Root agent of this agent. Computed dynamically by traversing up the parent chain.

#### Returns [BaseAgent](BaseAgent.html)

Inherited from BaseAgent.rootAgent

    * Defined in [core/src/agents/base_agent.ts:124](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L124)




## Methods

### `Protected`callLlmAsync

  * callLlmAsync(  
invocationContext: [InvocationContext](InvocationContext.html),  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
modelResponseEvent: [Event](../interfaces/Event.html),  
): AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void, void>

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)
    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)
    * modelResponseEvent: [Event](../interfaces/Event.html)

#### Returns AsyncGenerator<[LlmResponse](../interfaces/LlmResponse.html), void, void>

    * Defined in [core/src/agents/llm_agent.ts:1832](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L1832)




### canonicalGlobalInstruction

  * canonicalGlobalInstruction(  
context: [ReadonlyContext](ReadonlyContext.html),  
): Promise<{ instruction: string; requireStateInjection: boolean }>

The resolved globalInstruction field to construct global instruction.

This method is only for use by Agent Development Kit.

#### Parameters

    * context: [ReadonlyContext](ReadonlyContext.html)

The context to retrieve the session state.

#### Returns Promise<{ instruction: string; requireStateInjection: boolean }>

The resolved globalInstruction field.

#### Deprecated

Use GlobalInstructionPlugin instead.

    * Defined in [core/src/agents/llm_agent.ts:724](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L724)




### canonicalInstruction

  * canonicalInstruction(  
context: [ReadonlyContext](ReadonlyContext.html),  
): Promise<{ instruction: string; requireStateInjection: boolean }>

The resolved instruction field to construct instruction for this agent.

This method is only for use by Agent Development Kit.

#### Parameters

    * context: [ReadonlyContext](ReadonlyContext.html)

The context to retrieve the session state.

#### Returns Promise<{ instruction: string; requireStateInjection: boolean }>

The resolved instruction field.

    * Defined in [core/src/agents/llm_agent.ts:704](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L704)




### canonicalTools

  * canonicalTools(context?: [ReadonlyContext](ReadonlyContext.html)): Promise<[BaseTool](BaseTool.html)[]>

The resolved tools field as a list of BaseTool based on the context.

This method is only for use by Agent Development Kit.

#### Parameters

    * `Optional`context: [ReadonlyContext](ReadonlyContext.html)

#### Returns Promise<[BaseTool](BaseTool.html)[]>

    * Defined in [core/src/agents/llm_agent.ts:744](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L744)




### clone

  * clone(overrides?: Partial<[LlmAgentConfig](../interfaces/LlmAgentConfig.html)>): this

Creates a copy of this agent with the given config fields overridden.

The clone is a detached root: its `parentAgent` is always `undefined`. Sub-agents are recursively cloned (and re-parented to the clone) unless `subAgents` is overridden. Rebuilding via the concrete constructor re-derives all state, so a cloned `LlmAgent` gets a fresh `requestProcessors` array rather than sharing the original's. See google/adk-js#534.

#### Parameters

    * `Optional`overrides: Partial<[LlmAgentConfig](../interfaces/LlmAgentConfig.html)>

Config fields to override on the clone. Overriding `parentAgent` is rejected: parentage is assigned only when a parent agent is constructed with its sub-agents.

#### Returns this

A new detached agent instance of the same concrete class.

Inherited from [BaseAgent](BaseAgent.html).[clone](BaseAgent.html#clone)

    * Defined in [core/src/agents/base_agent.ts:209](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L209)




### `Protected`createInvocationContext

  * createInvocationContext(parentContext: [InvocationContext](InvocationContext.html)): [InvocationContext](InvocationContext.html)

Creates an invocation context for this agent.

#### Parameters

    * parentContext: [InvocationContext](InvocationContext.html)

The invocation context of the parent agent.

#### Returns [InvocationContext](InvocationContext.html)

The invocation context for this agent.

Inherited from [BaseAgent](BaseAgent.html).[createInvocationContext](BaseAgent.html#createinvocationcontext)

    * Defined in [core/src/agents/base_agent.ts:434](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L434)




### findAgent

  * findAgent(name: string): [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)> | undefined

Finds the agent with the given name in this agent and its descendants.

#### Parameters

    * name: string

The name of the agent to find.

#### Returns [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)> | undefined

The agent with the given name, or undefined if not found.

Inherited from [BaseAgent](BaseAgent.html).[findAgent](BaseAgent.html#findagent)

    * Defined in [core/src/agents/base_agent.ts:403](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L403)




### findSubAgent

  * findSubAgent(name: string): [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)> | undefined

Finds the agent with the given name in this agent's descendants.

#### Parameters

    * name: string

The name of the agent to find.

#### Returns [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)> | undefined

The agent with the given name, or undefined if not found.

Inherited from [BaseAgent](BaseAgent.html).[findSubAgent](BaseAgent.html#findsubagent)

    * Defined in [core/src/agents/base_agent.ts:417](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L417)




### `Protected`handleAfterAgentCallback

  * handleAfterAgentCallback(  
invocationContext: [InvocationContext](InvocationContext.html),  
): Promise<[Event](../interfaces/Event.html) | undefined>

Runs the after agent callback if it exists.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The invocation context of the agent.

#### Returns Promise<[Event](../interfaces/Event.html) | undefined>

The event to return to the user, or undefined if no event is generated.

Inherited from [BaseAgent](BaseAgent.html).[handleAfterAgentCallback](BaseAgent.html#handleafteragentcallback)

    * Defined in [core/src/agents/base_agent.ts:497](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L497)




### `Protected`handleBeforeAgentCallback

  * handleBeforeAgentCallback(  
invocationContext: [InvocationContext](InvocationContext.html),  
): Promise<[Event](../interfaces/Event.html) | undefined>

Runs the before agent callback if it exists.

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

The invocation context of the agent.

#### Returns Promise<[Event](../interfaces/Event.html) | undefined>

The event to return to the user, or undefined if no event is generated.

Inherited from [BaseAgent](BaseAgent.html).[handleBeforeAgentCallback](BaseAgent.html#handlebeforeagentcallback)

    * Defined in [core/src/agents/base_agent.ts:450](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L450)




### run

  * run(ctx: [NodeContext](NodeContext.html), input: unknown): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Runs the node, normalizing every yielded item into an [Event](../interfaces/Event.html). This is what the engine (and `ctx.runNode()`) consumes. Validates the input against `inputSchema` once, up front (skipping genai `Content`, which nodes coerce themselves).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * input: unknown

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Inherited from [BaseAgent](BaseAgent.html).[run](BaseAgent.html#run)

    * Defined in [core/src/workflow/base_node.ts:155](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L155)




### `Protected`runAndHandleError

  * runAndHandleError<T extends [LlmResponse](../interfaces/LlmResponse.html) | [Event](../interfaces/Event.html)>(  
responseGenerator: AsyncGenerator<T, void, void>,  
invocationContext: [InvocationContext](InvocationContext.html),  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
modelResponseEvent: [Event](../interfaces/Event.html),  
): AsyncGenerator<T, void, void>

#### Type Parameters

    * T extends [LlmResponse](../interfaces/LlmResponse.html) | [Event](../interfaces/Event.html)

#### Parameters

    * responseGenerator: AsyncGenerator<T, void, void>
    * invocationContext: [InvocationContext](InvocationContext.html)
    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)
    * modelResponseEvent: [Event](../interfaces/Event.html)

#### Returns AsyncGenerator<T, void, void>

    * Defined in [core/src/agents/llm_agent.ts:1987](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L1987)




### runAsync

  * runAsync(parentContext: [InvocationContext](InvocationContext.html)): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Entry method to run an agent via text-based conversation.

#### Parameters

    * parentContext: [InvocationContext](InvocationContext.html)

The invocation context of the parent agent.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

An AsyncGenerator that yields the events generated by the agent.

#### Yields

The events generated by the agent.

Inherited from [BaseAgent](BaseAgent.html).[runAsync](BaseAgent.html#runasync)

    * Defined in [core/src/agents/base_agent.ts:254](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L254)




### `Protected`runAsyncImpl

  * runAsyncImpl(context: [InvocationContext](InvocationContext.html)): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Core logic to run this agent via text-based conversation.

#### Parameters

    * context: [InvocationContext](InvocationContext.html)

The invocation context of the agent.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

An AsyncGenerator that yields the events generated by the agent.

#### Yields

The events generated by the agent.

Overrides [BaseAgent](BaseAgent.html).[runAsyncImpl](BaseAgent.html#runasyncimpl)

    * Defined in [core/src/agents/llm_agent.ts:918](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L918)




### `Protected`runImpl

  * runImpl(ctx: [NodeContext](NodeContext.html), nodeInput: unknown): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Runs this agent as a workflow node.

Where [BaseAgent.runImpl](BaseAgent.html#runimpl) delegates straight to `runAsync`, an `LlmAgent` has a node input to inject into the conversation, instruction placeholders to resolve against it, a reply to promote to node output, and — in `task` mode — a `finish_task` round-trip to drive. All of that lives in `runLlmAgentAsNode`, mirroring adk-python's `LlmAgent._run_impl` delegating to `run_llm_agent_as_node`.

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * nodeInput: unknown

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Overrides [BaseAgent](BaseAgent.html).[runImpl](BaseAgent.html#runimpl)

    * Defined in [core/src/agents/llm_agent.ts:911](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L911)




### runLive

  * runLive(parentContext: [InvocationContext](InvocationContext.html)): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Entry method to run an agent via video/audio-based conversation.

#### Parameters

    * parentContext: [InvocationContext](InvocationContext.html)

The invocation context of the parent agent.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

An AsyncGenerator that yields the events generated by the agent.

#### Yields

The events generated by the agent.

Inherited from [BaseAgent](BaseAgent.html).[runLive](BaseAgent.html#runlive)

    * Defined in [core/src/agents/base_agent.ts:333](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/base_agent.ts#L333)




### `Protected`runLiveImpl

  * runLiveImpl(context: [InvocationContext](InvocationContext.html)): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Core logic to run this agent via video/audio-based conversation.

#### Parameters

    * context: [InvocationContext](InvocationContext.html)

The invocation context of the agent.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

An AsyncGenerator that yields the events generated by the agent.

#### Yields

The events generated by the agent.

Overrides [BaseAgent](BaseAgent.html).[runLiveImpl](BaseAgent.html#runliveimpl)

    * Defined in [core/src/agents/llm_agent.ts:964](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L964)




### `Protected`toEvent

  * toEvent(ctx: [NodeContext](NodeContext.html), data: unknown): [Event](../interfaces/Event.html) | null

Normalizes a single yielded item into an [Event](../interfaces/Event.html) (or `null` to skip). Subclasses may override for richer coercion (e.g. `FunctionNode`).

#### Parameters

    * ctx: [NodeContext](NodeContext.html)
    * data: unknown

#### Returns [Event](../interfaces/Event.html) | null

Inherited from [BaseAgent](BaseAgent.html).[toEvent](BaseAgent.html#toevent)

    * Defined in [core/src/workflow/base_node.ts:217](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L217)




### `Protected`validateInput

  * validateInput(input: unknown): unknown

Validates node input against `inputSchema` (Content passes through). Only enforced for Zod schemas; a genai `Schema` is left unvalidated (see `parseWithSchema`).

#### Parameters

    * input: unknown

#### Returns unknown

Inherited from [BaseAgent](BaseAgent.html).[validateInput](BaseAgent.html#validateinput)

    * Defined in [core/src/workflow/base_node.ts:178](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/base_node.ts#L178)




### validateOutput

  * validateOutput(value: unknown): unknown

Validates a value against this agent's output schema, in whichever dialect it was declared, and returns the parsed value.

Prefers the schema as supplied (outputSchemaSource) over the genai form derived from it, since the conversion drops constraints Zod can express and genai cannot.

#### Parameters

    * value: unknown

#### Returns unknown

#### Throws

if the value does not satisfy the schema.

Overrides [BaseAgent](BaseAgent.html).[validateOutput](BaseAgent.html#validateoutput)

    * Defined in [core/src/agents/llm_agent.ts:897](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/llm_agent.ts#L897)




Constructors

constructor

Properties

[BASE_AGENT_SIGNATURE_SYMBOL][BASE_NODE_SIGNATURE_SYMBOL][LLM_AGENT_SIGNATURE_SYMBOL]afterAgentCallbackafterModelCallbackafterToolCallbackbeforeAgentCallbackbeforeModelCallbackbeforeToolCallbackcodeExecutorconfigdescriptiondisallowTransferToParentdisallowTransferToPeersgenerateContentConfigglobalInstructionincludeContentsincludeContentsExplicitinputSchemainputSchemaSourceinstructionisolationScopemodemodelnameoutputKeyoutputSchemaoutputSchemaSourceparentAgentplannerpreparedRetryConfigrequestProcessorsrerunOnResumeresponseProcessorsretryConfigstateSchemasubAgentstimeouttoolswaitForOutput

Accessors

canonicalAfterModelCallbackscanonicalAfterToolCallbackscanonicalBeforeModelCallbackscanonicalBeforeToolCallbackscanonicalModelfinishTaskToolrequiresAllPredecessorsrootAgent

Methods

callLlmAsynccanonicalGlobalInstructioncanonicalInstructioncanonicalToolsclonecreateInvocationContextfindAgentfindSubAgenthandleAfterAgentCallbackhandleBeforeAgentCallbackrunrunAndHandleErrorrunAsyncrunAsyncImplrunImplrunLiverunLiveImpltoEventvalidateInputvalidateOutput

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


