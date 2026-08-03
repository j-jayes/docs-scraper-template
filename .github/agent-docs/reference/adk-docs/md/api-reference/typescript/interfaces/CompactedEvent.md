[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [CompactedEvent]()



# Interface CompactedEvent

A specialized Event type that represents a synthesized summary of past events. This is used to compress session history without losing critical context.

interface CompactedEvent {  
actions: [EventActions](EventActions.html);  
author?: string;  
branch?: string;  
citationMetadata?: CitationMetadata;  
compactedContent: string;  
content?: Content;  
customMetadata?: { [key: string]: unknown };  
endTime: number;  
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
isCompacted: true;  
isScratchpad?: boolean;  
liveSessionId?: string;  
liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate;  
longRunningToolIds?: string[];  
modelVersion?: string;  
outputTranscription?: Transcription;  
partial?: boolean;  
startTime: number;  
timestamp: number;  
turnComplete?: boolean;  
usageMetadata?: GenerateContentResponseUsageMetadata;  
}

#### Hierarchy ([View Summary](../hierarchy.html#CompactedEvent))

  * [Event](Event.html)
    * CompactedEvent



  * Defined in [core/src/events/compacted_event.ts:13](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/compacted_event.ts#L13)



## Properties

### actions

actions: [EventActions](EventActions.html)

The actions taken by the agent.

Inherited from [Event](Event.html).[actions](Event.html#actions)

  * Defined in [core/src/events/event.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L43)



### `Optional`author

author?: string

"user" or the name of the agent, indicating who appended the event to the session.

Inherited from [Event](Event.html).[author](Event.html#author)

  * Defined in [core/src/events/event.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L38)



### `Optional`branch

branch?: string

The branch of the event. The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3.

Branch is used when multiple sub-agent shouldn't see their peer agents' conversation history.

Inherited from [Event](Event.html).[branch](Event.html#branch)

  * Defined in [core/src/events/event.ts:60](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L60)



### `Optional`citationMetadata

citationMetadata?: CitationMetadata

The citation metadata of the response.

Inherited from [Event](Event.html).[citationMetadata](Event.html#citationmetadata)

  * Defined in [core/src/models/llm_response.ts:37](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L37)



### compactedContent

compactedContent: string

The summarized content of the compacted events.

  * Defined in [core/src/events/compacted_event.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/compacted_event.ts#L32)



### `Optional`content

content?: Content

The content of the response.

Inherited from [Event](Event.html).[content](Event.html#content)

  * Defined in [core/src/models/llm_response.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L27)



### `Optional`customMetadata

customMetadata?: { [key: string]: unknown }

The custom metadata of the LlmResponse. An optional key-value pair to label an LlmResponse. NOTE: the entire object must be JSON serializable.

Inherited from [Event](Event.html).[customMetadata](Event.html#custommetadata)

  * Defined in [core/src/models/llm_response.ts:72](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L72)



### endTime

endTime: number

The end time of the context that was compacted.

  * Defined in [core/src/events/compacted_event.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/compacted_event.ts#L27)



### `Optional`errorCode

errorCode?: string

Error code if the response is an error. Code varies by model.

Inherited from [Event](Event.html).[errorCode](Event.html#errorcode)

  * Defined in [core/src/models/llm_response.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L54)



### `Optional`errorMessage

errorMessage?: string

Error message if the response is an error.

Inherited from [Event](Event.html).[errorMessage](Event.html#errormessage)

  * Defined in [core/src/models/llm_response.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L59)



### `Optional`finishReason

finishReason?: FinishReason

The finish reason of the response.

Inherited from [Event](Event.html).[finishReason](Event.html#finishreason)

  * Defined in [core/src/models/llm_response.ts:82](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L82)



### `Optional`goAway

goAway?: LiveServerGoAway

Server-side signal that the live connection will be closed soon. The caller should reconnect using the latest session resumption handle.

Inherited from [Event](Event.html).[goAway](Event.html#goaway)

  * Defined in [core/src/models/llm_response.ts:93](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L93)



### `Optional`groundingMetadata

groundingMetadata?: GroundingMetadata

The grounding metadata of the response.

Inherited from [Event](Event.html).[groundingMetadata](Event.html#groundingmetadata)

  * Defined in [core/src/models/llm_response.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L32)



### id

id: string

The unique identifier of the event. Do not assign the ID. It will be assigned by the session.

Inherited from [Event](Event.html).[id](Event.html#id)

  * Defined in [core/src/events/event.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L26)



### `Optional`inputTranscription

inputTranscription?: Transcription

Audio transcription of user input.

Inherited from [Event](Event.html).[inputTranscription](Event.html#inputtranscription)

  * Defined in [core/src/models/llm_response.ts:98](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L98)



### `Optional`interactionId

interactionId?: string

The interaction ID returned by the model, if any.

Inherited from [Event](Event.html).[interactionId](Event.html#interactionid)

  * Defined in [core/src/models/llm_response.ts:108](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L108)



### `Optional`interrupted

interrupted?: boolean

Flag indicating that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

Inherited from [Event](Event.html).[interrupted](Event.html#interrupted)

  * Defined in [core/src/models/llm_response.ts:65](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L65)



### invocationId

invocationId: string

The invocation ID of the event. Should be non-empty before appending to a session.

Inherited from [Event](Event.html).[invocationId](Event.html#invocationid)

  * Defined in [core/src/events/event.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L32)



### `Readonly`isCompacted

isCompacted: true

Identifies this event as a compacted event.

  * Defined in [core/src/events/compacted_event.ts:17](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/compacted_event.ts#L17)



### `Optional`isScratchpad

isScratchpad?: boolean

Identifies this compacted event as the persistent context scratchpad.

  * Defined in [core/src/events/compacted_event.ts:37](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/compacted_event.ts#L37)



### `Optional`liveSessionId

liveSessionId?: string

The session ID of the Live session.

Inherited from [Event](Event.html).[liveSessionId](Event.html#livesessionid)

  * Defined in [core/src/models/llm_response.ts:114](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L114)



### `Optional`liveSessionResumptionUpdate

liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate

The session resumption update of the LlmResponse

Inherited from [Event](Event.html).[liveSessionResumptionUpdate](Event.html#livesessionresumptionupdate)

  * Defined in [core/src/models/llm_response.ts:87](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L87)



### `Optional`longRunningToolIds

longRunningToolIds?: string[]

Set of ids of the long running function calls. Agent client will know from this field about which function call is long running. Only valid for function call event

Inherited from [Event](Event.html).[longRunningToolIds](Event.html#longrunningtoolids)

  * Defined in [core/src/events/event.ts:50](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L50)



### `Optional`modelVersion

modelVersion?: string

The model version used to generate the response.

Inherited from [Event](Event.html).[modelVersion](Event.html#modelversion)

  * Defined in [core/src/models/llm_response.ts:111](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L111)



### `Optional`outputTranscription

outputTranscription?: Transcription

Audio transcription of model output.

Inherited from [Event](Event.html).[outputTranscription](Event.html#outputtranscription)

  * Defined in [core/src/models/llm_response.ts:103](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L103)



### `Optional`partial

partial?: boolean

Indicates whether the text content is part of a unfinished text stream. Only used for streaming mode and when the content is plain text.

Inherited from [Event](Event.html).[partial](Event.html#partial)

  * Defined in [core/src/models/llm_response.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L43)



### startTime

startTime: number

The start time of the context that was compacted.

  * Defined in [core/src/events/compacted_event.ts:22](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/compacted_event.ts#L22)



### timestamp

timestamp: number

The timestamp of the event.

Inherited from [Event](Event.html).[timestamp](Event.html#timestamp)

  * Defined in [core/src/events/event.ts:65](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/events/event.ts#L65)



### `Optional`turnComplete

turnComplete?: boolean

Indicates whether the response from the model is complete. Only used for streaming mode.

Inherited from [Event](Event.html).[turnComplete](Event.html#turncomplete)

  * Defined in [core/src/models/llm_response.ts:49](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L49)



### `Optional`usageMetadata

usageMetadata?: GenerateContentResponseUsageMetadata

The usage metadata of the LlmResponse.

Inherited from [Event](Event.html).[usageMetadata](Event.html#usagemetadata)

  * Defined in [core/src/models/llm_response.ts:77](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_response.ts#L77)



Properties

actionsauthorbranchcitationMetadatacompactedContentcontentcustomMetadataendTimeerrorCodeerrorMessagefinishReasongoAwaygroundingMetadataidinputTranscriptioninteractionIdinterruptedinvocationIdisCompactedisScratchpadliveSessionIdliveSessionResumptionUpdatelongRunningToolIdsmodelVersionoutputTranscriptionpartialstartTimetimestampturnCompleteusageMetadata

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


