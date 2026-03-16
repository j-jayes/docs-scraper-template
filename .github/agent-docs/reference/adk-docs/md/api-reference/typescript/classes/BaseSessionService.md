[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseSessionService]()



# Class BaseSessionService`Abstract`

Base class for session services.

The service provides a set of methods for managing sessions and events.

#### Hierarchy ([View Summary](../hierarchy.html#BaseSessionService))

  * BaseSessionService
    * [DatabaseSessionService](DatabaseSessionService.html)
    * [InMemorySessionService](InMemorySessionService.html)



  * Defined in [sessions/base_session_service.ts:100](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L100)



## Constructors

### constructor

  * new BaseSessionService(): [BaseSessionService]()

#### Returns [BaseSessionService]()




## Methods

### appendEvent

  * appendEvent(request: [AppendEventRequest](../interfaces/AppendEventRequest.html)): Promise<[Event](../interfaces/Event.html)>

Appends an event to a session.

#### Parameters

    * request: [AppendEventRequest](../interfaces/AppendEventRequest.html)

The request to append an event.

#### Returns Promise<[Event](../interfaces/Event.html)>

A promise that resolves to the event that was appended.

    * Defined in [sessions/base_session_service.ts:163](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L163)




### `Abstract`createSession

  * createSession(request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)): Promise<[Session](../interfaces/Session.html)>

Creates a new session.

#### Parameters

    * request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)

The request to create a session.

#### Returns Promise<[Session](../interfaces/Session.html)>

A promise that resolves to the newly created session instance.

    * Defined in [sessions/base_session_service.ts:107](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L107)




### `Abstract`deleteSession

  * deleteSession(request: [DeleteSessionRequest](../interfaces/DeleteSessionRequest.html)): Promise<void>

Deletes a session.

#### Parameters

    * request: [DeleteSessionRequest](../interfaces/DeleteSessionRequest.html)

The request to delete a session.

#### Returns Promise<void>

A promise that resolves when the session is deleted.

    * Defined in [sessions/base_session_service.ts:155](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L155)




### getOrCreateSession

  * getOrCreateSession(request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)): Promise<[Session](../interfaces/Session.html)>

Gets a session or creates one if it doesn't exist.

#### Parameters

    * request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)

The request to get or create a session.

#### Returns Promise<[Session](../interfaces/Session.html)>

A promise that resolves to the session instance.

    * Defined in [sessions/base_session_service.ts:124](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L124)




### `Abstract`getSession

  * getSession(request: [GetSessionRequest](../interfaces/GetSessionRequest.html)): Promise<[Session](../interfaces/Session.html) | undefined>

Gets a session.

#### Parameters

    * request: [GetSessionRequest](../interfaces/GetSessionRequest.html)

The request to get a session.

#### Returns Promise<[Session](../interfaces/Session.html) | undefined>

A promise that resolves to the session instance or undefined if not found.

    * Defined in [sessions/base_session_service.ts:116](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L116)




### `Abstract`listSessions

  * listSessions(request: [ListSessionsRequest](../interfaces/ListSessionsRequest.html)): Promise<[ListSessionsResponse](../interfaces/ListSessionsResponse.html)>

Lists sessions for a user.

#### Parameters

    * request: [ListSessionsRequest](../interfaces/ListSessionsRequest.html)

The request to list sessions.

#### Returns Promise<[ListSessionsResponse](../interfaces/ListSessionsResponse.html)>

A promise that resolves to a list of sessions for the user.

    * Defined in [sessions/base_session_service.ts:145](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L145)




Constructors

constructor

Methods

appendEventcreateSessiondeleteSessiongetOrCreateSessiongetSessionlistSessions

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


