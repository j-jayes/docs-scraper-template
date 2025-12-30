[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseCredentialService]()



# Interface BaseCredentialService

Abstract class for Service that loads / saves tool credentials from / to the backend credential store.

interface BaseCredentialService {  
loadCredential(  
authConfig: AuthConfig,  
toolContext: [ToolContext](../classes/ToolContext.html),  
): Promise<AuthCredential | undefined>;  
saveCredential(  
authConfig: AuthConfig,  
toolContext: [ToolContext](../classes/ToolContext.html),  
): Promise<void>;  
}

  * Defined in [core/src/auth/credential_service/base_credential_service.ts:15](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/auth/credential_service/base_credential_service.ts#L15)



## Methods

### loadCredential

  * loadCredential(  
authConfig: AuthConfig,  
toolContext: [ToolContext](../classes/ToolContext.html),  
): Promise<AuthCredential | undefined>

Loads the credential by auth config and current tool context from the backend credential store.

#### Parameters

    * authConfig: AuthConfig

The auth config which contains the auth scheme and auth credential information. auth_config.get_credential_key will be used to build the key to load the credential.

    * toolContext: [ToolContext](../classes/ToolContext.html)

The context of the current invocation when the tool is trying to load the credential.

#### Returns Promise<AuthCredential | undefined>

A promise that resolves to the credential saved in the store.

    * Defined in [core/src/auth/credential_service/base_credential_service.ts:27](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/auth/credential_service/base_credential_service.ts#L27)




### saveCredential

  * saveCredential(authConfig: AuthConfig, toolContext: [ToolContext](../classes/ToolContext.html)): Promise<void>

#### Parameters

    * authConfig: AuthConfig
    * toolContext: [ToolContext](../classes/ToolContext.html)

#### Returns Promise<void>

    * Defined in [core/src/auth/credential_service/base_credential_service.ts:43](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/auth/credential_service/base_credential_service.ts#L43)




Methods

loadCredentialsaveCredential

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


