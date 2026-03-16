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



  * Defined in [agents/context.ts:29](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L29)



## Constructors

### constructor

  * new Context(  
options: {  
eventActions?: [EventActions](../interfaces/EventActions.html);  
functionCallId?: string;  
invocationContext: [InvocationContext](InvocationContext.html);  
toolConfirmation?: [ToolConfirmation](ToolConfirmation.html);  
},  
): [Context]()

#### Parameters

    * options: {  
eventActions?: [EventActions](../interfaces/EventActions.html);  
functionCallId?: string;  
invocationContext: [InvocationContext](InvocationContext.html);  
toolConfirmation?: [ToolConfirmation](ToolConfirmation.html);  
}

The configuration options for the Context.

      * ##### `Optional`eventActions?: [EventActions](../interfaces/EventActions.html)

The event actions of the current call.

      * ##### `Optional`functionCallId?: string

The function call id of the current tool call. This id was returned in the function call event from LLM to identify a function call. If LLM didn't return this id, ADK will assign one to it. This id is used to map function call response to the original function call.

      * ##### invocationContext: [InvocationContext](InvocationContext.html)

The invocation context.

      * ##### `Optional`toolConfirmation?: [ToolConfirmation](ToolConfirmation.html)

The tool confirmation of the current tool call.

#### Returns [Context]()

Overrides [ReadonlyContext](ReadonlyContext.html).[constructor](ReadonlyContext.html#constructor)

    * Defined in [agents/context.ts:48](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L48)




## Properties

### `Readonly`eventActions

eventActions: [EventActions](../interfaces/EventActions.html)

  * Defined in [agents/context.ts:32](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L32)



### `Optional` `Readonly`functionCallId

functionCallId?: string

  * Defined in [agents/context.ts:33](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L33)



### `Readonly`invocationContext

invocationContext: [InvocationContext](InvocationContext.html)

Inherited from [ReadonlyContext](ReadonlyContext.html).[invocationContext](ReadonlyContext.html#invocationcontext)

  * Defined in [agents/readonly_context.ts:17](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/readonly_context.ts#L17)



### `Optional`toolConfirmation

toolConfirmation?: [ToolConfirmation](ToolConfirmation.html)

  * Defined in [agents/context.ts:34](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L34)



## Accessors

### actions

  * get actions(): [EventActions](../interfaces/EventActions.html)

#### Returns [EventActions](../interfaces/EventActions.html)

    * Defined in [agents/context.ts:71](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L71)




### agentName

  * get agentName(): string

The current agent name.

#### Returns string

Inherited from ReadonlyContext.agentName

    * Defined in [agents/readonly_context.ts:50](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/readonly_context.ts#L50)




### invocationId

  * get invocationId(): string

The current invocation id.

#### Returns string

Inherited from ReadonlyContext.invocationId

    * Defined in [agents/readonly_context.ts:29](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/readonly_context.ts#L29)




### sessionId

  * get sessionId(): string

The ID of the current session.

#### Returns string

Inherited from ReadonlyContext.sessionId

    * Defined in [agents/readonly_context.ts:43](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/readonly_context.ts#L43)




### state

  * get state(): [State](State.html)

The delta-aware state of the current session.

#### Returns [State](State.html)

Overrides ReadonlyContext.state

    * Defined in [agents/context.ts:67](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L67)




### userContent

  * get userContent(): Content | undefined

The user content that started this invocation.

#### Returns Content | undefined

Inherited from ReadonlyContext.userContent

    * Defined in [agents/readonly_context.ts:22](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/readonly_context.ts#L22)




### userId

  * get userId(): string

The user ID of the current session.

#### Returns string

Inherited from ReadonlyContext.userId

    * Defined in [agents/readonly_context.ts:36](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/readonly_context.ts#L36)




## Methods

### getAuthResponse

  * getAuthResponse(authConfig: [AuthConfig](../interfaces/AuthConfig.html)): [AuthCredential](../interfaces/AuthCredential.html) | undefined

Gets the auth credential for the given auth config.

#### Parameters

    * authConfig: [AuthConfig](../interfaces/AuthConfig.html)

The auth config to get the auth credential for.

#### Returns [AuthCredential](../interfaces/AuthCredential.html) | undefined

The auth credential for the given auth config.

    * Defined in [agents/context.ts:137](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L137)




### listArtifacts

  * listArtifacts(): Promise<string[]>

Lists the filenames of the artifacts attached to the current session.

#### Returns Promise<string[]>

A promise that resolves to a list of artifact filenames.

    * Defined in [agents/context.ts:148](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L148)




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

    * Defined in [agents/context.ts:83](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L83)




### requestConfirmation

  * requestConfirmation(  
__namedParameters: { hint?: string; payload?: unknown },  
): void

Requests confirmation for the current tool call.

#### Parameters

    * __namedParameters: { hint?: string; payload?: unknown }

#### Returns void

    * Defined in [agents/context.ts:182](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L182)




### requestCredential

  * requestCredential(authConfig: [AuthConfig](../interfaces/AuthConfig.html)): void

#### Parameters

    * authConfig: [AuthConfig](../interfaces/AuthConfig.html)

#### Returns void

    * Defined in [agents/context.ts:121](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L121)




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

    * Defined in [agents/context.ts:104](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L104)




### searchMemory

  * searchMemory(query: string): Promise<[SearchMemoryResponse](../interfaces/SearchMemoryResponse.html)>

Searches the memory of the current user.

#### Parameters

    * query: string

The query to search memory for.

#### Returns Promise<[SearchMemoryResponse](../interfaces/SearchMemoryResponse.html)>

A promise that resolves to SearchMemoryResponse containing the matching memories.

    * Defined in [agents/context.ts:167](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/context.ts#L167)




Constructors

constructor

Properties

eventActionsfunctionCallIdinvocationContexttoolConfirmation

Accessors

actionsagentNameinvocationIdsessionIdstateuserContentuserId

Methods

getAuthResponselistArtifactsloadArtifactrequestConfirmationrequestCredentialsaveArtifactsearchMemory

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


