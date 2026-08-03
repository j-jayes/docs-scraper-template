[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SessionArtifactService]()



# Interface SessionArtifactService

interface SessionArtifactService {  
deleteArtifact(filename: string): Promise<void>;  
getArtifactVersion(  
request: [SessionLoadArtifactRequest](SessionLoadArtifactRequest.html),  
): Promise<[ArtifactVersion](ArtifactVersion.html) | undefined>;  
listArtifactKeys(): Promise<string[]>;  
listArtifactVersions(filename: string): Promise<[ArtifactVersion](ArtifactVersion.html)[]>;  
listVersions(filename: string): Promise<number[]>;  
loadArtifact(  
request: [SessionLoadArtifactRequest](SessionLoadArtifactRequest.html),  
): Promise<Part | undefined>;  
saveArtifact(request: [SessionSaveArtifactRequest](SessionSaveArtifactRequest.html)): Promise<number>;  
}

  * Defined in [core/src/artifacts/session_artifact_service.ts:21](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/session_artifact_service.ts#L21)



## Methods

### deleteArtifact

  * deleteArtifact(filename: string): Promise<void>

#### Parameters

    * filename: string

#### Returns Promise<void>

    * Defined in [core/src/artifacts/session_artifact_service.ts:25](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/session_artifact_service.ts#L25)




### getArtifactVersion

  * getArtifactVersion(  
request: [SessionLoadArtifactRequest](SessionLoadArtifactRequest.html),  
): Promise<[ArtifactVersion](ArtifactVersion.html) | undefined>

#### Parameters

    * request: [SessionLoadArtifactRequest](SessionLoadArtifactRequest.html)

#### Returns Promise<[ArtifactVersion](ArtifactVersion.html) | undefined>

    * Defined in [core/src/artifacts/session_artifact_service.ts:28](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/session_artifact_service.ts#L28)




### listArtifactKeys

  * listArtifactKeys(): Promise<string[]>

#### Returns Promise<string[]>

    * Defined in [core/src/artifacts/session_artifact_service.ts:24](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/session_artifact_service.ts#L24)




### listArtifactVersions

  * listArtifactVersions(filename: string): Promise<[ArtifactVersion](ArtifactVersion.html)[]>

#### Parameters

    * filename: string

#### Returns Promise<[ArtifactVersion](ArtifactVersion.html)[]>

    * Defined in [core/src/artifacts/session_artifact_service.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/session_artifact_service.ts#L27)




### listVersions

  * listVersions(filename: string): Promise<number[]>

#### Parameters

    * filename: string

#### Returns Promise<number[]>

    * Defined in [core/src/artifacts/session_artifact_service.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/session_artifact_service.ts#L26)




### loadArtifact

  * loadArtifact(request: [SessionLoadArtifactRequest](SessionLoadArtifactRequest.html)): Promise<Part | undefined>

#### Parameters

    * request: [SessionLoadArtifactRequest](SessionLoadArtifactRequest.html)

#### Returns Promise<Part | undefined>

    * Defined in [core/src/artifacts/session_artifact_service.ts:23](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/session_artifact_service.ts#L23)




### saveArtifact

  * saveArtifact(request: [SessionSaveArtifactRequest](SessionSaveArtifactRequest.html)): Promise<number>

#### Parameters

    * request: [SessionSaveArtifactRequest](SessionSaveArtifactRequest.html)

#### Returns Promise<number>

    * Defined in [core/src/artifacts/session_artifact_service.ts:22](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/artifacts/session_artifact_service.ts#L22)




Methods

deleteArtifactgetArtifactVersionlistArtifactKeyslistArtifactVersionslistVersionsloadArtifactsaveArtifact

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


