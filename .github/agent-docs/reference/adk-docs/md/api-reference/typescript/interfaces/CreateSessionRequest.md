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

  * Defined in [core/src/sessions/base_session_service.ts:25](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/base_session_service.ts#L25)



## Properties

### appName

appName: string

The name of the application.

  * Defined in [core/src/sessions/base_session_service.ts:27](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/base_session_service.ts#L27)



### `Optional`sessionId

sessionId?: string

The ID of the session. A new ID will be generated if not provided.

  * Defined in [core/src/sessions/base_session_service.ts:33](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/base_session_service.ts#L33)



### `Optional`state

state?: Record<string, unknown>

The initial state of the session.

  * Defined in [core/src/sessions/base_session_service.ts:31](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/base_session_service.ts#L31)



### userId

userId: string

The ID of the user.

  * Defined in [core/src/sessions/base_session_service.ts:29](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/base_session_service.ts#L29)



Properties

appNamesessionIdstateuserId

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


