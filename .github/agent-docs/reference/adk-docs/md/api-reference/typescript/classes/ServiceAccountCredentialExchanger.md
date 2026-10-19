[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ServiceAccountCredentialExchanger]()



# Class ServiceAccountCredentialExchanger

Fetches credentials for Google Service Account.

#### Implements

  * [BaseCredentialExchanger](../interfaces/BaseCredentialExchanger.html)



  * Defined in [core/src/tools/openapi_tool/auth/credential_exchangers/service_account_exchanger.ts:32](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/auth/credential_exchangers/service_account_exchanger.ts#L32)



## Constructors

### constructor

  * new ServiceAccountCredentialExchanger(): [ServiceAccountCredentialExchanger]()

#### Returns [ServiceAccountCredentialExchanger]()




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

    * Defined in [core/src/tools/openapi_tool/auth/credential_exchangers/service_account_exchanger.ts:34](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/auth/credential_exchangers/service_account_exchanger.ts#L34)




Constructors

constructor

Methods

exchange

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


