[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OAuth2BearerExchanger]()



# Class OAuth2BearerExchanger

Converts OAuth2 and OpenID Connect credentials into HTTP bearer credentials.

Ports `OAuth2CredentialExchanger` from adk-python `src/google/adk/tools/openapi_tool/auth/credential_exchangers/oauth2_exchanger.py` at tag `v0.1.0`. The adk-js class carries a different name because `OAuth2CredentialExchanger` in `core/src/auth/oauth2/` already owns that one, and it solves a different problem: it fetches tokens from the token endpoint, where this class converts a token it is given.

#### Implements

  * [BaseCredentialExchanger](../interfaces/BaseCredentialExchanger.html)



  * Defined in [core/src/tools/openapi_tool/auth/credential_exchangers/oauth2_exchanger.ts:119](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/auth/credential_exchangers/oauth2_exchanger.ts#L119)



## Constructors

### constructor

  * new OAuth2BearerExchanger(): [OAuth2BearerExchanger]()

#### Returns [OAuth2BearerExchanger]()




## Methods

### exchange

  * exchange(  
params: { authCredential: [AuthCredential](../interfaces/AuthCredential.html); authScheme?: [AuthScheme](../types/AuthScheme.html) },  
): Promise<[ExchangeResult](../interfaces/ExchangeResult.html)>

Exchange credential if needed.

#### Parameters

    * params: { authCredential: [AuthCredential](../interfaces/AuthCredential.html); authScheme?: [AuthScheme](../types/AuthScheme.html) }
      * ##### authCredential: [AuthCredential](../interfaces/AuthCredential.html)

The credential to exchange.

      * ##### `Optional`authScheme?: [AuthScheme](../types/AuthScheme.html)

The authentication scheme (optional, some exchangers don't need it).

#### Returns Promise<[ExchangeResult](../interfaces/ExchangeResult.html)>

The exchanged credential.

#### Throws

CredentialExchangeError: If credential exchange fails.

Implementation of [BaseCredentialExchanger](../interfaces/BaseCredentialExchanger.html).[exchange](../interfaces/BaseCredentialExchanger.html#exchange)

    * Defined in [core/src/tools/openapi_tool/auth/credential_exchangers/oauth2_exchanger.ts:121](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/auth/credential_exchangers/oauth2_exchanger.ts#L121)




Constructors

constructor

Methods

exchange

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


