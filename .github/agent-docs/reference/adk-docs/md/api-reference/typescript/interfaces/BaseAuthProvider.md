[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseAuthProvider]()



# Interface BaseAuthProvider

Abstract base interface for custom authentication providers.

interface BaseAuthProvider {  
getAuthCredential(  
authConfig: [AuthConfig](AuthConfig.html),  
context?: unknown,  
): Promise<[AuthCredential](AuthCredential.html) | undefined>;  
}

  * Defined in [core/src/auth/base_auth_provider.ts:13](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/base_auth_provider.ts#L13)



## Methods

### getAuthCredential

  * getAuthCredential(  
authConfig: [AuthConfig](AuthConfig.html),  
context?: unknown,  
): Promise<[AuthCredential](AuthCredential.html) | undefined>

Provide an AuthCredential asynchronously.

#### Parameters

    * authConfig: [AuthConfig](AuthConfig.html)

The current authentication configuration.

    * `Optional`context: unknown

The current callback context (placeholder).

#### Returns Promise<[AuthCredential](AuthCredential.html) | undefined>

The retrieved AuthCredential, or undefined if unavailable.

    * Defined in [core/src/auth/base_auth_provider.ts:21](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/base_auth_provider.ts#L21)




Methods

getAuthCredential

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


