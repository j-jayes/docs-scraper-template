[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [DatabaseSessionService]()



# Class DatabaseSessionService

A session service that uses a SQL database for storage via MikroORM.

#### Hierarchy ([View Summary](../hierarchy.html#DatabaseSessionService))

  * [BaseSessionService](BaseSessionService.html)
    * DatabaseSessionService



  * Defined in [sessions/database_session_service.ts:66](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/database_session_service.ts#L66)



## Constructors

### constructor

  * new DatabaseSessionService(  
connectionStringOrOptions: string | Options,  
): [DatabaseSessionService]()

#### Parameters

    * connectionStringOrOptions: string | Options

#### Returns [DatabaseSessionService]()

Overrides [BaseSessionService](BaseSessionService.html).[constructor](BaseSessionService.html#constructor)

    * Defined in [sessions/database_session_service.ts:72](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/database_session_service.ts#L72)




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

    * Defined in [sessions/database_session_service.ts:309](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/database_session_service.ts#L309)




### createSession

  * createSession(request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)): Promise<[Session](../interfaces/Session.html)>

Creates a new session.

#### Parameters

    * request: [CreateSessionRequest](../interfaces/CreateSessionRequest.html)

The request to create a session.

#### Returns Promise<[Session](../interfaces/Session.html)>

A promise that resolves to the newly created session instance.

Overrides [BaseSessionService](BaseSessionService.html).[createSession](BaseSessionService.html#createsession)

    * Defined in [sessions/database_session_service.ts:103](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/database_session_service.ts#L103)




### deleteSession

  * deleteSession(request: [DeleteSessionRequest](../interfaces/DeleteSessionRequest.html)): Promise<void>

Deletes a session.

#### Parameters

    * request: [DeleteSessionRequest](../interfaces/DeleteSessionRequest.html)

The request to delete a session.

#### Returns Promise<void>

A promise that resolves when the session is deleted.

Overrides [BaseSessionService](BaseSessionService.html).[deleteSession](BaseSessionService.html#deletesession)

    * Defined in [sessions/database_session_service.ts:297](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/database_session_service.ts#L297)




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

    * Defined in [sessions/database_session_service.ts:194](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/database_session_service.ts#L194)




### init

  * init(): Promise<void>

#### Returns Promise<void>

    * Defined in [sessions/database_session_service.ts:88](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/database_session_service.ts#L88)




### listSessions

  * listSessions(request: [ListSessionsRequest](../interfaces/ListSessionsRequest.html)): Promise<[ListSessionsResponse](../interfaces/ListSessionsResponse.html)>

Lists sessions for a user.

#### Parameters

    * request: [ListSessionsRequest](../interfaces/ListSessionsRequest.html)

The request to list sessions.

#### Returns Promise<[ListSessionsResponse](../interfaces/ListSessionsResponse.html)>

A promise that resolves to a list of sessions for the user.

Overrides [BaseSessionService](BaseSessionService.html).[listSessions](BaseSessionService.html#listsessions)

    * Defined in [sessions/database_session_service.ts:254](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/database_session_service.ts#L254)




Constructors

constructor

Methods

appendEventcreateSessiondeleteSessiongetOrCreateSessiongetSessioninitlistSessions

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


