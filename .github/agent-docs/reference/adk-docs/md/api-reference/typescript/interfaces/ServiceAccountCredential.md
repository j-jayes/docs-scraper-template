[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ServiceAccountCredential]()



# Interface ServiceAccountCredential

Represents Google Service Account configuration.

#### Example
    
    
    config = {  
      type: "service_account",  
      projectId: "your_project_id",  
      privateKeyId: "your_private_key_id",  
      privateKey: "-----BEGIN PRIVATE KEY-----...",  
      clientEmail: "...@....iam.gserviceaccount.com",  
      clientId: "your_client_id",  
      authUri: "https://accounts.google.com/o/oauth2/auth",  
      tokenUri: "https://oauth2.googleapis.com/token",  
      authProviderX509CertUrl: "https://www.googleapis.com/oauth2/v1/certs",  
      clientX509CertUrl: "https://www.googleapis.com/robot/v1/metadata/x509/...",  
      universeDomain: "googleapis.com",  
    }
    Copy

interface ServiceAccountCredential {  
authProviderX509CertUrl: string;  
authUri: string;  
clientEmail: string;  
clientId: string;  
clientX509CertUrl: string;  
privateKey: string;  
privateKeyId: string;  
projectId: string;  
tokenUri: string;  
type: "service_account";  
universeDomain: string;  
}

  * Defined in [core/src/auth/auth_credential.ts:82](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L82)



## Properties

### authProviderX509CertUrl

authProviderX509CertUrl: string

URL for auth provider's X.509 cert.

  * Defined in [core/src/auth/auth_credential.ts:126](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L126)



### authUri

authUri: string

The authorization URI.

  * Defined in [core/src/auth/auth_credential.ts:116](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L116)



### clientEmail

clientEmail: string

The client email.

  * Defined in [core/src/auth/auth_credential.ts:106](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L106)



### clientId

clientId: string

The client ID.

  * Defined in [core/src/auth/auth_credential.ts:111](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L111)



### clientX509CertUrl

clientX509CertUrl: string

URL for the client's X.509 cert.

  * Defined in [core/src/auth/auth_credential.ts:131](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L131)



### privateKey

privateKey: string

The private key value.

  * Defined in [core/src/auth/auth_credential.ts:101](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L101)



### privateKeyId

privateKeyId: string

The ID of the private key.

  * Defined in [core/src/auth/auth_credential.ts:96](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L96)



### projectId

projectId: string

The project ID of the Google Cloud project.

  * Defined in [core/src/auth/auth_credential.ts:91](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L91)



### tokenUri

tokenUri: string

The token URI.

  * Defined in [core/src/auth/auth_credential.ts:121](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L121)



### type

type: "service_account"

The type should be 'service_account'.

  * Defined in [core/src/auth/auth_credential.ts:86](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L86)



### universeDomain

universeDomain: string

The universe domain.

  * Defined in [core/src/auth/auth_credential.ts:136](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L136)



Properties

authProviderX509CertUrlauthUriclientEmailclientIdclientX509CertUrlprivateKeyprivateKeyIdprojectIdtokenUritypeuniverseDomain

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


