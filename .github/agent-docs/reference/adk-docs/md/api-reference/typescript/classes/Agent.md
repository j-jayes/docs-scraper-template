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



  * Defined in [core/src/agents/llm_agent.ts:351](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L351)



## Constructors

### constructor

  * new Agent(config: [LlmAgentConfig](../interfaces/LlmAgentConfig.html)): [Agent]()

#### Parameters

    * config: [LlmAgentConfig](../interfaces/LlmAgentConfig.html)

#### Returns [Agent]()

Overrides [BaseAgent](BaseAgent.html).[constructor](BaseAgent.html#constructor)

    * Defined in [core/src/agents/llm_agent.ts:375](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L375)




## Properties

### `Readonly`[BASE_AGENT_SIGNATURE_SYMBOL]

"[BASE_AGENT_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK agent classes.

Inherited from [BaseAgent](BaseAgent.html).[[BASE_AGENT_SIGNATURE_SYMBOL]](BaseAgent.html#base_agent_signature_symbol)

  * Defined in [core/src/agents/base_agent.ts:84](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L84)



### `Readonly`[LLM_AGENT_SIGNATURE_SYMBOL]

"[LLM_AGENT_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK LLM agent class.

  * Defined in [core/src/agents/llm_agent.ts:353](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L353)



### `Readonly`afterAgentCallback

afterAgentCallback: [SingleAgentCallback](../types/SingleAgentCallback.html)[]

Callback or list of callbacks to be invoked after the agent run.

When a list of callbacks is provided, the callbacks will be called in the order they are listed until a callback does not return undefined.

#### Param: callbackContext:

MUST be named 'callbackContext' (enforced).

#### Returns

Content: The content to return to the user. When the content is present, the provided content will be used as agent response and appended to event history as agent response.

Inherited from [BaseAgent](BaseAgent.html).[afterAgentCallback](BaseAgent.html#afteragentcallback)

  * Defined in [core/src/agents/base_agent.ts:163](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L163)



### `Optional`afterModelCallback

afterModelCallback?: [AfterModelCallback](../types/AfterModelCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:368](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L368)



### `Optional`afterToolCallback

afterToolCallback?: [AfterToolCallback](../types/AfterToolCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:370](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L370)



### `Readonly`beforeAgentCallback

beforeAgentCallback: [SingleAgentCallback](../types/SingleAgentCallback.html)[]

Callback or list of callbacks to be invoked before the agent run.

When a list of callbacks is provided, the callbacks will be called in the order they are listed until a callback does not return undefined.

#### Param: callbackContext:

MUST be named 'callbackContext' (enforced).

#### Returns

Content: The content to return to the user. When the content is present, the agent run will be skipped and the provided content will be returned to user.

Inherited from [BaseAgent](BaseAgent.html).[beforeAgentCallback](BaseAgent.html#beforeagentcallback)

  * Defined in [core/src/agents/base_agent.ts:149](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L149)



### `Optional`beforeModelCallback

beforeModelCallback?: [BeforeModelCallback](../types/BeforeModelCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:367](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L367)



### `Optional`beforeToolCallback

beforeToolCallback?: [BeforeToolCallback](../types/BeforeToolCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:369](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L369)



### `Optional`codeExecutor

codeExecutor?: [BaseCodeExecutor](BaseCodeExecutor.html)

  * Defined in [core/src/agents/llm_agent.ts:373](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L373)



### `Protected` `Readonly`config

config: [LlmAgentConfig](../interfaces/LlmAgentConfig.html)

The config this agent was constructed from.

Stored so clone can rebuild the agent by re-running the concrete constructor with overrides applied, which re-derives all state correctly instead of copying an already-mutated instance. Shallow-copied so later external mutation of the caller's object does not leak into clones.

Inherited from [BaseAgent](BaseAgent.html).[config](BaseAgent.html#config)

  * Defined in [core/src/agents/base_agent.ts:94](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L94)



### `Optional` `Readonly`description

description?: string

Description about the agent's capability.

The model uses this to determine whether to delegate control to the agent. One-line description is enough and preferred.

Inherited from [BaseAgent](BaseAgent.html).[description](BaseAgent.html#description)

  * Defined in [core/src/agents/base_agent.ts:109](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L109)



### disallowTransferToParent

disallowTransferToParent: boolean

  * Defined in [core/src/agents/llm_agent.ts:361](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L361)



### disallowTransferToPeers

disallowTransferToPeers: boolean

  * Defined in [core/src/agents/llm_agent.ts:362](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L362)



### `Optional`generateContentConfig

generateContentConfig?: GenerateContentConfig

  * Defined in [core/src/agents/llm_agent.ts:360](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L360)



### globalInstruction

globalInstruction: string | [InstructionProvider](../types/InstructionProvider.html)

#### Deprecated

Use GlobalInstructionPlugin instead.

  * Defined in [core/src/agents/llm_agent.ts:358](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L358)



### includeContents

includeContents: "default" | "none"

  * Defined in [core/src/agents/llm_agent.ts:363](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L363)



### `Optional`inputSchema

inputSchema?: Schema

  * Defined in [core/src/agents/llm_agent.ts:364](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L364)



### instruction

instruction: string | [InstructionProvider](../types/InstructionProvider.html)

  * Defined in [core/src/agents/llm_agent.ts:356](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L356)



### `Optional`model

model?: string | [BaseLlm](BaseLlm.html)

  * Defined in [core/src/agents/llm_agent.ts:355](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L355)



### `Readonly`name

name: string

The agent's name. Agent name must be a JS identifier and unique within the agent tree. Agent name cannot be "user", since it's reserved for end-user's input.

Inherited from [BaseAgent](BaseAgent.html).[name](BaseAgent.html#name)

  * Defined in [core/src/agents/base_agent.ts:101](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L101)



### `Optional`outputKey

outputKey?: string

  * Defined in [core/src/agents/llm_agent.ts:366](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L366)



### `Optional`outputSchema

outputSchema?: Schema

  * Defined in [core/src/agents/llm_agent.ts:365](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L365)



### `Optional`parentAgent

parentAgent?: [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)>

The parent agent of this agent.

Note that an agent can ONLY be added as sub-agent once.

If you want to add one agent twice as sub-agent, consider to create two agent instances with identical config, but with different name and add them to the agent tree.

The parent agent is the agent that created this agent.

Inherited from [BaseAgent](BaseAgent.html).[parentAgent](BaseAgent.html#parentagent)

  * Defined in [core/src/agents/base_agent.ts:130](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L130)



### requestProcessors

requestProcessors: [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html)[]

  * Defined in [core/src/agents/llm_agent.ts:371](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L371)



### responseProcessors

responseProcessors: [BaseLlmResponseProcessor](BaseLlmResponseProcessor.html)[]

  * Defined in [core/src/agents/llm_agent.ts:372](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L372)



### `Readonly`subAgents

subAgents: [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)>[]

The sub-agents of this agent.

Inherited from [BaseAgent](BaseAgent.html).[subAgents](BaseAgent.html#subagents)

  * Defined in [core/src/agents/base_agent.ts:135](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L135)



### tools

tools: [ToolUnion](../types/ToolUnion.html)[]

  * Defined in [core/src/agents/llm_agent.ts:359](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L359)



## Accessors

### canonicalAfterModelCallbacks

  * get canonicalAfterModelCallbacks(): [SingleAfterModelCallback](../types/SingleAfterModelCallback.html)[]

The resolved afterModelCallback field as a list of SingleAfterModelCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleAfterModelCallback](../types/SingleAfterModelCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:591](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L591)




### canonicalAfterToolCallbacks

  * get canonicalAfterToolCallbacks(): [SingleAfterToolCallback](../types/SingleAfterToolCallback.html)[]

The resolved afterToolCallback field as a list of AfterToolCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleAfterToolCallback](../types/SingleAfterToolCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:610](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L610)




### canonicalBeforeModelCallbacks

  * get canonicalBeforeModelCallbacks(): [SingleBeforeModelCallback](../types/SingleBeforeModelCallback.html)[]

The resolved beforeModelCallback field as a list of SingleBeforeModelCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleBeforeModelCallback](../types/SingleBeforeModelCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:581](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L581)




### canonicalBeforeToolCallbacks

  * get canonicalBeforeToolCallbacks(): [SingleBeforeToolCallback](../types/SingleBeforeToolCallback.html)[]

The resolved beforeToolCallback field as a list of BeforeToolCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleBeforeToolCallback](../types/SingleBeforeToolCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:601](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L601)




### canonicalModel

  * get canonicalModel(): [BaseLlm](BaseLlm.html)

The resolved BaseLlm instance.

When not set, the agent will inherit the model from its ancestor.

#### Returns [BaseLlm](BaseLlm.html)

    * Defined in [core/src/agents/llm_agent.ts:483](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L483)




### rootAgent

  * get rootAgent(): [BaseAgent](BaseAgent.html)

Root agent of this agent. Computed dynamically by traversing up the parent chain.

#### Returns [BaseAgent](BaseAgent.html)

Inherited from BaseAgent.rootAgent

    * Defined in [core/src/agents/base_agent.ts:115](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L115)




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

    * Defined in [core/src/agents/llm_agent.ts:1051](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L1051)




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

    * Defined in [core/src/agents/llm_agent.ts:530](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L530)




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

    * Defined in [core/src/agents/llm_agent.ts:510](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L510)




### canonicalTools

  * canonicalTools(context?: [ReadonlyContext](ReadonlyContext.html)): Promise<[BaseTool](BaseTool.html)[]>

The resolved tools field as a list of BaseTool based on the context.

This method is only for use by Agent Development Kit.

#### Parameters

    * `Optional`context: [ReadonlyContext](ReadonlyContext.html)

#### Returns Promise<[BaseTool](BaseTool.html)[]>

    * Defined in [core/src/agents/llm_agent.ts:550](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L550)




### clone

  * clone(overrides?: Partial<[LlmAgentConfig](../interfaces/LlmAgentConfig.html)>): this

Creates a copy of this agent with the given config fields overridden.

Mirrors adk-python's `BaseAgent.clone(update=...)`. The clone is a detached root: its `parentAgent` is always `undefined`. Sub-agents are recursively cloned (and re-parented to the clone) unless `subAgents` is overridden. Rebuilding via the concrete constructor re-derives all state, so a cloned `LlmAgent` gets a fresh `requestProcessors` array rather than sharing the original's. See google/adk-js#534.

#### Parameters

    * `Optional`overrides: Partial<[LlmAgentConfig](../interfaces/LlmAgentConfig.html)>

Config fields to override on the clone. Overriding `parentAgent` is rejected, matching adk-python.

#### Returns this

A new detached agent instance of the same concrete class.

Inherited from [BaseAgent](BaseAgent.html).[clone](BaseAgent.html#clone)

    * Defined in [core/src/agents/base_agent.ts:195](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L195)




### `Protected`createInvocationContext

  * createInvocationContext(parentContext: [InvocationContext](InvocationContext.html)): [InvocationContext](InvocationContext.html)

Creates an invocation context for this agent.

#### Parameters

    * parentContext: [InvocationContext](InvocationContext.html)

The invocation context of the parent agent.

#### Returns [InvocationContext](InvocationContext.html)

The invocation context for this agent.

Inherited from [BaseAgent](BaseAgent.html).[createInvocationContext](BaseAgent.html#createinvocationcontext)

    * Defined in [core/src/agents/base_agent.ts:392](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L392)




### findAgent

  * findAgent(name: string): [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)> | undefined

Finds the agent with the given name in this agent and its descendants.

#### Parameters

    * name: string

The name of the agent to find.

#### Returns [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)> | undefined

The agent with the given name, or undefined if not found.

Inherited from [BaseAgent](BaseAgent.html).[findAgent](BaseAgent.html#findagent)

    * Defined in [core/src/agents/base_agent.ts:361](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L361)




### findSubAgent

  * findSubAgent(name: string): [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)> | undefined

Finds the agent with the given name in this agent's descendants.

#### Parameters

    * name: string

The name of the agent to find.

#### Returns [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)> | undefined

The agent with the given name, or undefined if not found.

Inherited from [BaseAgent](BaseAgent.html).[findSubAgent](BaseAgent.html#findsubagent)

    * Defined in [core/src/agents/base_agent.ts:375](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L375)




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

    * Defined in [core/src/agents/base_agent.ts:455](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L455)




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

    * Defined in [core/src/agents/base_agent.ts:408](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L408)




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

    * Defined in [core/src/agents/llm_agent.ts:1207](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L1207)




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

    * Defined in [core/src/agents/base_agent.ts:241](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L241)




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

    * Defined in [core/src/agents/llm_agent.ts:675](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L675)




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

    * Defined in [core/src/agents/base_agent.ts:291](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L291)




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

    * Defined in [core/src/agents/llm_agent.ts:720](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/llm_agent.ts#L720)




Constructors

constructor

Properties

[BASE_AGENT_SIGNATURE_SYMBOL][LLM_AGENT_SIGNATURE_SYMBOL]afterAgentCallbackafterModelCallbackafterToolCallbackbeforeAgentCallbackbeforeModelCallbackbeforeToolCallbackcodeExecutorconfigdescriptiondisallowTransferToParentdisallowTransferToPeersgenerateContentConfigglobalInstructionincludeContentsinputSchemainstructionmodelnameoutputKeyoutputSchemaparentAgentrequestProcessorsresponseProcessorssubAgentstools

Accessors

canonicalAfterModelCallbackscanonicalAfterToolCallbackscanonicalBeforeModelCallbackscanonicalBeforeToolCallbackscanonicalModelrootAgent

Methods

callLlmAsynccanonicalGlobalInstructioncanonicalInstructioncanonicalToolsclonecreateInvocationContextfindAgentfindSubAgenthandleAfterAgentCallbackhandleBeforeAgentCallbackrunAndHandleErrorrunAsyncrunAsyncImplrunLiverunLiveImpl

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


