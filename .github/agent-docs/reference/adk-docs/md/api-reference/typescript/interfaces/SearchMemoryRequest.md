[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SearchMemoryRequest]()



# Interface SearchMemoryRequest

The parameters for `searchMemory`.

interface SearchMemoryRequest {  
appName: string;  
query: string;  
userId: string;  
}

  * Defined in [core/src/memory/base_memory_service.ts:24](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/base_memory_service.ts#L24)



## Properties

### appName

appName: string

The app name associated with the memory to search.

  * Defined in [core/src/memory/base_memory_service.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/base_memory_service.ts#L26)



### query

query: string

The natural language query used to retrieve relevant memories. Implementations may use keyword matching or semantic search.

  * Defined in [core/src/memory/base_memory_service.ts:35](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/base_memory_service.ts#L35)



### userId

userId: string

The user ID whose memory is being searched.

  * Defined in [core/src/memory/base_memory_service.ts:29](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/base_memory_service.ts#L29)



Properties

appNamequeryuserId

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


