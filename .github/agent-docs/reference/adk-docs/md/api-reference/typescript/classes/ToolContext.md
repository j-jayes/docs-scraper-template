[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolContext]()



# Class ToolContext

The context of various callbacks within an agent run.

#### Hierarchy ([View Summary](../hierarchy.html#ToolContext))

  * [CallbackContext](CallbackContext.html)
    * ToolContext



  * Defined in [core/src/tools/tool_context.ts:24](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/tool_context.ts#L24)



## Constructors

### constructor

  * new ToolContext(  
__namedParameters: {  
eventActions?: [EventActions](../interfaces/EventActions.html);  
functionCallId?: string;  
invocationContext: [InvocationContext](InvocationContext.html);  
toolConfirmation?: [ToolConfirmation](ToolConfirmation.html);  
},  
): [ToolContext]()

#### Parameters

    * __namedParameters: {  
eventActions?: [EventActions](../interfaces/EventActions.html);  
functionCallId?: string;  
invocationContext: [InvocationContext](InvocationContext.html);  
toolConfirmation?: [ToolConfirmation](ToolConfirmation.html);  
}

#### Returns [ToolContext]()

Overrides [CallbackContext](CallbackContext.html).[constructor](CallbackContext.html#constructor)

    * Defined in [core/src/tools/tool_context.ts:39](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/tool_context.ts#L39)




## Properties

### `Readonly`eventActions

eventActions: [EventActions](../interfaces/EventActions.html)

Inherited from [CallbackContext](CallbackContext.html).[eventActions](CallbackContext.html#eventactions)

  * Defined in [core/src/agents/callback_context.ts:21](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/callback_context.ts#L21)



### `Optional` `Readonly`functionCallId

functionCallId?: string

  * Defined in [core/src/tools/tool_context.ts:25](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/tool_context.ts#L25)



### `Readonly`invocationContext

invocationContext: [InvocationContext](InvocationContext.html)

Inherited from [CallbackContext](CallbackContext.html).[invocationContext](CallbackContext.html#invocationcontext)

  * Defined in [core/src/agents/readonly_context.ts:17](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/readonly_context.ts#L17)



### `Optional`toolConfirmation

toolConfirmation?: [ToolConfirmation](ToolConfirmation.html)

  * Defined in [core/src/tools/tool_context.ts:26](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/tool_context.ts#L26)



## Accessors

### actions

  * get actions(): [EventActions](../interfaces/EventActions.html)

#### Returns [EventActions](../interfaces/EventActions.html)

    * Defined in [core/src/tools/tool_context.ts:55](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/tool_context.ts#L55)




### agentName

  * get agentName(): string

The current agent name.

#### Returns string

Inherited from CallbackContext.agentName

    * Defined in [core/src/agents/readonly_context.ts:36](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/readonly_context.ts#L36)




### invocationId

  * get invocationId(): string

The current invocation id.

#### Returns string

Inherited from CallbackContext.invocationId

    * Defined in [core/src/agents/readonly_context.ts:29](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/readonly_context.ts#L29)




### state

  * get state(): State

The delta-aware state of the current session.

#### Returns State

Inherited from CallbackContext.state

    * Defined in [core/src/agents/callback_context.ts:38](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/callback_context.ts#L38)




### userContent

  * get userContent(): Content | undefined

The user content that started this invocation.

#### Returns Content | undefined

Inherited from CallbackContext.userContent

    * Defined in [core/src/agents/readonly_context.ts:22](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/readonly_context.ts#L22)




## Methods

### getAuthResponse

  * getAuthResponse(authConfig: AuthConfig): AuthCredential | undefined

Gets the auth credential for the given auth config.

#### Parameters

    * authConfig: AuthConfig

The auth config to get the auth credential for.

#### Returns AuthCredential | undefined

The auth credential for the given auth config.

    * Defined in [core/src/tools/tool_context.ts:75](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/tool_context.ts#L75)




### listArtifacts

  * listArtifacts(): Promise<string[]>

Lists the filenames of the artifacts attached to the current session.

#### Returns Promise<string[]>

A promise that resolves to a list of artifact filenames.

    * Defined in [core/src/tools/tool_context.ts:86](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/tool_context.ts#L86)




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

Inherited from [CallbackContext](CallbackContext.html).[loadArtifact](CallbackContext.html#loadartifact)

    * Defined in [core/src/agents/callback_context.ts:50](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/callback_context.ts#L50)




### requestConfirmation

  * requestConfirmation(  
__namedParameters: { hint?: string; payload?: unknown },  
): void

Requests confirmation for the current tool call.

#### Parameters

    * __namedParameters: { hint?: string; payload?: unknown }

#### Returns void

    * Defined in [core/src/tools/tool_context.ts:120](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/tool_context.ts#L120)




### requestCredential

  * requestCredential(authConfig: AuthConfig): void

#### Parameters

    * authConfig: AuthConfig

#### Returns void

    * Defined in [core/src/tools/tool_context.ts:59](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/tool_context.ts#L59)




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

Inherited from [CallbackContext](CallbackContext.html).[saveArtifact](CallbackContext.html#saveartifact)

    * Defined in [core/src/agents/callback_context.ts:71](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/callback_context.ts#L71)




### searchMemory

  * searchMemory(query: string): Promise<[SearchMemoryResponse](../interfaces/SearchMemoryResponse.html)>

Searches the memory of the current user.

#### Parameters

    * query: string

The query to search memory for.

#### Returns Promise<[SearchMemoryResponse](../interfaces/SearchMemoryResponse.html)>

A promise that resolves to SearchMemoryResponse containing the matching memories.

    * Defined in [core/src/tools/tool_context.ts:105](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/tool_context.ts#L105)




Constructors

constructor

Properties

eventActionsfunctionCallIdinvocationContexttoolConfirmation

Accessors

actionsagentNameinvocationIdstateuserContent

Methods

getAuthResponselistArtifactsloadArtifactrequestConfirmationrequestCredentialsaveArtifactsearchMemory

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


