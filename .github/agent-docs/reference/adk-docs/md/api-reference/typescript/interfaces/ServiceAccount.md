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

  * Defined in [core/src/auth/auth_credential.ts:147](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L147)



## Properties

### `Optional`audience

audience?: string

The audience for the ID token. Required if useIdToken is true.

  * Defined in [core/src/auth/auth_credential.ts:160](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L160)



### `Optional`scopes

scopes?: string[]

  * Defined in [core/src/auth/auth_credential.ts:149](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L149)



### `Optional`serviceAccountCredential

serviceAccountCredential?: [ServiceAccountCredential](ServiceAccountCredential.html)

  * Defined in [core/src/auth/auth_credential.ts:148](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L148)



### `Optional`useDefaultCredential

useDefaultCredential?: boolean

  * Defined in [core/src/auth/auth_credential.ts:150](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L150)



### `Optional`useIdToken

useIdToken?: boolean

If true, get an ID token instead of an access token.

  * Defined in [core/src/auth/auth_credential.ts:155](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L155)



Properties

audiencescopesserviceAccountCredentialuseDefaultCredentialuseIdToken

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


