[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SaveArtifactRequest]()



# Interface SaveArtifactRequest

The parameters for `saveArtifact`.

interface SaveArtifactRequest {  
appName: string;  
artifact: Part;  
customMetadata?: Record<string, unknown>;  
filename: string;  
sessionId: string;  
userId: string;  
}

#### Hierarchy ([View Summary](../hierarchy.html#SaveArtifactRequest))

  * [CompositeSessionKey](CompositeSessionKey.html)
    * SaveArtifactRequest



  * Defined in [core/src/artifacts/base_artifact_service.ts:13](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L13)



## Properties

### appName

appName: string

The name of the application.

Inherited from [CompositeSessionKey](CompositeSessionKey.html).[appName](CompositeSessionKey.html#appname)

  * Defined in [core/src/sessions/session.ts:14](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/sessions/session.ts#L14)



### artifact

artifact: Part

The artifact to save.

  * Defined in [core/src/artifacts/base_artifact_service.ts:17](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L17)



### `Optional`customMetadata

customMetadata?: Record<string, unknown>

Optional custom metadata to save with the artifact.

  * Defined in [core/src/artifacts/base_artifact_service.ts:21](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L21)



### filename

filename: string

The filename of the artifact.

  * Defined in [core/src/artifacts/base_artifact_service.ts:15](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L15)



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

appNameartifactcustomMetadatafilenamesessionIduserId

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


