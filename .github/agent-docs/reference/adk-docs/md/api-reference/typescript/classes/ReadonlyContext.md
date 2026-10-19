[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ReadonlyContext]()



# Class ReadonlyContext

A readonly context represents the data of a single invocation of an agent.

#### Hierarchy ([View Summary](../hierarchy.html#ReadonlyContext))

  * ReadonlyContext
    * [Context](Context.html)



  * Defined in [core/src/agents/readonly_context.ts:16](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L16)



## Constructors

### constructor

  * new ReadonlyContext(invocationContext: [InvocationContext](InvocationContext.html)): [ReadonlyContext]()

#### Parameters

    * invocationContext: [InvocationContext](InvocationContext.html)

#### Returns [ReadonlyContext]()

    * Defined in [core/src/agents/readonly_context.ts:17](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L17)




## Properties

### `Readonly`invocationContext

invocationContext: [InvocationContext](InvocationContext.html)

  * Defined in [core/src/agents/readonly_context.ts:17](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L17)



## Accessors

### a2aMetadata

  * get a2aMetadata(): Record<string, unknown> | undefined

Request-level metadata passed from an incoming A2A request or caller.

#### Returns Record<string, unknown> | undefined

    * Defined in [core/src/agents/readonly_context.ts:67](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L67)




### agentName

  * get agentName(): string

The current agent name.

#### Returns string

    * Defined in [core/src/agents/readonly_context.ts:50](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L50)




### invocationId

  * get invocationId(): string

The current invocation id.

#### Returns string

    * Defined in [core/src/agents/readonly_context.ts:29](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L29)




### sessionId

  * get sessionId(): string

The ID of the current session.

#### Returns string

    * Defined in [core/src/agents/readonly_context.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L43)




### state

  * get state(): Readonly<[State](State.html)>

The state of the current session.

#### Returns Readonly<[State](State.html)>

    * Defined in [core/src/agents/readonly_context.ts:57](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L57)




### userContent

  * get userContent(): Content | undefined

The user content that started this invocation.

#### Returns Content | undefined

    * Defined in [core/src/agents/readonly_context.ts:22](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L22)




### userId

  * get userId(): string

The user ID of the current session.

#### Returns string

    * Defined in [core/src/agents/readonly_context.ts:36](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/readonly_context.ts#L36)




Constructors

constructor

Properties

invocationContext

Accessors

a2aMetadataagentNameinvocationIdsessionIdstateuserContentuserId

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


