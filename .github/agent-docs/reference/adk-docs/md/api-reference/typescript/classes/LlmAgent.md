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



  * Defined in [core/src/agents/llm_agent.ts:675](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L675)



## Constructors

### constructor

  * new LlmAgent(config: LlmAgentConfig): [LlmAgent]()

#### Parameters

    * config: LlmAgentConfig

#### Returns [LlmAgent]()

Overrides [BaseAgent](BaseAgent.html).[constructor](BaseAgent.html#constructor)

    * Defined in [core/src/agents/llm_agent.ts:694](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L694)




## Properties

### `Readonly`afterAgentCallback

afterAgentCallback: SingleAgentCallback[]

Callback or list of callbacks to be invoked after the agent run.

When a list of callbacks is provided, the callbacks will be called in the order they are listed until a callback does not return undefined.

#### Param: callbackContext:

MUST be named 'callbackContext' (enforced).

#### Returns

Content: The content to return to the user. When the content is present, the provided content will be used as agent response and appended to event history as agent response.

Inherited from [BaseAgent](BaseAgent.html).[afterAgentCallback](BaseAgent.html#afteragentcallback)

  * Defined in [core/src/agents/base_agent.ts:102](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L102)



### `Optional`afterModelCallback

afterModelCallback?: [AfterModelCallback](../types/AfterModelCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:688](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L688)



### `Optional`afterToolCallback

afterToolCallback?: [AfterToolCallback](../types/AfterToolCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:690](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L690)



### `Readonly`beforeAgentCallback

beforeAgentCallback: SingleAgentCallback[]

Callback or list of callbacks to be invoked before the agent run.

When a list of callbacks is provided, the callbacks will be called in the order they are listed until a callback does not return undefined.

#### Param: callbackContext:

MUST be named 'callbackContext' (enforced).

#### Returns

Content: The content to return to the user. When the content is present, the agent run will be skipped and the provided content will be returned to user.

Inherited from [BaseAgent](BaseAgent.html).[beforeAgentCallback](BaseAgent.html#beforeagentcallback)

  * Defined in [core/src/agents/base_agent.ts:88](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L88)



### `Optional`beforeModelCallback

beforeModelCallback?: [BeforeModelCallback](../types/BeforeModelCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:687](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L687)



### `Optional`beforeToolCallback

beforeToolCallback?: [BeforeToolCallback](../types/BeforeToolCallback.html)

  * Defined in [core/src/agents/llm_agent.ts:689](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L689)



### `Optional` `Readonly`description

description?: string

Description about the agent's capability.

The model uses this to determine whether to delegate control to the agent. One-line description is enough and preferred.

Inherited from [BaseAgent](BaseAgent.html).[description](BaseAgent.html#description)

  * Defined in [core/src/agents/base_agent.ts:51](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L51)



### disallowTransferToParent

disallowTransferToParent: boolean

  * Defined in [core/src/agents/llm_agent.ts:681](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L681)



### disallowTransferToPeers

disallowTransferToPeers: boolean

  * Defined in [core/src/agents/llm_agent.ts:682](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L682)



### `Optional`generateContentConfig

generateContentConfig?: GenerateContentConfig

  * Defined in [core/src/agents/llm_agent.ts:680](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L680)



### globalInstruction

globalInstruction: string | InstructionProvider

  * Defined in [core/src/agents/llm_agent.ts:678](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L678)



### includeContents

includeContents: "none" | "default"

  * Defined in [core/src/agents/llm_agent.ts:683](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L683)



### `Optional`inputSchema

inputSchema?: Schema

  * Defined in [core/src/agents/llm_agent.ts:684](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L684)



### instruction

instruction: string | InstructionProvider

  * Defined in [core/src/agents/llm_agent.ts:677](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L677)



### `Optional`model

model?: string | [BaseLlm](BaseLlm.html)

  * Defined in [core/src/agents/llm_agent.ts:676](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L676)



### `Readonly`name

name: string

The agent's name. Agent name must be a JS identifier and unique within the agent tree. Agent name cannot be "user", since it's reserved for end-user's input.

Inherited from [BaseAgent](BaseAgent.html).[name](BaseAgent.html#name)

  * Defined in [core/src/agents/base_agent.ts:43](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L43)



### `Optional`outputKey

outputKey?: string

  * Defined in [core/src/agents/llm_agent.ts:686](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L686)



### `Optional`outputSchema

outputSchema?: Schema

  * Defined in [core/src/agents/llm_agent.ts:685](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L685)



### `Optional`parentAgent

parentAgent?: [BaseAgent](BaseAgent.html)

The parent agent of this agent.

Note that an agent can ONLY be added as sub-agent once.

If you want to add one agent twice as sub-agent, consider to create two agent instances with identical config, but with different name and add them to the agent tree.

The parent agent is the agent that created this agent.

Inherited from [BaseAgent](BaseAgent.html).[parentAgent](BaseAgent.html#parentagent)

  * Defined in [core/src/agents/base_agent.ts:69](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L69)



### requestProcessors

requestProcessors: BaseLlmRequestProcessor[]

  * Defined in [core/src/agents/llm_agent.ts:691](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L691)



### responseProcessors

responseProcessors: BaseLlmResponseProcessor[]

  * Defined in [core/src/agents/llm_agent.ts:692](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L692)



### `Readonly`rootAgent

rootAgent: [BaseAgent](BaseAgent.html)

Root agent of this agent.

Inherited from [BaseAgent](BaseAgent.html).[rootAgent](BaseAgent.html#rootagent)

  * Defined in [core/src/agents/base_agent.ts:56](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L56)



### `Readonly`subAgents

subAgents: [BaseAgent](BaseAgent.html)[]

The sub-agents of this agent.

Inherited from [BaseAgent](BaseAgent.html).[subAgents](BaseAgent.html#subagents)

  * Defined in [core/src/agents/base_agent.ts:74](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L74)



### tools

tools: ToolUnion[]

  * Defined in [core/src/agents/llm_agent.ts:679](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L679)



## Accessors

### canonicalAfterModelCallbacks

  * get canonicalAfterModelCallbacks(): [SingleAfterModelCallback](../types/SingleAfterModelCallback.html)[]

The resolved self.after_model_callback field as a list of SingleAfterModelCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleAfterModelCallback](../types/SingleAfterModelCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:881](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L881)




### canonicalAfterToolCallbacks

  * get canonicalAfterToolCallbacks(): [SingleAfterToolCallback](../types/SingleAfterToolCallback.html)[]

The resolved self.after_tool_callback field as a list of AfterToolCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleAfterToolCallback](../types/SingleAfterToolCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:900](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L900)




### canonicalBeforeModelCallbacks

  * get canonicalBeforeModelCallbacks(): [SingleBeforeModelCallback](../types/SingleBeforeModelCallback.html)[]

The resolved self.before_model_callback field as a list of SingleBeforeModelCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleBeforeModelCallback](../types/SingleBeforeModelCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:871](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L871)




### canonicalBeforeToolCallbacks

  * get canonicalBeforeToolCallbacks(): [SingleBeforeToolCallback](../types/SingleBeforeToolCallback.html)[]

The resolved self.before_tool_callback field as a list of BeforeToolCallback.

This method is only for use by Agent Development Kit.

#### Returns [SingleBeforeToolCallback](../types/SingleBeforeToolCallback.html)[]

    * Defined in [core/src/agents/llm_agent.ts:891](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L891)




### canonicalModel

  * get canonicalModel(): [BaseLlm](BaseLlm.html)

The resolved BaseLlm instance.

When not set, the agent will inherit the model from its ancestor.

#### Returns [BaseLlm](BaseLlm.html)

    * Defined in [core/src/agents/llm_agent.ts:780](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L780)




## Methods

### canonicalGlobalInstruction

  * canonicalGlobalInstruction(  
context: ReadonlyContext,  
): Promise<{ instruction: string; requireStateInjection: boolean }>

The resolved self.instruction field to construct global instruction.

This method is only for use by Agent Development Kit.

#### Parameters

    * context: ReadonlyContext

The context to retrieve the session state.

#### Returns Promise<{ instruction: string; requireStateInjection: boolean }>

The resolved self.global_instruction field.

    * Defined in [core/src/agents/llm_agent.ts:824](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L824)




### canonicalInstruction

  * canonicalInstruction(  
context: ReadonlyContext,  
): Promise<{ instruction: string; requireStateInjection: boolean }>

The resolved self.instruction field to construct instruction for this agent.

This method is only for use by Agent Development Kit.

#### Parameters

    * context: ReadonlyContext

The context to retrieve the session state.

#### Returns Promise<{ instruction: string; requireStateInjection: boolean }>

The resolved self.instruction field.

    * Defined in [core/src/agents/llm_agent.ts:806](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L806)




### canonicalTools

  * canonicalTools(context?: ReadonlyContext): Promise<[BaseTool](BaseTool.html)[]>

The resolved self.tools field as a list of BaseTool based on the context.

This method is only for use by Agent Development Kit.

#### Parameters

    * `Optional`context: ReadonlyContext

#### Returns Promise<[BaseTool](BaseTool.html)[]>

    * Defined in [core/src/agents/llm_agent.ts:840](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L840)




### `Protected`createInvocationContext

  * createInvocationContext(parentContext: [InvocationContext](InvocationContext.html)): [InvocationContext](InvocationContext.html)

Creates an invocation context for this agent.

#### Parameters

    * parentContext: [InvocationContext](InvocationContext.html)

The invocation context of the parent agent.

#### Returns [InvocationContext](InvocationContext.html)

The invocation context for this agent.

Inherited from [BaseAgent](BaseAgent.html).[createInvocationContext](BaseAgent.html#createinvocationcontext)

    * Defined in [core/src/agents/base_agent.ts:237](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L237)




### findAgent

  * findAgent(name: string): [BaseAgent](BaseAgent.html) | undefined

Finds the agent with the given name in this agent and its descendants.

#### Parameters

    * name: string

The name of the agent to find.

#### Returns [BaseAgent](BaseAgent.html) | undefined

The agent with the given name, or undefined if not found.

Inherited from [BaseAgent](BaseAgent.html).[findAgent](BaseAgent.html#findagent)

    * Defined in [core/src/agents/base_agent.ts:206](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L206)




### findSubAgent

  * findSubAgent(name: string): [BaseAgent](BaseAgent.html) | undefined

Finds the agent with the given name in this agent's descendants.

#### Parameters

    * name: string

The name of the agent to find.

#### Returns [BaseAgent](BaseAgent.html) | undefined

The agent with the given name, or undefined if not found.

Inherited from [BaseAgent](BaseAgent.html).[findSubAgent](BaseAgent.html#findsubagent)

    * Defined in [core/src/agents/base_agent.ts:220](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L220)




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

    * Defined in [core/src/agents/base_agent.ts:294](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L294)




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

    * Defined in [core/src/agents/base_agent.ts:252](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L252)




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

    * Defined in [core/src/agents/base_agent.ts:125](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L125)




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

    * Defined in [core/src/agents/llm_agent.ts:964](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L964)




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

    * Defined in [core/src/agents/base_agent.ts:168](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L168)




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

    * Defined in [core/src/agents/llm_agent.ts:986](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/llm_agent.ts#L986)




Constructors

constructor

Properties

afterAgentCallbackafterModelCallbackafterToolCallbackbeforeAgentCallbackbeforeModelCallbackbeforeToolCallbackdescriptiondisallowTransferToParentdisallowTransferToPeersgenerateContentConfigglobalInstructionincludeContentsinputSchemainstructionmodelnameoutputKeyoutputSchemaparentAgentrequestProcessorsresponseProcessorsrootAgentsubAgentstools

Accessors

canonicalAfterModelCallbackscanonicalAfterToolCallbackscanonicalBeforeModelCallbackscanonicalBeforeToolCallbackscanonicalModel

Methods

canonicalGlobalInstructioncanonicalInstructioncanonicalToolscreateInvocationContextfindAgentfindSubAgenthandleAfterAgentCallbackhandleBeforeAgentCallbackrunAsyncrunAsyncImplrunLiverunLiveImpl

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


