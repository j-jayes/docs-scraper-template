[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [VertexAiSessionService]()



# Class VertexAiSessionService

A session service implementation that integrates with Vertex AI Agent Engine Sessions.

#### Hierarchy ([View Summary](../hierarchy.html#VertexAiSessionService))

  * [BaseSessionService](BaseSessionService.html)
    * VertexAiSessionService



  * Defined in [core/src/sessions/vertex_ai_session_service.ts:75](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/vertex_ai_session_service.ts#L75)



## Constructors

### constructor

  * new VertexAiSessionService(  
options: [VertexAiSessionServiceOptions](../interfaces/VertexAiSessionServiceOptions.html),  
): [VertexAiSessionService]()

#### Parameters

    * options: [VertexAiSessionServiceOptions](../interfaces/VertexAiSessionServiceOptions.html)

#### Returns [VertexAiSessionService]()

Overrides [BaseSessionService](BaseSessionService.html).[constructor](BaseSessionService.html#constructor)

    * Defined in [core/src/sessions/vertex_ai_session_service.ts:82](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/vertex_ai_session_service.ts#L82)




## Methods

### appendEvent

  * appendEvent(request: [AppendEventRequest](../interfaces/AppendEventRequest.html)): Promise<[Event](../interfaces/Event.html)>

Appends an event to a session.

#### Parameters

    * request: [AppendEventRequest](../interfaces/AppendEventRequest.html)

The request to append an event.

#### Returns Promise<[Event](../interfaces/Event.html)>

A promise that resolves to the event that was appended.

Overrides [BaseSessionService](BaseSessionService.html).[appendEvent](BaseSessionService.html#appendevent)

    * Defined in [core/src/sessions/vertex_ai_session_service.ts:373](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/vertex_ai_session_service.ts#L373)




### createSession

  * createSession(request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)): Promise<[Session](../interfaces/Session.html)>

Creates a new session.

#### Parameters

    * request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)

The request to create a session.

#### Returns Promise<[Session](../interfaces/Session.html)>

A promise that resolves to the newly created session instance.

Overrides [BaseSessionService](BaseSessionService.html).[createSession](BaseSessionService.html#createsession)

    * Defined in [core/src/sessions/vertex_ai_session_service.ts:131](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/vertex_ai_session_service.ts#L131)




### deleteSession

  * deleteSession(request: [CompositeSessionKey](../interfaces/CompositeSessionKey.html)): Promise<void>

Deletes a session.

#### Parameters

    * request: [CompositeSessionKey](../interfaces/CompositeSessionKey.html)

The request to delete a session.

#### Returns Promise<void>

A promise that resolves when the session is deleted.

Overrides [BaseSessionService](BaseSessionService.html).[deleteSession](BaseSessionService.html#deletesession)

    * Defined in [core/src/sessions/vertex_ai_session_service.ts:346](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/vertex_ai_session_service.ts#L346)




### getOrCreateSession

  * getOrCreateSession(request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)): Promise<[Session](../interfaces/Session.html)>

Gets a session or creates one if it doesn't exist.

#### Parameters

    * request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)

The request to get or create a session.

#### Returns Promise<[Session](../interfaces/Session.html)>

A promise that resolves to the session instance.

Inherited from [BaseSessionService](BaseSessionService.html).[getOrCreateSession](BaseSessionService.html#getorcreatesession)

    * Defined in [core/src/sessions/base_session_service.ts:129](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L129)




### getSession

  * getSession(request: [GetSessionRequest](../interfaces/GetSessionRequest.html)): Promise<[Session](../interfaces/Session.html) | undefined>

Gets a session.

#### Parameters

    * request: [GetSessionRequest](../interfaces/GetSessionRequest.html)

The request to get a session.

#### Returns Promise<[Session](../interfaces/Session.html) | undefined>

A promise that resolves to the session instance or undefined if not found.

Overrides [BaseSessionService](BaseSessionService.html).[getSession](BaseSessionService.html#getsession)

    * Defined in [core/src/sessions/vertex_ai_session_service.ts:183](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/vertex_ai_session_service.ts#L183)




### listSessions

  * listSessions(request: [ListSessionsRequest](../interfaces/ListSessionsRequest.html)): Promise<[ListSessionsResponse](../interfaces/ListSessionsResponse.html)>

Lists sessions for a user.

#### Parameters

    * request: [ListSessionsRequest](../interfaces/ListSessionsRequest.html)

The request to list sessions.

#### Returns Promise<[ListSessionsResponse](../interfaces/ListSessionsResponse.html)>

A promise that resolves to a list of sessions for the user.

Overrides [BaseSessionService](BaseSessionService.html).[listSessions](BaseSessionService.html#listsessions)

    * Defined in [core/src/sessions/vertex_ai_session_service.ts:259](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/vertex_ai_session_service.ts#L259)




Constructors

constructor

Methods

appendEventcreateSessiondeleteSessiongetOrCreateSessiongetSessionlistSessions

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


