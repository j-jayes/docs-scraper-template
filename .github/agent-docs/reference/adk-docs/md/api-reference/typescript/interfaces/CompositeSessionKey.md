[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [CompositeSessionKey]()



# Interface CompositeSessionKey

Represents a unified composite session key grouping application, user, and session identifiers.

interface CompositeSessionKey {  
appName: string;  
sessionId: string;  
userId: string;  
}

#### Hierarchy ([View Summary](../hierarchy.html#CompositeSessionKey))

  * CompositeSessionKey
    * [DeleteArtifactRequest](DeleteArtifactRequest.html)
    * [ListVersionsRequest](ListVersionsRequest.html)
    * [LoadArtifactRequest](LoadArtifactRequest.html)
    * [SaveArtifactRequest](SaveArtifactRequest.html)
    * [GetSessionRequest](GetSessionRequest.html)



  * Defined in [core/src/sessions/session.ts:12](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L12)



## Properties

### appName

appName: string

The name of the application.

  * Defined in [core/src/sessions/session.ts:14](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L14)



### sessionId

sessionId: string

The ID of the session.

  * Defined in [core/src/sessions/session.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L18)



### userId

userId: string

The ID of the user.

  * Defined in [core/src/sessions/session.ts:16](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L16)



Properties

appNamesessionIduserId

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


