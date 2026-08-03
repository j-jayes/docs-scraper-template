[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [CreateSessionRequest]()



# Interface CreateSessionRequest

The parameters for `createSession`.

interface CreateSessionRequest {  
appName: string;  
sessionId?: string;  
state?: Record<string, unknown>;  
userId: string;  
}

  * Defined in [core/src/sessions/base_session_service.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L27)



## Properties

### appName

appName: string

The name of the application.

  * Defined in [core/src/sessions/base_session_service.ts:29](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L29)



### `Optional`sessionId

sessionId?: string

The ID of the session. A new ID will be generated if not provided.

  * Defined in [core/src/sessions/base_session_service.ts:35](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L35)



### `Optional`state

state?: Record<string, unknown>

The initial state of the session.

  * Defined in [core/src/sessions/base_session_service.ts:33](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L33)



### userId

userId: string

The ID of the user.

  * Defined in [core/src/sessions/base_session_service.ts:31](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L31)



Properties

appNamesessionIdstateuserId

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


