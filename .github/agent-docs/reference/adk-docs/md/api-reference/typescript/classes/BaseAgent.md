[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseAgent]()



# Class BaseAgent`Abstract`

Base class for all agents in Agent Development Kit.

#### Hierarchy ([View Summary](../hierarchy.html#BaseAgent))

  * BaseAgent
    * [LlmAgent](LlmAgent.html)
    * [LoopAgent](LoopAgent.html)
    * [ParallelAgent](ParallelAgent.html)
    * [SequentialAgent](SequentialAgent.html)



  * Defined in [core/src/agents/base_agent.ts:37](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L37)



## Constructors

### constructor

  * new BaseAgent(config: BaseAgentConfig): [BaseAgent]()

#### Parameters

    * config: BaseAgentConfig

#### Returns [BaseAgent]()

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

  * Defined in [core/src/agents/base_agent.ts:102](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L102)



### `Readonly`beforeAgentCallback

beforeAgentCallback: SingleAgentCallback[]

Callback or list of callbacks to be invoked before the agent run.

When a list of callbacks is provided, the callbacks will be called in the order they are listed until a callback does not return undefined.

#### Param: callbackContext:

MUST be named 'callbackContext' (enforced).

#### Returns

Content: The content to return to the user. When the content is present, the agent run will be skipped and the provided content will be returned to user.

  * Defined in [core/src/agents/base_agent.ts:88](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L88)



### `Optional` `Readonly`description

description?: string

Description about the agent's capability.

The model uses this to determine whether to delegate control to the agent. One-line description is enough and preferred.

  * Defined in [core/src/agents/base_agent.ts:51](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L51)



### `Readonly`name

name: string

The agent's name. Agent name must be a JS identifier and unique within the agent tree. Agent name cannot be "user", since it's reserved for end-user's input.

  * Defined in [core/src/agents/base_agent.ts:43](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L43)



### `Optional`parentAgent

parentAgent?: [BaseAgent]()

The parent agent of this agent.

Note that an agent can ONLY be added as sub-agent once.

If you want to add one agent twice as sub-agent, consider to create two agent instances with identical config, but with different name and add them to the agent tree.

The parent agent is the agent that created this agent.

  * Defined in [core/src/agents/base_agent.ts:69](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L69)



### `Readonly`rootAgent

rootAgent: [BaseAgent]()

Root agent of this agent.

  * Defined in [core/src/agents/base_agent.ts:56](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L56)



### `Readonly`subAgents

subAgents: [BaseAgent]()[]

The sub-agents of this agent.

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

    * Defined in [core/src/agents/base_agent.ts:237](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L237)




### findAgent

  * findAgent(name: string): [BaseAgent]() | undefined

Finds the agent with the given name in this agent and its descendants.

#### Parameters

    * name: string

The name of the agent to find.

#### Returns [BaseAgent]() | undefined

The agent with the given name, or undefined if not found.

    * Defined in [core/src/agents/base_agent.ts:206](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L206)




### findSubAgent

  * findSubAgent(name: string): [BaseAgent]() | undefined

Finds the agent with the given name in this agent's descendants.

#### Parameters

    * name: string

The name of the agent to find.

#### Returns [BaseAgent]() | undefined

The agent with the given name, or undefined if not found.

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

    * Defined in [core/src/agents/base_agent.ts:125](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L125)




### `Protected` `Abstract`runAsyncImpl

  * runAsyncImpl(context: [InvocationContext](InvocationContext.html)): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Core logic to run this agent via text-based conversation.

#### Parameters

    * context: [InvocationContext](InvocationContext.html)

The invocation context of the agent.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

An AsyncGenerator that yields the events generated by the agent.

#### Yields

The events generated by the agent.

    * Defined in [core/src/agents/base_agent.ts:187](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L187)




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

    * Defined in [core/src/agents/base_agent.ts:168](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L168)




### `Protected` `Abstract`runLiveImpl

  * runLiveImpl(context: [InvocationContext](InvocationContext.html)): AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Core logic to run this agent via video/audio-based conversation.

#### Parameters

    * context: [InvocationContext](InvocationContext.html)

The invocation context of the agent.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

An AsyncGenerator that yields the events generated by the agent.

#### Yields

The events generated by the agent.

    * Defined in [core/src/agents/base_agent.ts:197](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/base_agent.ts#L197)




Constructors

constructor

Properties

afterAgentCallbackbeforeAgentCallbackdescriptionnameparentAgentrootAgentsubAgents

Methods

createInvocationContextfindAgentfindSubAgenthandleAfterAgentCallbackhandleBeforeAgentCallbackrunAsyncrunAsyncImplrunLiverunLiveImpl

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


