[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AuthCredential]()



# Interface AuthCredential

Data class representing an authentication credential.

To exchange for the actual credential, please use CredentialExchanger.exchangeCredential().

#### Example
    
    
    // API Key Auth  
    const authCredential: AuthCredential = {  
      authType: AuthCredentialTypes.API_KEY,  
      apiKey: "your_api_key",  
    };
    Copy

#### Example
    
    
    // HTTP Auth  
    const authCredential: AuthCredential = {  
      authType: AuthCredentialTypes.HTTP,  
      http: {  
        scheme: "basic",  
        credentials: {  
          username: "user",  
          password: "password",  
        },  
      }  
    }
    Copy

#### Example
    
    
    // OAuth2 Bearer Token in HTTP Header  
    const authCredential: AuthCredential = {  
      authType: AuthCredentialTypes.HTTP,  
      http: {  
        scheme: "bearer",  
        credentials: {  
          token: "your_access_token",  
        },  
      }  
    }
    Copy

#### Example
    
    
    // OAuth2 Auth with Authorization Code Flow  
    const authCredential: AuthCredential = {  
      authType: AuthCredentialTypes.OAUTH2,  
      oauth2: {  
        clientId: "your_client_id",  
        clientSecret: "your_client_secret",  
      }  
    }  
      
    @example:  
    // Open ID Connect Auth  
    const authCredential: AuthCredential = {  
      authType: AuthCredentialTypes.OPEN_ID_CONNECT,  
      oauth2: {  
        clientId: "1234",  
        clientSecret: "secret",  
        redirectUri: "https://example.com",  
        scopes: ["scope1", "scope2"],  
      }  
    }  
      
    @example:  
    // Auth with resource reference  
    const authCredential: AuthCredential = {  
      authType: AuthCredentialTypes.API_KEY,  
      resourceRef: "projects/1234/locations/us-central1/resources/resource1"  
    }
    Copy

interface AuthCredential {  
apiKey?: string;  
authType: [AuthCredentialTypes](../enums/AuthCredentialTypes.html);  
http?: [HttpAuth](HttpAuth.html);  
oauth2?: [OAuth2Auth](OAuth2Auth.html);  
resourceRef?: string;  
serviceAccount?: [ServiceAccount](ServiceAccount.html);  
}

  * Defined in [auth/auth_credential.ts:240](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L240)



## Properties

### `Optional`apiKey

apiKey?: string

  * Defined in [auth/auth_credential.ts:249](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L249)



### authType

authType: [AuthCredentialTypes](../enums/AuthCredentialTypes.html)

  * Defined in [auth/auth_credential.ts:241](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L241)



### `Optional`http

http?: [HttpAuth](HttpAuth.html)

  * Defined in [auth/auth_credential.ts:250](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L250)



### `Optional`oauth2

oauth2?: [OAuth2Auth](OAuth2Auth.html)

  * Defined in [auth/auth_credential.ts:252](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L252)



### `Optional`resourceRef

resourceRef?: string

Resource reference for the credential. This will be supported in the future.

  * Defined in [auth/auth_credential.ts:247](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L247)



### `Optional`serviceAccount

serviceAccount?: [ServiceAccount](ServiceAccount.html)

  * Defined in [auth/auth_credential.ts:251](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L251)



Properties

apiKeyauthTypehttpoauth2resourceRefserviceAccount

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


