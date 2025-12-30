[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [Event]()



# Interface Event

Represents an event in a conversation between agents and users.

It is used to store the content of the conversation, as well as the actions taken by the agents like function calls, etc.

interface Event {  
actions: [EventActions](EventActions.html);  
author?: string;  
branch?: string;  
content?: Content;  
customMetadata?: { [key: string]: any };  
errorCode?: string;  
errorMessage?: string;  
finishReason?: FinishReason;  
groundingMetadata?: GroundingMetadata;  
id: string;  
inputTranscription?: Transcription;  
interrupted?: boolean;  
invocationId: string;  
liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate;  
longRunningToolIds?: string[];  
outputTranscription?: Transcription;  
partial?: boolean;  
timestamp: number;  
turnComplete?: boolean;  
usageMetadata?: GenerateContentResponseUsageMetadata;  
}

#### Hierarchy ([View Summary](../hierarchy.html#Event))

  * [LlmResponse](LlmResponse.html)
    * Event



  * Defined in [core/src/events/event.ts:19](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event.ts#L19)



## Properties

### actions

actions: [EventActions](EventActions.html)

The actions taken by the agent.

  * Defined in [core/src/events/event.ts:41](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event.ts#L41)



### `Optional`author

author?: string

"user" or the name of the agent, indicating who appended the event to the session.

  * Defined in [core/src/events/event.ts:36](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event.ts#L36)



### `Optional`branch

branch?: string

The branch of the event. The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3.

Branch is used when multiple sub-agent shouldn't see their peer agents' conversation history.

  * Defined in [core/src/events/event.ts:58](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event.ts#L58)



### `Optional`content

content?: Content

The content of the response.

Inherited from [LlmResponse](LlmResponse.html).[content](LlmResponse.html#content)

  * Defined in [core/src/models/llm_response.ts:17](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L17)



### `Optional`customMetadata

customMetadata?: { [key: string]: any }

The custom metadata of the LlmResponse. An optional key-value pair to label an LlmResponse. NOTE: the entire object must be JSON serializable.

Inherited from [LlmResponse](LlmResponse.html).[customMetadata](LlmResponse.html#custommetadata)

  * Defined in [core/src/models/llm_response.ts:57](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L57)



### `Optional`errorCode

errorCode?: string

Error code if the response is an error. Code varies by model.

Inherited from [LlmResponse](LlmResponse.html).[errorCode](LlmResponse.html#errorcode)

  * Defined in [core/src/models/llm_response.ts:39](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L39)



### `Optional`errorMessage

errorMessage?: string

Error message if the response is an error.

Inherited from [LlmResponse](LlmResponse.html).[errorMessage](LlmResponse.html#errormessage)

  * Defined in [core/src/models/llm_response.ts:44](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L44)



### `Optional`finishReason

finishReason?: FinishReason

The finish reason of the response.

Inherited from [LlmResponse](LlmResponse.html).[finishReason](LlmResponse.html#finishreason)

  * Defined in [core/src/models/llm_response.ts:67](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L67)



### `Optional`groundingMetadata

groundingMetadata?: GroundingMetadata

The grounding metadata of the response.

Inherited from [LlmResponse](LlmResponse.html).[groundingMetadata](LlmResponse.html#groundingmetadata)

  * Defined in [core/src/models/llm_response.ts:22](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L22)



### id

id: string

The unique identifier of the event. Do not assign the ID. It will be assigned by the session.

  * Defined in [core/src/events/event.ts:24](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event.ts#L24)



### `Optional`inputTranscription

inputTranscription?: Transcription

Audio transcription of user input.

Inherited from [LlmResponse](LlmResponse.html).[inputTranscription](LlmResponse.html#inputtranscription)

  * Defined in [core/src/models/llm_response.ts:77](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L77)



### `Optional`interrupted

interrupted?: boolean

Flag indicating that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

Inherited from [LlmResponse](LlmResponse.html).[interrupted](LlmResponse.html#interrupted)

  * Defined in [core/src/models/llm_response.ts:50](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L50)



### invocationId

invocationId: string

The invocation ID of the event. Should be non-empty before appending to a session.

  * Defined in [core/src/events/event.ts:30](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event.ts#L30)



### `Optional`liveSessionResumptionUpdate

liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate

The session resumption update of the LlmResponse

Inherited from [LlmResponse](LlmResponse.html).[liveSessionResumptionUpdate](LlmResponse.html#livesessionresumptionupdate)

  * Defined in [core/src/models/llm_response.ts:72](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L72)



### `Optional`longRunningToolIds

longRunningToolIds?: string[]

Set of ids of the long running function calls. Agent client will know from this field about which function call is long running. Only valid for function call event

  * Defined in [core/src/events/event.ts:48](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event.ts#L48)



### `Optional`outputTranscription

outputTranscription?: Transcription

Audio transcription of model output.

Inherited from [LlmResponse](LlmResponse.html).[outputTranscription](LlmResponse.html#outputtranscription)

  * Defined in [core/src/models/llm_response.ts:82](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L82)



### `Optional`partial

partial?: boolean

Indicates whether the text content is part of a unfinished text stream. Only used for streaming mode and when the content is plain text.

Inherited from [LlmResponse](LlmResponse.html).[partial](LlmResponse.html#partial)

  * Defined in [core/src/models/llm_response.ts:28](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L28)



### timestamp

timestamp: number

The timestamp of the event.

  * Defined in [core/src/events/event.ts:63](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/events/event.ts#L63)



### `Optional`turnComplete

turnComplete?: boolean

Indicates whether the response from the model is complete. Only used for streaming mode.

Inherited from [LlmResponse](LlmResponse.html).[turnComplete](LlmResponse.html#turncomplete)

  * Defined in [core/src/models/llm_response.ts:34](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L34)



### `Optional`usageMetadata

usageMetadata?: GenerateContentResponseUsageMetadata

The usage metadata of the LlmResponse.

Inherited from [LlmResponse](LlmResponse.html).[usageMetadata](LlmResponse.html#usagemetadata)

  * Defined in [core/src/models/llm_response.ts:62](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_response.ts#L62)



Properties

actionsauthorbranchcontentcustomMetadataerrorCodeerrorMessagefinishReasongroundingMetadataidinputTranscriptioninterruptedinvocationIdliveSessionResumptionUpdatelongRunningToolIdsoutputTranscriptionpartialtimestampturnCompleteusageMetadata

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


