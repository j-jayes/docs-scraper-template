[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseMemoryService]()



# Interface BaseMemoryService

Base interface for memory services.

The service provides functionalities to ingest sessions into memory so that the memory can be used for user queries.

interface BaseMemoryService {  
addSessionToMemory(session: [Session](Session.html)): Promise<void>;  
searchMemory(request: [SearchMemoryRequest](SearchMemoryRequest.html)): Promise<[SearchMemoryResponse](SearchMemoryResponse.html)>;  
}

#### Implemented by

  * [InMemoryMemoryService](../classes/InMemoryMemoryService.html)
  * [VertexAiMemoryBankService](../classes/VertexAiMemoryBankService.html)



  * Defined in [core/src/memory/base_memory_service.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/base_memory_service.ts#L44)



## Methods

### addSessionToMemory

  * addSessionToMemory(session: [Session](Session.html)): Promise<void>

Adds a session to the memory.

#### Parameters

    * session: [Session](Session.html)

The session to add to the memory.

#### Returns Promise<void>

A promise that resolves when the session is added to the memory.

    * Defined in [core/src/memory/base_memory_service.ts:51](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/base_memory_service.ts#L51)




### searchMemory

  * searchMemory(request: [SearchMemoryRequest](SearchMemoryRequest.html)): Promise<[SearchMemoryResponse](SearchMemoryResponse.html)>

Searches for sessions that match the query.

#### Parameters

    * request: [SearchMemoryRequest](SearchMemoryRequest.html)

The request to search memory.

#### Returns Promise<[SearchMemoryResponse](SearchMemoryResponse.html)>

A promise that resolves to SearchMemoryResponse containing the matching memories.

    * Defined in [core/src/memory/base_memory_service.ts:60](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/base_memory_service.ts#L60)




Methods

addSessionToMemorysearchMemory

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


