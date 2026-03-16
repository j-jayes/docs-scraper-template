[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InvocationContext]()



# Class InvocationContext

An invocation context represents the data of a single invocation of an agent.

An invocation: 1\. Starts with a user message and ends with a final response. 2\. Can contain one or multiple agent calls. 3\. Is handled by runner.runAsync().

An invocation runs an agent until it does not request to transfer to another agent.

An agent call: 1\. Is handled by agent.runAsync(). 2\. Ends when agent.runAsync() ends.

An LLM agent call is an agent with a BaseLLMFlow. An LLM agent call can contain one or multiple steps.

An LLM agent runs steps in a loop until:

  1. A final response is generated.
  2. The agent transfers to another agent.
  3. The end_invocation is set to true by any callbacks or tools.



A step:

  1. Calls the LLM only once and yields its response.
  2. Calls the tools and yields their responses if requested.



The summarization of the function response is considered another step, since it is another llm call. A step ends when it's done calling llm and tools, or if the end_invocation is set to true at any time.
    
    
       ┌─────────────────────── invocation ──────────────────────────┐  
       ┌──────────── llm_agent_call_1 ────────────┐ ┌─ agent_call_2 ─┐  
       ┌──── step_1 ────────┐ ┌───── step_2 ──────┐  
       [call_llm] [call_tool] [call_llm] [transfer]
    Copy

  * Defined in [agents/invocation_context.ts:114](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L114)



## Constructors

### constructor

  * new InvocationContext(params: [InvocationContextParams](../interfaces/InvocationContextParams.html)): [InvocationContext]()

#### Parameters

    * params: [InvocationContextParams](../interfaces/InvocationContextParams.html)

The parameters for creating an invocation context.

#### Returns [InvocationContext]()

    * Defined in [agents/invocation_context.ts:191](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L191)




## Properties

### `Optional`activeStreamingTools

activeStreamingTools?: Record<string, [ActiveStreamingTool](ActiveStreamingTool.html)>

The running streaming tools of this invocation.

  * Defined in [agents/invocation_context.ts:181](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L181)



### agent

agent: [BaseAgent](BaseAgent.html)

The current agent of this invocation context.

  * Defined in [agents/invocation_context.ts:139](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L139)



### `Optional` `Readonly`artifactService

artifactService?: [BaseArtifactService](../interfaces/BaseArtifactService.html)

  * Defined in [agents/invocation_context.ts:115](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L115)



### `Optional`branch

branch?: string

The branch of the invocation context.

The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3.

Branch is used when multiple sub-agents shouldn't see their peer agents' conversation history.

  * Defined in [agents/invocation_context.ts:134](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L134)



### `Optional` `Readonly`credentialService

credentialService?: [BaseCredentialService](../interfaces/BaseCredentialService.html)

  * Defined in [agents/invocation_context.ts:118](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L118)



### endInvocation

endInvocation: boolean

Whether to end this invocation. Set to True in callbacks or tools to terminate this invocation.

  * Defined in [agents/invocation_context.ts:155](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L155)



### `Readonly`invocationId

invocationId: string

The id of this invocation context.

  * Defined in [agents/invocation_context.ts:123](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L123)



### `Optional`liveRequestQueue

liveRequestQueue?: [LiveRequestQueue](LiveRequestQueue.html)

The queue to receive live requests.

  * Defined in [agents/invocation_context.ts:176](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L176)



### `Optional` `Readonly`memoryService

memoryService?: [BaseMemoryService](../interfaces/BaseMemoryService.html)

  * Defined in [agents/invocation_context.ts:117](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L117)



### pluginManager

pluginManager: [PluginManager](PluginManager.html)

The manager for keeping track of plugins in this invocation.

  * Defined in [agents/invocation_context.ts:186](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L186)



### `Optional`runConfig

runConfig?: [RunConfig](../interfaces/RunConfig.html)

Configurations for live agents under this invocation.

  * Defined in [agents/invocation_context.ts:165](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L165)



### `Readonly`session

session: [Session](../interfaces/Session.html)

The current session of this invocation context.

  * Defined in [agents/invocation_context.ts:149](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L149)



### `Optional` `Readonly`sessionService

sessionService?: [BaseSessionService](BaseSessionService.html)

  * Defined in [agents/invocation_context.ts:116](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L116)



### `Optional`transcriptionCache

transcriptionCache?: [TranscriptionEntry](../interfaces/TranscriptionEntry.html)[]

Caches necessary, data audio or contents, that are needed by transcription.

  * Defined in [agents/invocation_context.ts:160](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L160)



### `Optional` `Readonly`userContent

userContent?: Content

The user content that started this invocation.

  * Defined in [agents/invocation_context.ts:144](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L144)



## Accessors

### appName

  * get appName(): string

The app name of the current session.

#### Returns string

    * Defined in [agents/invocation_context.ts:211](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L211)




### userId

  * get userId(): string

The user ID of the current session.

#### Returns string

    * Defined in [agents/invocation_context.ts:218](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L218)




## Methods

### incrementLlmCallCount

  * incrementLlmCallCount(): void

Tracks number of llm calls made.

#### Returns void

#### Throws

If number of llm calls made exceed the set threshold.

    * Defined in [agents/invocation_context.ts:227](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L227)




Constructors

constructor

Properties

activeStreamingToolsagentartifactServicebranchcredentialServiceendInvocationinvocationIdliveRequestQueuememoryServicepluginManagerrunConfigsessionsessionServicetranscriptionCacheuserContent

Accessors

appNameuserId

Methods

incrementLlmCallCount

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


