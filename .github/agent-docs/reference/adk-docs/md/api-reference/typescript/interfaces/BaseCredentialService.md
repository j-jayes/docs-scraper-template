[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseCredentialService]()



# Interface BaseCredentialService

Abstract class for Service that loads / saves tool credentials from / to the backend credential store.

interface BaseCredentialService {  
loadCredential(  
authConfig: [AuthConfig](AuthConfig.html),  
toolContext: [Context](../classes/Context.html),  
): Promise<[AuthCredential](AuthCredential.html) | undefined>;  
saveCredential(authConfig: [AuthConfig](AuthConfig.html), toolContext: [Context](../classes/Context.html)): Promise<void>;  
}

  * Defined in [auth/credential_service/base_credential_service.ts:15](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/credential_service/base_credential_service.ts#L15)



## Methods

### loadCredential

  * loadCredential(  
authConfig: [AuthConfig](AuthConfig.html),  
toolContext: [Context](../classes/Context.html),  
): Promise<[AuthCredential](AuthCredential.html) | undefined>

Loads the credential by auth config and current tool context from the backend credential store.

#### Parameters

    * authConfig: [AuthConfig](AuthConfig.html)

The auth config which contains the auth scheme and auth credential information. auth_config.get_credential_key will be used to build the key to load the credential.

    * toolContext: [Context](../classes/Context.html)

The context of the current invocation when the tool is trying to load the credential.

#### Returns Promise<[AuthCredential](AuthCredential.html) | undefined>

A promise that resolves to the credential saved in the store.

    * Defined in [auth/credential_service/base_credential_service.ts:27](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/credential_service/base_credential_service.ts#L27)




### saveCredential

  * saveCredential(authConfig: [AuthConfig](AuthConfig.html), toolContext: [Context](../classes/Context.html)): Promise<void>

#### Parameters

    * authConfig: [AuthConfig](AuthConfig.html)
    * toolContext: [Context](../classes/Context.html)

#### Returns Promise<void>

    * Defined in [auth/credential_service/base_credential_service.ts:43](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/auth/credential_service/base_credential_service.ts#L43)




Methods

loadCredentialsaveCredential

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


