JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseSessionService.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.sessions](package-summary.html)
  2. [BaseSessionService](BaseSessionService.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. createSession(String, String, ConcurrentMap, String)
     2. createSession(String, String)
     3. getSession(String, String, String, Optional)
     4. listSessions(String, String)
     5. deleteSession(String, String, String)
     6. listEvents(String, String, String)
     7. closeSession(Session)
     8. appendEvent(Session, Event)



# Interface BaseSessionService

All Known Implementing Classes:
    `[InMemorySessionService](InMemorySessionService.html "class in com.google.adk.sessions")`, `[VertexAiSessionService](VertexAiSessionService.html "class in com.google.adk.sessions")`

* * *

public interface BaseSessionService

Defines the contract for managing [`Session`](Session.html "class in com.google.adk.sessions")s and their associated [`Event`](../events/Event.html "class in com.google.adk.events")s. Provides methods for creating, retrieving, listing, and deleting sessions, as well as listing and appending events to a session. Implementations of this interface handle the underlying storage and retrieval logic.

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsDefault Methods

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Single<[Event](../events/Event.html "class in com.google.adk.events")>`

`appendEvent([Session](Session.html "class in com.google.adk.sessions") session, [Event](../events/Event.html "class in com.google.adk.events") event)`

Appends an event to an in-memory session object and updates the session's state based on the event's state delta, if applicable.

`default io.reactivex.rxjava3.core.Completable`

`closeSession([Session](Session.html "class in com.google.adk.sessions") session)`

Closes a session.

`default io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")>`

`createSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)`

Creates a new session with the specified application name and user ID, using a default state (null) and allowing the service to generate a unique session ID.

`io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")>`

`createSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Creates a new session with the specified parameters.

`io.reactivex.rxjava3.core.Completable`

`deleteSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Deletes a specific session.

`io.reactivex.rxjava3.core.Maybe<[Session](Session.html "class in com.google.adk.sessions")>`

`getSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[GetSessionConfig](GetSessionConfig.html "class in com.google.adk.sessions")> config)`

Retrieves a specific session, optionally filtering the events included.

`io.reactivex.rxjava3.core.Single<[ListEventsResponse](ListEventsResponse.html "class in com.google.adk.sessions")>`

`listEvents([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)`

Lists the events within a specific session.

`io.reactivex.rxjava3.core.Single<[ListSessionsResponse](ListSessionsResponse.html "class in com.google.adk.sessions")>`

`listSessions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)`

Lists sessions associated with a specific application and user.




  * ## Method Details

    * ### createSession

io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")> createSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, @Nullable [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "class or interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> state, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)

Creates a new session with the specified parameters.

Parameters:
    `appName` \- The name of the application associated with the session.
    `userId` \- The identifier for the user associated with the session.
    `state` \- An optional map representing the initial state of the session. Can be null or empty.
    `sessionId` \- An optional client-provided identifier for the session. If empty or null, the service should generate a unique ID.
Returns:
    The newly created [`Session`](Session.html "class in com.google.adk.sessions") instance.
Throws:
    `[SessionException](SessionException.html "class in com.google.adk.sessions")` \- if creation fails.

    * ### createSession

default io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")> createSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)

Creates a new session with the specified application name and user ID, using a default state (null) and allowing the service to generate a unique session ID. 

This is a shortcut for `createSession(String, String, Map, String)` with null state and a null session ID.

Parameters:
    `appName` \- The name of the application associated with the session.
    `userId` \- The identifier for the user associated with the session.
Returns:
    The newly created [`Session`](Session.html "class in com.google.adk.sessions") instance.
Throws:
    `[SessionException](SessionException.html "class in com.google.adk.sessions")` \- if creation fails.

    * ### getSession

io.reactivex.rxjava3.core.Maybe<[Session](Session.html "class in com.google.adk.sessions")> getSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[GetSessionConfig](GetSessionConfig.html "class in com.google.adk.sessions")> config)

Retrieves a specific session, optionally filtering the events included.

Parameters:
    `appName` \- The name of the application.
    `userId` \- The identifier of the user.
    `sessionId` \- The unique identifier of the session to retrieve.
    `config` \- Optional configuration to filter the events returned within the session (e.g., limit number of recent events, filter by timestamp). If empty, default retrieval behavior is used (potentially all events or a service-defined limit).
Returns:
    An [`Optional`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util") containing the [`Session`](Session.html "class in com.google.adk.sessions") if found, otherwise [`Optional.empty()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html#empty\(\) "class or interface in java.util").
Throws:
    `[SessionException](SessionException.html "class in com.google.adk.sessions")` \- for retrieval errors other than not found.

    * ### listSessions

io.reactivex.rxjava3.core.Single<[ListSessionsResponse](ListSessionsResponse.html "class in com.google.adk.sessions")> listSessions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId)

Lists sessions associated with a specific application and user. 

The [`Session`](Session.html "class in com.google.adk.sessions") objects in the response typically contain only metadata (like ID, creation time) and not the full event list or state to optimize performance.

Parameters:
    `appName` \- The name of the application.
    `userId` \- The identifier of the user whose sessions are to be listed.
Returns:
    A [`ListSessionsResponse`](ListSessionsResponse.html "class in com.google.adk.sessions") containing a list of matching sessions.
Throws:
    `[SessionException](SessionException.html "class in com.google.adk.sessions")` \- if listing fails.

    * ### deleteSession

io.reactivex.rxjava3.core.Completable deleteSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)

Deletes a specific session.

Parameters:
    `appName` \- The name of the application.
    `userId` \- The identifier of the user.
    `sessionId` \- The unique identifier of the session to delete.
Throws:
    `[SessionNotFoundException](SessionNotFoundException.html "class in com.google.adk.sessions")` \- if the session doesn't exist.
    `[SessionException](SessionException.html "class in com.google.adk.sessions")` \- for other deletion errors.

    * ### listEvents

io.reactivex.rxjava3.core.Single<[ListEventsResponse](ListEventsResponse.html "class in com.google.adk.sessions")> listEvents([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId)

Lists the events within a specific session. Supports pagination via the response object.

Parameters:
    `appName` \- The name of the application.
    `userId` \- The identifier of the user.
    `sessionId` \- The unique identifier of the session whose events are to be listed.
Returns:
    A [`ListEventsResponse`](ListEventsResponse.html "class in com.google.adk.sessions") containing a list of events and an optional token for retrieving the next page.
Throws:
    `[SessionNotFoundException](SessionNotFoundException.html "class in com.google.adk.sessions")` \- if the session doesn't exist.
    `[SessionException](SessionException.html "class in com.google.adk.sessions")` \- for other listing errors.

    * ### closeSession

default io.reactivex.rxjava3.core.Completable closeSession([Session](Session.html "class in com.google.adk.sessions") session)

Closes a session. This is currently a placeholder and may involve finalizing session state or performing cleanup actions in future implementations. The default implementation does nothing.

Parameters:
    `session` \- The session object to close.

    * ### appendEvent

@CanIgnoreReturnValue default io.reactivex.rxjava3.core.Single<[Event](../events/Event.html "class in com.google.adk.events")> appendEvent([Session](Session.html "class in com.google.adk.sessions") session, [Event](../events/Event.html "class in com.google.adk.events") event)

Appends an event to an in-memory session object and updates the session's state based on the event's state delta, if applicable. 

This method primarily modifies the passed `session` object in memory. Persisting these changes typically requires a separate call to an update/save method provided by the specific service implementation, or might happen implicitly depending on the implementation's design. 

If the event is marked as partial (e.g., `event.isPartial() == true`), it is returned directly without modifying the session state or event list. State delta keys starting with [`State.TEMP_PREFIX`](State.html#TEMP_PREFIX) are ignored during state updates.

Parameters:
    `session` \- The [`Session`](Session.html "class in com.google.adk.sessions") object to which the event should be appended (will be mutated).
    `event` \- The [`Event`](../events/Event.html "class in com.google.adk.events") to append.
Returns:
    The appended [`Event`](../events/Event.html "class in com.google.adk.events") instance (or the original event if it was partial).
Throws:
    `[NullPointerException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html "class or interface in java.lang")` \- if session or event is null.




* * *

Copyright (C) 2025\. All rights reserved.
