[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [Context]()



# Class Context

The context of various callbacks within an agent run.

This class provides the context for callbacks and tool invocations, including access to the invocation context, function call ID, event actions, and authentication response. It also provides methods for requesting credentials, retrieving authentication responses, loading and saving artifacts, and searching memory.

#### Hierarchy ([View Summary](../hierarchy.html#Context))

  * [ReadonlyContext](ReadonlyContext.html)
    * Context



  * Defined in [core/src/agents/context.ts:30](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L30)



## Constructors

### constructor

  * new Context(  
options: {  
eventActions?: [EventActions](../interfaces/EventActions.html);  
functionCallId?: string;  
invocationContext: [InvocationContext](InvocationContext.html);  
resumeInputs?: [ResumeInputs](../types/ResumeInputs.html);  
toolConfirmation?: [ToolConfirmation](ToolConfirmation.html);  
},  
): [Context]()

#### Parameters

    * options: {  
eventActions?: [EventActions](../interfaces/EventActions.html);  
functionCallId?: string;  
invocationContext: [InvocationContext](InvocationContext.html);  
resumeInputs?: [ResumeInputs](../types/ResumeInputs.html);  
toolConfirmation?: [ToolConfirmation](ToolConfirmation.html);  
}

The configuration options for the Context.

      * ##### `Optional`eventActions?: [EventActions](../interfaces/EventActions.html)

The event actions of the current call.

      * ##### `Optional`functionCallId?: string

The function call id of the current tool call. This id was returned in the function call event from LLM to identify a function call. If LLM didn't return this id, ADK will assign one to it. This id is used to map function call response to the original function call.

      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The invocation context.

      * ##### `Optional`resumeInputs?: [ResumeInputs](../types/ResumeInputs.html)

The inputs the current tool call is being resumed with, if it paused to ask for them, keyed by interrupt id. Defaults to empty rather than absent, matching adk-python's `Context.resume_inputs`. Carries no approval; see [ResumeInputs](../types/ResumeInputs.html).

      * ##### `Optional`toolConfirmation?: [ToolConfirmation](ToolConfirmation.html)

The tool confirmation of the current tool call.

#### Returns [Context]()

Overrides [ReadonlyContext](ReadonlyContext.html).[constructor](ReadonlyContext.html#constructor)

    * Defined in [core/src/agents/context.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L56)




## Properties

### `Optional` `Readonly`abortSignal

abortSignal?: AbortSignal

  * Defined in [core/src/agents/context.ts:37](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L37)



### `Readonly`eventActions

eventActions: [EventActions](../interfaces/EventActions.html)

  * Defined in [core/src/agents/context.ts:33](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L33)



### `Optional` `Readonly`functionCallId

functionCallId?: string

  * Defined in [core/src/agents/context.ts:34](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L34)



### `Readonly`invocationContext

invocationContext: [InvocationContext](InvocationContext.html)

Inherited from [ReadonlyContext](ReadonlyContext.html).[invocationContext](ReadonlyContext.html#invocationcontext)

  * Defined in [core/src/agents/readonly_context.ts:17](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L17)



### `Readonly`resumeInputs

resumeInputs: [ResumeInputs](../types/ResumeInputs.html)

  * Defined in [core/src/agents/context.ts:36](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L36)



### `Optional`toolConfirmation

toolConfirmation?: [ToolConfirmation](ToolConfirmation.html)

  * Defined in [core/src/agents/context.ts:35](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L35)



## Accessors

### a2aMetadata

  * get a2aMetadata(): Record<string, unknown> | undefined

Request-level metadata passed from an incoming A2A request or caller.

#### Returns Record<string, unknown> | undefined

Inherited from ReadonlyContext.a2aMetadata

    * Defined in [core/src/agents/readonly_context.ts:67](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L67)




### actions

  * get actions(): [EventActions](../interfaces/EventActions.html)

#### Returns [EventActions](../interfaces/EventActions.html)

    * Defined in [core/src/agents/context.ts:82](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L82)




### agentName

  * get agentName(): string

The current agent name.

#### Returns string

Inherited from ReadonlyContext.agentName

    * Defined in [core/src/agents/readonly_context.ts:50](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L50)




### invocationId

  * get invocationId(): string

The current invocation id.

#### Returns string

Inherited from ReadonlyContext.invocationId

    * Defined in [core/src/agents/readonly_context.ts:29](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L29)




### sessionId

  * get sessionId(): string

The ID of the current session.

#### Returns string

Inherited from ReadonlyContext.sessionId

    * Defined in [core/src/agents/readonly_context.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L43)




### state

  * get state(): [State](State.html)

The delta-aware state of the current session.

#### Returns [State](State.html)

Overrides ReadonlyContext.state

    * Defined in [core/src/agents/context.ts:78](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L78)




### userContent

  * get userContent(): Content | undefined

The user content that started this invocation.

#### Returns Content | undefined

Inherited from ReadonlyContext.userContent

    * Defined in [core/src/agents/readonly_context.ts:22](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L22)




### userId

  * get userId(): string

The user ID of the current session.

#### Returns string

Inherited from ReadonlyContext.userId

    * Defined in [core/src/agents/readonly_context.ts:36](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L36)




## Methods

### getAuthResponse

  * getAuthResponse(authConfig: [AuthConfig](../interfaces/AuthConfig.html)): [AuthCredential](../interfaces/AuthCredential.html) | undefined

Gets the auth credential for the given auth config.

#### Parameters

    * authConfig: [AuthConfig](../interfaces/AuthConfig.html)

The auth config to get the auth credential for.

#### Returns [AuthCredential](../interfaces/AuthCredential.html) | undefined

The auth credential for the given auth config.

    * Defined in [core/src/agents/context.ts:142](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L142)




### listArtifacts

  * listArtifacts(): Promise<string[]>

Lists the filenames of the artifacts attached to the current session.

#### Returns Promise<string[]>

A promise that resolves to a list of artifact filenames.

    * Defined in [core/src/agents/context.ts:153](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L153)




### loadArtifact

  * loadArtifact(filename: string, version?: number): Promise<Part | undefined>

Loads an artifact attached to the current session.

#### Parameters

    * filename: string

The filename of the artifact.

    * `Optional`version: number

The version of the artifact. If not provided, the latest version will be used.

#### Returns Promise<Part | undefined>

A promise that resolves to the loaded artifact.

    * Defined in [core/src/agents/context.ts:94](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L94)




### requestConfirmation

  * requestConfirmation(  
__namedParameters: { hint?: string; payload?: unknown },  
): void

Requests confirmation for the current tool call.

#### Parameters

    * __namedParameters: { hint?: string; payload?: unknown }

#### Returns void

    * Defined in [core/src/agents/context.ts:183](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L183)




### requestCredential

  * requestCredential(authConfig: [AuthConfig](../interfaces/AuthConfig.html)): void

#### Parameters

    * authConfig: [AuthConfig](../interfaces/AuthConfig.html)

#### Returns void

    * Defined in [core/src/agents/context.ts:126](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L126)




### saveArtifact

  * saveArtifact(filename: string, artifact: Part): Promise<number>

Saves an artifact attached to the current session.

#### Parameters

    * filename: string

The filename of the artifact.

    * artifact: Part

The artifact to save.

#### Returns Promise<number>

A promise that resolves to the version of the saved artifact.

    * Defined in [core/src/agents/context.ts:112](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L112)




### searchMemory

  * searchMemory(query: string): Promise<[SearchMemoryResponse](../interfaces/SearchMemoryResponse.html)>

Searches the memory of the current user.

#### Parameters

    * query: string

The query to search memory for.

#### Returns Promise<[SearchMemoryResponse](../interfaces/SearchMemoryResponse.html)>

A promise that resolves to SearchMemoryResponse containing the matching memories.

    * Defined in [core/src/agents/context.ts:168](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/context.ts#L168)




Constructors

constructor

Properties

abortSignaleventActionsfunctionCallIdinvocationContextresumeInputstoolConfirmation

Accessors

a2aMetadataactionsagentNameinvocationIdsessionIdstateuserContentuserId

Methods

getAuthResponselistArtifactsloadArtifactrequestConfirmationrequestCredentialsaveArtifactsearchMemory

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


