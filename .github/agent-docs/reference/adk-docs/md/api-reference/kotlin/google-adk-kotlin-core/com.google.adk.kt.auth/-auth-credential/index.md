[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.5.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.auth](../index.html)/AuthCredential

# AuthCredential

common

@[ExperimentalAuthApi](../../com.google.adk.kt.annotations/-experimental-auth-api/index.html)

sealed interface [AuthCredential](index.html)

A credential that a tool uses to call a service: an [ApiKey](-api-key/index.html), an [Http](-http/index.html) credential, an [OAuth2](-o-auth2/index.html) or OpenID Connect credential, or a [ServiceAccount](-service-account/index.html).

Secret fields are [Secret](../-secret/index.html)s, so a credential's `toString()` prints them as `<redacted>`. [OAuth2](-o-auth2/index.html) also redacts its `state`, `nonce`, `authUri` and `redirectUri`, which are plain strings.

#### Inheritors

[ApiKey](-api-key/index.html)

[Http](-http/index.html)

[OAuth2](-o-auth2/index.html)

[ServiceAccount](-service-account/index.html)

Members

## Types

[ApiKey](-api-key/index.html)

Link copied to clipboard

common

@[ExperimentalAuthApi](../../com.google.adk.kt.annotations/-experimental-auth-api/index.html)

data class [ApiKey](-api-key/index.html)(val apiKey: [Secret](../-secret/index.html)? = null) : [AuthCredential](index.html)

An API key, which the tool sends where the service's auth scheme says, such as in a header.

[Http](-http/index.html)

Link copied to clipboard

common

@[ExperimentalAuthApi](../../com.google.adk.kt.annotations/-experimental-auth-api/index.html)

data class [Http](-http/index.html)(val scheme: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val credentials: [AuthCredential.Http.Credentials](-http/-credentials/index.html), val additionalHeaders: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Secret](../-secret/index.html)>? = null) : [AuthCredential](index.html)

An HTTP authentication credential, usually sent in the `Authorization` header.

[OAuth2](-o-auth2/index.html)

Link copied to clipboard

common

@[ExperimentalAuthApi](../../com.google.adk.kt.annotations/-experimental-auth-api/index.html)

data class [OAuth2](-o-auth2/index.html)(val variant: [AuthCredential.OAuth2.Variant](-o-auth2/-variant/index.html) = Variant.OAUTH2, val clientId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val clientSecret: [Secret](../-secret/index.html)? = null, val authUri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val nonce: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val state: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val redirectUri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val authResponseUri: [Secret](../-secret/index.html)? = null, val authCode: [Secret](../-secret/index.html)? = null, val accessToken: [Secret](../-secret/index.html)? = null, val refreshToken: [Secret](../-secret/index.html)? = null, val idToken: [Secret](../-secret/index.html)? = null, val expiresAt: [Instant](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-instant/index.html)? = null, val expiresIn: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)? = null, val audience: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val prompt: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val codeVerifier: [Secret](../-secret/index.html)? = null, val codeChallengeMethod: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val tokenEndpointAuthMethod: [AuthCredential.OAuth2.TokenEndpointAuthMethod](-o-auth2/-token-endpoint-auth-method/index.html)? = TokenEndpointAuthMethod.CLIENT_SECRET_BASIC) : [AuthCredential](index.html)

An OAuth2 or OpenID Connect credential: the client's configuration, the sign-in state and, once the user has signed in, the tokens.

[ServiceAccount](-service-account/index.html)

Link copied to clipboard

common

@[ExperimentalAuthApi](../../com.google.adk.kt.annotations/-experimental-auth-api/index.html)

data class [ServiceAccount](-service-account/index.html)(val serviceAccountCredential: [AuthCredential.ServiceAccount.Credential](-service-account/-credential/index.html)? = null, val scopes: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val useDefaultCredential: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val useIdToken: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val audience: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null) : [AuthCredential](index.html)

A Google Cloud credential: a service account key, or Application Default Credentials.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
