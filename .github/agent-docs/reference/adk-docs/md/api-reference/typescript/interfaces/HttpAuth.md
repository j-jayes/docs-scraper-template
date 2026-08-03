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

  * Defined in [core/src/auth/auth_credential.ts:20](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L20)



## Properties

### `Optional`additionalHeaders

additionalHeaders?: Record<string, string>

Additional HTTP headers to include in the request.

  * Defined in [core/src/auth/auth_credential.ts:33](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L33)



### credentials

credentials: [HttpCredentials](HttpCredentials.html)

  * Defined in [core/src/auth/auth_credential.ts:28](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L28)



### scheme

scheme: string

The name of the HTTP Authorization scheme to be used in the Authorization header as defined in RFC7235. The values used SHOULD be registered in the IANA Authentication Scheme registry. Examples: 'basic', 'bearer'

  * Defined in [core/src/auth/auth_credential.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L27)



Properties

additionalHeaderscredentialsscheme

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


