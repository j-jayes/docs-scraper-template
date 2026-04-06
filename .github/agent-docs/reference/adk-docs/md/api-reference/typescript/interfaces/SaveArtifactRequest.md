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

  * Defined in [artifacts/base_artifact_service.ts:12](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L12)



## Properties

### appName

appName: string

The app name.

  * Defined in [artifacts/base_artifact_service.ts:14](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L14)



### artifact

artifact: Part

The artifact to save.

  * Defined in [artifacts/base_artifact_service.ts:22](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L22)



### `Optional`customMetadata

customMetadata?: Record<string, unknown>

Optional custom metadata to save with the artifact.

  * Defined in [artifacts/base_artifact_service.ts:26](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L26)



### filename

filename: string

The filename of the artifact.

  * Defined in [artifacts/base_artifact_service.ts:20](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L20)



### sessionId

sessionId: string

The session ID.

  * Defined in [artifacts/base_artifact_service.ts:18](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L18)



### userId

userId: string

The user ID.

  * Defined in [artifacts/base_artifact_service.ts:16](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L16)



Properties

appNameartifactcustomMetadatafilenamesessionIduserId

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


