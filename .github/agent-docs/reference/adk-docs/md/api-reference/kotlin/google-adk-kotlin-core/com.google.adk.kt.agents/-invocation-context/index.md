toggle menu

[ google-adk-kotlin ](../../../index.html)

0.1.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/InvocationContext

# InvocationContext

data class [InvocationContext](index.html)(val session: [Session](../../com.google.adk.kt.sessions/-session/index.html), val runConfig: [RunConfig](../-run-config/index.html)? = null, val agent: [BaseAgent](../-base-agent/index.html), val branch: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "e-" + Uuid.random(), val artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = null, val memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = null, val sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)? = null, val resumabilityConfig: [ResumabilityConfig](../-resumability-config/index.html)? = null, val userContent: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, val agentStates: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [TypedData](../-typed-data/index.html)> = concurrentMutableMapOf(), val endOfAgents: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)> = concurrentMutableMapOf(), val extraTools: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)> = concurrentMutableMapOf(), var isEndOfInvocation: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, var isPaused: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html) = PluginManager())

An invocation context represents the data of a single invocation of an agent.

An invocation:

  1. Starts with a user message and ends with a final response.

  2. Can contain one or multiple agent calls.

  3. Is handled by runner.run_async().




An invocation runs an agent until it does not request to transfer to another agent.

An agent call:

  1. Is handled by agent.run().

  2. Ends when agent.run() ends.




An LLM agent call is an agent with a BaseLLMFlow. An LLM agent call can contain one or multiple steps.

An LLM agent runs steps in a loop until:

  1. A final response is generated.

  2. The agent transfers to another agent.

  3. The end_invocation is set to true by any callbacks or tools.




A step:

  1. Calls the LLM only once and yields its response.

  2. Calls the tools and yields their responses if requested.




The summarization of the function response is considered another step, since it is another llm call. A step ends when it's done calling llm and tools, or if the end_invocation is set to true at any time.
    
    
        ┌─────────────────────── invocation ──────────────────────────┐  
        ┌──────────── llm_agent_call_1 ────────────┐ ┌─ agent_call_2 ─┐  
        ┌──── step_1 ────────┐ ┌───── step_2 ──────┐  
        [call_llm] [call_tool] [call_llm] [transfer]

Content copied to clipboard

Members

## Constructors

[InvocationContext](-invocation-context.html)

Link copied to clipboard

constructor(session: [Session](../../com.google.adk.kt.sessions/-session/index.html), runConfig: [RunConfig](../-run-config/index.html)? = null, agent: [BaseAgent](../-base-agent/index.html), branch: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "e-" + Uuid.random(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = null, memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = null, sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)? = null, resumabilityConfig: [ResumabilityConfig](../-resumability-config/index.html)? = null, userContent: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, agentStates: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [TypedData](../-typed-data/index.html)> = concurrentMutableMapOf(), endOfAgents: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)> = concurrentMutableMapOf(), extraTools: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)> = concurrentMutableMapOf(), isEndOfInvocation: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, isPaused: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html) = PluginManager())

## Properties

[agent](agent.html)

Link copied to clipboard

val [agent](agent.html): [BaseAgent](../-base-agent/index.html)

The current agent of this invocation context. Readonly.

[agentStates](agent-states.html)

Link copied to clipboard

val [agentStates](agent-states.html): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [TypedData](../-typed-data/index.html)>

The state of the agent for this invocation.

[artifactService](artifact-service.html)

Link copied to clipboard

val [artifactService](artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = null

[branch](branch.html)

Link copied to clipboard

val [branch](branch.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null

The branch of the invocation context.

[endOfAgents](end-of-agents.html)

Link copied to clipboard

val [endOfAgents](end-of-agents.html): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)>

The end of agent status for each agent in this invocation.

[extraTools](extra-tools.html)

Link copied to clipboard

val [extraTools](extra-tools.html): [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)>

Extra tools injected dynamically during invocation (e.g., by SequentialAgent).

[invocationId](invocation-id.html)

Link copied to clipboard

val [invocationId](invocation-id.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The id of this invocation context. Readonly.

[isEndOfInvocation](is-end-of-invocation.html)

Link copied to clipboard

@[Volatile](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.jvm/-volatile/index.html)

var [isEndOfInvocation](is-end-of-invocation.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)

Whether to end this invocation.

[isPaused](is-paused.html)

Link copied to clipboard

@[Volatile](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.jvm/-volatile/index.html)

var [isPaused](is-paused.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)

Whether this invocation is paused.

[isResumable](is-resumable.html)

Link copied to clipboard

val [isResumable](is-resumable.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)

Returns whether the current invocation is resumable.

[memoryService](memory-service.html)

Link copied to clipboard

val [memoryService](memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = null

[pluginManager](plugin-manager.html)

Link copied to clipboard

val [pluginManager](plugin-manager.html): [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html)

The manager for keeping track of plugins in this invocation.

[resumabilityConfig](resumability-config.html)

Link copied to clipboard

val [resumabilityConfig](resumability-config.html): [ResumabilityConfig](../-resumability-config/index.html)? = null

Optional resumability configuration for this invocation.

[runConfig](run-config.html)

Link copied to clipboard

val [runConfig](run-config.html): [RunConfig](../-run-config/index.html)? = null

Configurations for live agents under this invocation.

[session](session.html)

Link copied to clipboard

val [session](session.html): [Session](../../com.google.adk.kt.sessions/-session/index.html)

The current session of this invocation context. Readonly.

[sessionService](session-service.html)

Link copied to clipboard

val [sessionService](session-service.html): [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)? = null

[userContent](user-content.html)

Link copied to clipboard

val [userContent](user-content.html): [Content](../../com.google.adk.kt.types/-content/index.html)? = null

The user content that started this invocation. Readonly.

## Functions

[branch](branch.html)

Link copied to clipboard

fun [branch](branch.html)(childAgent: [BaseAgent](../-base-agent/index.html)): [InvocationContext](index.html)

Creates a new InvocationContext for a child agent, derived from this context. Appends the given agent's name to the branch path.

[executeSingleFunctionCall](execute-single-function-call.html)

Link copied to clipboard

suspend fun [executeSingleFunctionCall](execute-single-function-call.html)(functionCall: [FunctionCall](../../com.google.adk.kt.types/-function-call/index.html), tools: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)>, toolConfirmation: [ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html)? = null): [Event](../../com.google.adk.kt.events/-event/index.html)?

Executes a single function call synchronously and builds a corresponding response event.

[findMatchingFunctionCall](find-matching-function-call.html)

Link copied to clipboard

suspend fun [findMatchingFunctionCall](find-matching-function-call.html)(functionResponseEvent: [Event](../../com.google.adk.kt.events/-event/index.html)): [Event](../../com.google.adk.kt.events/-event/index.html)?

Finds the function call event in the current invocation that matches the function response id.

[getEvents](get-events.html)

Link copied to clipboard

suspend fun [getEvents](get-events.html)(currentInvocation: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, currentBranch: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Returns the events from the current session.

[handleFunctionCalls](handle-function-calls.html)

Link copied to clipboard

suspend fun [handleFunctionCalls](handle-function-calls.html)(functionCalls: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[FunctionCall](../../com.google.adk.kt.types/-function-call/index.html)>, tools: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)>, filters: [Set](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)> = emptySet(), toolConfirmations: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html)>? = null): [Event](../../com.google.adk.kt.events/-event/index.html)?

Processes a list of function calls by executing them efficiently and safely.

[populateInvocationAgentStates](populate-invocation-agent-states.html)

Link copied to clipboard

suspend fun [populateInvocationAgentStates](populate-invocation-agent-states.html)()

Populates agent states for the current invocation if it is resumable.

[resetSubAgentStates](reset-sub-agent-states.html)

Link copied to clipboard

fun [resetSubAgentStates](reset-sub-agent-states.html)(agentName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html))

Resets the state of all sub-agents of the given agent recursively.

[setAgentState](set-agent-state.html)

Link copied to clipboard

fun [setAgentState](set-agent-state.html)(agentName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), agentState: [TypedData](../-typed-data/index.html)? = null, endOfAgent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Set state of an agent explicitly. Does not implicitly initialize.

[shouldPauseInvocation](should-pause-invocation.html)

Link copied to clipboard

fun [shouldPauseInvocation](should-pause-invocation.html)(event: [Event](../../com.google.adk.kt.events/-event/index.html)): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)

Returns whether to pause the invocation right after this event.

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
