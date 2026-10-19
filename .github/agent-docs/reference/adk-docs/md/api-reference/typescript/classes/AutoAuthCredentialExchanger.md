[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AutoAuthCredentialExchanger]()



# Class AutoAuthCredentialExchanger

Automatically selects the appropriate credential exchanger based on the auth scheme. Ported from Python implementation.

#### Example
    
    
    // Common case: a built-in exchanger handles the credential.  
    const exchanger = new AutoAuthCredentialExchanger();  
    const result = await exchanger.exchange({  
      authScheme: serviceAccountScheme,  
      authCredential: serviceAccountCredential,  
    });  
    // result.credential carries an OAuth token as a bearer token.
    Copy

#### Example
    
    
    // Use CustomAuthExchanger for OAuth2 instead of the built-in exchanger.  
    const exchanger = new AutoAuthCredentialExchanger({  
      [AuthCredentialTypes.OAUTH2]: new CustomAuthExchanger(),  
    });
    Copy

#### Implements

  * [BaseCredentialExchanger](../interfaces/BaseCredentialExchanger.html)



  * Defined in [core/src/tools/openapi_tool/auth/credential_exchangers/auto_auth_credential_exchanger.ts:48](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/auth/credential_exchangers/auto_auth_credential_exchanger.ts#L48)



## Constructors

### constructor

  * new AutoAuthCredentialExchanger(  
customExchangers?: Partial<  
Record<[AuthCredentialTypes](../enums/AuthCredentialTypes.html), [BaseCredentialExchanger](../interfaces/BaseCredentialExchanger.html)>,  
>,  
): [AutoAuthCredentialExchanger]()

#### Parameters

    * `Optional`customExchangers: Partial<Record<[AuthCredentialTypes](../enums/AuthCredentialTypes.html), [BaseCredentialExchanger](../interfaces/BaseCredentialExchanger.html)>>

Optional exchangers that add to or override the built-in ones. The key is the auth credential type; the value is the exchanger instance to use for that type.

#### Returns [AutoAuthCredentialExchanger]()

    * Defined in [core/src/tools/openapi_tool/auth/credential_exchangers/auto_auth_credential_exchanger.ts:57](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/auth/credential_exchangers/auto_auth_credential_exchanger.ts#L57)




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

    * Defined in [core/src/tools/openapi_tool/auth/credential_exchangers/auto_auth_credential_exchanger.ts:79](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/auth/credential_exchangers/auto_auth_credential_exchanger.ts#L79)

  * exchange(  
params: { authCredential?: [AuthCredential](../interfaces/AuthCredential.html); authScheme?: [AuthScheme](../types/AuthScheme.html) },  
): Promise<[ExchangeResult](../interfaces/ExchangeResult.html) | null>

#### Parameters

    * params: { authCredential?: [AuthCredential](../interfaces/AuthCredential.html); authScheme?: [AuthScheme](../types/AuthScheme.html) }

#### Returns Promise<[ExchangeResult](../interfaces/ExchangeResult.html) | null>

Implementation of BaseCredentialExchanger.exchange

    * Defined in [core/src/tools/openapi_tool/auth/credential_exchangers/auto_auth_credential_exchanger.ts:83](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/openapi_tool/auth/credential_exchangers/auto_auth_credential_exchanger.ts#L83)




Constructors

constructor

Methods

exchange

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


