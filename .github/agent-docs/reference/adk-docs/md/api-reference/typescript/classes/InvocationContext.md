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

  * Defined in [core/src/agents/invocation_context.ts:113](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L113)



## Constructors

### constructor

  * new InvocationContext(params: [InvocationContextParams](../interfaces/InvocationContextParams.html)): [InvocationContext]()

#### Parameters

    * params: [InvocationContextParams](../interfaces/InvocationContextParams.html)

The parameters for creating an invocation context.

#### Returns [InvocationContext]()

    * Defined in [core/src/agents/invocation_context.ts:191](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L191)




## Properties

### `Optional` `Readonly`abortSignal

abortSignal?: AbortSignal

  * Defined in [core/src/agents/invocation_context.ts:186](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L186)



### `Optional`activeStreamingTools

activeStreamingTools?: Record<string, [ActiveStreamingTool](ActiveStreamingTool.html)>

The running streaming tools of this invocation.

  * Defined in [core/src/agents/invocation_context.ts:179](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L179)



### agent

agent: [BaseAgent](BaseAgent.html)

The current agent of this invocation context.

  * Defined in [core/src/agents/invocation_context.ts:138](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L138)



### `Optional` `Readonly`artifactService

artifactService?: [SessionArtifactService](../interfaces/SessionArtifactService.html)

  * Defined in [core/src/agents/invocation_context.ts:114](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L114)



### `Optional`branch

branch?: string

The branch of the invocation context.

The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3.

Branch is used when multiple sub-agents shouldn't see their peer agents' conversation history.

  * Defined in [core/src/agents/invocation_context.ts:133](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L133)



### `Optional` `Readonly`credentialService

credentialService?: [BaseCredentialService](../interfaces/BaseCredentialService.html)

  * Defined in [core/src/agents/invocation_context.ts:117](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L117)



### endInvocation

endInvocation: boolean

Whether to end this invocation. Set to True in callbacks or tools to terminate this invocation.

  * Defined in [core/src/agents/invocation_context.ts:154](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L154)



### `Readonly`invocationId

invocationId: string

The id of this invocation context.

  * Defined in [core/src/agents/invocation_context.ts:122](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L122)



### `Optional` `Readonly`memoryService

memoryService?: [BaseMemoryService](../interfaces/BaseMemoryService.html)

  * Defined in [core/src/agents/invocation_context.ts:116](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L116)



### pluginManager

pluginManager: [PluginManager](PluginManager.html)

The manager for keeping track of plugins in this invocation.

  * Defined in [core/src/agents/invocation_context.ts:184](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L184)



### `Optional`runConfig

runConfig?: [RunConfig](../interfaces/RunConfig.html)

Configurations for live agents under this invocation.

  * Defined in [core/src/agents/invocation_context.ts:164](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L164)



### `Readonly`session

session: [Session](../interfaces/Session.html)

The current session of this invocation context.

  * Defined in [core/src/agents/invocation_context.ts:148](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L148)



### `Optional` `Readonly`sessionService

sessionService?: [BaseSessionService](BaseSessionService.html)

  * Defined in [core/src/agents/invocation_context.ts:115](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L115)



### `Optional`transcriptionCache

transcriptionCache?: [TranscriptionEntry](../interfaces/TranscriptionEntry.html)[]

Caches necessary, data audio or contents, that are needed by transcription.

  * Defined in [core/src/agents/invocation_context.ts:159](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L159)



### `Optional` `Readonly`userContent

userContent?: Content

The user content that started this invocation.

  * Defined in [core/src/agents/invocation_context.ts:143](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L143)



## Accessors

### appName

  * get appName(): string

The app name of the current session.

#### Returns string

    * Defined in [core/src/agents/invocation_context.ts:220](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L220)




### userId

  * get userId(): string

The user ID of the current session.

#### Returns string

    * Defined in [core/src/agents/invocation_context.ts:227](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L227)




## Methods

### incrementLlmCallCount

  * incrementLlmCallCount(): void

Tracks number of llm calls made.

#### Returns void

#### Throws

If number of llm calls made exceed the set threshold.

    * Defined in [core/src/agents/invocation_context.ts:236](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L236)




Constructors

constructor

Properties

abortSignalactiveStreamingToolsagentartifactServicebranchcredentialServiceendInvocationinvocationIdmemoryServicepluginManagerrunConfigsessionsessionServicetranscriptionCacheuserContent

Accessors

appNameuserId

Methods

incrementLlmCallCount

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


