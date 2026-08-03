[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ServiceAccount]()



# Interface ServiceAccount

Represents Google Service Account configuration.

interface ServiceAccount {  
audience?: string;  
scopes?: string[];  
serviceAccountCredential?: [ServiceAccountCredential](ServiceAccountCredential.html);  
useDefaultCredential?: boolean;  
useIdToken?: boolean;  
}

  * Defined in [core/src/auth/auth_credential.ts:142](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L142)



## Properties

### `Optional`audience

audience?: string

The audience for the ID token. Required if useIdToken is true.

  * Defined in [core/src/auth/auth_credential.ts:155](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L155)



### `Optional`scopes

scopes?: string[]

  * Defined in [core/src/auth/auth_credential.ts:144](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L144)



### `Optional`serviceAccountCredential

serviceAccountCredential?: [ServiceAccountCredential](ServiceAccountCredential.html)

  * Defined in [core/src/auth/auth_credential.ts:143](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L143)



### `Optional`useDefaultCredential

useDefaultCredential?: boolean

  * Defined in [core/src/auth/auth_credential.ts:145](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L145)



### `Optional`useIdToken

useIdToken?: boolean

If true, get an ID token instead of an access token.

  * Defined in [core/src/auth/auth_credential.ts:150](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L150)



Properties

audiencescopesserviceAccountCredentialuseDefaultCredentialuseIdToken

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


