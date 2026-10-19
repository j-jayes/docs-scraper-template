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
  3. `endInvocation` is set to true by any callbacks or tools.



A step:

  1. Calls the LLM only once and yields its response.
  2. Calls the tools and yields their responses if requested.



The summarization of the function response is considered another step, since it is another llm call. A step ends when it's done calling llm and tools, or if `endInvocation` is set to true at any time.
    
    
       ┌─────────────────────── invocation ──────────────────────────┐  
       ┌──────────── llm_agent_call_1 ────────────┐ ┌─ agent_call_2 ─┐  
       ┌──── step_1 ────────┐ ┌───── step_2 ──────┐  
       [call_llm] [call_tool] [call_llm] [transfer]
    Copy

  * Defined in [core/src/agents/invocation_context.ts:139](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L139)



## Constructors

### constructor

  * new InvocationContext(params: [InvocationContextParams](../interfaces/InvocationContextParams.html)): [InvocationContext]()

#### Parameters

    * params: [InvocationContextParams](../interfaces/InvocationContextParams.html)

The parameters for creating an invocation context.

#### Returns [InvocationContext]()

    * Defined in [core/src/agents/invocation_context.ts:273](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L273)




## Properties

### `Optional` `Readonly`a2aMetadata

a2aMetadata?: Record<string, unknown>

Request-level metadata passed from an incoming A2A request or caller.

  * Defined in [core/src/agents/invocation_context.ts:268](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L268)



### `Optional` `Readonly`abortSignal

abortSignal?: AbortSignal

  * Defined in [core/src/agents/invocation_context.ts:222](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L222)



### `Optional`activeStreamingTools

activeStreamingTools?: Record<string, [ActiveStreamingTool](ActiveStreamingTool.html)>

The running streaming tools of this invocation.

  * Defined in [core/src/agents/invocation_context.ts:215](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L215)



### `Optional`agent

agent?: [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)>

The agent driving this invocation.

Unset when the root being run is a bare [BaseNode](BaseNode.html) — a `Workflow` handed straight to the `Runner` — because there is no agent in play at that level. Nodes deeper in the graph that _are_ agents get their own contexts with this set. Mirrors adk-python, whose field is `BaseAgent | BaseNode | None` and which passes `None` on the node path.

Most code reaches this from inside an agent's own execution, where it is always set; prefer [requireAgent](../functions/requireAgent.html) there, so a broken invariant fails by name rather than as a property access on `undefined`.

  * Defined in [core/src/agents/invocation_context.ts:174](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L174)



### `Optional` `Readonly`artifactService

artifactService?: [SessionArtifactService](../interfaces/SessionArtifactService.html)

  * Defined in [core/src/agents/invocation_context.ts:140](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L140)



### `Optional`branch

branch?: string

The branch of the invocation context.

The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3.

Branch is used when multiple sub-agents shouldn't see their peer agents' conversation history.

  * Defined in [core/src/agents/invocation_context.ts:159](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L159)



### `Optional` `Readonly`credentialService

credentialService?: [BaseCredentialService](../interfaces/BaseCredentialService.html)

  * Defined in [core/src/agents/invocation_context.ts:143](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L143)



### endInvocation

endInvocation: boolean

Whether to end this invocation. Set to `true` in callbacks or tools to terminate this invocation.

  * Defined in [core/src/agents/invocation_context.ts:190](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L190)



### `Optional`eventQueue

eventQueue?: [AsyncQueue](AsyncQueue.html)<[Event](../interfaces/Event.html)>

An optional channel into which a running tool can push events to be interleaved into the agent's output stream. Set by the LLM flow around tool execution so a [NodeTool](NodeTool.html) (running a node/workflow) can surface the node's intermediate and interrupt events. Cleared once tools finish.

  * Defined in [core/src/agents/invocation_context.ts:230](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L230)



### `Readonly`invocationId

invocationId: string

The id of this invocation context.

  * Defined in [core/src/agents/invocation_context.ts:148](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L148)



### `Optional`isolationScope

isolationScope?: string

Workflow: the isolation scope of the node this context runs in. Events carrying a different scope are withheld from this agent's LLM request.

  * Defined in [core/src/agents/invocation_context.ts:243](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L243)



### `Optional` `Readonly`liveRequestQueue

liveRequestQueue?: [LiveRequestQueue](LiveRequestQueue.html)

The live request queue feeding the model on the bidirectional (live) path. Set only for invocations started via `runner.runLive`.

  * Defined in [core/src/agents/invocation_context.ts:256](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L256)



### `Optional`liveSessionResumptionHandle

liveSessionResumptionHandle?: string

The most recent session resumption handle observed on the live path. Updated as the server emits resumption updates so a reconnect can restore server-side state instead of replaying history. Mutable by design.

  * Defined in [core/src/agents/invocation_context.ts:263](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L263)



### `Optional` `Readonly`memoryService

memoryService?: [BaseMemoryService](../interfaces/BaseMemoryService.html)

  * Defined in [core/src/agents/invocation_context.ts:142](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L142)



### `Readonly`nodeToolDepth

nodeToolDepth: number

Nesting depth of node-as-tool ([NodeTool](NodeTool.html)) executions in this invocation. Incremented each time a node runs as a tool (via a depth+1 clone), so `NodeTool` can bound `node -> tool -> node` recursion.

  * Defined in [core/src/agents/invocation_context.ts:250](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L250)



### pluginManager

pluginManager: [PluginManager](PluginManager.html)

The manager for keeping track of plugins in this invocation.

  * Defined in [core/src/agents/invocation_context.ts:220](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L220)



### `Optional`runConfig

runConfig?: [RunConfig](../interfaces/RunConfig.html)

Configurations for live agents under this invocation.

  * Defined in [core/src/agents/invocation_context.ts:200](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L200)



### `Readonly`session

session: [Session](../interfaces/Session.html)

The current session of this invocation context.

  * Defined in [core/src/agents/invocation_context.ts:184](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L184)



### `Optional` `Readonly`sessionService

sessionService?: [BaseSessionService](BaseSessionService.html)

  * Defined in [core/src/agents/invocation_context.ts:141](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L141)



### `Optional`transcriptionCache

transcriptionCache?: [TranscriptionEntry](../interfaces/TranscriptionEntry.html)[]

Caches necessary, data audio or contents, that are needed by transcription.

  * Defined in [core/src/agents/invocation_context.ts:195](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L195)



### `Optional` `Readonly`userContent

userContent?: Content

The user content that started this invocation.

  * Defined in [core/src/agents/invocation_context.ts:179](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L179)



### `Optional`workflowInstructionScope

workflowInstructionScope?: [WorkflowInstructionScope](../interfaces/WorkflowInstructionScope.html)

Workflow: field-resolution scope for `{Class.field}` / `<Class.field from node>` instruction placeholders (set by `LLMAgentWrapper`).

  * Defined in [core/src/agents/invocation_context.ts:237](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L237)



## Accessors

### appName

  * get appName(): string

The app name of the current session.

#### Returns string

    * Defined in [core/src/agents/invocation_context.ts:309](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L309)




### userId

  * get userId(): string

The user ID of the current session.

#### Returns string

    * Defined in [core/src/agents/invocation_context.ts:316](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L316)




## Methods

### clone

  * clone(overrides?: Partial<[InvocationContextParams](../interfaces/InvocationContextParams.html)>): [InvocationContext]()

Returns a copy of this context with `overrides` applied. The spread carries every own field over (including the shared cost manager), so the copy keeps a single LLM-call counter for the invocation.

Note: this copies own enumerable fields by value — scalar mutable fields (e.g. `endInvocation`) are decoupled from the original, while object-valued fields (`session`, …) stay shared by reference.

#### Parameters

    * overrides: Partial<[InvocationContextParams](../interfaces/InvocationContextParams.html)> = {}

#### Returns [InvocationContext]()

    * Defined in [core/src/agents/invocation_context.ts:338](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L338)




### incrementLlmCallCount

  * incrementLlmCallCount(): void

Tracks number of llm calls made.

#### Returns void

#### Throws

If number of llm calls made exceed the set threshold.

    * Defined in [core/src/agents/invocation_context.ts:325](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L325)




Constructors

constructor

Properties

a2aMetadataabortSignalactiveStreamingToolsagentartifactServicebranchcredentialServiceendInvocationeventQueueinvocationIdisolationScopeliveRequestQueueliveSessionResumptionHandlememoryServicenodeToolDepthpluginManagerrunConfigsessionsessionServicetranscriptionCacheuserContentworkflowInstructionScope

Accessors

appNameuserId

Methods

cloneincrementLlmCallCount

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


