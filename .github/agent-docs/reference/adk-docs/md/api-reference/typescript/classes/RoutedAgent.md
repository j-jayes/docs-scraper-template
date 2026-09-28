[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [RoutedAgent]()



# Class RoutedAgent

A BaseAgent implementation that delegates to one of multiple agents based on a router function. Routing is strictly limited to the agents passed in the config.

#### Remarks

Cloning is supported: RoutedAgent.clone deep-clones the routing targets from `config.agents` and re-parents the fresh copies onto the clone, so the clone is a detached root that routes identically to the original while leaving the original agent tree untouched.

#### Hierarchy ([View Summary](../hierarchy.html#RoutedAgent))

  * [BaseAgent](BaseAgent.html)<[RoutedAgentConfig](../interfaces/RoutedAgentConfig.html)>
    * RoutedAgent



  * Defined in [core/src/agents/routed_agent.ts:70](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/routed_agent.ts#L70)



## Constructors

### constructor

  * new RoutedAgent(config: [RoutedAgentConfig](../interfaces/RoutedAgentConfig.html)): [RoutedAgent]()

#### Parameters

    * config: [RoutedAgentConfig](../interfaces/RoutedAgentConfig.html)

#### Returns [RoutedAgent]()

Overrides [BaseAgent](BaseAgent.html).[constructor](BaseAgent.html#constructor)

    * Defined in [core/src/agents/routed_agent.ts:76](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/routed_agent.ts#L76)




## Properties

### `Readonly`[BASE_AGENT_SIGNATURE_SYMBOL]

"[BASE_AGENT_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK agent classes.

Inherited from [BaseAgent](BaseAgent.html).[[BASE_AGENT_SIGNATURE_SYMBOL]](BaseAgent.html#base_agent_signature_symbol)

  * Defined in [core/src/agents/base_agent.ts:84](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L84)



### `Readonly`[ROUTED_AGENT_SIGNATURE_SYMBOL]

"[ROUTED_AGENT_SIGNATURE_SYMBOL]": true

  * Defined in [core/src/agents/routed_agent.ts:71](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/routed_agent.ts#L71)



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



### `Protected` `Readonly`config

config: [RoutedAgentConfig](../interfaces/RoutedAgentConfig.html)

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



### `Readonly`name

name: string

The agent's name. Agent name must be a JS identifier and unique within the agent tree. Agent name cannot be "user", since it's reserved for end-user's input.

Inherited from [BaseAgent](BaseAgent.html).[name](BaseAgent.html#name)

  * Defined in [core/src/agents/base_agent.ts:101](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L101)



### `Optional`parentAgent

parentAgent?: [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)>

The parent agent of this agent.

Note that an agent can ONLY be added as sub-agent once.

If you want to add one agent twice as sub-agent, consider to create two agent instances with identical config, but with different name and add them to the agent tree.

The parent agent is the agent that created this agent.

Inherited from [BaseAgent](BaseAgent.html).[parentAgent](BaseAgent.html#parentagent)

  * Defined in [core/src/agents/base_agent.ts:130](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L130)



### `Readonly`subAgents

subAgents: [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)>[]

The sub-agents of this agent.

Inherited from [BaseAgent](BaseAgent.html).[subAgents](BaseAgent.html#subagents)

  * Defined in [core/src/agents/base_agent.ts:135](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L135)



## Accessors

### rootAgent

  * get rootAgent(): [BaseAgent](BaseAgent.html)

Root agent of this agent. Computed dynamically by traversing up the parent chain.

#### Returns [BaseAgent](BaseAgent.html)

Inherited from BaseAgent.rootAgent

    * Defined in [core/src/agents/base_agent.ts:115](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/base_agent.ts#L115)




## Methods

### clone

  * clone(overrides?: Partial<[RoutedAgentConfig](../interfaces/RoutedAgentConfig.html)>): this

Creates a detached copy of this routed agent.

The inherited [BaseAgent.clone](BaseAgent.html#clone) only deep-clones `subAgents`, but a `RoutedAgent` derives its routing targets from `config.agents`. Rebuilding through the base clone alone would re-read the already-parented original agents and throw "already has a parent agent". This override deep-clones the routing targets (unless the caller overrides `agents`) so the rebuilt constructor re-parents fresh, detached copies. The array-vs-record shape and, for records, the keys are preserved so the router keeps selecting the same targets.

#### Parameters

    * `Optional`overrides: Partial<[RoutedAgentConfig](../interfaces/RoutedAgentConfig.html)>

Config fields to override on the clone. Overriding `parentAgent` is rejected by the base implementation.

#### Returns this

A new detached `RoutedAgent` of the same concrete class.

Overrides [BaseAgent](BaseAgent.html).[clone](BaseAgent.html#clone)

    * Defined in [core/src/agents/routed_agent.ts:112](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/routed_agent.ts#L112)




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

Runs the selected agent via text-based conversation.

#### Parameters

    * context: [InvocationContext](InvocationContext.html)

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Overrides [BaseAgent](BaseAgent.html).[runAsyncImpl](BaseAgent.html#runasyncimpl)

    * Defined in [core/src/agents/routed_agent.ts:123](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/routed_agent.ts#L123)




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

Runs the selected agent via video/audio-based conversation.

#### Parameters

    * context: [InvocationContext](InvocationContext.html)

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, void>

Overrides [BaseAgent](BaseAgent.html).[runLiveImpl](BaseAgent.html#runliveimpl)

    * Defined in [core/src/agents/routed_agent.ts:134](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/routed_agent.ts#L134)




Constructors

constructor

Properties

[BASE_AGENT_SIGNATURE_SYMBOL][ROUTED_AGENT_SIGNATURE_SYMBOL]afterAgentCallbackbeforeAgentCallbackconfigdescriptionnameparentAgentsubAgents

Accessors

rootAgent

Methods

clonecreateInvocationContextfindAgentfindSubAgenthandleAfterAgentCallbackhandleBeforeAgentCallbackrunAsyncrunAsyncImplrunLiverunLiveImpl

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


