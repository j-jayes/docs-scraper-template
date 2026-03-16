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



  * Defined in [events/event.ts:20](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event.ts#L20)



## Properties

### actions

actions: [EventActions](EventActions.html)

The actions taken by the agent.

  * Defined in [events/event.ts:42](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event.ts#L42)



### `Optional`author

author?: string

"user" or the name of the agent, indicating who appended the event to the session.

  * Defined in [events/event.ts:37](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event.ts#L37)



### `Optional`branch

branch?: string

The branch of the event. The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3.

Branch is used when multiple sub-agent shouldn't see their peer agents' conversation history.

  * Defined in [events/event.ts:59](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event.ts#L59)



### `Optional`citationMetadata

citationMetadata?: CitationMetadata

The citation metadata of the response.

Inherited from [LlmResponse](LlmResponse.html).[citationMetadata](LlmResponse.html#citationmetadata)

  * Defined in [models/llm_response.ts:36](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L36)



### `Optional`content

content?: Content

The content of the response.

Inherited from [LlmResponse](LlmResponse.html).[content](LlmResponse.html#content)

  * Defined in [models/llm_response.ts:26](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L26)



### `Optional`customMetadata

customMetadata?: { [key: string]: unknown }

The custom metadata of the LlmResponse. An optional key-value pair to label an LlmResponse. NOTE: the entire object must be JSON serializable.

Inherited from [LlmResponse](LlmResponse.html).[customMetadata](LlmResponse.html#custommetadata)

  * Defined in [models/llm_response.ts:71](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L71)



### `Optional`errorCode

errorCode?: string

Error code if the response is an error. Code varies by model.

Inherited from [LlmResponse](LlmResponse.html).[errorCode](LlmResponse.html#errorcode)

  * Defined in [models/llm_response.ts:53](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L53)



### `Optional`errorMessage

errorMessage?: string

Error message if the response is an error.

Inherited from [LlmResponse](LlmResponse.html).[errorMessage](LlmResponse.html#errormessage)

  * Defined in [models/llm_response.ts:58](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L58)



### `Optional`finishReason

finishReason?: FinishReason

The finish reason of the response.

Inherited from [LlmResponse](LlmResponse.html).[finishReason](LlmResponse.html#finishreason)

  * Defined in [models/llm_response.ts:81](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L81)



### `Optional`groundingMetadata

groundingMetadata?: GroundingMetadata

The grounding metadata of the response.

Inherited from [LlmResponse](LlmResponse.html).[groundingMetadata](LlmResponse.html#groundingmetadata)

  * Defined in [models/llm_response.ts:31](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L31)



### id

id: string

The unique identifier of the event. Do not assign the ID. It will be assigned by the session.

  * Defined in [events/event.ts:25](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event.ts#L25)



### `Optional`inputTranscription

inputTranscription?: Transcription

Audio transcription of user input.

Inherited from [LlmResponse](LlmResponse.html).[inputTranscription](LlmResponse.html#inputtranscription)

  * Defined in [models/llm_response.ts:91](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L91)



### `Optional`interrupted

interrupted?: boolean

Flag indicating that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

Inherited from [LlmResponse](LlmResponse.html).[interrupted](LlmResponse.html#interrupted)

  * Defined in [models/llm_response.ts:64](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L64)



### invocationId

invocationId: string

The invocation ID of the event. Should be non-empty before appending to a session.

  * Defined in [events/event.ts:31](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event.ts#L31)



### `Optional`liveSessionResumptionUpdate

liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate

The session resumption update of the LlmResponse

Inherited from [LlmResponse](LlmResponse.html).[liveSessionResumptionUpdate](LlmResponse.html#livesessionresumptionupdate)

  * Defined in [models/llm_response.ts:86](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L86)



### `Optional`longRunningToolIds

longRunningToolIds?: string[]

Set of ids of the long running function calls. Agent client will know from this field about which function call is long running. Only valid for function call event

  * Defined in [events/event.ts:49](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event.ts#L49)



### `Optional`outputTranscription

outputTranscription?: Transcription

Audio transcription of model output.

Inherited from [LlmResponse](LlmResponse.html).[outputTranscription](LlmResponse.html#outputtranscription)

  * Defined in [models/llm_response.ts:96](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L96)



### `Optional`partial

partial?: boolean

Indicates whether the text content is part of a unfinished text stream. Only used for streaming mode and when the content is plain text.

Inherited from [LlmResponse](LlmResponse.html).[partial](LlmResponse.html#partial)

  * Defined in [models/llm_response.ts:42](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L42)



### timestamp

timestamp: number

The timestamp of the event.

  * Defined in [events/event.ts:64](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/events/event.ts#L64)



### `Optional`turnComplete

turnComplete?: boolean

Indicates whether the response from the model is complete. Only used for streaming mode.

Inherited from [LlmResponse](LlmResponse.html).[turnComplete](LlmResponse.html#turncomplete)

  * Defined in [models/llm_response.ts:48](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L48)



### `Optional`usageMetadata

usageMetadata?: GenerateContentResponseUsageMetadata

The usage metadata of the LlmResponse.

Inherited from [LlmResponse](LlmResponse.html).[usageMetadata](LlmResponse.html#usagemetadata)

  * Defined in [models/llm_response.ts:76](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_response.ts#L76)



Properties

actionsauthorbranchcitationMetadatacontentcustomMetadataerrorCodeerrorMessagefinishReasongroundingMetadataidinputTranscriptioninterruptedinvocationIdliveSessionResumptionUpdatelongRunningToolIdsoutputTranscriptionpartialtimestampturnCompleteusageMetadata

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


