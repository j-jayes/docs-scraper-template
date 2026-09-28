[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InMemoryCredentialService]()



# Class InMemoryCredentialService`Experimental`

(Experimental, subject to change) Class for in memory implementation of credential service

#### Implements

  * [BaseCredentialService](../interfaces/BaseCredentialService.html)



  * Defined in [core/src/auth/credential_service/in_memory_credential_service.ts:17](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/credential_service/in_memory_credential_service.ts#L17)



## Constructors

### constructor

  * new InMemoryCredentialService(): [InMemoryCredentialService]()

`Experimental`

#### Returns [InMemoryCredentialService]()




## Methods

### loadCredential

  * loadCredential(  
authConfig: [AuthConfig](../interfaces/AuthConfig.html),  
toolContext: [Context](Context.html),  
): Promise<[AuthCredential](../interfaces/AuthCredential.html) | undefined>

`Experimental`

Loads the credential by auth config and current tool context from the backend credential store.

#### Parameters

    * authConfig: [AuthConfig](../interfaces/AuthConfig.html)

The auth config which contains the auth scheme and auth credential information. auth_config.get_credential_key will be used to build the key to load the credential.

    * toolContext: [Context](Context.html)

The context of the current invocation when the tool is trying to load the credential.

#### Returns Promise<[AuthCredential](../interfaces/AuthCredential.html) | undefined>

A promise that resolves to the credential saved in the store.

Implementation of [BaseCredentialService](../interfaces/BaseCredentialService.html).[loadCredential](../interfaces/BaseCredentialService.html#loadcredential)

    * Defined in [core/src/auth/credential_service/in_memory_credential_service.ts:23](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/credential_service/in_memory_credential_service.ts#L23)




### saveCredential

  * saveCredential(authConfig: [AuthConfig](../interfaces/AuthConfig.html), toolContext: [Context](Context.html)): Promise<void>

`Experimental`

#### Parameters

    * authConfig: [AuthConfig](../interfaces/AuthConfig.html)
    * toolContext: [Context](Context.html)

#### Returns Promise<void>

Implementation of [BaseCredentialService](../interfaces/BaseCredentialService.html).[saveCredential](../interfaces/BaseCredentialService.html#savecredential)

    * Defined in [core/src/auth/credential_service/in_memory_credential_service.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/credential_service/in_memory_credential_service.ts#L32)




Constructors

constructor

Methods

loadCredentialsaveCredential

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


