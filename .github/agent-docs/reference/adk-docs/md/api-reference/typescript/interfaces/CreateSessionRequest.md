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

  * Defined in [sessions/base_session_service.ts:27](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L27)



## Properties

### appName

appName: string

The name of the application.

  * Defined in [sessions/base_session_service.ts:29](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L29)



### `Optional`sessionId

sessionId?: string

The ID of the session. A new ID will be generated if not provided.

  * Defined in [sessions/base_session_service.ts:35](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L35)



### `Optional`state

state?: Record<string, unknown>

The initial state of the session.

  * Defined in [sessions/base_session_service.ts:33](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L33)



### userId

userId: string

The ID of the user.

  * Defined in [sessions/base_session_service.ts:31](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/sessions/base_session_service.ts#L31)



Properties

appNamesessionIdstateuserId

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


