[ google-adk-kotlin ](../../index.html) Toggle table of contents 

1.4.0 

commonJvmAndroid common jvm

Target filter __

    * commonJvmAndroid 
    * common 
    * jvm 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../index.html)/com.google.adk.kt.sessions

# Package-level declarations

TypesFunctions

## Types

[GetSessionConfig](-get-session-config/index.html)

Link copied to clipboard

common

data class [GetSessionConfig](-get-session-config/index.html)(val numRecentEvents: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, val afterTimestamp: [Instant](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-instant/index.html)? = null)

Configuration for getting a session.

[InMemorySessionService](-in-memory-session-service/index.html)

Link copied to clipboard

common

class [InMemorySessionService](-in-memory-session-service/index.html) : [SessionService](-session-service/index.html)

An in-memory implementation of [SessionService](-session-service/index.html) assuming [Session](-session/index.html) objects are mutable regarding their state map, events list, and last update time.

[ListEventsResponse](-list-events-response/index.html)

Link copied to clipboard

common

data class [ListEventsResponse](-list-events-response/index.html)(val events: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../com.google.adk.kt.events/-event/index.html)> = emptyList(), val nextPageToken: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null)

Response for listing events.

[ListSessionsResponse](-list-sessions-response/index.html)

Link copied to clipboard

common

data class [ListSessionsResponse](-list-sessions-response/index.html)(val sessions: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Session](-session/index.html)> = emptyList())

Response for listing sessions.

[Lock](-lock/index.html)

Link copied to clipboard

common

interface [Lock](-lock/index.html)

A read/write lock.

[Session](-session/index.html)

Link copied to clipboard

common

data class [Session](-session/index.html)(val key: [SessionKey](-session-key/index.html), val state: [State](-state/index.html) = State(), val events: [MutableList](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-list/index.html)<[Event](../com.google.adk.kt.events/-event/index.html)> = concurrentMutableListOf(), var lastUpdateTime: [Instant](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-instant/index.html) = Instant.fromEpochMilliseconds(0))

A [Session](-session/index.html) object that encapsulates the [State](-state/index.html) and [Event](../com.google.adk.kt.events/-event/index.html)s of a session.

[SessionException](-session-exception/index.html)

Link copied to clipboard

common

class [SessionException](-session-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), cause: [Throwable](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [RuntimeException](https://developer.android.com/reference/kotlin/java/lang/RuntimeException.html)

Thrown when a [SessionService](-session-service/index.html) operation fails. A caller that needs to act on one particular failure matches [message](../../google-adk-kotlin-core/com.google.adk.kt.sessions/-session-exception/--root--.html) against the constants declared here, so this stays one type rather than a hierarchy.

[SessionKey](-session-key/index.html)

Link copied to clipboard

common

data class [SessionKey](-session-key/index.html)(val appName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val userId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val id: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?)

Composite identifier for a [Session](-session/index.html).

[SessionService](-session-service/index.html)

Link copied to clipboard

common

interface [SessionService](-session-service/index.html)

Defines the contract for managing [Session](-session/index.html)s and their associated [Event](../com.google.adk.kt.events/-event/index.html)s. Provides methods for creating, retrieving, listing, and deleting sessions, as well as listing and appending events to a session. Implementations of this interface handle the underlying storage and retrieval logic.

[State](-state/index.html)

Link copied to clipboard

common

class [State](-state/index.html)(initialState: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap(), initialDelta: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap()) : [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>

A thread-safe state map that maintains the current value and tracks modifications.

[VertexAiSessionService](-vertex-ai-session-service/index.html)

Link copied to clipboard

jvm

class [VertexAiSessionService](-vertex-ai-session-service/index.html) : [SessionService](-session-service/index.html)

A [SessionService](-session-service/index.html) backed by the managed Vertex AI Session Service.

## Functions

[Lock](-lock.html)

Link copied to clipboard

commonJvmAndroidcommon

actual fun [Lock](-lock.html)(): [Lock](-lock/index.html)

expect fun [Lock](-lock.html)(): [Lock](-lock/index.html)

Creates a new [Lock](-lock.html).

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
