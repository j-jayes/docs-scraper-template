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

  * Defined in [auth/auth_credential.ts:72](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L72)



## Properties

### authProviderX509CertUrl

authProviderX509CertUrl: string

URL for auth provider's X.509 cert.

  * Defined in [auth/auth_credential.ts:116](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L116)



### authUri

authUri: string

The authorization URI.

  * Defined in [auth/auth_credential.ts:106](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L106)



### clientEmail

clientEmail: string

The client email.

  * Defined in [auth/auth_credential.ts:96](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L96)



### clientId

clientId: string

The client ID.

  * Defined in [auth/auth_credential.ts:101](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L101)



### clientX509CertUrl

clientX509CertUrl: string

URL for the client's X.509 cert.

  * Defined in [auth/auth_credential.ts:121](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L121)



### privateKey

privateKey: string

The private key value.

  * Defined in [auth/auth_credential.ts:91](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L91)



### privateKeyId

privateKeyId: string

The ID of the private key.

  * Defined in [auth/auth_credential.ts:86](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L86)



### projectId

projectId: string

The project ID of the Google Cloud project.

  * Defined in [auth/auth_credential.ts:81](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L81)



### tokenUri

tokenUri: string

The token URI.

  * Defined in [auth/auth_credential.ts:111](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L111)



### type

type: "service_account"

The type should be 'service_account'.

  * Defined in [auth/auth_credential.ts:76](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L76)



### universeDomain

universeDomain: string

The universe domain.

  * Defined in [auth/auth_credential.ts:126](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L126)



Properties

authProviderX509CertUrlauthUriclientEmailclientIdclientX509CertUrlprivateKeyprivateKeyIdprojectIdtokenUritypeuniverseDomain

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


