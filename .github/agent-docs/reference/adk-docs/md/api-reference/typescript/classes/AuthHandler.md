[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AuthHandler]()



# Class AuthHandler

A handler that handles the auth flow in Agent Development Kit to help orchestrates the credential request and response flow (e.g. OAuth flow) This class should only be used by Agent Development Kit.

  * Defined in [core/src/auth/auth_handler.ts:19](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_handler.ts#L19)



## Constructors

### constructor

  * new AuthHandler(authConfig: [AuthConfig](../interfaces/AuthConfig.html)): [AuthHandler]()

#### Parameters

    * authConfig: [AuthConfig](../interfaces/AuthConfig.html)

#### Returns [AuthHandler]()

    * Defined in [core/src/auth/auth_handler.ts:20](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_handler.ts#L20)




## Methods

### generateAuthRequest

  * generateAuthRequest(): [AuthConfig](../interfaces/AuthConfig.html)

#### Returns [AuthConfig](../interfaces/AuthConfig.html)

    * Defined in [core/src/auth/auth_handler.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_handler.ts#L48)




### generateAuthUri

  * generateAuthUri(): [AuthCredential](../interfaces/AuthCredential.html) | undefined

Generates an response containing the auth uri for user to sign in.

#### Returns [AuthCredential](../interfaces/AuthCredential.html) | undefined

An AuthCredential object containing the auth URI and state.

#### Throws

Error: If the authorization endpoint is not configured in the auth scheme.

    * Defined in [core/src/auth/auth_handler.ts:102](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_handler.ts#L102)




### getAuthResponse

  * getAuthResponse(state: [State](State.html)): [AuthCredential](../interfaces/AuthCredential.html) | undefined

#### Parameters

    * state: [State](State.html)

#### Returns [AuthCredential](../interfaces/AuthCredential.html) | undefined

    * Defined in [core/src/auth/auth_handler.ts:22](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_handler.ts#L22)




### parseAndStoreAuthResponse

  * parseAndStoreAuthResponse(state: [State](State.html)): Promise<void>

#### Parameters

    * state: [State](State.html)

#### Returns Promise<void>

    * Defined in [core/src/auth/auth_handler.ts:28](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_handler.ts#L28)




Constructors

constructor

Methods

generateAuthRequestgenerateAuthUrigetAuthResponseparseAndStoreAuthResponse

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


