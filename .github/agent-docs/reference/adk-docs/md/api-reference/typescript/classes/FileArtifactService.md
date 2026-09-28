[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [FileArtifactService]()



# Class FileArtifactService

Service for managing artifacts stored on the local filesystem.

Stores filesystem-backed artifacts beneath a configurable root directory.

Storage layout matches the cloud and in-memory services: root/ └── users/ └── {userId}/ ├── sessions/ │ └── {sessionId}/ │ └── artifacts/ │ └── {artifactPath}/ // derived from filename │ └── versions/ │ └── {version}/ │ ├── {originalFilename} │ └── metadata.json └── artifacts/ └── {artifactPath}/...

Artifact paths are derived from the provided filenames: separators create nested directories, and path traversal is rejected to keep the layout portable across filesystems. `{artifactPath}` therefore mirrors the sanitized, scope-relative path derived from each filename.

#### Implements

  * [BaseArtifactService](../interfaces/BaseArtifactService.html)



  * Defined in [core/src/artifacts/file_artifact_service.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/file_artifact_service.ts#L59)



## Constructors

### constructor

  * new FileArtifactService(rootDirOrUri: string): [FileArtifactService]()

#### Parameters

    * rootDirOrUri: string

#### Returns [FileArtifactService]()

    * Defined in [core/src/artifacts/file_artifact_service.ts:62](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/file_artifact_service.ts#L62)




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

    * Defined in [core/src/artifacts/file_artifact_service.ts:282](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/file_artifact_service.ts#L282)




### getArtifactVersion

  * getArtifactVersion(  
request: [LoadArtifactRequest](../interfaces/LoadArtifactRequest.html),  
): Promise<[ArtifactVersion](../interfaces/ArtifactVersion.html) | undefined>

Gets metadata for a specific artifact version.

#### Parameters

    * request: [LoadArtifactRequest](../interfaces/LoadArtifactRequest.html)

The request to get an artifact version.

#### Returns Promise<[ArtifactVersion](../interfaces/ArtifactVersion.html) | undefined>

A promise that resolves to the artifact version metadata or undefined.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[getArtifactVersion](../interfaces/BaseArtifactService.html#getartifactversion)

    * Defined in [core/src/artifacts/file_artifact_service.ts:366](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/file_artifact_service.ts#L366)




### listArtifactKeys

  * listArtifactKeys(request: [CompositeSessionKey](../interfaces/CompositeSessionKey.html)): Promise<string[]>

Lists all the artifact filenames within a session.

#### Parameters

    * request: [CompositeSessionKey](../interfaces/CompositeSessionKey.html)

The request to list artifact keys.

#### Returns Promise<string[]>

A promise that resolves to a list of all artifact filenames within a session.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listArtifactKeys](../interfaces/BaseArtifactService.html#listartifactkeys)

    * Defined in [core/src/artifacts/file_artifact_service.ts:248](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/file_artifact_service.ts#L248)




### listArtifactVersions

  * listArtifactVersions(request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)): Promise<[ArtifactVersion](../interfaces/ArtifactVersion.html)[]>

Lists metadata for each artifact version.

#### Parameters

    * request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)

The request to list artifact versions.

#### Returns Promise<[ArtifactVersion](../interfaces/ArtifactVersion.html)[]>

A promise that resolves to a list of artifact version metadata.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listArtifactVersions](../interfaces/BaseArtifactService.html#listartifactversions)

    * Defined in [core/src/artifacts/file_artifact_service.ts:325](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/file_artifact_service.ts#L325)




### listVersions

  * listVersions(request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)): Promise<number[]>

Lists all versions of an artifact.

#### Parameters

    * request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)

The request to list versions.

#### Returns Promise<number[]>

A promise that resolves to a list of all available versions of the artifact.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listVersions](../interfaces/BaseArtifactService.html#listversions)

    * Defined in [core/src/artifacts/file_artifact_service.ts:303](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/file_artifact_service.ts#L303)




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

    * Defined in [core/src/artifacts/file_artifact_service.ts:141](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/file_artifact_service.ts#L141)




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

    * Defined in [core/src/artifacts/file_artifact_service.ts:73](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/file_artifact_service.ts#L73)




Constructors

constructor

Methods

deleteArtifactgetArtifactVersionlistArtifactKeyslistArtifactVersionslistVersionsloadArtifactsaveArtifact

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


