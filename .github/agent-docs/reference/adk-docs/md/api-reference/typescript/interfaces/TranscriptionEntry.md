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

  * Defined in [agents/transcription_entry.ts:12](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/transcription_entry.ts#L12)



## Properties

### data

data: Content | Blob_2

  * Defined in [agents/transcription_entry.ts:22](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/transcription_entry.ts#L22)



### `Optional`role

role?: string

The role that created this data, typically "user" or "model". For function call, this is undefined.

  * Defined in [agents/transcription_entry.ts:17](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/transcription_entry.ts#L17)



Properties

datarole

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


