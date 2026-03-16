[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InMemorySessionService]()



# Class InMemorySessionService

An in-memory implementation of the session service.

#### Hierarchy ([View Summary](../hierarchy.html#InMemorySessionService))

  * [BaseSessionService](BaseSessionService.html)
    * InMemorySessionService



  * Defined in [sessions/in_memory_session_service.ts:35](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/in_memory_session_service.ts#L35)



## Constructors

### constructor

  * new InMemorySessionService(): [InMemorySessionService]()

#### Returns [InMemorySessionService]()

Inherited from [BaseSessionService](BaseSessionService.html).[constructor](BaseSessionService.html#constructor)




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

    * Defined in [sessions/in_memory_session_service.ts:173](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/in_memory_session_service.ts#L173)




### createSession

  * createSession(request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)): Promise<[Session](../interfaces/Session.html)>

Creates a new session.

#### Parameters

    * request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)

The request to create a session.

#### Returns Promise<[Session](../interfaces/Session.html)>

A promise that resolves to the newly created session instance.

Overrides [BaseSessionService](BaseSessionService.html).[createSession](BaseSessionService.html#createsession)

    * Defined in [sessions/in_memory_session_service.ts:54](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/in_memory_session_service.ts#L54)




### deleteSession

  * deleteSession(request: [DeleteSessionRequest](../interfaces/DeleteSessionRequest.html)): Promise<void>

Deletes a session.

#### Parameters

    * request: [DeleteSessionRequest](../interfaces/DeleteSessionRequest.html)

The request to delete a session.

#### Returns Promise<void>

A promise that resolves when the session is deleted.

Overrides [BaseSessionService](BaseSessionService.html).[deleteSession](BaseSessionService.html#deletesession)

    * Defined in [sessions/in_memory_session_service.ts:159](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/in_memory_session_service.ts#L159)




### getOrCreateSession

  * getOrCreateSession(request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)): Promise<[Session](../interfaces/Session.html)>

Gets a session or creates one if it doesn't exist.

#### Parameters

    * request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)

The request to get or create a session.

#### Returns Promise<[Session](../interfaces/Session.html)>

A promise that resolves to the session instance.

Inherited from [BaseSessionService](BaseSessionService.html).[getOrCreateSession](BaseSessionService.html#getorcreatesession)

    * Defined in [sessions/base_session_service.ts:124](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L124)




### getSession

  * getSession(request: [GetSessionRequest](../interfaces/GetSessionRequest.html)): Promise<[Session](../interfaces/Session.html) | undefined>

Gets a session.

#### Parameters

    * request: [GetSessionRequest](../interfaces/GetSessionRequest.html)

The request to get a session.

#### Returns Promise<[Session](../interfaces/Session.html) | undefined>

A promise that resolves to the session instance or undefined if not found.

Overrides [BaseSessionService](BaseSessionService.html).[getSession](BaseSessionService.html#getsession)

    * Defined in [sessions/in_memory_session_service.ts:88](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/in_memory_session_service.ts#L88)




### listSessions

  * listSessions(request: [ListSessionsRequest](../interfaces/ListSessionsRequest.html)): Promise<[ListSessionsResponse](../interfaces/ListSessionsResponse.html)>

Lists sessions for a user.

#### Parameters

    * request: [ListSessionsRequest](../interfaces/ListSessionsRequest.html)

The request to list sessions.

#### Returns Promise<[ListSessionsResponse](../interfaces/ListSessionsResponse.html)>

A promise that resolves to a list of sessions for the user.

Overrides [BaseSessionService](BaseSessionService.html).[listSessions](BaseSessionService.html#listsessions)

    * Defined in [sessions/in_memory_session_service.ts:134](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/in_memory_session_service.ts#L134)




Constructors

constructor

Methods

appendEventcreateSessiondeleteSessiongetOrCreateSessiongetSessionlistSessions

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


