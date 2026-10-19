[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [CreateEventParams]()



# Interface CreateEventParams

Parameters for creating an event with partial fields.

interface CreateEventParams {  
"[EVENT_SIGNATURE_SYMBOL]"?: true;  
actions?: Partial<[EventActions](EventActions.html)>;  
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
id?: string;  
inputTranscription?: Transcription;  
interactionId?: string;  
interrupted?: boolean;  
invocationId?: string;  
isolationScope?: string;  
liveSessionId?: string;  
liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate;  
longRunningToolIds?: string[];  
modelVersion?: string;  
nodeInfo?: [NodeInfo](NodeInfo.html);  
output?: unknown;  
outputTranscription?: Transcription;  
partial?: boolean;  
route?: [Route](../types/Route.html);  
timestamp?: number;  
turnComplete?: boolean;  
usageMetadata?: GenerateContentResponseUsageMetadata;  
}

#### Hierarchy ([View Summary](../hierarchy.html#CreateEventParams))

  * Omit<Partial<[Event](Event.html)>, "actions">
    * CreateEventParams
      * [CreateNodeErrorEventParams](CreateNodeErrorEventParams.html)



  * Defined in [core/src/events/event.ts:161](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L161)



## Properties

### `Optional` `Readonly`[EVENT_SIGNATURE_SYMBOL]

"[EVENT_SIGNATURE_SYMBOL]"?: true

Signature brand identifying this object as an ADK [Event](Event.html).

Set by [createEvent](../functions/createEvent.html) and checked by `isEvent`. Optional because events are also reconstructed from storage/session payloads, where the (non-serializable) brand is absent.

Inherited from [Event](Event.html).[[EVENT_SIGNATURE_SYMBOL]](Event.html#event_signature_symbol)

  * Defined in [core/src/events/event.ts:82](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L82)



### `Optional`actions

actions?: Partial<[EventActions](EventActions.html)>

  * Defined in [core/src/events/event.ts:162](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L162)



### `Optional`author

author?: string

"user" or the name of the agent, indicating who appended the event to the session.

Inherited from [Event](Event.html).[author](Event.html#author)

  * Defined in [core/src/events/event.ts:100](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L100)



### `Optional`branch

branch?: string

The branch of the event. The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3.

Branch is used when multiple sub-agent shouldn't see their peer agents' conversation history.

Inherited from [Event](Event.html).[branch](Event.html#branch)

  * Defined in [core/src/events/event.ts:122](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L122)



### `Optional`citationMetadata

citationMetadata?: CitationMetadata

The citation metadata of the response.

Inherited from [LlmResponse](LlmResponse.html).[citationMetadata](LlmResponse.html#citationmetadata)

  * Defined in [core/src/models/llm_response.ts:37](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L37)



### `Optional`content

content?: Content

The content of the response.

Inherited from [LlmResponse](LlmResponse.html).[content](LlmResponse.html#content)

  * Defined in [core/src/models/llm_response.ts:27](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L27)



### `Optional`customMetadata

customMetadata?: { [key: string]: unknown }

The custom metadata of the LlmResponse. An optional key-value pair to label an LlmResponse. NOTE: the entire object must be JSON serializable.

Inherited from [LlmResponse](LlmResponse.html).[customMetadata](LlmResponse.html#custommetadata)

  * Defined in [core/src/models/llm_response.ts:72](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L72)



### `Optional`errorCode

errorCode?: string

Error code if the response is an error. Code varies by model.

Inherited from [LlmResponse](LlmResponse.html).[errorCode](LlmResponse.html#errorcode)

  * Defined in [core/src/models/llm_response.ts:54](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L54)



### `Optional`errorMessage

errorMessage?: string

Error message if the response is an error.

Inherited from [LlmResponse](LlmResponse.html).[errorMessage](LlmResponse.html#errormessage)

  * Defined in [core/src/models/llm_response.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L59)



### `Optional`finishReason

finishReason?: FinishReason

The finish reason of the response.

Inherited from [LlmResponse](LlmResponse.html).[finishReason](LlmResponse.html#finishreason)

  * Defined in [core/src/models/llm_response.ts:82](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L82)



### `Optional`goAway

goAway?: LiveServerGoAway

Server-side signal that the live connection will be closed soon. The caller should reconnect using the latest session resumption handle.

Inherited from [LlmResponse](LlmResponse.html).[goAway](LlmResponse.html#goaway)

  * Defined in [core/src/models/llm_response.ts:93](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L93)



### `Optional`groundingMetadata

groundingMetadata?: GroundingMetadata

The grounding metadata of the response.

Inherited from [LlmResponse](LlmResponse.html).[groundingMetadata](LlmResponse.html#groundingmetadata)

  * Defined in [core/src/models/llm_response.ts:32](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L32)



### `Optional`id

id?: string

The unique identifier of the event. Do not assign the ID. It will be assigned by the session.

Inherited from [Event](Event.html).[id](Event.html#id)

  * Defined in [core/src/events/event.ts:88](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L88)



### `Optional`inputTranscription

inputTranscription?: Transcription

Audio transcription of user input.

Inherited from [LlmResponse](LlmResponse.html).[inputTranscription](LlmResponse.html#inputtranscription)

  * Defined in [core/src/models/llm_response.ts:98](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L98)



### `Optional`interactionId

interactionId?: string

The interaction ID returned by the model, if any.

Inherited from [LlmResponse](LlmResponse.html).[interactionId](LlmResponse.html#interactionid)

  * Defined in [core/src/models/llm_response.ts:108](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L108)



### `Optional`interrupted

interrupted?: boolean

Flag indicating that LLM was interrupted when generating the content. Usually it's due to user interruption during a bidi streaming.

Inherited from [LlmResponse](LlmResponse.html).[interrupted](LlmResponse.html#interrupted)

  * Defined in [core/src/models/llm_response.ts:65](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L65)



### `Optional`invocationId

invocationId?: string

The invocation ID of the event. Should be non-empty before appending to a session.

Inherited from [Event](Event.html).[invocationId](Event.html#invocationid)

  * Defined in [core/src/events/event.ts:94](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L94)



### `Optional`isolationScope

isolationScope?: string

Workflow: scope tag used to isolate multi-agent conversations so peer scopes don't see each other's events. Mirrors Python `Event.isolation_scope`.

Inherited from [Event](Event.html).[isolationScope](Event.html#isolationscope)

  * Defined in [core/src/events/event.ts:155](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L155)



### `Optional`liveSessionId

liveSessionId?: string

The session ID of the Live session.

Inherited from [LlmResponse](LlmResponse.html).[liveSessionId](LlmResponse.html#livesessionid)

  * Defined in [core/src/models/llm_response.ts:114](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L114)



### `Optional`liveSessionResumptionUpdate

liveSessionResumptionUpdate?: LiveServerSessionResumptionUpdate

The session resumption update of the LlmResponse

Inherited from [LlmResponse](LlmResponse.html).[liveSessionResumptionUpdate](LlmResponse.html#livesessionresumptionupdate)

  * Defined in [core/src/models/llm_response.ts:87](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L87)



### `Optional`longRunningToolIds

longRunningToolIds?: string[]

Set of ids of the long running function calls. Agent client will know from this field about which function call is long running. Only valid for function call event

Inherited from [Event](Event.html).[longRunningToolIds](Event.html#longrunningtoolids)

  * Defined in [core/src/events/event.ts:112](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L112)



### `Optional`modelVersion

modelVersion?: string

The model version used to generate the response.

Inherited from [LlmResponse](LlmResponse.html).[modelVersion](LlmResponse.html#modelversion)

  * Defined in [core/src/models/llm_response.ts:111](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L111)



### `Optional`nodeInfo

nodeInfo?: [NodeInfo](NodeInfo.html)

Workflow: provenance of the emitting node. Mirrors Python `Event.node_info`.

Inherited from [Event](Event.html).[nodeInfo](Event.html#nodeinfo)

  * Defined in [core/src/events/event.ts:148](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L148)



### `Optional`output

output?: unknown

Workflow: the structured output produced by the emitting node, if any.

First-class field mirroring `google/adk-python` `Event.output`. Used by the workflow engine to carry a node's return value alongside its content.

Inherited from [Event](Event.html).[output](Event.html#output)

  * Defined in [core/src/events/event.ts:135](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L135)



### `Optional`outputTranscription

outputTranscription?: Transcription

Audio transcription of model output.

Inherited from [LlmResponse](LlmResponse.html).[outputTranscription](LlmResponse.html#outputtranscription)

  * Defined in [core/src/models/llm_response.ts:103](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L103)



### `Optional`partial

partial?: boolean

Indicates whether the text content is part of a unfinished text stream. Only used for streaming mode and when the content is plain text.

Inherited from [LlmResponse](LlmResponse.html).[partial](LlmResponse.html#partial)

  * Defined in [core/src/models/llm_response.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L43)



### `Optional`route

route?: [Route](../types/Route.html)

Workflow: the route key(s) emitted by a routing node, used by the graph to select the matching outgoing edge(s). A single value fires one branch; an array fires every branch whose route matches any listed value (multi-route dispatch). Mirrors Python `Event.route`.

Inherited from [Event](Event.html).[route](Event.html#route)

  * Defined in [core/src/events/event.ts:143](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L143)



### `Optional`timestamp

timestamp?: number

The timestamp of the event.

Inherited from [Event](Event.html).[timestamp](Event.html#timestamp)

  * Defined in [core/src/events/event.ts:127](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/events/event.ts#L127)



### `Optional`turnComplete

turnComplete?: boolean

Indicates whether the response from the model is complete. Only used for streaming mode.

Inherited from [LlmResponse](LlmResponse.html).[turnComplete](LlmResponse.html#turncomplete)

  * Defined in [core/src/models/llm_response.ts:49](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L49)



### `Optional`usageMetadata

usageMetadata?: GenerateContentResponseUsageMetadata

The usage metadata of the LlmResponse.

Inherited from [LlmResponse](LlmResponse.html).[usageMetadata](LlmResponse.html#usagemetadata)

  * Defined in [core/src/models/llm_response.ts:77](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/llm_response.ts#L77)



Properties

[EVENT_SIGNATURE_SYMBOL]actionsauthorbranchcitationMetadatacontentcustomMetadataerrorCodeerrorMessagefinishReasongoAwaygroundingMetadataidinputTranscriptioninteractionIdinterruptedinvocationIdisolationScopeliveSessionIdliveSessionResumptionUpdatelongRunningToolIdsmodelVersionnodeInfooutputoutputTranscriptionpartialroutetimestampturnCompleteusageMetadata

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


