[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LlmResponse]()



# Interface LlmResponse

LLM response class that provides the first candidate response from the model if available. Otherwise, returns error code and message.

interface LlmResponse {  
content?: Content;  
customMetadata?: { [key: string]: any };  
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



  * Defined in [core/src/models/llm_response.ts:13](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L13)



## Properties

### `Optional`content

content?: Content

The content of the response.

  * Defined in [core/src/models/llm_response.ts:17](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L17)



### `Optional`customMetadata

customMetadata?: { [key: string]: any }

The custom metadata of the LlmResponse. An optional key-value pair to label an LlmResponse. NOTE: the entire object must be JSON serializable.

  * Defined in [core/src/models/llm_response.ts:57](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L57)



### `Optional`errorCode

errorCode?: string

Error code if the response is an error. Code varies by model.

  * Defined in [core/src/models/llm_response.ts:39](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L39)



### `Optional`errorMessage

errorMessage?: string

Error message if the response is an error.

  * Defined in [core/src/models/llm_response.ts:44](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L44)



### `Optional`finishReason

finishReason?: FinishReason

The finish reason of the response.

  * Defined in [core/src/models/llm_response.ts:67](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L67)



### `Optional`groundingMetadata

groundingMetadata?: GroundingMetadata

The grounding metadata of the response.

  * Defined in [core/src/models/llm_response.ts:22](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L22)



### `Optional`inputTranscription

inputTranscription?: Transcription

Audio transcription of user input.

  * Defined in [core/src/models/llm_response.ts:77](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L77)



### `Optional`interrupted

interrupted?: boolean

Flag indicating that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

  * Defined in [core/src/models/llm_response.ts:50](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L50)



### `Optional`liveSessionResumptionUpdate

liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate

The session resumption update of the LlmResponse

  * Defined in [core/src/models/llm_response.ts:72](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L72)



### `Optional`outputTranscription

outputTranscription?: Transcription

Audio transcription of model output.

  * Defined in [core/src/models/llm_response.ts:82](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L82)



### `Optional`partial

partial?: boolean

Indicates whether the text content is part of a unfinished text stream. Only used for streaming mode and when the content is plain text.

  * Defined in [core/src/models/llm_response.ts:28](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L28)



### `Optional`turnComplete

turnComplete?: boolean

Indicates whether the response from the model is complete. Only used for streaming mode.

  * Defined in [core/src/models/llm_response.ts:34](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L34)



### `Optional`usageMetadata

usageMetadata?: GenerateContentResponseUsageMetadata

The usage metadata of the LlmResponse.

  * Defined in [core/src/models/llm_response.ts:62](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L62)



Properties

contentcustomMetadataerrorCodeerrorMessagefinishReasongroundingMetadatainputTranscriptioninterruptedliveSessionResumptionUpdateoutputTranscriptionpartialturnCompleteusageMetadata

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


