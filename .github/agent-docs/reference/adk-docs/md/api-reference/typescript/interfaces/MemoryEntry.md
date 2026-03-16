[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [MemoryEntry]()



# Interface MemoryEntry

Represents one memory entry.

interface MemoryEntry {  
author?: string;  
content: Content;  
timestamp?: string;  
}

  * Defined in [memory/memory_entry.ts:12](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/memory/memory_entry.ts#L12)



## Properties

### `Optional`author

author?: string

The author of the memory.

  * Defined in [memory/memory_entry.ts:21](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/memory/memory_entry.ts#L21)



### content

content: Content

The content of the memory entry.

  * Defined in [memory/memory_entry.ts:16](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/memory/memory_entry.ts#L16)



### `Optional`timestamp

timestamp?: string

The timestamp when the original content of this memory happened. This string will be forwarded to LLM. Preferred format is ISO 8601 format.

  * Defined in [memory/memory_entry.ts:27](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/memory/memory_entry.ts#L27)



Properties

authorcontenttimestamp

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


