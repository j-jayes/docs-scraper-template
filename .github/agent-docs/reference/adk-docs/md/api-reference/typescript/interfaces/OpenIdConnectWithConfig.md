[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OpenIdConnectWithConfig]()



# Interface OpenIdConnectWithConfig

OpenIdConnectWithConfig extends OpenIdSecurityScheme with additional configuration options.

interface OpenIdConnectWithConfig {  
authorizationEndpoint: string;  
grantTypesSupported?: string[];  
revocationEndpoint?: string;  
scopes?: string[];  
tokenEndpoint: string;  
tokenEndpointAuthMethodsSupported?: string[];  
userinfoEndpoint?: string;  
}

#### Hierarchy

  * OpenIdSecurityScheme
    * OpenIdConnectWithConfig



  * Defined in [core/src/auth/auth_schemes.ts:15](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_schemes.ts#L15)



## Properties

### authorizationEndpoint

authorizationEndpoint: string

  * Defined in [core/src/auth/auth_schemes.ts:17](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_schemes.ts#L17)



### `Optional`grantTypesSupported

grantTypesSupported?: string[]

  * Defined in [core/src/auth/auth_schemes.ts:22](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_schemes.ts#L22)



### `Optional`revocationEndpoint

revocationEndpoint?: string

  * Defined in [core/src/auth/auth_schemes.ts:20](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_schemes.ts#L20)



### `Optional`scopes

scopes?: string[]

  * Defined in [core/src/auth/auth_schemes.ts:23](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_schemes.ts#L23)



### tokenEndpoint

tokenEndpoint: string

  * Defined in [core/src/auth/auth_schemes.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_schemes.ts#L18)



### `Optional`tokenEndpointAuthMethodsSupported

tokenEndpointAuthMethodsSupported?: string[]

  * Defined in [core/src/auth/auth_schemes.ts:21](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_schemes.ts#L21)



### `Optional`userinfoEndpoint

userinfoEndpoint?: string

  * Defined in [core/src/auth/auth_schemes.ts:19](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_schemes.ts#L19)



Properties

authorizationEndpointgrantTypesSupportedrevocationEndpointscopestokenEndpointtokenEndpointAuthMethodsSupporteduserinfoEndpoint

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


