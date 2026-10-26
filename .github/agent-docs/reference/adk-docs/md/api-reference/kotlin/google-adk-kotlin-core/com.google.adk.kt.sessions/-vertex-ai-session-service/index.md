[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

jvm

Target filter __

    * jvm 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.sessions](../index.html)/VertexAiSessionService

# VertexAiSessionService

jvm

class [VertexAiSessionService](index.html) : [SessionService](../-session-service/index.html)

A [SessionService](../-session-service/index.html) backed by the managed Vertex AI Session Service.

This is a Kotlin port of the Java ADK `com.google.adk.sessions.VertexAiSessionService`. It talks to the service through a [VertexAiSessionsClient](../../../google-adk-kotlin-core/com.google.adk.kt.sessions/-vertex-ai-sessions-client/index.html) over a shared GoogleApiClient. The wire format (defined by `session.proto`) is modeled with a small set of `@Serializable` DTOs in the `dto` sub-package; this class only translates between those DTOs and the ADK domain types via the mapper extensions in `com.google.adk.kt.sessions.dto.SessionMappers`.

The reasoning engine is fixed at construction from [project](../../../google-adk-kotlin-core/com.google.adk.kt.sessions/-vertex-ai-session-service/--root--.html), [location](../../../google-adk-kotlin-core/com.google.adk.kt.sessions/-vertex-ai-session-service/--root--.html), and [reasoningEngineId](../../../google-adk-kotlin-core/com.google.adk.kt.sessions/-vertex-ai-session-service/--root--.html). Unlike the Python and Java ADK, the session key's [SessionKey.appName](../-session-key/app-name.html) is never parsed to derive the engine - it is only a label - so the engine must be supplied explicitly here.

Members

## Constructors

[VertexAiSessionService](-vertex-ai-session-service.html)

Link copied to clipboard

jvm

constructor(project: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), location: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), reasoningEngineId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), credentials: [GoogleCredentials](https://javadoc.io/doc/com.google.auth/google-auth-library-oauth2-http/1.48.0/com/google/auth/oauth2/GoogleCredentials.html) = GoogleApiClient.defaultCredentials(), httpClient: HttpClient = HttpClient(Java), sessionTtl: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)? = null)

Creates a service for reasoning engine [reasoningEngineId](../../../google-adk-kotlin-core/com.google.adk.kt.sessions/-vertex-ai-session-service/--root--.html) under [project](../../../google-adk-kotlin-core/com.google.adk.kt.sessions/-vertex-ai-session-service/--root--.html) and [location](../../../google-adk-kotlin-core/com.google.adk.kt.sessions/-vertex-ai-session-service/--root--.html).

## Types

[Builder](-builder/index.html)

Link copied to clipboard

jvm

class [Builder](-builder/index.html)

Fluent builder for [VertexAiSessionService](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

jvm

object [Companion](-companion/index.html)

## Functions

[appendEvent](append-event.html)

Link copied to clipboard

jvm

open suspend override fun [appendEvent](append-event.html)(session: [Session](../-session/index.html), event: [Event](../../com.google.adk.kt.events/-event/index.html)): [Event](../../com.google.adk.kt.events/-event/index.html)

Appends [event](../-session-service/append-event.html) to [session](../-session-service/append-event.html), applying its state delta to the in-memory session and recording the event; `temp:` keys are applied to the in-memory state (so later agents in the invocation can read them) but removed from [event](../-session-service/append-event.html) before persistence.

[closeSession](../-session-service/close-session.html)

Link copied to clipboard

jvm

open suspend fun [closeSession](../-session-service/close-session.html)(session: [Session](../-session/index.html))

Closes a session.

[createSession](create-session.html)

Link copied to clipboard

jvm

open suspend override fun [createSession](create-session.html)(key: [SessionKey](../-session-key/index.html), state: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>? = null): [Session](../-session/index.html)

Creates a new session with the specified parameters.

suspend fun [createSession](create-session.html)(key: [SessionKey](../-session-key/index.html), state: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>? = null, ttl: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html)? = null, expireTime: [Instant](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-instant/index.html)? = null): [Session](../-session/index.html)

Creates a session that expires, addressing the reasoning engine fixed at construction.

[deleteSession](delete-session.html)

Link copied to clipboard

jvm

open suspend override fun [deleteSession](delete-session.html)(key: [SessionKey](../-session-key/index.html))

Deletes a specific session.

[flush](../-session-service/flush.html)

Link copied to clipboard

jvm

open suspend fun [flush](../-session-service/flush.html)(key: [SessionKey](../-session-key/index.html)? = null)

Waits until the writes appended before this call are persisted: those to [key](../-session-service/flush.html), or to every session when [key](../-session-service/flush.html) is `null`. Canceling the caller stops the wait, not the writes.

[getSession](get-session.html)

Link copied to clipboard

jvm

open suspend override fun [getSession](get-session.html)(key: [SessionKey](../-session-key/index.html), config: [GetSessionConfig](../-get-session-config/index.html)? = null): [Session](../-session/index.html)?

Retrieves a specific session, optionally filtering the events included.

[listEvents](list-events.html)

Link copied to clipboard

jvm

open suspend override fun [listEvents](list-events.html)(key: [SessionKey](../-session-key/index.html)): [ListEventsResponse](../-list-events-response/index.html)

Lists the events within a specific session.

[listSessions](list-sessions.html)

Link copied to clipboard

jvm

open suspend override fun [listSessions](list-sessions.html)(appName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), userId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [ListSessionsResponse](../-list-sessions-response/index.html)

Lists sessions associated with a specific application and user.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
