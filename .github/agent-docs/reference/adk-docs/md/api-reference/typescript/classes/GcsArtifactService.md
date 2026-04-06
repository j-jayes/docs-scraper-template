[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [GcsArtifactService]()



# Class GcsArtifactService

Interface for artifact services.

#### Implements

  * [BaseArtifactService](../interfaces/BaseArtifactService.html)



  * Defined in [artifacts/gcs_artifact_service.ts:21](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/gcs_artifact_service.ts#L21)



## Constructors

### constructor

  * new GcsArtifactService(bucket: string): [GcsArtifactService]()

#### Parameters

    * bucket: string

#### Returns [GcsArtifactService]()

    * Defined in [artifacts/gcs_artifact_service.ts:24](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/gcs_artifact_service.ts#L24)




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

    * Defined in [artifacts/gcs_artifact_service.ts:119](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/gcs_artifact_service.ts#L119)




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

    * Defined in [artifacts/gcs_artifact_service.ts:175](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/gcs_artifact_service.ts#L175)




### listArtifactKeys

  * listArtifactKeys(request: [ListArtifactKeysRequest](../interfaces/ListArtifactKeysRequest.html)): Promise<string[]>

Lists all the artifact filenames within a session.

#### Parameters

    * request: [ListArtifactKeysRequest](../interfaces/ListArtifactKeysRequest.html)

The request to list artifact keys.

#### Returns Promise<string[]>

A promise that resolves to a list of all artifact filenames within a session.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listArtifactKeys](../interfaces/BaseArtifactService.html#listartifactkeys)

    * Defined in [artifacts/gcs_artifact_service.ts:105](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/gcs_artifact_service.ts#L105)




### listArtifactVersions

  * listArtifactVersions(request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)): Promise<[ArtifactVersion](../interfaces/ArtifactVersion.html)[]>

Lists metadata for each artifact version.

#### Parameters

    * request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)

The request to list artifact versions.

#### Returns Promise<[ArtifactVersion](../interfaces/ArtifactVersion.html)[]>

A promise that resolves to a list of artifact version metadata.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listArtifactVersions](../interfaces/BaseArtifactService.html#listartifactversions)

    * Defined in [artifacts/gcs_artifact_service.ts:155](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/gcs_artifact_service.ts#L155)




### listVersions

  * listVersions(request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)): Promise<number[]>

Lists all versions of an artifact.

#### Parameters

    * request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)

The request to list versions.

#### Returns Promise<number[]>

A promise that resolves to a list of all available versions of the artifact.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listVersions](../interfaces/BaseArtifactService.html#listversions)

    * Defined in [artifacts/gcs_artifact_service.ts:138](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/gcs_artifact_service.ts#L138)




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

    * Defined in [artifacts/gcs_artifact_service.ts:64](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/gcs_artifact_service.ts#L64)




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

    * Defined in [artifacts/gcs_artifact_service.ts:28](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/gcs_artifact_service.ts#L28)




Constructors

constructor

Methods

deleteArtifactgetArtifactVersionlistArtifactKeyslistArtifactVersionslistVersionsloadArtifactsaveArtifact

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


