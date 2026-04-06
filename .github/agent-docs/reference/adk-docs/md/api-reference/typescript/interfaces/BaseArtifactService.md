[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseArtifactService]()



# Interface BaseArtifactService

Interface for artifact services.

interface BaseArtifactService {  
deleteArtifact(request: [DeleteArtifactRequest](DeleteArtifactRequest.html)): Promise<void>;  
getArtifactVersion(  
request: [LoadArtifactRequest](LoadArtifactRequest.html),  
): Promise<[ArtifactVersion](ArtifactVersion.html) | undefined>;  
listArtifactKeys(request: [ListArtifactKeysRequest](ListArtifactKeysRequest.html)): Promise<string[]>;  
listArtifactVersions(  
request: [ListVersionsRequest](ListVersionsRequest.html),  
): Promise<[ArtifactVersion](ArtifactVersion.html)[]>;  
listVersions(request: [ListVersionsRequest](ListVersionsRequest.html)): Promise<number[]>;  
loadArtifact(request: [LoadArtifactRequest](LoadArtifactRequest.html)): Promise<Part | undefined>;  
saveArtifact(request: [SaveArtifactRequest](SaveArtifactRequest.html)): Promise<number>;  
}

#### Implemented by

  * [FileArtifactService](../classes/FileArtifactService.html)
  * [GcsArtifactService](../classes/GcsArtifactService.html)
  * [InMemoryArtifactService](../classes/InMemoryArtifactService.html)



  * Defined in [artifacts/base_artifact_service.ts:105](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L105)



## Methods

### deleteArtifact

  * deleteArtifact(request: [DeleteArtifactRequest](DeleteArtifactRequest.html)): Promise<void>

Deletes an artifact.

#### Parameters

    * request: [DeleteArtifactRequest](DeleteArtifactRequest.html)

The request to delete an artifact.

#### Returns Promise<void>

A promise that resolves when the artifact is deleted.

    * Defined in [artifacts/base_artifact_service.ts:146](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L146)




### getArtifactVersion

  * getArtifactVersion(  
request: [LoadArtifactRequest](LoadArtifactRequest.html),  
): Promise<[ArtifactVersion](ArtifactVersion.html) | undefined>

Gets metadata for a specific artifact version.

#### Parameters

    * request: [LoadArtifactRequest](LoadArtifactRequest.html)

The request to get an artifact version.

#### Returns Promise<[ArtifactVersion](ArtifactVersion.html) | undefined>

A promise that resolves to the artifact version metadata or undefined.

    * Defined in [artifacts/base_artifact_service.ts:173](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L173)




### listArtifactKeys

  * listArtifactKeys(request: [ListArtifactKeysRequest](ListArtifactKeysRequest.html)): Promise<string[]>

Lists all the artifact filenames within a session.

#### Parameters

    * request: [ListArtifactKeysRequest](ListArtifactKeysRequest.html)

The request to list artifact keys.

#### Returns Promise<string[]>

A promise that resolves to a list of all artifact filenames within a session.

    * Defined in [artifacts/base_artifact_service.ts:138](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L138)




### listArtifactVersions

  * listArtifactVersions(request: [ListVersionsRequest](ListVersionsRequest.html)): Promise<[ArtifactVersion](ArtifactVersion.html)[]>

Lists metadata for each artifact version.

#### Parameters

    * request: [ListVersionsRequest](ListVersionsRequest.html)

The request to list artifact versions.

#### Returns Promise<[ArtifactVersion](ArtifactVersion.html)[]>

A promise that resolves to a list of artifact version metadata.

    * Defined in [artifacts/base_artifact_service.ts:163](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L163)




### listVersions

  * listVersions(request: [ListVersionsRequest](ListVersionsRequest.html)): Promise<number[]>

Lists all versions of an artifact.

#### Parameters

    * request: [ListVersionsRequest](ListVersionsRequest.html)

The request to list versions.

#### Returns Promise<number[]>

A promise that resolves to a list of all available versions of the artifact.

    * Defined in [artifacts/base_artifact_service.ts:155](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L155)




### loadArtifact

  * loadArtifact(request: [LoadArtifactRequest](LoadArtifactRequest.html)): Promise<Part | undefined>

Gets an artifact from the artifact service storage.

The artifact is a file identified by the app name, user ID, session ID, and filename.

#### Parameters

    * request: [LoadArtifactRequest](LoadArtifactRequest.html)

The request to load an artifact.

#### Returns Promise<Part | undefined>

A promise that resolves to the artifact or undefined if not found.

    * Defined in [artifacts/base_artifact_service.ts:129](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L129)




### saveArtifact

  * saveArtifact(request: [SaveArtifactRequest](SaveArtifactRequest.html)): Promise<number>

Saves an artifact to the artifact service storage.

The artifact is a file identified by the app name, user ID, session ID, and filename. After saving the artifact, a revision ID is returned to identify the artifact version.

#### Parameters

    * request: [SaveArtifactRequest](SaveArtifactRequest.html)

The request to save an artifact.

#### Returns Promise<number>

A promise that resolves to The revision ID. The first version of the artifact has a revision ID of 0. This is incremented by 1 after each successful save.

    * Defined in [artifacts/base_artifact_service.ts:118](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/base_artifact_service.ts#L118)




Methods

deleteArtifactgetArtifactVersionlistArtifactKeyslistArtifactVersionslistVersionsloadArtifactsaveArtifact

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


