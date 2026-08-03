[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [VertexAiMemoryBankService]()



# Class VertexAiMemoryBankService

Implementation of the BaseMemoryService using Vertex AI Memory Bank.

#### Implements

  * [BaseMemoryService](../interfaces/BaseMemoryService.html)



  * Defined in [core/src/memory/vertex_ai_memory_bank_service.ts:112](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/vertex_ai_memory_bank_service.ts#L112)



## Constructors

### constructor

  * new VertexAiMemoryBankService(  
options: [VertexAiMemoryBankServiceOptions](../interfaces/VertexAiMemoryBankServiceOptions.html),  
): [VertexAiMemoryBankService]()

#### Parameters

    * options: [VertexAiMemoryBankServiceOptions](../interfaces/VertexAiMemoryBankServiceOptions.html)

#### Returns [VertexAiMemoryBankService]()

    * Defined in [core/src/memory/vertex_ai_memory_bank_service.ts:119](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/vertex_ai_memory_bank_service.ts#L119)




## Methods

### addEventsToMemory

  * addEventsToMemory(  
request: {  
appName: string;  
customMetadata?: Record<string, unknown>;  
events: [Event](../interfaces/Event.html)[];  
sessionId?: string;  
userId: string;  
},  
): Promise<void>

Adds events to Vertex AI Memory Bank via memories.generate.

#### Parameters

    * request: {  
appName: string;  
customMetadata?: Record<string, unknown>;  
events: [Event](../interfaces/Event.html)[];  
sessionId?: string;  
userId: string;  
}

#### Returns Promise<void>

    * Defined in [core/src/memory/vertex_ai_memory_bank_service.ts:165](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/vertex_ai_memory_bank_service.ts#L165)




### addMemory

  * addMemory(  
request: {  
appName: string;  
customMetadata?: Record<string, unknown>;  
memories: [MemoryEntry](../interfaces/MemoryEntry.html)[];  
userId: string;  
},  
): Promise<void>

Adds explicit memory items using Vertex Memory Bank.

#### Parameters

    * request: {  
appName: string;  
customMetadata?: Record<string, unknown>;  
memories: [MemoryEntry](../interfaces/MemoryEntry.html)[];  
userId: string;  
}

#### Returns Promise<void>

    * Defined in [core/src/memory/vertex_ai_memory_bank_service.ts:183](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/vertex_ai_memory_bank_service.ts#L183)




### addSessionToMemory

  * addSessionToMemory(session: [Session](../interfaces/Session.html)): Promise<void>

Adds a session to the memory.

#### Parameters

    * session: [Session](../interfaces/Session.html)

The session to add to the memory.

#### Returns Promise<void>

A promise that resolves when the session is added to the memory.

Implementation of [BaseMemoryService](../interfaces/BaseMemoryService.html).[addSessionToMemory](../interfaces/BaseMemoryService.html#addsessiontomemory)

    * Defined in [core/src/memory/vertex_ai_memory_bank_service.ts:154](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/vertex_ai_memory_bank_service.ts#L154)




### searchMemory

  * searchMemory(request: [SearchMemoryRequest](../interfaces/SearchMemoryRequest.html)): Promise<[SearchMemoryResponse](../interfaces/SearchMemoryResponse.html)>

Searches for sessions that match the query.

#### Parameters

    * request: [SearchMemoryRequest](../interfaces/SearchMemoryRequest.html)

The request to search memory.

#### Returns Promise<[SearchMemoryResponse](../interfaces/SearchMemoryResponse.html)>

A promise that resolves to SearchMemoryResponse containing the matching memories.

Implementation of [BaseMemoryService](../interfaces/BaseMemoryService.html).[searchMemory](../interfaces/BaseMemoryService.html#searchmemory)

    * Defined in [core/src/memory/vertex_ai_memory_bank_service.ts:196](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/vertex_ai_memory_bank_service.ts#L196)




Constructors

constructor

Methods

addEventsToMemoryaddMemoryaddSessionToMemorysearchMemory

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


