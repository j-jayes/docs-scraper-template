[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AuthCredential]()



# Interface AuthCredential

An authentication credential, in one of several shapes selected by `authType`.

To turn one of these into the credential a request actually carries, use the `exchange()` method of a [BaseCredentialExchanger](BaseCredentialExchanger.html).

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
    Copy

#### Example
    
    
    // Open ID Connect Auth  
    const authCredential: AuthCredential = {  
      authType: AuthCredentialTypes.OPEN_ID_CONNECT,  
      oauth2: {  
        clientId: "1234",  
        clientSecret: "secret",  
        redirectUri: "https://example.com",  
      }  
    }
    Copy

#### Example
    
    
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

  * Defined in [core/src/auth/auth_credential.ts:265](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L265)



## Properties

### `Optional`apiKey

apiKey?: string

  * Defined in [core/src/auth/auth_credential.ts:274](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L274)



### authType

authType: [AuthCredentialTypes](../enums/AuthCredentialTypes.html)

  * Defined in [core/src/auth/auth_credential.ts:266](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L266)



### `Optional`http

http?: [HttpAuth](HttpAuth.html)

  * Defined in [core/src/auth/auth_credential.ts:275](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L275)



### `Optional`oauth2

oauth2?: [OAuth2Auth](OAuth2Auth.html)

  * Defined in [core/src/auth/auth_credential.ts:277](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L277)



### `Optional`resourceRef

resourceRef?: string

Resource reference for the credential. This will be supported in the future.

  * Defined in [core/src/auth/auth_credential.ts:272](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L272)



### `Optional`serviceAccount

serviceAccount?: [ServiceAccount](ServiceAccount.html)

  * Defined in [core/src/auth/auth_credential.ts:276](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/auth_credential.ts#L276)



Properties

apiKeyauthTypehttpoauth2resourceRefserviceAccount

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


