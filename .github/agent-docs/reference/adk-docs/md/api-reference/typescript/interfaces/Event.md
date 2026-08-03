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
citationMetadata?: CitationMetadata;  
content?: Content;  
customMetadata?: { [key: string]: unknown };  
errorCode?: string;  
errorMessage?: string;  
finishReason?: FinishReason;  
goAway?: LiveServerGoAway;  
groundingMetadata?: GroundingMetadata;  
id: string;  
inputTranscription?: Transcription;  
interactionId?: string;  
interrupted?: boolean;  
invocationId: string;  
liveSessionId?: string;  
liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate;  
longRunningToolIds?: string[];  
modelVersion?: string;  
outputTranscription?: Transcription;  
partial?: boolean;  
timestamp: number;  
turnComplete?: boolean;  
usageMetadata?: GenerateContentResponseUsageMetadata;  
}

#### Hierarchy ([View Summary](../hierarchy.html#Event))

  * [LlmResponse](LlmResponse.html)
    * Event
      * [CompactedEvent](CompactedEvent.html)



  * Defined in [core/src/events/event.ts:21](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L21)



## Properties

### actions

actions: [EventActions](EventActions.html)

The actions taken by the agent.

  * Defined in [core/src/events/event.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L43)



### `Optional`author

author?: string

"user" or the name of the agent, indicating who appended the event to the session.

  * Defined in [core/src/events/event.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L38)



### `Optional`branch

branch?: string

The branch of the event. The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3.

Branch is used when multiple sub-agent shouldn't see their peer agents' conversation history.

  * Defined in [core/src/events/event.ts:60](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L60)



### `Optional`citationMetadata

citationMetadata?: CitationMetadata

The citation metadata of the response.

Inherited from [LlmResponse](LlmResponse.html).[citationMetadata](LlmResponse.html#citationmetadata)

  * Defined in [core/src/models/llm_response.ts:37](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L37)



### `Optional`content

content?: Content

The content of the response.

Inherited from [LlmResponse](LlmResponse.html).[content](LlmResponse.html#content)

  * Defined in [core/src/models/llm_response.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L27)



### `Optional`customMetadata

customMetadata?: { [key: string]: unknown }

The custom metadata of the LlmResponse. An optional key-value pair to label an LlmResponse. NOTE: the entire object must be JSON serializable.

Inherited from [LlmResponse](LlmResponse.html).[customMetadata](LlmResponse.html#custommetadata)

  * Defined in [core/src/models/llm_response.ts:72](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L72)



### `Optional`errorCode

errorCode?: string

Error code if the response is an error. Code varies by model.

Inherited from [LlmResponse](LlmResponse.html).[errorCode](LlmResponse.html#errorcode)

  * Defined in [core/src/models/llm_response.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L54)



### `Optional`errorMessage

errorMessage?: string

Error message if the response is an error.

Inherited from [LlmResponse](LlmResponse.html).[errorMessage](LlmResponse.html#errormessage)

  * Defined in [core/src/models/llm_response.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L59)



### `Optional`finishReason

finishReason?: FinishReason

The finish reason of the response.

Inherited from [LlmResponse](LlmResponse.html).[finishReason](LlmResponse.html#finishreason)

  * Defined in [core/src/models/llm_response.ts:82](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L82)



### `Optional`goAway

goAway?: LiveServerGoAway

Server-side signal that the live connection will be closed soon. The caller should reconnect using the latest session resumption handle.

Inherited from [LlmResponse](LlmResponse.html).[goAway](LlmResponse.html#goaway)

  * Defined in [core/src/models/llm_response.ts:93](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L93)



### `Optional`groundingMetadata

groundingMetadata?: GroundingMetadata

The grounding metadata of the response.

Inherited from [LlmResponse](LlmResponse.html).[groundingMetadata](LlmResponse.html#groundingmetadata)

  * Defined in [core/src/models/llm_response.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L32)



### id

id: string

The unique identifier of the event. Do not assign the ID. It will be assigned by the session.

  * Defined in [core/src/events/event.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L26)



### `Optional`inputTranscription

inputTranscription?: Transcription

Audio transcription of user input.

Inherited from [LlmResponse](LlmResponse.html).[inputTranscription](LlmResponse.html#inputtranscription)

  * Defined in [core/src/models/llm_response.ts:98](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L98)



### `Optional`interactionId

interactionId?: string

The interaction ID returned by the model, if any.

Inherited from [LlmResponse](LlmResponse.html).[interactionId](LlmResponse.html#interactionid)

  * Defined in [core/src/models/llm_response.ts:108](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L108)



### `Optional`interrupted

interrupted?: boolean

Flag indicating that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

Inherited from [LlmResponse](LlmResponse.html).[interrupted](LlmResponse.html#interrupted)

  * Defined in [core/src/models/llm_response.ts:65](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L65)



### invocationId

invocationId: string

The invocation ID of the event. Should be non-empty before appending to a session.

  * Defined in [core/src/events/event.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L32)



### `Optional`liveSessionId

liveSessionId?: string

The session ID of the Live session.

Inherited from [LlmResponse](LlmResponse.html).[liveSessionId](LlmResponse.html#livesessionid)

  * Defined in [core/src/models/llm_response.ts:114](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L114)



### `Optional`liveSessionResumptionUpdate

liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate

The session resumption update of the LlmResponse

Inherited from [LlmResponse](LlmResponse.html).[liveSessionResumptionUpdate](LlmResponse.html#livesessionresumptionupdate)

  * Defined in [core/src/models/llm_response.ts:87](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L87)



### `Optional`longRunningToolIds

longRunningToolIds?: string[]

Set of ids of the long running function calls. Agent client will know from this field about which function call is long running. Only valid for function call event

  * Defined in [core/src/events/event.ts:50](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L50)



### `Optional`modelVersion

modelVersion?: string

The model version used to generate the response.

Inherited from [LlmResponse](LlmResponse.html).[modelVersion](LlmResponse.html#modelversion)

  * Defined in [core/src/models/llm_response.ts:111](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L111)



### `Optional`outputTranscription

outputTranscription?: Transcription

Audio transcription of model output.

Inherited from [LlmResponse](LlmResponse.html).[outputTranscription](LlmResponse.html#outputtranscription)

  * Defined in [core/src/models/llm_response.ts:103](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L103)



### `Optional`partial

partial?: boolean

Indicates whether the text content is part of a unfinished text stream. Only used for streaming mode and when the content is plain text.

Inherited from [LlmResponse](LlmResponse.html).[partial](LlmResponse.html#partial)

  * Defined in [core/src/models/llm_response.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L43)



### timestamp

timestamp: number

The timestamp of the event.

  * Defined in [core/src/events/event.ts:65](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L65)



### `Optional`turnComplete

turnComplete?: boolean

Indicates whether the response from the model is complete. Only used for streaming mode.

Inherited from [LlmResponse](LlmResponse.html).[turnComplete](LlmResponse.html#turncomplete)

  * Defined in [core/src/models/llm_response.ts:49](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L49)



### `Optional`usageMetadata

usageMetadata?: GenerateContentResponseUsageMetadata

The usage metadata of the LlmResponse.

Inherited from [LlmResponse](LlmResponse.html).[usageMetadata](LlmResponse.html#usagemetadata)

  * Defined in [core/src/models/llm_response.ts:77](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L77)



Properties

actionsauthorbranchcitationMetadatacontentcustomMetadataerrorCodeerrorMessagefinishReasongoAwaygroundingMetadataidinputTranscriptioninteractionIdinterruptedinvocationIdliveSessionIdliveSessionResumptionUpdatelongRunningToolIdsmodelVersionoutputTranscriptionpartialtimestampturnCompleteusageMetadata

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


