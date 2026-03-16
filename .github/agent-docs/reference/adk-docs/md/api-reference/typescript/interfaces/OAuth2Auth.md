[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OAuth2Auth]()



# Interface OAuth2Auth

Represents credential value and its metadata for a OAuth2 credential.

interface OAuth2Auth {  
accessToken?: string;  
authCode?: string;  
authResponseUri?: string;  
authUri?: string;  
clientId?: string;  
clientSecret?: string;  
expiresAt?: number;  
expiresIn?: number;  
redirectUri?: string;  
refreshToken?: string;  
state?: string;  
}

  * Defined in [auth/auth_credential.ts:34](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L34)



## Properties

### `Optional`accessToken

accessToken?: string

  * Defined in [auth/auth_credential.ts:49](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L49)



### `Optional`authCode

authCode?: string

  * Defined in [auth/auth_credential.ts:48](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L48)



### `Optional`authResponseUri

authResponseUri?: string

  * Defined in [auth/auth_credential.ts:47](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L47)



### `Optional`authUri

authUri?: string

tool or adk can generate the authUri with the state info thus client can verify the state

  * Defined in [auth/auth_credential.ts:41](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L41)



### `Optional`clientId

clientId?: string

  * Defined in [auth/auth_credential.ts:35](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L35)



### `Optional`clientSecret

clientSecret?: string

  * Defined in [auth/auth_credential.ts:36](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L36)



### `Optional`expiresAt

expiresAt?: number

  * Defined in [auth/auth_credential.ts:51](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L51)



### `Optional`expiresIn

expiresIn?: number

  * Defined in [auth/auth_credential.ts:52](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L52)



### `Optional`redirectUri

redirectUri?: string

tool or adk can decide the redirect_uri if they don't want client to decide

  * Defined in [auth/auth_credential.ts:46](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L46)



### `Optional`refreshToken

refreshToken?: string

  * Defined in [auth/auth_credential.ts:50](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L50)



### `Optional`state

state?: string

  * Defined in [auth/auth_credential.ts:42](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/auth_credential.ts#L42)



Properties

accessTokenauthCodeauthResponseUriauthUriclientIdclientSecretexpiresAtexpiresInredirectUrirefreshTokenstate

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


