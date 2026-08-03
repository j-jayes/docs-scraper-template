[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [MemoryEntry]()



# Interface MemoryEntry

Represents one memory entry retrieved from a memory service.

Memory entries are created from session events and surfaced to the agent to provide relevant context from past interactions.

interface MemoryEntry {  
author?: string;  
content: Content;  
timestamp?: string;  
}

  * Defined in [core/src/memory/memory_entry.ts:15](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/memory_entry.ts#L15)



## Properties

### `Optional`author

author?: string

The author of the memory. Common values are `'user'` and `'model'`, but this can also be the name of an agent when the content was produced by a named sub-agent.

  * Defined in [core/src/memory/memory_entry.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/memory_entry.ts#L26)



### content

content: Content

The content of the memory entry, as originally produced during a session.

  * Defined in [core/src/memory/memory_entry.ts:19](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/memory_entry.ts#L19)



### `Optional`timestamp

timestamp?: string

The time when the original content was produced. Forwarded to the LLM as part of the memory context. Preferred format is ISO 8601 (e.g. `'2024-01-15T10:30:00.000Z'`).

  * Defined in [core/src/memory/memory_entry.ts:33](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/memory/memory_entry.ts#L33)



Properties

authorcontenttimestamp

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


