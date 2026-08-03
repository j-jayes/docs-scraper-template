[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AuthConfig]()



# Interface AuthConfig

The auth config sent by tool asking client to collect auth credentials and adk and client will help to fill in the response.

interface AuthConfig {  
authScheme: [AuthScheme](../types/AuthScheme.html);  
credentialKey: string;  
exchangedAuthCredential?: [AuthCredential](AuthCredential.html);  
rawAuthCredential?: [AuthCredential](AuthCredential.html);  
}

  * Defined in [core/src/auth/auth_tool.ts:14](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_tool.ts#L14)



## Properties

### authScheme

authScheme: [AuthScheme](../types/AuthScheme.html)

The auth scheme used to collect credentials

  * Defined in [core/src/auth/auth_tool.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_tool.ts#L18)



### credentialKey

credentialKey: string

A user specified key used to load and save this credential in a credential service.

  * Defined in [core/src/auth/auth_tool.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_tool.ts#L47)



### `Optional`exchangedAuthCredential

exchangedAuthCredential?: [AuthCredential](AuthCredential.html)

The exchanged auth credential used to collect credentials. adk and client will work together to fill it. For those auth scheme that doesn't need to exchange auth credentials, e.g. API key, service account etc. It's filled by client directly. For those auth scheme that need to exchange auth credentials, e.g. OAuth2 and OIDC, it's first filled by adk. If the raw credentials passed by tool only has client id and client credential, adk will help to generate the corresponding authorization uri and state and store the processed credential in this field. If the raw credentials passed by tool already has authorization uri, state, etc. then it's copied to this field. Client will use this field to guide the user through the OAuth2 flow and fill auth response in this field

  * Defined in [core/src/auth/auth_tool.ts:41](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_tool.ts#L41)



### `Optional`rawAuthCredential

rawAuthCredential?: [AuthCredential](AuthCredential.html)

The raw auth credential used to collect credentials. The raw auth credentials are used in some auth scheme that needs to exchange auth credentials. e.g. OAuth2 and OIDC. For other auth scheme, it could be undefined.

  * Defined in [core/src/auth/auth_tool.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_tool.ts#L26)



Properties

authSchemecredentialKeyexchangedAuthCredentialrawAuthCredential

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


