[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [TranscriptionEntry]()



# Interface TranscriptionEntry

Store the data that can be used for transcription.

interface TranscriptionEntry {  
data: Content | Blob_2;  
role?: string;  
}

  * Defined in [core/src/agents/transcription_entry.ts:12](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/transcription_entry.ts#L12)



## Properties

### data

data: Content | Blob_2

  * Defined in [core/src/agents/transcription_entry.ts:22](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/transcription_entry.ts#L22)



### `Optional`role

role?: string

The role that created this data, typically "user" or "model". For function call, this is undefined.

  * Defined in [core/src/agents/transcription_entry.ts:17](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/transcription_entry.ts#L17)



Properties

datarole

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


