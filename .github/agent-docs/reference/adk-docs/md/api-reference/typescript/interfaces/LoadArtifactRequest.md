[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LoadArtifactRequest]()



# Interface LoadArtifactRequest

The parameters for `loadArtifact`.

interface LoadArtifactRequest {  
appName: string;  
filename: string;  
sessionId: string;  
userId: string;  
version?: number;  
}

#### Hierarchy ([View Summary](../hierarchy.html#LoadArtifactRequest))

  * [CompositeSessionKey](CompositeSessionKey.html)
    * LoadArtifactRequest



  * Defined in [core/src/artifacts/base_artifact_service.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L27)



## Properties

### appName

appName: string

The name of the application.

Inherited from [CompositeSessionKey](CompositeSessionKey.html).[appName](CompositeSessionKey.html#appname)

  * Defined in [core/src/sessions/session.ts:14](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L14)



### filename

filename: string

The filename of the artifact.

  * Defined in [core/src/artifacts/base_artifact_service.ts:29](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L29)



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



### `Optional`version

version?: number

The version of the artifact to load. If not provided, the latest version of the artifact is loaded.

  * Defined in [core/src/artifacts/base_artifact_service.ts:34](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L34)



Properties

appNamefilenamesessionIduserIdversion

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


