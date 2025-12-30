[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [GcsArtifactService]()



# Class GcsArtifactService

Interface for artifact services.

#### Implements

  * [BaseArtifactService](../interfaces/BaseArtifactService.html)



  * Defined in [core/src/artifacts/gcs_artifact_service.ts:12](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/gcs_artifact_service.ts#L12)



## Constructors

### constructor

  * new GcsArtifactService(bucket: string): [GcsArtifactService]()

#### Parameters

    * bucket: string

#### Returns [GcsArtifactService]()

    * Defined in [core/src/artifacts/gcs_artifact_service.ts:15](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/gcs_artifact_service.ts#L15)




## Methods

### deleteArtifact

  * deleteArtifact(request: [DeleteArtifactRequest](../interfaces/DeleteArtifactRequest.html)): Promise<void>

Deletes an artifact.

#### Parameters

    * request: [DeleteArtifactRequest](../interfaces/DeleteArtifactRequest.html)

The request to delete an artifact.

#### Returns Promise<void>

A promise that resolves when the artifact is deleted.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[deleteArtifact](../interfaces/BaseArtifactService.html#deleteartifact)

    * Defined in [core/src/artifacts/gcs_artifact_service.ts:97](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/gcs_artifact_service.ts#L97)




### listArtifactKeys

  * listArtifactKeys(request: [ListArtifactKeysRequest](../interfaces/ListArtifactKeysRequest.html)): Promise<string[]>

Lists all the artifact filenames within a session.

#### Parameters

    * request: [ListArtifactKeysRequest](../interfaces/ListArtifactKeysRequest.html)

The request to list artifact keys.

#### Returns Promise<string[]>

A promise that resolves to a list of all artifact filenames within a session.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listArtifactKeys](../interfaces/BaseArtifactService.html#listartifactkeys)

    * Defined in [core/src/artifacts/gcs_artifact_service.ts:73](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/gcs_artifact_service.ts#L73)




### listVersions

  * listVersions(request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)): Promise<number[]>

Lists all versions of an artifact.

#### Parameters

    * request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)

The request to list versions.

#### Returns Promise<number[]>

A promise that resolves to a list of all available versions of the artifact.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listVersions](../interfaces/BaseArtifactService.html#listversions)

    * Defined in [core/src/artifacts/gcs_artifact_service.ts:112](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/gcs_artifact_service.ts#L112)




### loadArtifact

  * loadArtifact(request: [LoadArtifactRequest](../interfaces/LoadArtifactRequest.html)): Promise<Part | undefined>

Gets an artifact from the artifact service storage.

The artifact is a file identified by the app name, user ID, session ID, and filename.

#### Parameters

    * request: [LoadArtifactRequest](../interfaces/LoadArtifactRequest.html)

The request to load an artifact.

#### Returns Promise<Part | undefined>

A promise that resolves to the artifact or undefined if not found.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[loadArtifact](../interfaces/BaseArtifactService.html#loadartifact)

    * Defined in [core/src/artifacts/gcs_artifact_service.ts:46](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/gcs_artifact_service.ts#L46)




### saveArtifact

  * saveArtifact(request: [SaveArtifactRequest](../interfaces/SaveArtifactRequest.html)): Promise<number>

Saves an artifact to the artifact service storage.

The artifact is a file identified by the app name, user ID, session ID, and filename. After saving the artifact, a revision ID is returned to identify the artifact version.

#### Parameters

    * request: [SaveArtifactRequest](../interfaces/SaveArtifactRequest.html)

The request to save an artifact.

#### Returns Promise<number>

A promise that resolves to The revision ID. The first version of the artifact has a revision ID of 0. This is incremented by 1 after each successful save.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[saveArtifact](../interfaces/BaseArtifactService.html#saveartifact)

    * Defined in [core/src/artifacts/gcs_artifact_service.ts:19](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/artifacts/gcs_artifact_service.ts#L19)




Constructors

constructor

Methods

deleteArtifactlistArtifactKeyslistVersionsloadArtifactsaveArtifact

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


