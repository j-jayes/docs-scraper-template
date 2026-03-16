[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LlmAgent]()



# Class LlmAgent

An agent that uses a large language model to generate responses.

#### Hierarchy ([View Summary](../hierarchy.html#LlmAgent))

  * [BaseAgent](BaseAgent.html)
    * LlmAgent



  * Defined in [agents/llm_agent.ts:336](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L336)



## Constructors

### constructor

  * new LlmAgent(config: [LlmAgentConfig](../interfaces/LlmAgentConfig.html)): [LlmAgent]()

#### Parameters

    * config: [LlmAgentConfig](../interfaces/LlmAgentConfig.html)

#### Returns [LlmAgent]()

Overrides [BaseAgent](BaseAgent.html).[constructor](BaseAgent.html#constructor)

    * Defined in [agents/llm_agent.ts:359](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L359)




## Properties

### `Readonly`[BASE_AGENT_SIGNATURE_SYMBOL]

"[BASE_AGENT_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK agent classes.

Inherited from [BaseAgent](BaseAgent.html).[[BASE_AGENT_SIGNATURE_SYMBOL]](BaseAgent.html#base_agent_signature_symbol)

  * Defined in [agents/base_agent.ts:78](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L78)



### `Readonly`[LLM_AGENT_SIGNATURE_SYMBOL]

"[LLM_AGENT_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK LLM agent class.

  * Defined in [agents/llm_agent.ts:338](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L338)



### `Readonly`afterAgentCallback

afterAgentCallback: [SingleAgentCallback](../types/SingleAgentCallback.html)[]

Callback or list of callbacks to be invoked after the agent run.

When a list of callbacks is provided, the callbacks will be called in the order they are listed until a callback does not return undefined.

#### Param: callbackContext:

MUST be named 'callbackContext' (enforced).

#### Returns

Content: The content to return to the user. When the content is present, the provided content will be used as agent response and appended to event history as agent response.

Inherited from [BaseAgent](BaseAgent.html).[afterAgentCallback](BaseAgent.html#afteragentcallback)

  * Defined in [agents/base_agent.ts:147](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L147)



### `Optional`afterModelCallback

afterModelCallback?: [AfterModelCallback](../types/AfterModelCallback.html)

  * Defined in [agents/llm_agent.ts:352](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L352)



### `Optional`afterToolCallback

afterToolCallback?: [AfterToolCallback](../types/AfterToolCallback.html)

  * Defined in [agents/llm_agent.ts:354](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L354)



### `Readonly`beforeAgentCallback

beforeAgentCallback: [SingleAgentCallback](../types/SingleAgentCallback.html)[]

Callback or list of callbacks to be invoked before the agent run.

When a list of callbacks is provided, the callbacks will be called in the order they are listed until a callback does not return undefined.

#### Param: callbackContext:

MUST be named 'callbackContext' (enforced).

#### Returns

Content: The content to return to the user. When the content is present, the agent run will be skipped and the provided content will be returned to user.

Inherited from [BaseAgent](BaseAgent.html).[beforeAgentCallback](BaseAgent.html#beforeagentcallback)

  * Defined in [agents/base_agent.ts:133](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L133)



### `Optional`beforeModelCallback

beforeModelCallback?: [BeforeModelCallback](../types/BeforeModelCallback.html)

  * Defined in [agents/llm_agent.ts:351](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L351)



### `Optional`beforeToolCallback

beforeToolCallback?: [BeforeToolCallback](../types/BeforeToolCallback.html)

  * Defined in [agents/llm_agent.ts:353](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L353)



### `Optional`codeExecutor

codeExecutor?: [BaseCodeExecutor](BaseCodeExecutor.html)

  * Defined in [agents/llm_agent.ts:357](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L357)



### `Optional` `Readonly`description

description?: string

Description about the agent's capability.

The model uses this to determine whether to delegate control to the agent. One-line description is enough and preferred.

Inherited from [BaseAgent](BaseAgent.html).[description](BaseAgent.html#description)

  * Defined in [agents/base_agent.ts:93](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L93)



### disallowTransferToParent

disallowTransferToParent: boolean

  * Defined in [agents/llm_agent.ts:345](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L345)



### disallowTransferToPeers

disallowTransferToPeers: boolean

  * Defined in [agents/llm_agent.ts:346](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L346)



### `Optional`generateContentConfig

generateContentConfig?: GenerateContentConfig

  * Defined in [agents/llm_agent.ts:344](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L344)



### globalInstruction

globalInstruction: string | [InstructionProvider](../types/InstructionProvider.html)

  * Defined in [agents/llm_agent.ts:342](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L342)



### includeContents

includeContents: "none" | "default"

  * Defined in [agents/llm_agent.ts:347](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L347)



### `Optional`inputSchema

inputSchema?: Schema

  * Defined in [agents/llm_agent.ts:348](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L348)



### instruction

instruction: string | [InstructionProvider](../types/InstructionProvider.html)

  * Defined in [agents/llm_agent.ts:341](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L341)



### `Optional`model

model?: string | [BaseLlm](BaseLlm.html)

  * Defined in [agents/llm_agent.ts:340](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L340)



### `Readonly`name

name: string

The agent's name. Agent name must be a JS identifier and unique within the agent tree. Agent name cannot be "user", since it's reserved for end-user's input.

Inherited from [BaseAgent](BaseAgent.html).[name](BaseAgent.html#name)

  * Defined in [agents/base_agent.ts:85](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L85)



### `Optional`outputKey

outputKey?: string

  * Defined in [agents/llm_agent.ts:350](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L350)



### `Optional`outputSchema

outputSchema?: Schema

  * Defined in [agents/llm_agent.ts:349](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L349)



### `Optional`parentAgent

parentAgent?: [BaseAgent](BaseAgent.html)

The parent agent of this agent.

Note that an agent can ONLY be added as sub-agent once.

If you want to add one agent twice as sub-agent, consider to create two agent instances with identical config, but with different name and add them to the agent tree.

The parent agent is the agent that created this agent.

Inherited from [BaseAgent](BaseAgent.html).[parentAgent](BaseAgent.html#parentagent)

  * Defined in [agents/base_agent.ts:114](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L114)



### requestProcessors

requestProcessors: [BaseLlmRequestProcessor](BaseLlmRequestProcessor.html)[]

  * Defined in [agents/llm_agent.ts:355](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L355)



### responseProcessors

responseProcessors: [BaseLlmResponseProcessor](BaseLlmResponseProcessor.html)[]

  * Defined in [agents/llm_agent.ts:356](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L356)



### `Readonly`subAgents

subAgents: [BaseAgent](BaseAgent.html)[]

The sub-agents of this agent.

Inherited from [BaseAgent](BaseAgent.html).[subAgents](BaseAgent.html#subagents)

  * Defined in [agents/base_agent.ts:119](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L119)



### tools

tools: [ToolUnion](../types/ToolUnion.html)[]

  * Defined in [agents/llm_agent.ts:343](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L343)



## Accessors

### canonicalAfterModelCallbacks

  * get canonicalAfterModelCallbacks(): [SingleAfterModelCallback](../types/SingleAfterModelCallback.html)[]

The resolved afterModelCallback field as a list of SingleAfterModelCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleAfterModelCallback](../types/SingleAfterModelCallback.html)[]

    * Defined in [agents/llm_agent.ts:548](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L548)




### canonicalAfterToolCallbacks

  * get canonicalAfterToolCallbacks(): [SingleAfterToolCallback](../types/SingleAfterToolCallback.html)[]

The resolved afterToolCallback field as a list of AfterToolCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleAfterToolCallback](../types/SingleAfterToolCallback.html)[]

    * Defined in [agents/llm_agent.ts:567](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L567)




### canonicalBeforeModelCallbacks

  * get canonicalBeforeModelCallbacks(): [SingleBeforeModelCallback](../types/SingleBeforeModelCallback.html)[]

The resolved beforeModelCallback field as a list of SingleBeforeModelCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleBeforeModelCallback](../types/SingleBeforeModelCallback.html)[]

    * Defined in [agents/llm_agent.ts:538](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L538)




### canonicalBeforeToolCallbacks

  * get canonicalBeforeToolCallbacks(): [SingleBeforeToolCallback](../types/SingleBeforeToolCallback.html)[]

The resolved beforeToolCallback field as a list of BeforeToolCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleBeforeToolCallback](../types/SingleBeforeToolCallback.html)[]

    * Defined in [agents/llm_agent.ts:558](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L558)




### canonicalModel

  * get canonicalModel(): [BaseLlm](BaseLlm.html)

The resolved BaseLlm instance.

When not set, the agent will inherit the model from its ancestor.

#### Returns [BaseLlm](BaseLlm.html)

    * Defined in [agents/llm_agent.ts:441](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L441)




### rootAgent

  * get rootAgent(): [BaseAgent](BaseAgent.html)

Root agent of this agent. Computed dynamically by traversing up the parent chain.

#### Returns [BaseAgent](BaseAgent.html)

Inherited from BaseAgent.rootAgent

    * Defined in [agents/base_agent.ts:99](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L99)




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

    * Defined in [agents/llm_agent.ts:905](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L905)




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

    * Defined in [agents/llm_agent.ts:487](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L487)




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

    * Defined in [agents/llm_agent.ts:468](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L468)




### canonicalTools

  * canonicalTools(context?: [ReadonlyContext](ReadonlyContext.html)): Promise<[BaseTool](BaseTool.html)[]>

The resolved tools field as a list of BaseTool based on the context.

This method is only for use by Agent Development Kit.

#### Parameters

    * `Optional`context: [ReadonlyContext](ReadonlyContext.html)

#### Returns Promise<[BaseTool](BaseTool.html)[]>

    * Defined in [agents/llm_agent.ts:507](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L507)




### `Protected`createInvocationContext

  * createInvocationContext(parentContext: [InvocationContext](InvocationContext.html)): [InvocationContext](InvocationContext.html)

Creates an invocation context for this agent.

#### Parameters

    * parentContext: [InvocationContext](InvocationContext.html)

The invocation context of the parent agent.

#### Returns [InvocationContext](InvocationContext.html)

The invocation context for this agent.

Inherited from [BaseAgent](BaseAgent.html).[createInvocationContext](BaseAgent.html#createinvocationcontext)

    * Defined in [agents/base_agent.ts:297](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L297)




### findAgent

  * findAgent(name: string): [BaseAgent](BaseAgent.html) | undefined

Finds the agent with the given name in this agent and its descendants.

#### Parameters

    * name: string

The name of the agent to find.

#### Returns [BaseAgent](BaseAgent.html) | undefined

The agent with the given name, or undefined if not found.

Inherited from [BaseAgent](BaseAgent.html).[findAgent](BaseAgent.html#findagent)

    * Defined in [agents/base_agent.ts:266](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L266)




### findSubAgent

  * findSubAgent(name: string): [BaseAgent](BaseAgent.html) | undefined

Finds the agent with the given name in this agent's descendants.

#### Parameters

    * name: string

The name of the agent to find.

#### Returns [BaseAgent](BaseAgent.html) | undefined

The agent with the given name, or undefined if not found.

Inherited from [BaseAgent](BaseAgent.html).[findSubAgent](BaseAgent.html#findsubagent)

    * Defined in [agents/base_agent.ts:280](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L280)




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

    * Defined in [agents/base_agent.ts:356](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L356)




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

    * Defined in [agents/base_agent.ts:313](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L313)




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

    * Defined in [agents/llm_agent.ts:1031](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L1031)




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

    * Defined in [agents/base_agent.ts:169](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L169)




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

    * Defined in [agents/llm_agent.ts:632](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L632)




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

    * Defined in [agents/base_agent.ts:219](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L219)




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

    * Defined in [agents/llm_agent.ts:653](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/llm_agent.ts#L653)




Constructors

constructor

Properties

[BASE_AGENT_SIGNATURE_SYMBOL][LLM_AGENT_SIGNATURE_SYMBOL]afterAgentCallbackafterModelCallbackafterToolCallbackbeforeAgentCallbackbeforeModelCallbackbeforeToolCallbackcodeExecutordescriptiondisallowTransferToParentdisallowTransferToPeersgenerateContentConfigglobalInstructionincludeContentsinputSchemainstructionmodelnameoutputKeyoutputSchemaparentAgentrequestProcessorsresponseProcessorssubAgentstools

Accessors

canonicalAfterModelCallbackscanonicalAfterToolCallbackscanonicalBeforeModelCallbackscanonicalBeforeToolCallbackscanonicalModelrootAgent

Methods

callLlmAsynccanonicalGlobalInstructioncanonicalInstructioncanonicalToolscreateInvocationContextfindAgentfindSubAgenthandleAfterAgentCallbackhandleBeforeAgentCallbackrunAndHandleErrorrunAsyncrunAsyncImplrunLiverunLiveImpl

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


