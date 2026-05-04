JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/FirestoreSessionService.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.sessions](package-summary.html)
  2. [FirestoreSessionService](FirestoreSessionService.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. FirestoreSessionService(Firestore)
  5. Method Details
     1. createSession(String, String, ConcurrentMap, String)
     2. createSession(String, String, Map, String)
     3. getSession(String, String, String, Optional)
     4. listSessions(String, String)
     5. deleteSession(String, String, String)
     6. listEvents(String, String, String)
     7. appendEvent(Session, Event)

Hide sidebar  Show sidebar

# Class FirestoreSessionService

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.sessions.FirestoreSessionService

All Implemented Interfaces:
    `[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")`

* * *

public class FirestoreSessionService extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")

FirestoreSessionService implements session management using Google Firestore as the backend storage.

  * ## Constructor Summary

Constructors

Constructor

Description

`FirestoreSessionService(com.google.cloud.firestore.Firestore firestore)`

Constructor for FirestoreSessionService.

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[Event](../events/Event.html "class in com.google.adk.events")>`

`appendEvent([Session](Session.html "class in com.google.adk.sessions") session, [Event](../events/Event.html "class in com.google.adk.events") event)`

Appends an event to a session, updating the session state and persisting to Firestore.

`io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")>`

`createSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> state, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)`

Creates a new session in Firestore.

`io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")>`

`createSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> state, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)`

Creates a new session in Firestore.

`io.reactivex.rxjava3.core.Completable`

`deleteSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)`

Deletes a session and all its associated events from Firestore.

`io.reactivex.rxjava3.core.Maybe<[Session](Session.html "class in com.google.adk.sessions")>`

`getSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[GetSessionConfig](GetSessionConfig.html "class in com.google.adk.sessions")> configOpt)`

Retrieves a session by appName, userId, and sessionId from Firestore.

`io.reactivex.rxjava3.core.Single<[ListEventsResponse](ListEventsResponse.html "class in com.google.adk.sessions")>`

`listEvents([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)`

Lists all events for a given appName, userId, and sessionId.

`io.reactivex.rxjava3.core.Single<[ListSessionsResponse](ListSessionsResponse.html "class in com.google.adk.sessions")>`

`listSessions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId)`

Lists all sessions for a given appName and userId.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [BaseSessionService](BaseSessionService.html#method-summary "interface in com.google.adk.sessions")

`[closeSession](BaseSessionService.html#closeSession\(com.google.adk.sessions.Session\) "closeSession\(Session\)"), [createSession](BaseSessionService.html#createSession\(com.google.adk.sessions.SessionKey\) "createSession\(SessionKey\)"), [createSession](BaseSessionService.html#createSession\(com.google.adk.sessions.SessionKey,java.util.Map\) "createSession\(SessionKey, Map\)"), [createSession](BaseSessionService.html#createSession\(java.lang.String,java.lang.String\) "createSession\(String, String\)"), [deleteSession](BaseSessionService.html#deleteSession\(com.google.adk.sessions.SessionKey\) "deleteSession\(SessionKey\)"), [getSession](BaseSessionService.html#getSession\(com.google.adk.sessions.SessionKey,com.google.adk.sessions.GetSessionConfig\) "getSession\(SessionKey, GetSessionConfig\)"), [listEvents](BaseSessionService.html#listEvents\(com.google.adk.sessions.SessionKey\) "listEvents\(SessionKey\)"), [listSessions](BaseSessionService.html#listSessions\(com.google.adk.sessions.SessionKey\) "listSessions\(SessionKey\)")`

Modifier and Type

Method

Description

`default io.reactivex.rxjava3.core.Completable`

`[closeSession](BaseSessionService.html#closeSession\(com.google.adk.sessions.Session\))([Session](Session.html "class in com.google.adk.sessions") session)`

Closes a session.

`default io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")>`

`[createSession](BaseSessionService.html#createSession\(com.google.adk.sessions.SessionKey\))([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Creates a new session with the specified application name and user ID, using a default state (null) and allowing the service to generate a unique session ID.

`default io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")>`

`[createSession](BaseSessionService.html#createSession\(com.google.adk.sessions.SessionKey,java.util.Map\))([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> state)`

Creates a new session with the specified parameters.

`default io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")>`

`[createSession](BaseSessionService.html#createSession\(java.lang.String,java.lang.String\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId)`

Creates a new session with the specified application name and user ID, using a default state (null) and allowing the service to generate a unique session ID.

`default io.reactivex.rxjava3.core.Completable`

`[deleteSession](BaseSessionService.html#deleteSession\(com.google.adk.sessions.SessionKey\))([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Deletes a specific session.

`default io.reactivex.rxjava3.core.Maybe<[Session](Session.html "class in com.google.adk.sessions")>`

`[getSession](BaseSessionService.html#getSession\(com.google.adk.sessions.SessionKey,com.google.adk.sessions.GetSessionConfig\))([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey, @Nullable [GetSessionConfig](GetSessionConfig.html "class in com.google.adk.sessions") config)`

Retrieves a specific session, optionally filtering the events included.

`default io.reactivex.rxjava3.core.Single<[ListEventsResponse](ListEventsResponse.html "class in com.google.adk.sessions")>`

`[listEvents](BaseSessionService.html#listEvents\(com.google.adk.sessions.SessionKey\))([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Lists the events within a specific session.

`default io.reactivex.rxjava3.core.Single<[ListSessionsResponse](ListSessionsResponse.html "class in com.google.adk.sessions")>`

`[listSessions](BaseSessionService.html#listSessions\(com.google.adk.sessions.SessionKey\))([SessionKey](SessionKey.html "class in com.google.adk.sessions") sessionKey)`

Lists sessions associated with a specific application and user.




  * ## Constructor Details

    * ### FirestoreSessionService

public FirestoreSessionService(com.google.cloud.firestore.Firestore firestore)

Constructor for FirestoreSessionService.

  * ## Method Details

    * ### createSession

public io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")> createSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, @Nullable [ConcurrentMap](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/concurrent/ConcurrentMap.html "interface in java.util.concurrent")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> state, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)

Creates a new session in Firestore.

Specified by:
    `[createSession](BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.concurrent.ConcurrentMap,java.lang.String\))` in interface `[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")`
Parameters:
    `appName` \- The name of the application associated with the session.
    `userId` \- The identifier for the user associated with the session.
    `state` \- An optional map representing the initial state of the session. Can be null or empty.
    `sessionId` \- An optional client-provided identifier for the session. If empty or null, the service should generate a unique ID.
Returns:
    The newly created [`Session`](Session.html "class in com.google.adk.sessions") instance.

    * ### createSession

public io.reactivex.rxjava3.core.Single<[Session](Session.html "class in com.google.adk.sessions")> createSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, @Nullable [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")> state, @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)

Creates a new session in Firestore.

Specified by:
    `[createSession](BaseSessionService.html#createSession\(java.lang.String,java.lang.String,java.util.Map,java.lang.String\))` in interface `[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")`
Parameters:
    `appName` \- The name of the application associated with the session.
    `userId` \- The identifier for the user associated with the session.
    `state` \- An optional map representing the initial state of the session. Can be null or empty.
    `sessionId` \- An optional client-provided identifier for the session. If empty or null, the service should generate a unique ID.
Returns:
    The newly created [`Session`](Session.html "class in com.google.adk.sessions") instance.

    * ### getSession

public io.reactivex.rxjava3.core.Maybe<[Session](Session.html "class in com.google.adk.sessions")> getSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[GetSessionConfig](GetSessionConfig.html "class in com.google.adk.sessions")> configOpt)

Retrieves a session by appName, userId, and sessionId from Firestore.

Specified by:
    `[getSession](BaseSessionService.html#getSession\(java.lang.String,java.lang.String,java.lang.String,java.util.Optional\))` in interface `[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")`
Parameters:
    `appName` \- The name of the application.
    `userId` \- The identifier of the user.
    `sessionId` \- The unique identifier of the session to retrieve.
    `configOpt` \- Optional configuration to filter the events returned within the session (e.g., limit number of recent events, filter by timestamp). If empty, default retrieval behavior is used (potentially all events or a service-defined limit).
Returns:
    An [`Optional`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util") containing the [`Session`](Session.html "class in com.google.adk.sessions") if found, otherwise [`Optional.empty()`](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html#empty\(\)).

    * ### listSessions

public io.reactivex.rxjava3.core.Single<[ListSessionsResponse](ListSessionsResponse.html "class in com.google.adk.sessions")> listSessions([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId)

Lists all sessions for a given appName and userId.

Specified by:
    `[listSessions](BaseSessionService.html#listSessions\(java.lang.String,java.lang.String\))` in interface `[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")`
Parameters:
    `appName` \- The name of the application.
    `userId` \- The identifier of the user whose sessions are to be listed.
Returns:
    A [`ListSessionsResponse`](ListSessionsResponse.html "class in com.google.adk.sessions") containing a list of matching sessions.

    * ### deleteSession

public io.reactivex.rxjava3.core.Completable deleteSession([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)

Deletes a session and all its associated events from Firestore.

Specified by:
    `[deleteSession](BaseSessionService.html#deleteSession\(java.lang.String,java.lang.String,java.lang.String\))` in interface `[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")`
Parameters:
    `appName` \- The name of the application.
    `userId` \- The identifier of the user.
    `sessionId` \- The unique identifier of the session to delete.

    * ### listEvents

public io.reactivex.rxjava3.core.Single<[ListEventsResponse](ListEventsResponse.html "class in com.google.adk.sessions")> listEvents([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") appName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") sessionId)

Lists all events for a given appName, userId, and sessionId.

Specified by:
    `[listEvents](BaseSessionService.html#listEvents\(java.lang.String,java.lang.String,java.lang.String\))` in interface `[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")`
Parameters:
    `appName` \- The name of the application.
    `userId` \- The identifier of the user.
    `sessionId` \- The unique identifier of the session whose events are to be listed.
Returns:
    A [`ListEventsResponse`](ListEventsResponse.html "class in com.google.adk.sessions") containing a list of events and an optional token for retrieving the next page.

    * ### appendEvent

@CanIgnoreReturnValue public io.reactivex.rxjava3.core.Single<[Event](../events/Event.html "class in com.google.adk.events")> appendEvent([Session](Session.html "class in com.google.adk.sessions") session, [Event](../events/Event.html "class in com.google.adk.events") event)

Appends an event to a session, updating the session state and persisting to Firestore.

Specified by:
    `[appendEvent](BaseSessionService.html#appendEvent\(com.google.adk.sessions.Session,com.google.adk.events.Event\))` in interface `[BaseSessionService](BaseSessionService.html "interface in com.google.adk.sessions")`
Parameters:
    `session` \- The [`Session`](Session.html "class in com.google.adk.sessions") object to which the event should be appended (will be mutated).
    `event` \- The [`Event`](../events/Event.html "class in com.google.adk.events") to append.
Returns:
    The appended [`Event`](../events/Event.html "class in com.google.adk.events") instance (or the original event if it was partial).




* * *

Copyright (C) 1980\. All rights reserved.
