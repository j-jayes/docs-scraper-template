[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LlmResponse]()



# Interface LlmResponse

LLM response class that provides the first candidate response from the model if available. Otherwise, returns error code and message.

interface LlmResponse {  
citationMetadata?: CitationMetadata;  
content?: Content;  
customMetadata?: { [key: string]: unknown };  
errorCode?: string;  
errorMessage?: string;  
finishReason?: FinishReason;  
groundingMetadata?: GroundingMetadata;  
inputTranscription?: Transcription;  
interrupted?: boolean;  
liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate;  
outputTranscription?: Transcription;  
partial?: boolean;  
turnComplete?: boolean;  
usageMetadata?: GenerateContentResponseUsageMetadata;  
}

#### Hierarchy ([View Summary](../hierarchy.html#LlmResponse))

  * LlmResponse
    * [Event](Event.html)



  * Defined in [models/llm_response.ts:22](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L22)



## Properties

### `Optional`citationMetadata

citationMetadata?: CitationMetadata

The citation metadata of the response.

  * Defined in [models/llm_response.ts:36](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L36)



### `Optional`content

content?: Content

The content of the response.

  * Defined in [models/llm_response.ts:26](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L26)



### `Optional`customMetadata

customMetadata?: { [key: string]: unknown }

The custom metadata of the LlmResponse. An optional key-value pair to label an LlmResponse. NOTE: the entire object must be JSON serializable.

  * Defined in [models/llm_response.ts:71](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L71)



### `Optional`errorCode

errorCode?: string

Error code if the response is an error. Code varies by model.

  * Defined in [models/llm_response.ts:53](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L53)



### `Optional`errorMessage

errorMessage?: string

Error message if the response is an error.

  * Defined in [models/llm_response.ts:58](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L58)



### `Optional`finishReason

finishReason?: FinishReason

The finish reason of the response.

  * Defined in [models/llm_response.ts:81](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L81)



### `Optional`groundingMetadata

groundingMetadata?: GroundingMetadata

The grounding metadata of the response.

  * Defined in [models/llm_response.ts:31](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L31)



### `Optional`inputTranscription

inputTranscription?: Transcription

Audio transcription of user input.

  * Defined in [models/llm_response.ts:91](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L91)



### `Optional`interrupted

interrupted?: boolean

Flag indicating that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

  * Defined in [models/llm_response.ts:64](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L64)



### `Optional`liveSessionResumptionUpdate

liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate

The session resumption update of the LlmResponse

  * Defined in [models/llm_response.ts:86](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L86)



### `Optional`outputTranscription

outputTranscription?: Transcription

Audio transcription of model output.

  * Defined in [models/llm_response.ts:96](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L96)



### `Optional`partial

partial?: boolean

Indicates whether the text content is part of a unfinished text stream. Only used for streaming mode and when the content is plain text.

  * Defined in [models/llm_response.ts:42](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L42)



### `Optional`turnComplete

turnComplete?: boolean

Indicates whether the response from the model is complete. Only used for streaming mode.

  * Defined in [models/llm_response.ts:48](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L48)



### `Optional`usageMetadata

usageMetadata?: GenerateContentResponseUsageMetadata

The usage metadata of the LlmResponse.

  * Defined in [models/llm_response.ts:76](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L76)



Properties

citationMetadatacontentcustomMetadataerrorCodeerrorMessagefinishReasongroundingMetadatainputTranscriptioninterruptedliveSessionResumptionUpdateoutputTranscriptionpartialturnCompleteusageMetadata

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


