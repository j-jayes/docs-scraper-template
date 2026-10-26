[ google-adk-kotlin ](../../index.html) Toggle table of contents 

1.4.0 

common

Target filter __

    * common 


Switch theme 

Search in API 

Skip to content

google-adk-kotlin  __




[google-adk-kotlin-core](../index.html)/com.google.adk.kt.agents

# Package-level declarations

TypesFunctions

## Types

[AgentState](-agent-state/index.html)

Link copied to clipboard

common

interface [AgentState](-agent-state/index.html)

Interface for agent-specific state classes in ADK.

[BaseAgent](-base-agent/index.html)

Link copied to clipboard

common

abstract class [BaseAgent](-base-agent/index.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", val subAgents: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](-base-agent/index.html)> = emptyList(), val beforeAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), val afterAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList(), val disallowTransferToParent: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val disallowTransferToPeers: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false) : [BaseNode](../com.google.adk.kt.workflow/-base-node/index.html)

Base class for all agents.

[CallbackContext](-callback-context/index.html)

Link copied to clipboard

common

class [CallbackContext](-callback-context/index.html)(invocationContext: [InvocationContext](-invocation-context/index.html), eventActions: [EventActions](../com.google.adk.kt.events/-event-actions/index.html)? = null) : [Context](-context/index.html)

Context passed to agent and model callbacks.

[Context](-context/index.html)

Link copied to clipboard

common

open class [Context](-context/index.html)(val invocationContext: [InvocationContext](-invocation-context/index.html), actions: [EventActions](../com.google.adk.kt.events/-event-actions/index.html)? = null, val functionCallId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val toolConfirmation: [ToolConfirmation](../com.google.adk.kt.events/-tool-confirmation/index.html)? = null, val eventId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null) : [ReadonlyContext](-readonly-context/index.html), [ReadonlyToolContext](../com.google.adk.kt.tools/-readonly-tool-context/index.html)

Execution context passed to agent callbacks, model callbacks, tools, and workflow nodes during an invocation.

[ContextCacheConfig](-context-cache-config/index.html)

Link copied to clipboard

common

data class [ContextCacheConfig](-context-cache-config/index.html) @[ExperimentalContextCachingFeature](../com.google.adk.kt.annotations/-experimental-context-caching-feature/index.html) constructor(val cacheIntervals: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 10, val ttl: [Duration](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.time/-duration/index.html) = 1800.seconds, val minTokens: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 0, val createHttpOptions: [HttpOptions](../com.google.adk.kt.types/-http-options/index.html)? = null)

Configuration for context caching across all agents in an app.

[ContextFrameworkData](-context-framework-data/index.html)

Link copied to clipboard

common

data class [ContextFrameworkData](-context-framework-data/index.html)(val callbackContextData: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = concurrentMutableMapOf())

Framework-internal per-invocation data holder. Groups scratch state used by ADK's own machinery and the ADK Java interop so it stays off [InvocationContext](-invocation-context/index.html)'s public constructor. The type itself needs no opt-in; its public members are marked [FrameworkInternalApi](../com.google.adk.kt.annotations/-framework-internal-api/index.html).

[Instruction](-instruction/index.html)

Link copied to clipboard

common

sealed interface [Instruction](-instruction/index.html)

A unit of instruction provided to an [LlmAgent](-llm-agent/index.html).

[InvocationContext](-invocation-context/index.html)

Link copied to clipboard

common

data class [InvocationContext](-invocation-context/index.html)(val session: [Session](../com.google.adk.kt.sessions/-session/index.html), val runConfig: [RunConfig](-run-config/index.html)? = null, val agent: [BaseAgent](-base-agent/index.html), val branch: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val invocationId: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "e-" + Uuid.random(), val artifactService: [ArtifactService](../com.google.adk.kt.artifacts/-artifact-service/index.html)? = null, val memoryService: [MemoryService](../com.google.adk.kt.memory/-memory-service/index.html)? = null, val sessionService: [SessionService](../com.google.adk.kt.sessions/-session-service/index.html)? = null, val resumabilityConfig: [ResumabilityConfig](-resumability-config/index.html)? = null, val eventsCompactionConfig: [EventsCompactionConfig](../com.google.adk.kt.summarizer/-events-compaction-config/index.html)? = null, val contextCacheConfig: [ContextCacheConfig](-context-cache-config/index.html)? = null, val userContent: [Content](../com.google.adk.kt.types/-content/index.html)? = null, val agentStates: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [TypedData](-typed-data/index.html)> = concurrentMutableMapOf(), val endOfAgents: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)> = concurrentMutableMapOf(), val extraTools: [MutableMap](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../com.google.adk.kt.tools/-base-tool/index.html)> = concurrentMutableMapOf(), val frameworkData: [ContextFrameworkData](-context-framework-data/index.html) = ContextFrameworkData(), var isEndOfInvocation: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val pluginManager: [PluginManager](../com.google.adk.kt.plugins/-plugin-manager/index.html) = PluginManager(), invocationCostManager: [InvocationCostManager](-invocation-cost-manager/index.html) = InvocationCostManager(), val node: [Node](../com.google.adk.kt.workflow/-node/index.html)? = null)

An invocation context represents the data of a single invocation of an agent.

[InvocationCostManager](-invocation-cost-manager/index.html)

Link copied to clipboard

common

class [InvocationCostManager](-invocation-cost-manager/index.html)

Per-invocation LLM-call counter for enforcing [RunConfig.maxLlmCalls](-run-config/max-llm-calls.html). The type is public only because it is an [InvocationContext](-invocation-context/index.html) constructor-property type; its constructor and members are non-public.

[LiveRequest](-live-request/index.html)

Link copied to clipboard

common

@[ExperimentalLiveApi](../com.google.adk.kt.annotations/-experimental-live-api/index.html)

data class [LiveRequest](-live-request/index.html)(val input: [LiveInput](../com.google.adk.kt.models/-live-input/index.html)? = null, val close: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val stateDelta: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)> = emptyMap())

One item sent to a live agent through a [LiveRequestQueue](-live-request-queue/index.html).

[LiveRequestQueue](-live-request-queue/index.html)

Link copied to clipboard

common

class [LiveRequestQueue](-live-request-queue/index.html) @[ExperimentalLiveApi](../com.google.adk.kt.annotations/-experimental-live-api/index.html) constructor : [AutoCloseable](https://developer.android.com/reference/kotlin/java/lang/AutoCloseable.html)

The input side of a live conversation: everything the user sends reaches the agent through one of these, from any thread and without suspending, so audio can be pushed from a microphone callback or a UI handler without a coroutine.

[LlmAgent](-llm-agent/index.html)

Link copied to clipboard

common

class [LlmAgent](-llm-agent/index.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val model: [Model](../com.google.adk.kt.models/-model/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", subAgents: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](-base-agent/index.html)> = emptyList(), beforeAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), afterAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList(), disallowTransferToParent: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, disallowTransferToPeers: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false, val tools: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseTool](../com.google.adk.kt.tools/-base-tool/index.html)> = emptyList(), val toolsets: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Toolset](../com.google.adk.kt.tools/-toolset/index.html)> = emptyList(), val generateContentConfig: [GenerateContentConfig](../com.google.adk.kt.types/-generate-content-config/index.html)? = null, val instruction: [Instruction](-instruction/index.html)? = null, val staticInstruction: [Content](../com.google.adk.kt.types/-content/index.html)? = null, val beforeModelCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeModelCallback](../com.google.adk.kt.callbacks/-before-model-callback/index.html)> = emptyList(), val afterModelCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterModelCallback](../com.google.adk.kt.callbacks/-after-model-callback/index.html)> = emptyList(), val beforeToolCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeToolCallback](../com.google.adk.kt.callbacks/-before-tool-callback/index.html)> = emptyList(), val afterToolCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterToolCallback](../com.google.adk.kt.callbacks/-after-tool-callback/index.html)> = emptyList(), val inputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, val outputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, val outputKey: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)? = null, val onModelErrorCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnModelErrorCallback](../com.google.adk.kt.callbacks/-on-model-error-callback/index.html)> = emptyList(), val onToolErrorCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnToolErrorCallback](../com.google.adk.kt.callbacks/-on-tool-error-callback/index.html)> = emptyList(), val includeContents: [LlmAgent.IncludeContents](-llm-agent/-include-contents/index.html) = IncludeContents.DEFAULT, val maxSteps: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null) : [BaseAgent](-base-agent/index.html)

LLM-based Agent.

[LlmCallsLimitExceededException](-llm-calls-limit-exceeded-exception/index.html)

Link copied to clipboard

common

class [LlmCallsLimitExceededException](-llm-calls-limit-exceeded-exception/index.html)(message: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : [Exception](https://developer.android.com/reference/kotlin/java/lang/Exception.html)

Thrown when an invocation exceeds [RunConfig.maxLlmCalls](-run-config/max-llm-calls.html).

[LoopAgent](-loop-agent/index.html)

Link copied to clipboard

common

class [LoopAgent](-loop-agent/index.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val maxIterations: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)? = null, description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", subAgents: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](-base-agent/index.html)> = emptyList(), beforeAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), afterAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList()) : [BaseAgent](-base-agent/index.html)

A shell agent that runs its sub-agents in a loop.

[LoopAgentState](-loop-agent-state/index.html)

Link copied to clipboard

common

data class [LoopAgentState](-loop-agent-state/index.html)(val currentSubAgent: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), val timesLooped: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html)) : [AgentState](-agent-state/index.html)

Persistent state of a [LoopAgent](-loop-agent/index.html).

[ParallelAgent](-parallel-agent/index.html)

Link copied to clipboard

common

class [ParallelAgent](-parallel-agent/index.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", subAgents: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](-base-agent/index.html)> = emptyList(), beforeAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), afterAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList()) : [BaseAgent](-base-agent/index.html)

A shell agent that runs its sub-agents in parallel in an isolated manner.

[ReadonlyContext](-readonly-context/index.html)

Link copied to clipboard

common

interface [ReadonlyContext](-readonly-context/index.html)

A readonly view of the invocation context.

[ResumabilityConfig](-resumability-config/index.html)

Link copied to clipboard

common

data class [ResumabilityConfig](-resumability-config/index.html)(val isResumable: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Configuration for resumability in ADK.

[RunConfig](-run-config/index.html)

Link copied to clipboard

common

data class [RunConfig](-run-config/index.html) @[JvmOverloads](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-overloads/index.html) constructor(val streamingMode: [StreamingMode](-streaming-mode/index.html) = StreamingMode.NONE, val maxLlmCalls: [Int](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html) = 500, val customMetadata: [Map](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html)>? = null, val responseModalities: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[Modality](../com.google.adk.kt.types/-modality/index.html)> = emptyList(), val speechConfig: [SpeechConfig](../com.google.adk.kt.types/-speech-config/index.html)? = null, val outputAudioTranscription: [AudioTranscriptionConfig](../com.google.adk.kt.types/-audio-transcription-config/index.html)? = AudioTranscriptionConfig(), val inputAudioTranscription: [AudioTranscriptionConfig](../com.google.adk.kt.types/-audio-transcription-config/index.html)? = AudioTranscriptionConfig(), val realtimeInputConfig: [RealtimeInputConfig](../com.google.adk.kt.types/-realtime-input-config/index.html)? = null, val explicitVadSignal: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val translationConfig: [TranslationConfig](../com.google.adk.kt.types/-translation-config/index.html)? = null, val enableAffectiveDialog: [Boolean](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html)? = null, val proactivity: [ProactivityConfig](../com.google.adk.kt.types/-proactivity-config/index.html)? = null, val sessionResumption: [SessionResumptionConfig](../com.google.adk.kt.types/-session-resumption-config/index.html)? = null, val contextWindowCompression: [ContextWindowCompressionConfig](../com.google.adk.kt.types/-context-window-compression-config/index.html)? = null)

Configs for runtime behavior of agents.

[SequentialAgent](-sequential-agent/index.html)

Link copied to clipboard

common

class [SequentialAgent](-sequential-agent/index.html)(name: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html) = "", subAgents: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](-base-agent/index.html)> = emptyList(), beforeAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), afterAgentCallbacks: [List](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList()) : [BaseAgent](-base-agent/index.html)

A shell agent that runs its sub-agents in sequence.

[SequentialAgentState](-sequential-agent-state/index.html)

Link copied to clipboard

common

data class [SequentialAgentState](-sequential-agent-state/index.html)(val currentSubAgent: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)) : [AgentState](-agent-state/index.html)

Persistent state of a [SequentialAgent](-sequential-agent/index.html).

[StreamingMode](-streaming-mode/index.html)

Link copied to clipboard

common

enum [StreamingMode](-streaming-mode/index.html) : [Enum](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html)<[StreamingMode](-streaming-mode/index.html)>

Streaming modes for agent execution.

[TypedData](-typed-data/index.html)

Link copied to clipboard

common

@[Serializable](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/index.html)

sealed class [TypedData](-typed-data/index.html)

A type-safe hierarchy for agent state variables, ensuring primitives don't collapse.

## Functions

[findAgent](find-agent.html)

Link copied to clipboard

common

fun [BaseAgent](-base-agent/index.html).[findAgent](find-agent.html)(targetName: [String](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html)): [BaseAgent](-base-agent/index.html)?

Finds an agent with the given name in this agent's subtree (including itself).

Generated by  [ Dokka ](https://github.com/Kotlin/dokka)

© 2026 Copyright
