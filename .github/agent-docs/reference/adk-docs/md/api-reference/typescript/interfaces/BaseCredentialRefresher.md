[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseCredentialRefresher]()



# Interface BaseCredentialRefresher

Base interface for credential refreshers.

Credential refreshers are responsible for checking if a credential is expired or needs to be refreshed, and for refreshing it if necessary.

interface BaseCredentialRefresher {  
isRefreshNeeded(  
authCredential: [AuthCredential](AuthCredential.html),  
authScheme?: [AuthScheme](../types/AuthScheme.html),  
): Promise<boolean>;  
refresh(  
authCredential: [AuthCredential](AuthCredential.html),  
authScheme?: [AuthScheme](../types/AuthScheme.html),  
): Promise<[AuthCredential](AuthCredential.html)>;  
}

  * Defined in [core/src/auth/refresher/base_credential_refresher.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/refresher/base_credential_refresher.ts#L26)



## Methods

### isRefreshNeeded

  * isRefreshNeeded(  
authCredential: [AuthCredential](AuthCredential.html),  
authScheme?: [AuthScheme](../types/AuthScheme.html),  
): Promise<boolean>

Checks if a credential needs to be refreshed.

#### Parameters

    * authCredential: [AuthCredential](AuthCredential.html)

The credential to check.

    * `Optional`authScheme: [AuthScheme](../types/AuthScheme.html)

The authentication scheme (optional).

#### Returns Promise<boolean>

True if the credential needs to be refreshed, False otherwise.

    * Defined in [core/src/auth/refresher/base_credential_refresher.ts:34](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/refresher/base_credential_refresher.ts#L34)




### refresh

  * refresh(  
authCredential: [AuthCredential](AuthCredential.html),  
authScheme?: [AuthScheme](../types/AuthScheme.html),  
): Promise<[AuthCredential](AuthCredential.html)>

Refreshes a credential if needed.

#### Parameters

    * authCredential: [AuthCredential](AuthCredential.html)

The credential to refresh.

    * `Optional`authScheme: [AuthScheme](../types/AuthScheme.html)

The authentication scheme (optional).

#### Returns Promise<[AuthCredential](AuthCredential.html)>

The refreshed credential.

#### Throws

If credential refresh fails.

    * Defined in [core/src/auth/refresher/base_credential_refresher.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/refresher/base_credential_refresher.ts#L47)




Methods

isRefreshNeededrefresh

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


