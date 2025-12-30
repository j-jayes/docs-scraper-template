[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseArtifactService]()



# Interface BaseArtifactService

Interface for artifact services.

interface BaseArtifactService {  
deleteArtifact(request: [DeleteArtifactRequest](DeleteArtifactRequest.html)): Promise<void>;  
listArtifactKeys(request: [ListArtifactKeysRequest](ListArtifactKeysRequest.html)): Promise<string[]>;  
listVersions(request: [ListVersionsRequest](ListVersionsRequest.html)): Promise<number[]>;  
loadArtifact(request: [LoadArtifactRequest](LoadArtifactRequest.html)): Promise<Part | undefined>;  
saveArtifact(request: [SaveArtifactRequest](SaveArtifactRequest.html)): Promise<number>;  
}

#### Implemented by

  * [GcsArtifactService](../classes/GcsArtifactService.html)
  * [InMemoryArtifactService](../classes/InMemoryArtifactService.html)



  * Defined in [core/src/artifacts/base_artifact_service.ts:87](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L87)



## Methods

### deleteArtifact

  * deleteArtifact(request: [DeleteArtifactRequest](DeleteArtifactRequest.html)): Promise<void>

Deletes an artifact.

#### Parameters

    * request: [DeleteArtifactRequest](DeleteArtifactRequest.html)

The request to delete an artifact.

#### Returns Promise<void>

A promise that resolves when the artifact is deleted.

    * Defined in [core/src/artifacts/base_artifact_service.ts:128](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L128)




### listArtifactKeys

  * listArtifactKeys(request: [ListArtifactKeysRequest](ListArtifactKeysRequest.html)): Promise<string[]>

Lists all the artifact filenames within a session.

#### Parameters

    * request: [ListArtifactKeysRequest](ListArtifactKeysRequest.html)

The request to list artifact keys.

#### Returns Promise<string[]>

A promise that resolves to a list of all artifact filenames within a session.

    * Defined in [core/src/artifacts/base_artifact_service.ts:120](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L120)




### listVersions

  * listVersions(request: [ListVersionsRequest](ListVersionsRequest.html)): Promise<number[]>

Lists all versions of an artifact.

#### Parameters

    * request: [ListVersionsRequest](ListVersionsRequest.html)

The request to list versions.

#### Returns Promise<number[]>

A promise that resolves to a list of all available versions of the artifact.

    * Defined in [core/src/artifacts/base_artifact_service.ts:137](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L137)




### loadArtifact

  * loadArtifact(request: [LoadArtifactRequest](LoadArtifactRequest.html)): Promise<Part | undefined>

Gets an artifact from the artifact service storage.

The artifact is a file identified by the app name, user ID, session ID, and filename.

#### Parameters

    * request: [LoadArtifactRequest](LoadArtifactRequest.html)

The request to load an artifact.

#### Returns Promise<Part | undefined>

A promise that resolves to the artifact or undefined if not found.

    * Defined in [core/src/artifacts/base_artifact_service.ts:111](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L111)




### saveArtifact

  * saveArtifact(request: [SaveArtifactRequest](SaveArtifactRequest.html)): Promise<number>

Saves an artifact to the artifact service storage.

The artifact is a file identified by the app name, user ID, session ID, and filename. After saving the artifact, a revision ID is returned to identify the artifact version.

#### Parameters

    * request: [SaveArtifactRequest](SaveArtifactRequest.html)

The request to save an artifact.

#### Returns Promise<number>

A promise that resolves to The revision ID. The first version of the artifact has a revision ID of 0. This is incremented by 1 after each successful save.

    * Defined in [core/src/artifacts/base_artifact_service.ts:100](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/base_artifact_service.ts#L100)




Methods

deleteArtifactlistArtifactKeyslistVersionsloadArtifactsaveArtifact

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


