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

  * Defined in [core/src/agents/invocation_context.ts:107](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L107)



## Constructors

### constructor

  * new InvocationContext(params: InvocationContextParams): [InvocationContext]()

#### Parameters

    * params: InvocationContextParams

The parameters for creating an invocation context.

#### Returns [InvocationContext]()

    * Defined in [core/src/agents/invocation_context.ts:184](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L184)




## Properties

### `Optional`activeStreamingTools

activeStreamingTools?: Record<string, ActiveStreamingTool>

The running streaming tools of this invocation.

  * Defined in [core/src/agents/invocation_context.ts:174](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L174)



### agent

agent: [BaseAgent](BaseAgent.html)

The current agent of this invocation context.

  * Defined in [core/src/agents/invocation_context.ts:132](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L132)



### `Optional` `Readonly`artifactService

artifactService?: [BaseArtifactService](../interfaces/BaseArtifactService.html)

  * Defined in [core/src/agents/invocation_context.ts:108](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L108)



### `Optional`branch

branch?: string

The branch of the invocation context.

The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3.

Branch is used when multiple sub-agents shouldn't see their peer agents' conversation history.

  * Defined in [core/src/agents/invocation_context.ts:127](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L127)



### `Optional` `Readonly`credentialService

credentialService?: [BaseCredentialService](../interfaces/BaseCredentialService.html)

  * Defined in [core/src/agents/invocation_context.ts:111](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L111)



### endInvocation

endInvocation: boolean

Whether to end this invocation. Set to True in callbacks or tools to terminate this invocation.

  * Defined in [core/src/agents/invocation_context.ts:148](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L148)



### `Readonly`invocationId

invocationId: string

The id of this invocation context.

  * Defined in [core/src/agents/invocation_context.ts:116](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L116)



### `Optional`liveRequestQueue

liveRequestQueue?: [LiveRequestQueue](LiveRequestQueue.html)

The queue to receive live requests.

  * Defined in [core/src/agents/invocation_context.ts:169](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L169)



### `Optional` `Readonly`memoryService

memoryService?: [BaseMemoryService](../interfaces/BaseMemoryService.html)

  * Defined in [core/src/agents/invocation_context.ts:110](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L110)



### pluginManager

pluginManager: [PluginManager](PluginManager.html)

The manager for keeping track of plugins in this invocation.

  * Defined in [core/src/agents/invocation_context.ts:179](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L179)



### `Optional`runConfig

runConfig?: [RunConfig](../interfaces/RunConfig.html)

Configurations for live agents under this invocation.

  * Defined in [core/src/agents/invocation_context.ts:158](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L158)



### `Readonly`session

session: [Session](../interfaces/Session.html)

The current session of this invocation context.

  * Defined in [core/src/agents/invocation_context.ts:142](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L142)



### `Optional` `Readonly`sessionService

sessionService?: [BaseSessionService](BaseSessionService.html)

  * Defined in [core/src/agents/invocation_context.ts:109](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L109)



### `Optional`transcriptionCache

transcriptionCache?: TranscriptionEntry[]

Caches necessary, data audio or contents, that are needed by transcription.

  * Defined in [core/src/agents/invocation_context.ts:153](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L153)



### `Optional` `Readonly`userContent

userContent?: Content

The user content that started this invocation.

  * Defined in [core/src/agents/invocation_context.ts:137](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L137)



## Accessors

### appName

  * get appName(): string

The app name of the current session.

#### Returns string

    * Defined in [core/src/agents/invocation_context.ts:204](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L204)




### userId

  * get userId(): string

The user ID of the current session.

#### Returns string

    * Defined in [core/src/agents/invocation_context.ts:211](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L211)




## Methods

### incrementLlmCallCount

  * incrementLlmCallCount(): void

Tracks number of llm calls made.

#### Returns void

#### Throws

If number of llm calls made exceed the set threshold.

    * Defined in [core/src/agents/invocation_context.ts:220](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/invocation_context.ts#L220)




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


