[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InMemoryArtifactService]()



# Class InMemoryArtifactService

An in-memory implementation of the ArtifactService.

#### Implements

  * [BaseArtifactService](../interfaces/BaseArtifactService.html)



  * Defined in [artifacts/in_memory_artifact_service.ts:26](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/in_memory_artifact_service.ts#L26)



## Constructors

### constructor

  * new InMemoryArtifactService(): [InMemoryArtifactService]()

#### Returns [InMemoryArtifactService]()




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

    * Defined in [artifacts/in_memory_artifact_service.ts:105](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/in_memory_artifact_service.ts#L105)




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

    * Defined in [artifacts/in_memory_artifact_service.ts:157](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/in_memory_artifact_service.ts#L157)




### listArtifactKeys

  * listArtifactKeys(request: [ListArtifactKeysRequest](../interfaces/ListArtifactKeysRequest.html)): Promise<string[]>

Lists all the artifact filenames within a session.

#### Parameters

    * request: [ListArtifactKeysRequest](../interfaces/ListArtifactKeysRequest.html)

The request to list artifact keys.

#### Returns Promise<string[]>

A promise that resolves to a list of all artifact filenames within a session.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listArtifactKeys](../interfaces/BaseArtifactService.html#listartifactkeys)

    * Defined in [artifacts/in_memory_artifact_service.ts:83](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/in_memory_artifact_service.ts#L83)




### listArtifactVersions

  * listArtifactVersions(request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)): Promise<[ArtifactVersion](../interfaces/ArtifactVersion.html)[]>

Lists metadata for each artifact version.

#### Parameters

    * request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)

The request to list artifact versions.

#### Returns Promise<[ArtifactVersion](../interfaces/ArtifactVersion.html)[]>

A promise that resolves to a list of artifact version metadata.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listArtifactVersions](../interfaces/BaseArtifactService.html#listartifactversions)

    * Defined in [artifacts/in_memory_artifact_service.ts:141](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/in_memory_artifact_service.ts#L141)




### listVersions

  * listVersions(request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)): Promise<number[]>

Lists all versions of an artifact.

#### Parameters

    * request: [ListVersionsRequest](../interfaces/ListVersionsRequest.html)

The request to list versions.

#### Returns Promise<number[]>

A promise that resolves to a list of all available versions of the artifact.

Implementation of [BaseArtifactService](../interfaces/BaseArtifactService.html).[listVersions](../interfaces/BaseArtifactService.html#listversions)

    * Defined in [artifacts/in_memory_artifact_service.ts:120](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/in_memory_artifact_service.ts#L120)




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

    * Defined in [artifacts/in_memory_artifact_service.ts:62](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/in_memory_artifact_service.ts#L62)




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

    * Defined in [artifacts/in_memory_artifact_service.ts:32](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/artifacts/in_memory_artifact_service.ts#L32)




Constructors

constructor

Methods

deleteArtifactgetArtifactVersionlistArtifactKeyslistArtifactVersionslistVersionsloadArtifactsaveArtifact

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


