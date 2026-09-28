[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AuthProviderRegistry]()



# Class AuthProviderRegistry

Registry for auth provider instances.

  * Defined in [core/src/auth/auth_provider_registry.ts:13](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_provider_registry.ts#L13)



## Constructors

### constructor

  * new AuthProviderRegistry(): [AuthProviderRegistry]()

#### Returns [AuthProviderRegistry]()




## Methods

### getProvider

  * getProvider(authScheme: [AuthScheme](../types/AuthScheme.html)): [BaseAuthProvider](../interfaces/BaseAuthProvider.html) | undefined

Get the provider instance for an auth scheme.

#### Parameters

    * authScheme: [AuthScheme](../types/AuthScheme.html)

The auth scheme to get provider for.

#### Returns [BaseAuthProvider](../interfaces/BaseAuthProvider.html) | undefined

The provider instance if registered, undefined otherwise.

    * Defined in [core/src/auth/auth_provider_registry.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_provider_registry.ts#L32)




### register

  * register(authSchemeType: string, providerInstance: [BaseAuthProvider](../interfaces/BaseAuthProvider.html)): void

Register a provider instance for an auth scheme type.

#### Parameters

    * authSchemeType: string

The auth scheme type (e.g., 'oauth2', 'apiKey').

    * providerInstance: [BaseAuthProvider](../interfaces/BaseAuthProvider.html)

The provider instance to register.

#### Returns void

    * Defined in [core/src/auth/auth_provider_registry.ts:22](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/auth/auth_provider_registry.ts#L22)




Constructors

constructor

Methods

getProviderregister

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


