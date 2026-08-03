[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [GetSessionRequest]()



# Interface GetSessionRequest

The parameters for `getSession`.

interface GetSessionRequest {  
appName: string;  
config?: [GetSessionConfig](GetSessionConfig.html);  
sessionId: string;  
userId: string;  
}

#### Hierarchy ([View Summary](../hierarchy.html#GetSessionRequest))

  * [CompositeSessionKey](CompositeSessionKey.html)
    * GetSessionRequest



  * Defined in [core/src/sessions/base_session_service.ts:41](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L41)



## Properties

### appName

appName: string

The name of the application.

Inherited from [CompositeSessionKey](CompositeSessionKey.html).[appName](CompositeSessionKey.html#appname)

  * Defined in [core/src/sessions/session.ts:14](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L14)



### `Optional`config

config?: [GetSessionConfig](GetSessionConfig.html)

The configurations for getting the session.

  * Defined in [core/src/sessions/base_session_service.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/base_session_service.ts#L43)



### sessionId

sessionId: string

The ID of the session.

Inherited from [CompositeSessionKey](CompositeSessionKey.html).[sessionId](CompositeSessionKey.html#sessionid)

  * Defined in [core/src/sessions/session.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L18)



### userId

userId: string

The ID of the user.

Inherited from [CompositeSessionKey](CompositeSessionKey.html).[userId](CompositeSessionKey.html#userid)

  * Defined in [core/src/sessions/session.ts:16](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L16)



Properties

appNameconfigsessionIduserId

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


