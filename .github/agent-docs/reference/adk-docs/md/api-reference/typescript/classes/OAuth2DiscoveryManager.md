[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OAuth2DiscoveryManager]()



# Class OAuth2DiscoveryManager

Implements Metadata discovery for OAuth2 following RFC8414 and RFC9728.

  * Defined in [core/src/auth/oauth2/oauth2_discovery.ts:40](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/oauth2/oauth2_discovery.ts#L40)



## Constructors

### constructor

  * new OAuth2DiscoveryManager(): [OAuth2DiscoveryManager]()

#### Returns [OAuth2DiscoveryManager]()




## Methods

### discoverAuthServerMetadata

  * discoverAuthServerMetadata(  
issuerUrl: string,  
): Promise<  
| {  
authorization_endpoint: string;  
issuer: string;  
registration_endpoint?: string;  
scopes_supported?: string[];  
token_endpoint: string;  
}  
| undefined,  
>

Discovers the OAuth2 authorization server metadata.

#### Parameters

    * issuerUrl: string

#### Returns Promise<  
| {  
authorization_endpoint: string;  
issuer: string;  
registration_endpoint?: string;  
scopes_supported?: string[];  
token_endpoint: string;  
}  
| undefined,  
>

    * Defined in [core/src/auth/oauth2/oauth2_discovery.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/oauth2/oauth2_discovery.ts#L44)




### discoverResourceMetadata

  * discoverResourceMetadata(  
resourceUrl: string,  
): Promise<  
{ authorization_servers: string[]; resource: string }  
| undefined,  
>

Discovers the OAuth2 protected resource metadata.

#### Parameters

    * resourceUrl: string

#### Returns Promise<{ authorization_servers: string[]; resource: string } | undefined>

    * Defined in [core/src/auth/oauth2/oauth2_discovery.ts:119](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/oauth2/oauth2_discovery.ts#L119)




Constructors

constructor

Methods

discoverAuthServerMetadatadiscoverResourceMetadata

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


