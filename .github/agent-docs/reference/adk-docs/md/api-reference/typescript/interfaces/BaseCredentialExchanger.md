[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseCredentialExchanger]()



# Interface BaseCredentialExchanger

Base interface for credential exchangers.

Credential exchangers are responsible for exchanging credentials from one format or scheme to another.

interface BaseCredentialExchanger {  
exchange(  
params: { authCredential: [AuthCredential](AuthCredential.html); authScheme?: [AuthScheme](../types/AuthScheme.html) },  
): Promise<[ExchangeResult](ExchangeResult.html)>;  
}

#### Implemented by

  * [OAuth2CredentialExchanger](../classes/OAuth2CredentialExchanger.html)



  * Defined in [core/src/auth/exchanger/base_credential_exchanger.ts:29](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/exchanger/base_credential_exchanger.ts#L29)



## Methods

### exchange

  * exchange(  
params: { authCredential: [AuthCredential](AuthCredential.html); authScheme?: [AuthScheme](../types/AuthScheme.html) },  
): Promise<[ExchangeResult](ExchangeResult.html)>

Exchange credential if needed.

#### Parameters

    * params: { authCredential: [AuthCredential](AuthCredential.html); authScheme?: [AuthScheme](../types/AuthScheme.html) }
      * ##### authCredential: [AuthCredential](AuthCredential.html)

The credential to exchange.

      * ##### `Optional`authScheme?: [AuthScheme](../types/AuthScheme.html)

The authentication scheme (optional, some exchangers don't need it).

#### Returns Promise<[ExchangeResult](ExchangeResult.html)>

The exchanged credential.

#### Throws

CredentialExchangeError: If credential exchange fails.

    * Defined in [core/src/auth/exchanger/base_credential_exchanger.ts:39](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/exchanger/base_credential_exchanger.ts#L39)




Methods

exchange

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


