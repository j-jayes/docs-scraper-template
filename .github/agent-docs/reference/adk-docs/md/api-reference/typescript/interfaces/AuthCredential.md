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

  * Defined in [core/src/auth/auth_credential.ts:260](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L260)



## Properties

### `Optional`apiKey

apiKey?: string

  * Defined in [core/src/auth/auth_credential.ts:269](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L269)



### authType

authType: [AuthCredentialTypes](../enums/AuthCredentialTypes.html)

  * Defined in [core/src/auth/auth_credential.ts:261](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L261)



### `Optional`http

http?: [HttpAuth](HttpAuth.html)

  * Defined in [core/src/auth/auth_credential.ts:270](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L270)



### `Optional`oauth2

oauth2?: [OAuth2Auth](OAuth2Auth.html)

  * Defined in [core/src/auth/auth_credential.ts:272](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L272)



### `Optional`resourceRef

resourceRef?: string

Resource reference for the credential. This will be supported in the future.

  * Defined in [core/src/auth/auth_credential.ts:267](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L267)



### `Optional`serviceAccount

serviceAccount?: [ServiceAccount](ServiceAccount.html)

  * Defined in [core/src/auth/auth_credential.ts:271](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L271)



Properties

apiKeyauthTypehttpoauth2resourceRefserviceAccount

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


