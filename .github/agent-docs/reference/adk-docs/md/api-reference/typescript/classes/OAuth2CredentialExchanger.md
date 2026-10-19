[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OAuth2CredentialExchanger]()



# Class OAuth2CredentialExchanger

Exchanges OAuth2 credentials from authorization responses using standard fetch.

#### Implements

  * [BaseCredentialExchanger](../interfaces/BaseCredentialExchanger.html)



  * Defined in [core/src/auth/oauth2/oauth2_credential_exchanger.ts:30](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/oauth2/oauth2_credential_exchanger.ts#L30)



## Constructors

### constructor

  * new OAuth2CredentialExchanger(): [OAuth2CredentialExchanger]()

#### Returns [OAuth2CredentialExchanger]()




## Methods

### exchange

  * exchange(  
__namedParameters: {  
authCredential: [AuthCredential](../interfaces/AuthCredential.html);  
authScheme?: [AuthScheme](../types/AuthScheme.html);  
},  
): Promise<[ExchangeResult](../interfaces/ExchangeResult.html)>

Exchange credential if needed.

#### Parameters

    * __namedParameters: { authCredential: [AuthCredential](../interfaces/AuthCredential.html); authScheme?: [AuthScheme](../types/AuthScheme.html) }

#### Returns Promise<[ExchangeResult](../interfaces/ExchangeResult.html)>

The exchanged credential.

#### Throws

CredentialExchangeError: If credential exchange fails.

Implementation of [BaseCredentialExchanger](../interfaces/BaseCredentialExchanger.html).[exchange](../interfaces/BaseCredentialExchanger.html#exchange)

    * Defined in [core/src/auth/oauth2/oauth2_credential_exchanger.ts:31](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/auth/oauth2/oauth2_credential_exchanger.ts#L31)




Constructors

constructor

Methods

exchange

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


