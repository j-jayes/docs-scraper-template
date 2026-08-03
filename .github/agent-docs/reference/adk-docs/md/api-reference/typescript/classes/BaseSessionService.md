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
    * [VertexAiSessionService](VertexAiSessionService.html)
    * [InMemorySessionService](InMemorySessionService.html)



  * Defined in [core/src/sessions/base_session_service.ts:105](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L105)



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

    * Defined in [core/src/sessions/base_session_service.ts:168](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L168)




### `Abstract`createSession

  * createSession(request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)): Promise<[Session](../interfaces/Session.html)>

Creates a new session.

#### Parameters

    * request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)

The request to create a session.

#### Returns Promise<[Session](../interfaces/Session.html)>

A promise that resolves to the newly created session instance.

    * Defined in [core/src/sessions/base_session_service.ts:112](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L112)




### `Abstract`deleteSession

  * deleteSession(request: [CompositeSessionKey](../interfaces/CompositeSessionKey.html)): Promise<void>

Deletes a session.

#### Parameters

    * request: [CompositeSessionKey](../interfaces/CompositeSessionKey.html)

The request to delete a session.

#### Returns Promise<void>

A promise that resolves when the session is deleted.

    * Defined in [core/src/sessions/base_session_service.ts:160](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L160)




### getOrCreateSession

  * getOrCreateSession(request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)): Promise<[Session](../interfaces/Session.html)>

Gets a session or creates one if it doesn't exist.

#### Parameters

    * request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)

The request to get or create a session.

#### Returns Promise<[Session](../interfaces/Session.html)>

A promise that resolves to the session instance.

    * Defined in [core/src/sessions/base_session_service.ts:129](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L129)




### `Abstract`getSession

  * getSession(request: [GetSessionRequest](../interfaces/GetSessionRequest.html)): Promise<[Session](../interfaces/Session.html) | undefined>

Gets a session.

#### Parameters

    * request: [GetSessionRequest](../interfaces/GetSessionRequest.html)

The request to get a session.

#### Returns Promise<[Session](../interfaces/Session.html) | undefined>

A promise that resolves to the session instance or undefined if not found.

    * Defined in [core/src/sessions/base_session_service.ts:121](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L121)




### `Abstract`listSessions

  * listSessions(request: [ListSessionsRequest](../interfaces/ListSessionsRequest.html)): Promise<[ListSessionsResponse](../interfaces/ListSessionsResponse.html)>

Lists sessions for a user.

#### Parameters

    * request: [ListSessionsRequest](../interfaces/ListSessionsRequest.html)

The request to list sessions.

#### Returns Promise<[ListSessionsResponse](../interfaces/ListSessionsResponse.html)>

A promise that resolves to a list of sessions for the user.

    * Defined in [core/src/sessions/base_session_service.ts:150](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L150)




Constructors

constructor

Methods

appendEventcreateSessiondeleteSessiongetOrCreateSessiongetSessionlistSessions

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


