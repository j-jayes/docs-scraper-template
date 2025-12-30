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



  * Defined in [core/src/agents/parallel_agent.ts:21](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/parallel_agent.ts#L21)



## Constructors

### constructor

  * new ParallelAgent(config: BaseAgentConfig): [ParallelAgent]()

#### Parameters

    * config: BaseAgentConfig

#### Returns [ParallelAgent]()

Inherited from [BaseAgent](BaseAgent.html).[constructor](BaseAgent.html#constructor)

    * Defined in [core/src/agents/base_agent.ts:104](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L104)




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



### `Optional` `Readonly`description

description?: string

Description about the agent's capability.

The model uses this to determine whether to delegate control to the agent. One-line description is enough and preferred.

Inherited from [BaseAgent](BaseAgent.html).[description](BaseAgent.html#description)

  * Defined in [core/src/agents/base_agent.ts:51](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L51)



### `Readonly`name

name: string

The agent's name. Agent name must be a JS identifier and unique within the agent tree. Agent name cannot be "user", since it's reserved for end-user's input.

Inherited from [BaseAgent](BaseAgent.html).[name](BaseAgent.html#name)

  * Defined in [core/src/agents/base_agent.ts:43](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L43)



### `Optional`parentAgent

parentAgent?: [BaseAgent](BaseAgent.html)

The parent agent of this agent.

Note that an agent can ONLY be added as sub-agent once.

If you want to add one agent twice as sub-agent, consider to create two agent instances with identical config, but with different name and add them to the agent tree.

The parent agent is the agent that created this agent.

Inherited from [BaseAgent](BaseAgent.html).[parentAgent](BaseAgent.html#parentagent)

  * Defined in [core/src/agents/base_agent.ts:69](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L69)



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

    * Defined in [core/src/agents/parallel_agent.ts:23](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/parallel_agent.ts#L23)




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

    * Defined in [core/src/agents/parallel_agent.ts:36](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/parallel_agent.ts#L36)




Constructors

constructor

Properties

afterAgentCallbackbeforeAgentCallbackdescriptionnameparentAgentrootAgentsubAgents

Methods

createInvocationContextfindAgentfindSubAgenthandleAfterAgentCallbackhandleBeforeAgentCallbackrunAsyncrunAsyncImplrunLiverunLiveImpl

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


