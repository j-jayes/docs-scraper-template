[ google-adk-kotlin ](../../../../../index.html) Toggle table of contents 

1.5.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../../../index.html)/[com.google.adk.kt.auth](../../../index.html)/[AuthCredential](../../index.html)/[ServiceAccount](../index.html)/Credential

# Credential

common

@[ExperimentalAuthApi](../../../../com.google.adk.kt.annotations/-experimental-auth-api/index.html)

data class [Credential](index.html)(val type: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val projectId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val privateKeyId: [Secret](../../../-secret/index.html), val privateKey: [Secret](../../../-secret/index.html), val clientEmail: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val clientId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val authUri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val tokenUri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val authProviderX509CertUrl: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val clientX509CertUrl: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val universeDomain: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html))

A service account key, as in the JSON key file Google Cloud issues.

Members

## Constructors

[Credential](-credential.html)

Link copied to clipboard

common

constructor(type: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", projectId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), privateKeyId: [Secret](../../../-secret/index.html), privateKey: [Secret](../../../-secret/index.html), clientEmail: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), clientId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), authUri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), tokenUri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), authProviderX509CertUrl: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), clientX509CertUrl: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), universeDomain: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html))

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [Credential](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[authProviderX509CertUrl](auth-provider-x509-cert-url.html)

Link copied to clipboard

common

val [authProviderX509CertUrl](auth-provider-x509-cert-url.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Where the provider's X.509 certificates are published.

[authUri](auth-uri.html)

Link copied to clipboard

common

val [authUri](auth-uri.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The OAuth2 authorization endpoint.

[clientEmail](client-email.html)

Link copied to clipboard

common

val [clientEmail](client-email.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The service account's email address.

[clientId](client-id.html)

Link copied to clipboard

common

val [clientId](client-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The service account's numeric client ID.

[clientX509CertUrl](client-x509-cert-url.html)

Link copied to clipboard

common

val [clientX509CertUrl](client-x509-cert-url.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Where the service account's X.509 certificate is published.

[privateKey](private-key.html)

Link copied to clipboard

common

val [privateKey](private-key.html): [Secret](../../../-secret/index.html)

The private key, in PEM format.

[privateKeyId](private-key-id.html)

Link copied to clipboard

common

val [privateKeyId](private-key-id.html): [Secret](../../../-secret/index.html)

The ID of the private key.

[projectId](project-id.html)

Link copied to clipboard

common

val [projectId](project-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The project the service account belongs to.

[tokenUri](token-uri.html)

Link copied to clipboard

common

val [tokenUri](token-uri.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The OAuth2 token endpoint.

[type](type.html)

Link copied to clipboard

common

val [type](type.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The key type, `service_account` in a key file.

[universeDomain](universe-domain.html)

Link copied to clipboard

common

val [universeDomain](universe-domain.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The Google Cloud universe domain, such as `googleapis.com`.

## Functions

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [AuthCredential.ServiceAccount.Credential.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
