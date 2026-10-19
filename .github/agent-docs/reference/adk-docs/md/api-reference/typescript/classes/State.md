[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [State]()



# Class State

A state mapping that maintains the current value and the pending-commit delta.

  * Defined in [core/src/sessions/state.ts:28](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L28)



## Constructors

### constructor

  * new State(  
value?: Record<string, unknown>,  
delta?: Record<string, unknown>,  
schema?: [SchemaLike](../types/SchemaLike.html),  
): [State]()

#### Parameters

    * value: Record<string, unknown> = {}

The current value of the state.

    * delta: Record<string, unknown> = {}

The delta change to the current value that hasn't been committed.

    * `Optional`schema: [SchemaLike](../types/SchemaLike.html)

Declares the keys this state may hold and their types. When set, every mutation is checked against it; prefixed keys are exempt.

#### Returns [State]()

    * Defined in [core/src/sessions/state.ts:33](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L33)




## Properties

### `Optional` `Readonly`schema

schema?: [SchemaLike](../types/SchemaLike.html)

Declares the keys this state may hold and their types. When set, every mutation is checked against it; prefixed keys are exempt.

  * Defined in [core/src/sessions/state.ts:42](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L42)



### `Static` `Readonly`APP_PREFIX

APP_PREFIX: "app:" = 'app:'

  * Defined in [core/src/sessions/state.ts:29](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L29)



### `Static` `Readonly`TEMP_PREFIX

TEMP_PREFIX: "temp:" = 'temp:'

  * Defined in [core/src/sessions/state.ts:31](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L31)



### `Static` `Readonly`USER_PREFIX

USER_PREFIX: "user:" = 'user:'

  * Defined in [core/src/sessions/state.ts:30](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L30)



## Methods

### get

  * get<T>(key: string, defaultValue?: T): T | undefined

Returns the value of the state dict for the given key.

#### Type Parameters

    * T

#### Parameters

    * key: string

The key to get the value for.

    * `Optional`defaultValue: T

The default value to return if the key is not found.

#### Returns T | undefined

The value of the state for the given key, or the default value if not found.

    * Defined in [core/src/sessions/state.ts:100](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L100)




### has

  * has(key: string): boolean

Whether the state has pending delta.

#### Parameters

    * key: string

#### Returns boolean

    * Defined in [core/src/sessions/state.ts:130](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L130)




### hasDelta

  * hasDelta(): boolean

Whether the state has pending delta.

#### Returns boolean

    * Defined in [core/src/sessions/state.ts:137](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L137)




### set

  * set(key: string, value: unknown): void

Sets the value of the state dict for the given key.

#### Parameters

    * key: string

The key to set the value for.

    * value: unknown

The value to set.

#### Returns void

    * Defined in [core/src/sessions/state.ts:118](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L118)




### toRecord

  * toRecord(): Record<string, unknown>

Returns the state as a plain JSON object.

#### Returns Record<string, unknown>

    * Defined in [core/src/sessions/state.ts:159](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L159)




### update

  * update(delta: Record<string, unknown>): void

Updates the state dict with the given delta.

#### Parameters

    * delta: Record<string, unknown>

The delta to update the state with.

#### Returns void

    * Defined in [core/src/sessions/state.ts:146](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L146)




### validateDelta

  * validateDelta(delta: Record<string, unknown>): void

Checks a whole delta against schema, for writes that reach the session without passing through this object — a node emitting an event that carries its own `stateDelta`.

#### Parameters

    * delta: Record<string, unknown>

#### Returns void

    * Defined in [core/src/sessions/state.ts:50](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/sessions/state.ts#L50)




Constructors

constructor

Properties

schemaAPP_PREFIXTEMP_PREFIXUSER_PREFIX

Methods

gethashasDeltasettoRecordupdatevalidateDelta

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


