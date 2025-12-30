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

  * Defined in [core/src/sessions/session.ts:12](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/session.ts#L12)



## Properties

### appName

appName: string

The name of the app.

  * Defined in [core/src/sessions/session.ts:21](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/session.ts#L21)



### events

events: [Event](Event.html)[]

The events of the session, e.g. user input, model response, function call/response, etc.

  * Defined in [core/src/sessions/session.ts:37](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/session.ts#L37)



### id

id: string

The unique identifier of the session.

  * Defined in [core/src/sessions/session.ts:16](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/session.ts#L16)



### lastUpdateTime

lastUpdateTime: number

The last update time of the session.

  * Defined in [core/src/sessions/session.ts:42](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/session.ts#L42)



### state

state: Record<string, unknown>

The state of the session.

  * Defined in [core/src/sessions/session.ts:31](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/session.ts#L31)



### userId

userId: string

The id of the user.

  * Defined in [core/src/sessions/session.ts:26](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/sessions/session.ts#L26)



Properties

appNameeventsidlastUpdateTimestateuserId

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


