[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InMemoryMemoryService]()



# Class InMemoryMemoryService

An in-memory memory service for prototyping purpose only.

Uses keyword matching instead of semantic search.

#### Implements

  * [BaseMemoryService](../interfaces/BaseMemoryService.html)



  * Defined in [core/src/memory/in_memory_memory_service.ts:18](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/memory/in_memory_memory_service.ts#L18)



## Constructors

### constructor

  * new InMemoryMemoryService(): [InMemoryMemoryService]()

#### Returns [InMemoryMemoryService]()




## Methods

### addSessionToMemory

  * addSessionToMemory(session: [Session](../interfaces/Session.html)): Promise<void>

Adds a session to the memory.

#### Parameters

    * session: [Session](../interfaces/Session.html)

The session to add to the memory.

#### Returns Promise<void>

A promise that resolves when the session is added to the memory.

Implementation of [BaseMemoryService](../interfaces/BaseMemoryService.html).[addSessionToMemory](../interfaces/BaseMemoryService.html#addsessiontomemory)

    * Defined in [core/src/memory/in_memory_memory_service.ts:23](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/memory/in_memory_memory_service.ts#L23)




### searchMemory

  * searchMemory(req: [SearchMemoryRequest](../interfaces/SearchMemoryRequest.html)): Promise<[SearchMemoryResponse](../interfaces/SearchMemoryResponse.html)>

Searches for sessions that match the query.

#### Parameters

    * req: [SearchMemoryRequest](../interfaces/SearchMemoryRequest.html)

#### Returns Promise<[SearchMemoryResponse](../interfaces/SearchMemoryResponse.html)>

A promise that resolves to SearchMemoryResponse containing the matching memories.

Implementation of [BaseMemoryService](../interfaces/BaseMemoryService.html).[searchMemory](../interfaces/BaseMemoryService.html#searchmemory)

    * Defined in [core/src/memory/in_memory_memory_service.ts:32](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/memory/in_memory_memory_service.ts#L32)




Constructors

constructor

Methods

addSessionToMemorysearchMemory

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


