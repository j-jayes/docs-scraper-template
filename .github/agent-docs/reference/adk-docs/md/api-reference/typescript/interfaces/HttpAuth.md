[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [HttpAuth]()



# Interface HttpAuth

The credentials and metadata for HTTP authentication.

interface HttpAuth {  
credentials: [HttpCredentials](HttpCredentials.html);  
scheme: string;  
}

  * Defined in [auth/auth_credential.ts:20](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L20)



## Properties

### credentials

credentials: [HttpCredentials](HttpCredentials.html)

  * Defined in [auth/auth_credential.ts:28](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L28)



### scheme

scheme: string

The name of the HTTP Authorization scheme to be used in the Authorization header as defined in RFC7235. The values used SHOULD be registered in the IANA Authentication Scheme registry. Examples: 'basic', 'bearer'

  * Defined in [auth/auth_credential.ts:27](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L27)



Properties

credentialsscheme

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


