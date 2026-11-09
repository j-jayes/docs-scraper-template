[ google-adk-kotlin ](../../../../index.html) Toggle table of contents 

1.5.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../../index.html)/[com.google.adk.kt.auth](../../index.html)/[AuthCredential](../index.html)/ServiceAccount

# ServiceAccount

common

@[ExperimentalAuthApi](../../../com.google.adk.kt.annotations/-experimental-auth-api/index.html)

data class [ServiceAccount](index.html)(val serviceAccountCredential: [AuthCredential.ServiceAccount.Credential](-credential/index.html)? = null, val scopes: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, val useDefaultCredential: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val useIdToken: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val audience: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null) : [AuthCredential](../index.html)

A Google Cloud credential: a service account key, or Application Default Credentials.

#### Throws

[IllegalArgumentException](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-illegal-argument-exception/index.html)

if [serviceAccountCredential](../../../../google-adk-kotlin-core/com.google.adk.kt.auth/-auth-credential/-service-account/--root--.html) is `null` and [useDefaultCredential](../../../../google-adk-kotlin-core/com.google.adk.kt.auth/-auth-credential/-service-account/--root--.html) is `false`, or if [useIdToken](../../../../google-adk-kotlin-core/com.google.adk.kt.auth/-auth-credential/-service-account/--root--.html) is `true` and [audience](../../../../google-adk-kotlin-core/com.google.adk.kt.auth/-auth-credential/-service-account/--root--.html) is `null` or empty.

Members

## Constructors

[ServiceAccount](-service-account.html)

Link copied to clipboard

common

constructor(serviceAccountCredential: [AuthCredential.ServiceAccount.Credential](-credential/index.html)? = null, scopes: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>? = null, useDefaultCredential: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, useIdToken: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, audience: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [ServiceAccount](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

[Credential](-credential/index.html)

Link copied to clipboard

common

@[ExperimentalAuthApi](../../../com.google.adk.kt.annotations/-experimental-auth-api/index.html)

data class [Credential](-credential/index.html)(val type: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val projectId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val privateKeyId: [Secret](../../-secret/index.html), val privateKey: [Secret](../../-secret/index.html), val clientEmail: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val clientId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val authUri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val tokenUri: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val authProviderX509CertUrl: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val clientX509CertUrl: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val universeDomain: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html))

A service account key, as in the JSON key file Google Cloud issues.

## Properties

[audience](audience.html)

Link copied to clipboard

common

val [audience](audience.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The audience of the ID token, usually the URL of the receiving service.

[scopes](scopes.html)

Link copied to clipboard

common

val [scopes](scopes.html): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>?

The OAuth2 scopes to request for the access token; pass at least one with a key. With Application Default Credentials, `null` or empty means `https://www.googleapis.com/auth/cloud-platform`. ID tokens ignore them.

[serviceAccountCredential](service-account-credential.html)

Link copied to clipboard

common

val [serviceAccountCredential](service-account-credential.html): [AuthCredential.ServiceAccount.Credential](-credential/index.html)?

The service account key; required unless [useDefaultCredential](../../../../google-adk-kotlin-core/com.google.adk.kt.auth/-auth-credential/-service-account/--root--.html) is `true`.

[useDefaultCredential](use-default-credential.html)

Link copied to clipboard

common

val [useDefaultCredential](use-default-credential.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether to use Application Default Credentials instead of a key.

[useIdToken](use-id-token.html)

Link copied to clipboard

common

val [useIdToken](use-id-token.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether to get an ID token instead of an access token; requires a non-empty [audience](../../../../google-adk-kotlin-core/com.google.adk.kt.auth/-auth-credential/-service-account/--root--.html).

## Functions

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [AuthCredential.ServiceAccount.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
