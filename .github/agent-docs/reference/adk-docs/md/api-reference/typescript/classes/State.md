[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [State]()



# Class State

A state mapping that maintains the current value and the pending-commit delta.

  * Defined in [sessions/state.ts:11](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L11)



## Constructors

### constructor

  * new State(  
value?: Record<string, unknown>,  
delta?: Record<string, unknown>,  
): [State]()

#### Parameters

    * value: Record<string, unknown> = {}

The current value of the state.

    * delta: Record<string, unknown> = {}

The delta change to the current value that hasn't been committed.

#### Returns [State]()

    * Defined in [sessions/state.ts:16](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L16)




## Properties

### `Static` `Readonly`APP_PREFIX

APP_PREFIX: "app:" = 'app:'

  * Defined in [sessions/state.ts:12](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L12)



### `Static` `Readonly`TEMP_PREFIX

TEMP_PREFIX: "temp:" = 'temp:'

  * Defined in [sessions/state.ts:14](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L14)



### `Static` `Readonly`USER_PREFIX

USER_PREFIX: "user:" = 'user:'

  * Defined in [sessions/state.ts:13](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L13)



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

    * Defined in [sessions/state.ts:31](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L31)




### has

  * has(key: string): boolean

Whether the state has pending delta.

#### Parameters

    * key: string

#### Returns boolean

    * Defined in [sessions/state.ts:57](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L57)




### hasDelta

  * hasDelta(): boolean

Whether the state has pending delta.

#### Returns boolean

    * Defined in [sessions/state.ts:64](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L64)




### set

  * set(key: string, value: unknown): void

Sets the value of the state dict for the given key.

#### Parameters

    * key: string

The key to set the value for.

    * value: unknown

The value to set.

#### Returns void

    * Defined in [sessions/state.ts:49](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L49)




### toRecord

  * toRecord(): Record<string, unknown>

Returns the state as a plain JSON object.

#### Returns Record<string, unknown>

    * Defined in [sessions/state.ts:81](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L81)




### update

  * update(delta: Record<string, unknown>): void

Updates the state dict with the given delta.

#### Parameters

    * delta: Record<string, unknown>

The delta to update the state with.

#### Returns void

    * Defined in [sessions/state.ts:73](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/state.ts#L73)




Constructors

constructor

Properties

APP_PREFIXTEMP_PREFIXUSER_PREFIX

Methods

gethashasDeltasettoRecordupdate

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


