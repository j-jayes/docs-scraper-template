[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OAuth2Auth]()



# Interface OAuth2Auth

Represents credential value and its metadata for a OAuth2 credential.

interface OAuth2Auth {  
accessToken?: string;  
audience?: string;  
authCode?: string;  
authResponseUri?: string;  
authUri?: string;  
clientId?: string;  
clientSecret?: string;  
codeVerifier?: string;  
expiresAt?: number;  
expiresIn?: number;  
idToken?: string;  
nonce?: string;  
redirectUri?: string;  
refreshToken?: string;  
state?: string;  
tokenEndpointAuthMethod?: string;  
}

  * Defined in [core/src/auth/auth_credential.ts:39](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L39)



## Properties

### `Optional`accessToken

accessToken?: string

  * Defined in [core/src/auth/auth_credential.ts:56](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L56)



### `Optional`audience

audience?: string

  * Defined in [core/src/auth/auth_credential.ts:61](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L61)



### `Optional`authCode

authCode?: string

  * Defined in [core/src/auth/auth_credential.ts:55](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L55)



### `Optional`authResponseUri

authResponseUri?: string

  * Defined in [core/src/auth/auth_credential.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L54)



### `Optional`authUri

authUri?: string

tool or adk can generate the authUri with the state info thus client can verify the state

  * Defined in [core/src/auth/auth_credential.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L46)



### `Optional`clientId

clientId?: string

  * Defined in [core/src/auth/auth_credential.ts:40](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L40)



### `Optional`clientSecret

clientSecret?: string

  * Defined in [core/src/auth/auth_credential.ts:41](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L41)



### `Optional`codeVerifier

codeVerifier?: string

  * Defined in [core/src/auth/auth_credential.ts:49](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L49)



### `Optional`expiresAt

expiresAt?: number

  * Defined in [core/src/auth/auth_credential.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L59)



### `Optional`expiresIn

expiresIn?: number

  * Defined in [core/src/auth/auth_credential.ts:60](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L60)



### `Optional`idToken

idToken?: string

  * Defined in [core/src/auth/auth_credential.ts:58](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L58)



### `Optional`nonce

nonce?: string

  * Defined in [core/src/auth/auth_credential.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L47)



### `Optional`redirectUri

redirectUri?: string

tool or adk can decide the redirect_uri if they don't want client to decide

  * Defined in [core/src/auth/auth_credential.ts:53](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L53)



### `Optional`refreshToken

refreshToken?: string

  * Defined in [core/src/auth/auth_credential.ts:57](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L57)



### `Optional`state

state?: string

  * Defined in [core/src/auth/auth_credential.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L48)



### `Optional`tokenEndpointAuthMethod

tokenEndpointAuthMethod?: string

  * Defined in [core/src/auth/auth_credential.ts:62](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_credential.ts#L62)



Properties

accessTokenaudienceauthCodeauthResponseUriauthUriclientIdclientSecretcodeVerifierexpiresAtexpiresInidTokennonceredirectUrirefreshTokenstatetokenEndpointAuthMethod

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


