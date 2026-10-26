[ google-adk-kotlin ](../../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/InvocationContext

# InvocationContext

common

data class [InvocationContext](index.html)(val session: [Session](../../com.google.adk.kt.sessions/-session/index.html), val runConfig: [RunConfig](../-run-config/index.html)? = null, val agent: [BaseAgent](../-base-agent/index.html), val branch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val invocationId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "e-" + Uuid.random(), val artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = null, val memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = null, val sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)? = null, val resumabilityConfig: [ResumabilityConfig](../-resumability-config/index.html)? = null, val eventsCompactionConfig: [EventsCompactionConfig](../../com.google.adk.kt.summarizer/-events-compaction-config/index.html)? = null, val contextCacheConfig: [ContextCacheConfig](../-context-cache-config/index.html)? = null, val userContent: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, val agentStates: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [TypedData](../-typed-data/index.html)> = concurrentMutableMapOf(), val endOfAgents: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)> = concurrentMutableMapOf(), val extraTools: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)> = concurrentMutableMapOf(), val frameworkData: [ContextFrameworkData](../-context-framework-data/index.html) = ContextFrameworkData(), var isEndOfInvocation: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html) = PluginManager(), invocationCostManager: [InvocationCostManager](../-invocation-cost-manager/index.html) = InvocationCostManager(), val node: [Node](../../com.google.adk.kt.workflow/-node/index.html)? = null)

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

common

constructor(session: [Session](../../com.google.adk.kt.sessions/-session/index.html), runConfig: [RunConfig](../-run-config/index.html)? = null, agent: [BaseAgent](../-base-agent/index.html), branch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, invocationId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "e-" + Uuid.random(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = null, memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = null, sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)? = null, resumabilityConfig: [ResumabilityConfig](../-resumability-config/index.html)? = null, eventsCompactionConfig: [EventsCompactionConfig](../../com.google.adk.kt.summarizer/-events-compaction-config/index.html)? = null, contextCacheConfig: [ContextCacheConfig](../-context-cache-config/index.html)? = null, userContent: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, agentStates: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [TypedData](../-typed-data/index.html)> = concurrentMutableMapOf(), endOfAgents: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)> = concurrentMutableMapOf(), extraTools: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)> = concurrentMutableMapOf(), frameworkData: [ContextFrameworkData](../-context-framework-data/index.html) = ContextFrameworkData(), isEndOfInvocation: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html) = PluginManager(), invocationCostManager: [InvocationCostManager](../-invocation-cost-manager/index.html) = InvocationCostManager(), node: [Node](../../com.google.adk.kt.workflow/-node/index.html)? = null)

constructor(session: [Session](../../com.google.adk.kt.sessions/-session/index.html), runConfig: [RunConfig](../-run-config/index.html)? = null, agent: [BaseAgent](../-base-agent/index.html), branch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, invocationId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "e-" + Uuid.random(), artifactService: [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)? = null, memoryService: [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)? = null, sessionService: [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)? = null, resumabilityConfig: [ResumabilityConfig](../-resumability-config/index.html)? = null, eventsCompactionConfig: [EventsCompactionConfig](../../com.google.adk.kt.summarizer/-events-compaction-config/index.html)? = null, contextCacheConfig: [ContextCacheConfig](../-context-cache-config/index.html)? = null, userContent: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, agentStates: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [TypedData](../-typed-data/index.html)> = concurrentMutableMapOf(), endOfAgents: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)> = concurrentMutableMapOf(), extraTools: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)> = concurrentMutableMapOf(), frameworkData: [ContextFrameworkData](../-context-framework-data/index.html) = ContextFrameworkData(), isEndOfInvocation: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, pluginManager: [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html) = PluginManager(), invocationCostManager: [InvocationCostManager](../-invocation-cost-manager/index.html) = InvocationCostManager())

The 1.1.0 constructor, which had no [node](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-invocation-context/--root--.html). Stays visible because javac skips hidden constructors, so Java code written against 1.1.0 would otherwise fail to compile.

## Properties

[agent](agent.html)

Link copied to clipboard

common

val [agent](agent.html): [BaseAgent](../-base-agent/index.html)

The agent this invocation runs. For a node-rooted invocation this is a NodeViewAgent over the running node, so `agent.name` and the other [BaseAgent](../-base-agent/index.html) members stay correct.

[agentStates](agent-states.html)

Link copied to clipboard

common

val [agentStates](agent-states.html): [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [TypedData](../-typed-data/index.html)>

The state of the agent for this invocation.

[artifactService](artifact-service.html)

Link copied to clipboard

common

val [artifactService](artifact-service.html): [ArtifactService](../../com.google.adk.kt.artifacts/-artifact-service/index.html)?

[branch](branch.html)

Link copied to clipboard

common

val [branch](branch.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)?

The branch of the invocation context.

[contextCacheConfig](context-cache-config.html)

Link copied to clipboard

common

val [contextCacheConfig](context-cache-config.html): [ContextCacheConfig](../-context-cache-config/index.html)?

Optional context cache configuration for this invocation, propagated from the [App](../../com.google.adk.kt.apps/-app/index.html). When `null`, context caching is disabled for the invocation.

[endOfAgents](end-of-agents.html)

Link copied to clipboard

common

val [endOfAgents](end-of-agents.html): [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)>

The end of agent status for each agent in this invocation.

[eventsCompactionConfig](events-compaction-config.html)

Link copied to clipboard

common

val [eventsCompactionConfig](events-compaction-config.html): [EventsCompactionConfig](../../com.google.adk.kt.summarizer/-events-compaction-config/index.html)?

Optional event-compaction configuration for this invocation.

[extraTools](extra-tools.html)

Link copied to clipboard

common

val [extraTools](extra-tools.html): [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)>

Extra tools injected dynamically during invocation (e.g., by SequentialAgent).

[frameworkData](framework-data.html)

Link copied to clipboard

common

val [frameworkData](framework-data.html): [ContextFrameworkData](../-context-framework-data/index.html)

Framework-internal per-invocation data (see [ContextFrameworkData](../-context-framework-data/index.html)). Kept as a dedicated holder so its opt-in-requiring members stay off this public constructor. Not a public API by contract, but the reference itself needs no opt-in; its fields do.

[invocationId](invocation-id.html)

Link copied to clipboard

common

val [invocationId](invocation-id.html): [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)

The id of this invocation context. Readonly.

[isEndOfInvocation](is-end-of-invocation.html)

Link copied to clipboard

common

@[Volatile](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-volatile/index.html)

var [isEndOfInvocation](is-end-of-invocation.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Whether to end this invocation.

[isResumable](is-resumable.html)

Link copied to clipboard

common

val [isResumable](is-resumable.html): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Returns whether the current invocation is resumable.

[memoryService](memory-service.html)

Link copied to clipboard

common

val [memoryService](memory-service.html): [MemoryService](../../com.google.adk.kt.memory/-memory-service/index.html)?

[node](node.html)

Link copied to clipboard

common

val [node](node.html): [Node](../../com.google.adk.kt.workflow/-node/index.html)?

The node this invocation runs, set when rooted on a node graph rather than an agent tree. The go-forward field; once [agent](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-invocation-context/--root--.html) is removed it holds the running unit for every invocation. Readonly.

[pluginManager](plugin-manager.html)

Link copied to clipboard

common

val [pluginManager](plugin-manager.html): [PluginManager](../../com.google.adk.kt.plugins/-plugin-manager/index.html)

The manager for keeping track of plugins in this invocation.

[resumabilityConfig](resumability-config.html)

Link copied to clipboard

common

val [resumabilityConfig](resumability-config.html): [ResumabilityConfig](../-resumability-config/index.html)?

Optional resumability configuration for this invocation.

[runConfig](run-config.html)

Link copied to clipboard

common

val [runConfig](run-config.html): [RunConfig](../-run-config/index.html)?

Configurations for live agents under this invocation.

[session](session.html)

Link copied to clipboard

common

val [session](session.html): [Session](../../com.google.adk.kt.sessions/-session/index.html)

The current session of this invocation context. Readonly.

[sessionService](session-service.html)

Link copied to clipboard

common

val [sessionService](session-service.html): [SessionService](../../com.google.adk.kt.sessions/-session-service/index.html)?

[userContent](user-content.html)

Link copied to clipboard

common

val [userContent](user-content.html): [Content](../../com.google.adk.kt.types/-content/index.html)?

The user content that started this invocation. Readonly.

## Functions

[branch](branch.html)

Link copied to clipboard

common

fun [branch](branch.html)(childAgent: [BaseAgent](../-base-agent/index.html)): [InvocationContext](index.html)

Creates a new InvocationContext for a child agent, derived from this context. Appends the given agent's name to the branch path.

[findMatchingFunctionCall](find-matching-function-call.html)

Link copied to clipboard

common

suspend fun [findMatchingFunctionCall](find-matching-function-call.html)(functionResponseEvent: [Event](../../com.google.adk.kt.events/-event/index.html)): [Event](../../com.google.adk.kt.events/-event/index.html)?

Finds the function call event in the current invocation that matches the function response id.

[getEvents](get-events.html)

Link copied to clipboard

common

suspend fun [getEvents](get-events.html)(currentInvocation: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, currentBranch: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false): [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Event](../../com.google.adk.kt.events/-event/index.html)>

Returns the current session's events from the in-memory [Session.events](../../com.google.adk.kt.sessions/-session/events.html), which [SessionService.appendEvent](../../com.google.adk.kt.sessions/-session-service/append-event.html) keeps in sync. Reads memory rather than re-fetching from the session service each step, matching Python, Java, and Go ADK.

[handleFunctionCalls](handle-function-calls.html)

Link copied to clipboard

common

suspend fun [handleFunctionCalls](handle-function-calls.html)(functionCalls: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[FunctionCall](../../com.google.adk.kt.types/-function-call/index.html)>, tools: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)>, filters: [Set](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-set/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)> = emptySet(), toolConfirmations: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [ToolConfirmation](../../com.google.adk.kt.events/-tool-confirmation/index.html)>? = null): [Event](../../com.google.adk.kt.events/-event/index.html)?

Processes a list of function calls by executing them efficiently and safely.

[incrementLlmCallsCount](increment-llm-calls-count.html)

Link copied to clipboard

common

fun [incrementLlmCallsCount](increment-llm-calls-count.html)()

Counts this LLM call and enforces [RunConfig.maxLlmCalls](../-run-config/max-llm-calls.html).

[populateInvocationAgentStates](populate-invocation-agent-states.html)

Link copied to clipboard

common

suspend fun [populateInvocationAgentStates](populate-invocation-agent-states.html)()

Populates agent states for the current invocation if it is resumable.

[resetSubAgentStates](reset-sub-agent-states.html)

Link copied to clipboard

common

fun [resetSubAgentStates](reset-sub-agent-states.html)(agentName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html))

Resets the state of all sub-agents of the given agent recursively.

[setAgentState](set-agent-state.html)

Link copied to clipboard

common

fun [setAgentState](set-agent-state.html)(agentName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), agentState: [TypedData](../-typed-data/index.html)? = null, endOfAgent: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Set state of an agent explicitly. Does not implicitly initialize.

[shouldPauseInvocation](should-pause-invocation.html)

Link copied to clipboard

common

fun [shouldPauseInvocation](should-pause-invocation.html)(event: [Event](../../com.google.adk.kt.events/-event/index.html)): [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)

Returns whether to pause the invocation right after this event.

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
