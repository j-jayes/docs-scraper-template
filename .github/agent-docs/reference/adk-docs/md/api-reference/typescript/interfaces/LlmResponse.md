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
goAway?: LiveServerGoAway;  
groundingMetadata?: GroundingMetadata;  
inputTranscription?: Transcription;  
interactionId?: string;  
interrupted?: boolean;  
liveSessionId?: string;  
liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate;  
modelVersion?: string;  
outputTranscription?: Transcription;  
partial?: boolean;  
turnComplete?: boolean;  
usageMetadata?: GenerateContentResponseUsageMetadata;  
}

#### Hierarchy ([View Summary](../hierarchy.html#LlmResponse))

  * LlmResponse
    * [Event](Event.html)



  * Defined in [core/src/models/llm_response.ts:23](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L23)



## Properties

### `Optional`citationMetadata

citationMetadata?: CitationMetadata

The citation metadata of the response.

  * Defined in [core/src/models/llm_response.ts:37](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L37)



### `Optional`content

content?: Content

The content of the response.

  * Defined in [core/src/models/llm_response.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L27)



### `Optional`customMetadata

customMetadata?: { [key: string]: unknown }

The custom metadata of the LlmResponse. An optional key-value pair to label an LlmResponse. NOTE: the entire object must be JSON serializable.

  * Defined in [core/src/models/llm_response.ts:72](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L72)



### `Optional`errorCode

errorCode?: string

Error code if the response is an error. Code varies by model.

  * Defined in [core/src/models/llm_response.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L54)



### `Optional`errorMessage

errorMessage?: string

Error message if the response is an error.

  * Defined in [core/src/models/llm_response.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L59)



### `Optional`finishReason

finishReason?: FinishReason

The finish reason of the response.

  * Defined in [core/src/models/llm_response.ts:82](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L82)



### `Optional`goAway

goAway?: LiveServerGoAway

Server-side signal that the live connection will be closed soon. The caller should reconnect using the latest session resumption handle.

  * Defined in [core/src/models/llm_response.ts:93](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L93)



### `Optional`groundingMetadata

groundingMetadata?: GroundingMetadata

The grounding metadata of the response.

  * Defined in [core/src/models/llm_response.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L32)



### `Optional`inputTranscription

inputTranscription?: Transcription

Audio transcription of user input.

  * Defined in [core/src/models/llm_response.ts:98](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L98)



### `Optional`interactionId

interactionId?: string

The interaction ID returned by the model, if any.

  * Defined in [core/src/models/llm_response.ts:108](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L108)



### `Optional`interrupted

interrupted?: boolean

Flag indicating that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

  * Defined in [core/src/models/llm_response.ts:65](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L65)



### `Optional`liveSessionId

liveSessionId?: string

The session ID of the Live session.

  * Defined in [core/src/models/llm_response.ts:114](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L114)



### `Optional`liveSessionResumptionUpdate

liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate

The session resumption update of the LlmResponse

  * Defined in [core/src/models/llm_response.ts:87](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L87)



### `Optional`modelVersion

modelVersion?: string

The model version used to generate the response.

  * Defined in [core/src/models/llm_response.ts:111](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L111)



### `Optional`outputTranscription

outputTranscription?: Transcription

Audio transcription of model output.

  * Defined in [core/src/models/llm_response.ts:103](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L103)



### `Optional`partial

partial?: boolean

Indicates whether the text content is part of a unfinished text stream. Only used for streaming mode and when the content is plain text.

  * Defined in [core/src/models/llm_response.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L43)



### `Optional`turnComplete

turnComplete?: boolean

Indicates whether the response from the model is complete. Only used for streaming mode.

  * Defined in [core/src/models/llm_response.ts:49](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L49)



### `Optional`usageMetadata

usageMetadata?: GenerateContentResponseUsageMetadata

The usage metadata of the LlmResponse.

  * Defined in [core/src/models/llm_response.ts:77](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L77)



Properties

citationMetadatacontentcustomMetadataerrorCodeerrorMessagefinishReasongoAwaygroundingMetadatainputTranscriptioninteractionIdinterruptedliveSessionIdliveSessionResumptionUpdatemodelVersionoutputTranscriptionpartialturnCompleteusageMetadata

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


