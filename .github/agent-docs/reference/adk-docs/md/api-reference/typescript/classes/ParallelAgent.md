[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ParallelAgent]()



# Class ParallelAgent

A shell agent that run its sub-agents in parallel in isolated manner.

This approach is beneficial for scenarios requiring multiple perspectives or attempts on a single task, such as:

  * Running different algorithms simultaneously.
  * Generating multiple responses for review by a subsequent evaluation agent.



#### Hierarchy ([View Summary](../hierarchy.html#ParallelAgent))

  * [BaseAgent](BaseAgent.html)
    * ParallelAgent



  * Defined in [agents/parallel_agent.ts:41](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/parallel_agent.ts#L41)



## Constructors

### constructor

  * new ParallelAgent(config: [BaseAgentConfig](../interfaces/BaseAgentConfig.html)): [ParallelAgent]()

#### Parameters

    * config: [BaseAgentConfig](../interfaces/BaseAgentConfig.html)

#### Returns [ParallelAgent]()

Inherited from [BaseAgent](BaseAgent.html).[constructor](BaseAgent.html#constructor)

    * Defined in [agents/base_agent.ts:149](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L149)




## Properties

### `Readonly`[BASE_AGENT_SIGNATURE_SYMBOL]

"[BASE_AGENT_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK agent classes.

Inherited from [BaseAgent](BaseAgent.html).[[BASE_AGENT_SIGNATURE_SYMBOL]](BaseAgent.html#base_agent_signature_symbol)

  * Defined in [agents/base_agent.ts:78](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L78)



### `Readonly`[PARALLEL_AGENT_SIGNATURE_SYMBOL]

"[PARALLEL_AGENT_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK parallel agent class.

  * Defined in [agents/parallel_agent.ts:45](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/parallel_agent.ts#L45)



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



### `Optional` `Readonly`description

description?: string

Description about the agent's capability.

The model uses this to determine whether to delegate control to the agent. One-line description is enough and preferred.

Inherited from [BaseAgent](BaseAgent.html).[description](BaseAgent.html#description)

  * Defined in [agents/base_agent.ts:93](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L93)



### `Readonly`name

name: string

The agent's name. Agent name must be a JS identifier and unique within the agent tree. Agent name cannot be "user", since it's reserved for end-user's input.

Inherited from [BaseAgent](BaseAgent.html).[name](BaseAgent.html#name)

  * Defined in [agents/base_agent.ts:85](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L85)



### `Optional`parentAgent

parentAgent?: [BaseAgent](BaseAgent.html)

The parent agent of this agent.

Note that an agent can ONLY be added as sub-agent once.

If you want to add one agent twice as sub-agent, consider to create two agent instances with identical config, but with different name and add them to the agent tree.

The parent agent is the agent that created this agent.

Inherited from [BaseAgent](BaseAgent.html).[parentAgent](BaseAgent.html#parentagent)

  * Defined in [agents/base_agent.ts:114](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L114)



### `Readonly`subAgents

subAgents: [BaseAgent](BaseAgent.html)[]

The sub-agents of this agent.

Inherited from [BaseAgent](BaseAgent.html).[subAgents](BaseAgent.html#subagents)

  * Defined in [agents/base_agent.ts:119](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L119)



## Accessors

### rootAgent

  * get rootAgent(): [BaseAgent](BaseAgent.html)

Root agent of this agent. Computed dynamically by traversing up the parent chain.

#### Returns [BaseAgent](BaseAgent.html)

Inherited from BaseAgent.rootAgent

    * Defined in [agents/base_agent.ts:99](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/base_agent.ts#L99)




## Methods

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

    * Defined in [agents/parallel_agent.ts:47](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/parallel_agent.ts#L47)




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

  * runLiveImpl(_context: [InvocationContext](InvocationContext.html)): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Core logic to run this agent via video/audio-based conversation.

#### Parameters

    * _context: [InvocationContext](InvocationContext.html)

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

An AsyncGenerator that yields the events generated by the agent.

#### Yields

The events generated by the agent.

Overrides [BaseAgent](BaseAgent.html).[runLiveImpl](BaseAgent.html#runliveimpl)

    * Defined in [agents/parallel_agent.ts:60](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/parallel_agent.ts#L60)




Constructors

constructor

Properties

[BASE_AGENT_SIGNATURE_SYMBOL][PARALLEL_AGENT_SIGNATURE_SYMBOL]afterAgentCallbackbeforeAgentCallbackdescriptionnameparentAgentsubAgents

Accessors

rootAgent

Methods

createInvocationContextfindAgentfindSubAgenthandleAfterAgentCallbackhandleBeforeAgentCallbackrunAsyncrunAsyncImplrunLiverunLiveImpl

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


