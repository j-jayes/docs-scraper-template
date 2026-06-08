toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.events](../index.html)/Event

# Event

data class [Event](index.html)(val id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = Uuid.random(), val invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val author: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val content: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, val actions: [EventActions](../-event-actions/index.html) = EventActions(), val longRunningToolIds: [Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)> = emptySet(), val partial: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val turnComplete: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val errorCode: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val errorMessage: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val finishReason: [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)? = null, val usageMetadata: [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)? = null, val avgLogProbs: [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html)? = null, val interrupted: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val branch: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val groundingMetadata: [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)? = null, val modelVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val citationMetadata: [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)? = null, val customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>? = null, val timestamp: [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-long/index.html) = Clock.System.now().toEpochMilliseconds())

Represents an event in a session.

Members

## Constructors

[Event](-event.html)

Link copied to clipboard

constructor(id: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = Uuid.random(), invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, author: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), content: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, actions: [EventActions](../-event-actions/index.html) = EventActions(), longRunningToolIds: [Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)> = emptySet(), partial: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, turnComplete: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, errorCode: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, errorMessage: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, finishReason: [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)? = null, usageMetadata: [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)? = null, avgLogProbs: [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html)? = null, interrupted: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, branch: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, groundingMetadata: [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)? = null, modelVersion: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, citationMetadata: [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)? = null, customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>? = null, timestamp: [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-long/index.html) = Clock.System.now().toEpochMilliseconds())

## Properties

[actions](actions.html)

Link copied to clipboard

val [actions](actions.html): [EventActions](../-event-actions/index.html)

Optional actions associated with this event.

[author](author.html)

Link copied to clipboard

val [author](author.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The author of the event, it could be the name of the agent or "user" literal.

[avgLogProbs](avg-log-probs.html)

Link copied to clipboard

val [avgLogProbs](avg-log-probs.html): [Double](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-double/index.html)? = null

The average log probabilities of the generated tokens.

[branch](branch.html)

Link copied to clipboard

val [branch](branch.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

The branch of the event. The format is like agent_1.agent_2.agent_3, where agent_1 is the parent of agent_2, and agent_2 is the parent of agent_3. Branch is used when multiple sub-agents shouldn't see their peer agents' conversation history.

[citationMetadata](citation-metadata.html)

Link copied to clipboard

val [citationMetadata](citation-metadata.html): [CitationMetadata](../../com.google.adk.kt.types/-citation-metadata/index.html)? = null

[content](content.html)

Link copied to clipboard

val [content](content.html): [Content](../../com.google.adk.kt.types/-content/index.html)? = null

The content of the event.

[customMetadata](custom-metadata.html)

Link copied to clipboard

val [customMetadata](custom-metadata.html): [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>? = null

[errorCode](error-code.html)

Link copied to clipboard

val [errorCode](error-code.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

An error code if an error occurred during the event processing.

[errorMessage](error-message.html)

Link copied to clipboard

val [errorMessage](error-message.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

A human-readable error message if an error occurred.

[finishReason](finish-reason.html)

Link copied to clipboard

val [finishReason](finish-reason.html): [FinishReason](../../com.google.adk.kt.types/-finish-reason/index.html)? = null

The reason the LLM generation finished.

[groundingMetadata](grounding-metadata.html)

Link copied to clipboard

val [groundingMetadata](grounding-metadata.html): [GroundingMetadata](../../com.google.adk.kt.types/-grounding-metadata/index.html)? = null

The grounding metadata of the event.

[id](id.html)

Link copied to clipboard

val [id](id.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The event id.

[interrupted](interrupted.html)

Link copied to clipboard

val [interrupted](interrupted.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

True if the generation of this event was interrupted.

[invocationId](invocation-id.html)

Link copied to clipboard

val [invocationId](invocation-id.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

Id of the invocation that this event belongs to.

[isFinalResponse](is-final-response.html)

Link copied to clipboard

val [isFinalResponse](is-final-response.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)

Returns true if this is a final response.

[longRunningToolIds](long-running-tool-ids.html)

Link copied to clipboard

val [longRunningToolIds](long-running-tool-ids.html): [Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)>

Set of ids of the long running function calls. Agent client will know from this field about which function call is long running.

[modelVersion](model-version.html)

Link copied to clipboard

val [modelVersion](model-version.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

The model version used to generate the response.

[partial](partial.html)

Link copied to clipboard

val [partial](partial.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

True for incomplete chunks from the LLM streaming response. The last chunk's partial is false.

[timestamp](timestamp.html)

Link copied to clipboard

val [timestamp](timestamp.html): [Long](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-long/index.html)

The timestamp of the event.

[turnComplete](turn-complete.html)

Link copied to clipboard

val [turnComplete](turn-complete.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

True if this event marks the completion of a turn.

[usageMetadata](usage-metadata.html)

Link copied to clipboard

val [usageMetadata](usage-metadata.html): [UsageMetadata](../../com.google.adk.kt.types/-usage-metadata/index.html)? = null

Metadata about the token usage for the LLM call.

## Functions

[functionCalls](function-calls.html)

Link copied to clipboard

fun [functionCalls](function-calls.html)(): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[FunctionCall](../../com.google.adk.kt.types/-function-call/index.html)>

Returns all function calls from this event.

[functionResponses](function-responses.html)

Link copied to clipboard

fun [functionResponses](function-responses.html)(): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[FunctionResponse](../../com.google.adk.kt.types/-function-response/index.html)>

Returns all function responses from this event.

[populateClientFunctionCallId](populate-client-function-call-id.html)

Link copied to clipboard

fun [populateClientFunctionCallId](populate-client-function-call-id.html)(): [Event](index.html)

Scans a model response event's parts for function calls missing an ID and generates one for them.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
