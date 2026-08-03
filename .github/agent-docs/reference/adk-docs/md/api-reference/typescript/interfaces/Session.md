[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [Session]()



# Interface Session

Represents a session in a conversation between agents and users.

interface Session {  
appName: string;  
events: [Event](Event.html)[];  
id: string;  
lastUpdateTime: number;  
state: Record<string, unknown>;  
userId: string;  
}

  * Defined in [core/src/sessions/session.ts:24](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L24)



## Properties

### appName

appName: string

The name of the app.

  * Defined in [core/src/sessions/session.ts:33](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L33)



### events

events: [Event](Event.html)[]

The events of the session, e.g. user input, model response, function call/response, etc.

  * Defined in [core/src/sessions/session.ts:49](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L49)



### id

id: string

The unique identifier of the session.

  * Defined in [core/src/sessions/session.ts:28](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L28)



### lastUpdateTime

lastUpdateTime: number

The last update time of the session.

  * Defined in [core/src/sessions/session.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L54)



### state

state: Record<string, unknown>

The state of the session.

  * Defined in [core/src/sessions/session.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L43)



### userId

userId: string

The id of the user.

  * Defined in [core/src/sessions/session.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L38)



Properties

appNameeventsidlastUpdateTimestateuserId

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


