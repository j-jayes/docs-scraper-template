[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.events](../index.html)/Event

# Event

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

data class [Event](index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val id: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = Uuid.random(), val invocationId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val author: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val content: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, val actions: [EventActions](../-event-actions/index.html) = EventActions(), val longRunningToolIds: [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)> = emptySet(), val partial: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val turnComplete: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val errorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val errorMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val finishReason: [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)? = null, val usageMetadata: [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)? = null, val avgLogProbs: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, val interrupted: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val branch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val groundingMetadata: [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)? = null, val modelVersion: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)? = null, val cacheMetadata: [CacheMetadata](../../com.google.adk.kt.models/-cache-metadata/index.html)? = null, val customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null, val output: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, val nodeInfo: [NodeInfo](../../com.google.adk.kt.workflow/-node-info/index.html)? = null, val timestamp: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html) = Clock.System.now().toEpochMilliseconds(), val turnCompleteReason: [TurnCompleteReason](../../com.google.adk.kt.types/-turn-complete-reason/index.html)? = null, val interactionStatus: [InteractionStatus](../../com.google.adk.kt.types/-interaction-status/index.html)? = null, val inputTranscription: [Transcription](../../com.google.adk.kt.types/-transcription/index.html)? = null, val outputTranscription: [Transcription](../../com.google.adk.kt.types/-transcription/index.html)? = null, val liveSessionId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val liveSessionResumptionUpdate: [LiveServerSessionResumptionUpdate](../../com.google.adk.kt.types/-live-server-session-resumption-update/index.html)? = null, val voiceActivity: [VoiceActivity](../../com.google.adk.kt.types/-voice-activity/index.html)? = null)

Represents an event in a session.

Members

## Constructors

[Event](-event.html)

Link copied to clipboard

common

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

constructor(id: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = Uuid.random(), invocationId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, author: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", content: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, actions: [EventActions](../-event-actions/index.html) = EventActions(), longRunningToolIds: [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)> = emptySet(), partial: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, turnComplete: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, errorCode: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, errorMessage: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, finishReason: [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)? = null, usageMetadata: [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)? = null, avgLogProbs: [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)? = null, interrupted: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, branch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, groundingMetadata: [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)? = null, modelVersion: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, citationMetadata: [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)? = null, cacheMetadata: [CacheMetadata](../../com.google.adk.kt.models/-cache-metadata/index.html)? = null, customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>? = null, output: [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)? = null, nodeInfo: [NodeInfo](../../com.google.adk.kt.workflow/-node-info/index.html)? = null, timestamp: [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html) = Clock.System.now().toEpochMilliseconds(), turnCompleteReason: [TurnCompleteReason](../../com.google.adk.kt.types/-turn-complete-reason/index.html)? = null, interactionStatus: [InteractionStatus](../../com.google.adk.kt.types/-interaction-status/index.html)? = null, inputTranscription: [Transcription](../../com.google.adk.kt.types/-transcription/index.html)? = null, outputTranscription: [Transcription](../../com.google.adk.kt.types/-transcription/index.html)? = null, liveSessionId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, liveSessionResumptionUpdate: [LiveServerSessionResumptionUpdate](../../com.google.adk.kt.types/-live-server-session-resumption-update/index.html)? = null, voiceActivity: [VoiceActivity](../../com.google.adk.kt.types/-voice-activity/index.html)? = null)

## Types

[Builder](-builder/index.html)

Link copied to clipboard

common

class [Builder](-builder/index.html)

Fluent builder for [Event](index.html), provided primarily for Java callers. Any property left unset falls back to the same default as the constructor.

[Companion](-companion/index.html)

Link copied to clipboard

common

object [Companion](-companion/index.html)

## Properties

[actions](actions.html)

Link copied to clipboard

common

val [actions](actions.html): [EventActions](../-event-actions/index.html)

Optional actions associated with this event.

[author](author.html)

Link copied to clipboard

common

@[EncodeDefault](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-encode-default/index.html)(mode = [EncodeDefault.Mode.ALWAYS](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-encode-default/-mode/-a-l-w-a-y-s/index.html))

val [author](author.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The author of the event, such as the name of the agent or node or "user"; defaults to `""` and is stamped with the workflow or node name when emitted from a workflow node.

[avgLogProbs](avg-log-probs.html)

Link copied to clipboard

common

@[SerialName](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serial-name/index.html)(value = "avgLogprobs")

val [avgLogProbs](avg-log-probs.html): [Double](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-double/index.html)?

The average log probabilities of the generated tokens.

[branch](branch.html)

Link copied to clipboard

common

val [branch](branch.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The branch of the event. The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3. Branch is used when multiple sub-agents shouldn't see their peer agents' conversation history.

[cacheMetadata](cache-metadata.html)

Link copied to clipboard

common

val [cacheMetadata](cache-metadata.html): [CacheMetadata](../../com.google.adk.kt.models/-cache-metadata/index.html)?

Context cache metadata associated with this event's LLM response, used to carry cache state across turns. `null` when context caching is disabled.

[citationMetadata](citation-metadata.html)

Link copied to clipboard

common

val [citationMetadata](citation-metadata.html): [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)?

[content](content.html)

Link copied to clipboard

common

val [content](content.html): [Content](../../com.google.adk.kt.types/-content/index.html)?

The content of the event.

[customMetadata](custom-metadata.html)

Link copied to clipboard

common

val [customMetadata](custom-metadata.html): [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?>?

[errorCode](error-code.html)

Link copied to clipboard

common

val [errorCode](error-code.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

An error code if an error occurred during the event processing.

[errorMessage](error-message.html)

Link copied to clipboard

common

val [errorMessage](error-message.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

A human-readable error message if an error occurred.

[finishReason](finish-reason.html)

Link copied to clipboard

common

val [finishReason](finish-reason.html): [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)?

The reason the LLM generation finished.

[groundingMetadata](grounding-metadata.html)

Link copied to clipboard

common

val [groundingMetadata](grounding-metadata.html): [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)?

The grounding metadata of the event.

[id](id.html)

Link copied to clipboard

common

@[EncodeDefault](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-encode-default/index.html)(mode = [EncodeDefault.Mode.ALWAYS](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-encode-default/-mode/-a-l-w-a-y-s/index.html))

val [id](id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The event id.

[inputTranscription](input-transcription.html)

Link copied to clipboard

common

val [inputTranscription](input-transcription.html): [Transcription](../../com.google.adk.kt.types/-transcription/index.html)?

Transcription of the audio the user sent on a live connection.

[interactionStatus](interaction-status.html)

Link copied to clipboard

common

val [interactionStatus](interaction-status.html): [InteractionStatus](../../com.google.adk.kt.types/-interaction-status/index.html)?

Whether the model is still working on the prompt, reported only with [turnComplete](../../../google-adk-kotlin-core/com.google.adk.kt.events/-event/--root--.html); see [InteractionStatus](../../com.google.adk.kt.types/-interaction-status/index.html). On a completed turn, `null` means the model is done.

[interrupted](interrupted.html)

Link copied to clipboard

common

val [interrupted](interrupted.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

True if the generation of this event was interrupted.

[invocationId](invocation-id.html)

Link copied to clipboard

common

val [invocationId](invocation-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

Id of the invocation that this event belongs to.

[isFinalResponse](is-final-response.html)

Link copied to clipboard

common

val [isFinalResponse](is-final-response.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Returns true if this event is the final response of an agent turn — i.e. it terminates the per-turn model loop in [com.google.adk.kt.agents.LlmAgent.executeTurns](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-llm-agent/execute-turns.html). Matches ADK Python's `Event.is_final_response()`: `skipSummarization` or a non-empty `longRunningToolIds` set both mark the event as final, otherwise the event is final iff it carries no function calls, no function responses, is not a partial streaming chunk, and has no trailing code-execution-result part.

[liveSessionId](live-session-id.html)

Link copied to clipboard

common

val [liveSessionId](live-session-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

Identifier of the live session this event came from.

[liveSessionResumptionUpdate](live-session-resumption-update.html)

Link copied to clipboard

common

val [liveSessionResumptionUpdate](live-session-resumption-update.html): [LiveServerSessionResumptionUpdate](../../com.google.adk.kt.types/-live-server-session-resumption-update/index.html)?

A resumption handle issued by the live server.

[longRunningToolIds](long-running-tool-ids.html)

Link copied to clipboard

common

val [longRunningToolIds](long-running-tool-ids.html): [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)>

Set of ids of the long running function calls. Agent client will know from this field about which function call is long running.

[modelVersion](model-version.html)

Link copied to clipboard

common

val [modelVersion](model-version.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The model version used to generate the response.

[nodeInfo](node-info.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [NodeInfoNullIfEmptySerializer::class](../../../google-adk-kotlin-core/com.google.adk.kt.workflow/-node-info-null-if-empty-serializer/index.html))

val [nodeInfo](node-info.html): [NodeInfo](../../com.google.adk.kt.workflow/-node-info/index.html)?

Identifies the workflow-node activation that emitted this event; `null` outside a workflow.

[output](output.html)

Link copied to clipboard

common

val [output](output.html): [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)?

For a workflow node, the value handed to successors, distinct from [content](../../../google-adk-kotlin-core/com.google.adk.kt.events/-event/--root--.html). Holds a JSON-native value (map with string keys, list, string, number, boolean, null, `JsonElement`) or a [Content](../../com.google.adk.kt.types/-content/index.html).

[outputTranscription](output-transcription.html)

Link copied to clipboard

common

val [outputTranscription](output-transcription.html): [Transcription](../../com.google.adk.kt.types/-transcription/index.html)?

Transcription of the audio the model returned on a live connection.

[partial](partial.html)

Link copied to clipboard

common

val [partial](partial.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

True for incomplete chunks from the LLM streaming response. The last chunk's partial is false.

[timestamp](timestamp.html)

Link copied to clipboard

common

@[EncodeDefault](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-encode-default/index.html)(mode = [EncodeDefault.Mode.ALWAYS](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-encode-default/-mode/-a-l-w-a-y-s/index.html))

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)(with = [LenientEpochMillisSerializer::class](../../../google-adk-kotlin-core/com.google.adk.kt.serialization/-lenient-epoch-millis-serializer/index.html))

val [timestamp](timestamp.html): [Long](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html)

The timestamp of the event.

[turnComplete](turn-complete.html)

Link copied to clipboard

common

val [turnComplete](turn-complete.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

True if this event marks the completion of a turn.

[turnCompleteReason](turn-complete-reason.html)

Link copied to clipboard

common

val [turnCompleteReason](turn-complete-reason.html): [TurnCompleteReason](../../com.google.adk.kt.types/-turn-complete-reason/index.html)?

Why the model ended its turn, when the live server reports a reason other than ordinary completion.

[usageMetadata](usage-metadata.html)

Link copied to clipboard

common

val [usageMetadata](usage-metadata.html): [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)?

Metadata about the token usage for the LLM call.

[voiceActivity](voice-activity.html)

Link copied to clipboard

common

val [voiceActivity](voice-activity.html): [VoiceActivity](../../com.google.adk.kt.types/-voice-activity/index.html)?

A voice activity signal from the live server, marking where it detected speech starting or stopping.

## Functions

[contentText](content-text.html)

Link copied to clipboard

common

@[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html)

fun [contentText](content-text.html)(separator: [CharSequence](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-char-sequence/index.html) = "", includeThoughts: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

Returns this event's [content](../../../google-adk-kotlin-core/com.google.adk.kt.events/-event/--root--.html) text joined with [separator](content-text.html) (none by default), or "" when the event has no content; forwards [includeThoughts](content-text.html) to [Content.text](../../com.google.adk.kt.types/-content/text.html).

[functionCalls](function-calls.html)

Link copied to clipboard

common

fun [functionCalls](function-calls.html)(): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[FunctionCall](../../com.google.adk.kt.types/-function-call/index.html)>

Returns all function calls from this event.

[functionResponses](function-responses.html)

Link copied to clipboard

common

fun [functionResponses](function-responses.html)(): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[FunctionResponse](../../com.google.adk.kt.types/-function-response/index.html)>

Returns all function responses from this event.

[hasTrailingCodeExecutionResult](has-trailing-code-execution-result.html)

Link copied to clipboard

common

fun [hasTrailingCodeExecutionResult](has-trailing-code-execution-result.html)(): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Returns true if the last part of this event is a code-execution result. Mirrors ADK Java's `Event.hasTrailingCodeExecutionResult()`, keeping such an event out of [isFinalResponse](is-final-response.html) so the turn loop runs again to let the model act on the result.

[populateClientFunctionCallId](populate-client-function-call-id.html)

Link copied to clipboard

common

fun [populateClientFunctionCallId](populate-client-function-call-id.html)(): [Event](index.html)

Scans a model response event's parts for function calls missing an ID and generates one for them.

[toBuilder](to-builder.html)

Link copied to clipboard

common

fun [toBuilder](to-builder.html)(): [Event.Builder](-builder/index.html)

Returns a [Builder](-builder/index.html) initialized with this instance's properties, primarily for Java callers. Prefer it over `copy` from Java: `copy` takes every property positionally, so its signature changes whenever a property is added.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
