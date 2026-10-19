[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [HttpAuth]()



# Interface HttpAuth

The credentials and metadata for HTTP authentication.

interface HttpAuth {  
additionalHeaders?: Record<string, string>;  
credentials: [HttpCredentials](HttpCredentials.html);  
scheme: string;  
}

  * Defined in [core/src/auth/auth_credential.ts:20](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L20)



## Properties

### `Optional`additionalHeaders

additionalHeaders?: Record<string, string>

Additional HTTP headers to include in the request.

  * Defined in [core/src/auth/auth_credential.ts:33](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L33)



### credentials

credentials: [HttpCredentials](HttpCredentials.html)

  * Defined in [core/src/auth/auth_credential.ts:28](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L28)



### scheme

scheme: string

The name of the HTTP Authorization scheme to be used in the Authorization header as defined in RFC7235. The values used SHOULD be registered in the IANA Authentication Scheme registry. Examples: 'basic', 'bearer'

  * Defined in [core/src/auth/auth_credential.ts:27](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L27)



Properties

additionalHeaderscredentialsscheme

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


