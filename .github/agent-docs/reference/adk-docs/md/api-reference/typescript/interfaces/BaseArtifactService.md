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
listArtifactKeys(request: [CompositeSessionKey](CompositeSessionKey.html)): Promise<string[]>;  
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



  * Defined in [core/src/artifacts/base_artifact_service.ts:75](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L75)



## Methods

### deleteArtifact

  * deleteArtifact(request: [DeleteArtifactRequest](DeleteArtifactRequest.html)): Promise<void>

Deletes an artifact.

#### Parameters

    * request: [DeleteArtifactRequest](DeleteArtifactRequest.html)

The request to delete an artifact.

#### Returns Promise<void>

A promise that resolves when the artifact is deleted.

    * Defined in [core/src/artifacts/base_artifact_service.ts:116](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L116)




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

    * Defined in [core/src/artifacts/base_artifact_service.ts:143](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L143)




### listArtifactKeys

  * listArtifactKeys(request: [CompositeSessionKey](CompositeSessionKey.html)): Promise<string[]>

Lists all the artifact filenames within a session.

#### Parameters

    * request: [CompositeSessionKey](CompositeSessionKey.html)

The request to list artifact keys.

#### Returns Promise<string[]>

A promise that resolves to a list of all artifact filenames within a session.

    * Defined in [core/src/artifacts/base_artifact_service.ts:108](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L108)




### listArtifactVersions

  * listArtifactVersions(request: [ListVersionsRequest](ListVersionsRequest.html)): Promise<[ArtifactVersion](ArtifactVersion.html)[]>

Lists metadata for each artifact version.

#### Parameters

    * request: [ListVersionsRequest](ListVersionsRequest.html)

The request to list artifact versions.

#### Returns Promise<[ArtifactVersion](ArtifactVersion.html)[]>

A promise that resolves to a list of artifact version metadata.

    * Defined in [core/src/artifacts/base_artifact_service.ts:133](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L133)




### listVersions

  * listVersions(request: [ListVersionsRequest](ListVersionsRequest.html)): Promise<number[]>

Lists all versions of an artifact.

#### Parameters

    * request: [ListVersionsRequest](ListVersionsRequest.html)

The request to list versions.

#### Returns Promise<number[]>

A promise that resolves to a list of all available versions of the artifact.

    * Defined in [core/src/artifacts/base_artifact_service.ts:125](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L125)




### loadArtifact

  * loadArtifact(request: [LoadArtifactRequest](LoadArtifactRequest.html)): Promise<Part | undefined>

Gets an artifact from the artifact service storage.

The artifact is a file identified by the app name, user ID, session ID, and filename.

#### Parameters

    * request: [LoadArtifactRequest](LoadArtifactRequest.html)

The request to load an artifact.

#### Returns Promise<Part | undefined>

A promise that resolves to the artifact or undefined if not found.

    * Defined in [core/src/artifacts/base_artifact_service.ts:99](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L99)




### saveArtifact

  * saveArtifact(request: [SaveArtifactRequest](SaveArtifactRequest.html)): Promise<number>

Saves an artifact to the artifact service storage.

The artifact is a file identified by the app name, user ID, session ID, and filename. After saving the artifact, a revision ID is returned to identify the artifact version.

#### Parameters

    * request: [SaveArtifactRequest](SaveArtifactRequest.html)

The request to save an artifact.

#### Returns Promise<number>

A promise that resolves to The revision ID. The first version of the artifact has a revision ID of 0. This is incremented by 1 after each successful save.

    * Defined in [core/src/artifacts/base_artifact_service.ts:88](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/base_artifact_service.ts#L88)




Methods

deleteArtifactgetArtifactVersionlistArtifactKeyslistArtifactVersionslistVersionsloadArtifactsaveArtifact

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


