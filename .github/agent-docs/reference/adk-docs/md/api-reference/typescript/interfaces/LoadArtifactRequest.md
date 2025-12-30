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

  * Defined in [core/src/artifacts/base_artifact_service.ts:28](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L28)



## Properties

### appName

appName: string

The app name.

  * Defined in [core/src/artifacts/base_artifact_service.ts:30](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L30)



### filename

filename: string

The filename of the artifact.

  * Defined in [core/src/artifacts/base_artifact_service.ts:36](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L36)



### sessionId

sessionId: string

The session ID.

  * Defined in [core/src/artifacts/base_artifact_service.ts:34](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L34)



### userId

userId: string

The user ID.

  * Defined in [core/src/artifacts/base_artifact_service.ts:32](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L32)



### `Optional`version

version?: number

The version of the artifact to load. If not provided, the latest version of the artifact is loaded.

  * Defined in [core/src/artifacts/base_artifact_service.ts:41](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L41)



Properties

appNamefilenamesessionIduserIdversion

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


