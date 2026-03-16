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



  * Defined in [memory/base_memory_service.ts:36](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/memory/base_memory_service.ts#L36)



## Methods

### addSessionToMemory

  * addSessionToMemory(session: [Session](Session.html)): Promise<void>

Adds a session to the memory.

#### Parameters

    * session: [Session](Session.html)

The session to add to the memory.

#### Returns Promise<void>

A promise that resolves when the session is added to the memory.

    * Defined in [memory/base_memory_service.ts:43](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/memory/base_memory_service.ts#L43)




### searchMemory

  * searchMemory(request: [SearchMemoryRequest](SearchMemoryRequest.html)): Promise<[SearchMemoryResponse](SearchMemoryResponse.html)>

Searches for sessions that match the query.

#### Parameters

    * request: [SearchMemoryRequest](SearchMemoryRequest.html)

The request to search memory.

#### Returns Promise<[SearchMemoryResponse](SearchMemoryResponse.html)>

A promise that resolves to SearchMemoryResponse containing the matching memories.

    * Defined in [memory/base_memory_service.ts:52](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/memory/base_memory_service.ts#L52)




Methods

addSessionToMemorysearchMemory

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


