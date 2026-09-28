[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [CredentialRefresherRegistry]()



# Class CredentialRefresherRegistry

Registry for credential refresher instances.

  * Defined in [core/src/auth/refresher/credential_refresher_registry.ts:13](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/refresher/credential_refresher_registry.ts#L13)



## Constructors

### constructor

  * new CredentialRefresherRegistry(): [CredentialRefresherRegistry]()

#### Returns [CredentialRefresherRegistry]()




## Methods

### getRefresher

  * getRefresher(  
credentialType: [AuthCredentialTypes](../enums/AuthCredentialTypes.html),  
): [BaseCredentialRefresher](../interfaces/BaseCredentialRefresher.html) | undefined

Get the refresher instance for a credential type.

#### Parameters

    * credentialType: [AuthCredentialTypes](../enums/AuthCredentialTypes.html)

The credential type to get refresher for.

#### Returns [BaseCredentialRefresher](../interfaces/BaseCredentialRefresher.html) | undefined

The refresher instance if registered, undefined otherwise.

    * Defined in [core/src/auth/refresher/credential_refresher_registry.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/refresher/credential_refresher_registry.ts#L44)




### register

  * register(  
credentialType: [AuthCredentialTypes](../enums/AuthCredentialTypes.html),  
refresherInstance: [BaseCredentialRefresher](../interfaces/BaseCredentialRefresher.html),  
): void

Register a refresher instance for a credential type.

#### Parameters

    * credentialType: [AuthCredentialTypes](../enums/AuthCredentialTypes.html)

The credential type to register for.

    * refresherInstance: [BaseCredentialRefresher](../interfaces/BaseCredentialRefresher.html)

The refresher instance to register.

#### Returns void

    * Defined in [core/src/auth/refresher/credential_refresher_registry.ts:31](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/refresher/credential_refresher_registry.ts#L31)




Constructors

constructor

Methods

getRefresherregister

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


