[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [CallbackContext]()



# Class CallbackContext

The context of various callbacks within an agent run.

#### Hierarchy ([View Summary](../hierarchy.html#CallbackContext))

  * ReadonlyContext
    * CallbackContext
      * [ToolContext](ToolContext.html)



  * Defined in [core/src/agents/callback_context.ts:18](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/callback_context.ts#L18)



## Constructors

### constructor

  * new CallbackContext(  
__namedParameters: {  
eventActions?: [EventActions](../interfaces/EventActions.html);  
invocationContext: [InvocationContext](InvocationContext.html);  
},  
): [CallbackContext]()

#### Parameters

    * __namedParameters: { eventActions?: [EventActions](../interfaces/EventActions.html); invocationContext: [InvocationContext](InvocationContext.html) }

#### Returns [CallbackContext]()

Overrides ReadonlyContext.constructor

    * Defined in [core/src/agents/callback_context.ts:23](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/callback_context.ts#L23)




## Properties

### `Readonly`eventActions

eventActions: [EventActions](../interfaces/EventActions.html)

  * Defined in [core/src/agents/callback_context.ts:21](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/callback_context.ts#L21)



### `Readonly`invocationContext

invocationContext: [InvocationContext](InvocationContext.html)

Inherited from ReadonlyContext.invocationContext

  * Defined in [core/src/agents/readonly_context.ts:17](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/readonly_context.ts#L17)



## Accessors

### agentName

  * get agentName(): string

The current agent name.

#### Returns string

Inherited from ReadonlyContext.agentName

    * Defined in [core/src/agents/readonly_context.ts:36](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/readonly_context.ts#L36)




### invocationId

  * get invocationId(): string

The current invocation id.

#### Returns string

Inherited from ReadonlyContext.invocationId

    * Defined in [core/src/agents/readonly_context.ts:29](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/readonly_context.ts#L29)




### state

  * get state(): State

The delta-aware state of the current session.

#### Returns State

Overrides ReadonlyContext.state

    * Defined in [core/src/agents/callback_context.ts:38](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/callback_context.ts#L38)




### userContent

  * get userContent(): Content | undefined

The user content that started this invocation.

#### Returns Content | undefined

Inherited from ReadonlyContext.userContent

    * Defined in [core/src/agents/readonly_context.ts:22](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/readonly_context.ts#L22)




## Methods

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

    * Defined in [core/src/agents/callback_context.ts:50](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/callback_context.ts#L50)




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

    * Defined in [core/src/agents/callback_context.ts:71](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/callback_context.ts#L71)




Constructors

constructor

Properties

eventActionsinvocationContext

Accessors

agentNameinvocationIdstateuserContent

Methods

loadArtifactsaveArtifact

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


