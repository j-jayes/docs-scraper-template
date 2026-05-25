toggle menu

[ google-adk-kotlin ](../../index.html)

0.1.0 

common

switch theme

search in API

[google-adk-kotlin-core](../index.html)/com.google.adk.kt.agents

# Package-level declarations

TypesFunctions

## Types

[AgentState](-agent-state/index.html)

Link copied to clipboard

interface [AgentState](-agent-state/index.html)

Interface for agent-specific state classes in ADK.

[BaseAgent](-base-agent/index.html)

Link copied to clipboard

abstract class [BaseAgent](-base-agent/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](-base-agent/index.html)> = emptyList(), val beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), val afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList(), val disallowTransferToParent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val disallowTransferToPeers: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Base class for all agents.

[CallbackContext](-callback-context/index.html)

Link copied to clipboard

class [CallbackContext](-callback-context/index.html)(invocationContext: [InvocationContext](-invocation-context/index.html), eventActions: [EventActions](../com.google.adk.kt.events/-event-actions/index.html)? = null) : [ReadonlyContext](-readonly-context/index.html)

The context provided to agents and tools during a callback, such as when a tool is run.

[Instruction](-instruction/index.html)

Link copied to clipboard

sealed interface [Instruction](-instruction/index.html)

A unit of instruction provided to an [LlmAgent](-llm-agent/index.html).

[InvocationContext](-invocation-context/index.html)

Link copied to clipboard

data class [InvocationContext](-invocation-context/index.html)(val session: [Session](../com.google.adk.kt.sessions/-session/index.html), val runConfig: [RunConfig](-run-config/index.html)? = null, val agent: [BaseAgent](-base-agent/index.html), val branch: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)? = null, val invocationId: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "e-" + Uuid.random(), val artifactService: [ArtifactService](../com.google.adk.kt.artifacts/-artifact-service/index.html)? = null, val memoryService: [MemoryService](../com.google.adk.kt.memory/-memory-service/index.html)? = null, val sessionService: [SessionService](../com.google.adk.kt.sessions/-session-service/index.html)? = null, val resumabilityConfig: [ResumabilityConfig](-resumability-config/index.html)? = null, val userContent: [Content](../com.google.adk.kt.types/-content/index.html)? = null, val agentStates: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [TypedData](-typed-data/index.html)> = concurrentMutableMapOf(), val endOfAgents: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html)> = concurrentMutableMapOf(), val extraTools: [MutableMap](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-mutable-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [BaseTool](../com.google.adk.kt.tools/-base-tool/index.html)> = concurrentMutableMapOf(), var isEndOfInvocation: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, var isPaused: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val pluginManager: [PluginManager](../com.google.adk.kt.plugins/-plugin-manager/index.html) = PluginManager())

An invocation context represents the data of a single invocation of an agent.

[LlmAgent](-llm-agent/index.html)

Link copied to clipboard

class [LlmAgent](-llm-agent/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val model: [Model](../com.google.adk.kt.models/-model/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](-base-agent/index.html)> = emptyList(), val beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), val afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList(), val disallowTransferToParent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val disallowTransferToPeers: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val tools: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseTool](../com.google.adk.kt.tools/-base-tool/index.html)> = emptyList(), val toolsets: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Toolset](../com.google.adk.kt.tools/-toolset/index.html)> = emptyList(), val generateContentConfig: [GenerateContentConfig](../com.google.adk.kt.types/-generate-content-config/index.html)? = null, val instruction: [Instruction](-instruction/index.html)? = null, val staticInstruction: [Content](../com.google.adk.kt.types/-content/index.html)? = null, val beforeModelCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeModelCallback](../com.google.adk.kt.callbacks/-before-model-callback/index.html)> = emptyList(), val afterModelCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterModelCallback](../com.google.adk.kt.callbacks/-after-model-callback/index.html)> = emptyList(), val beforeToolCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeToolCallback](../com.google.adk.kt.callbacks/-before-tool-callback/index.html)> = emptyList(), val afterToolCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterToolCallback](../com.google.adk.kt.callbacks/-after-tool-callback/index.html)> = emptyList(), val inputSchema: [Schema](../com.google.adk.kt.types/-schema/index.html)? = null, val onModelErrorCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnModelErrorCallback](../com.google.adk.kt.callbacks/-on-model-error-callback/index.html)> = emptyList(), val onToolErrorCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnToolErrorCallback](../com.google.adk.kt.callbacks/-on-tool-error-callback/index.html)> = emptyList(), val includeContents: [LlmAgent.IncludeContents](-llm-agent/-include-contents/index.html) = IncludeContents.DEFAULT) : [BaseAgent](-base-agent/index.html)

LLM-based Agent.

[LoopAgent](-loop-agent/index.html)

Link copied to clipboard

class [LoopAgent](-loop-agent/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val maxIterations: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)? = null, val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](-base-agent/index.html)> = emptyList(), val beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), val afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList()) : [BaseAgent](-base-agent/index.html)

A shell agent that runs its sub-agents in a loop.

[LoopAgentState](-loop-agent-state/index.html)

Link copied to clipboard

data class [LoopAgentState](-loop-agent-state/index.html)(val currentSubAgent: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val timesLooped: [Int](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-int/index.html)) : [AgentState](-agent-state/index.html)

Persistent state of a [LoopAgent](-loop-agent/index.html).

[ParallelAgent](-parallel-agent/index.html)

Link copied to clipboard

class [ParallelAgent](-parallel-agent/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](-base-agent/index.html)> = emptyList(), val beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), val afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList()) : [BaseAgent](-base-agent/index.html)

A shell agent that runs its sub-agents in parallel in an isolated manner.

[ReadonlyContext](-readonly-context/index.html)

Link copied to clipboard

interface [ReadonlyContext](-readonly-context/index.html)

A readonly view of the invocation context.

[ResumabilityConfig](-resumability-config/index.html)

Link copied to clipboard

data class [ResumabilityConfig](-resumability-config/index.html) @[ExperimentalResumabilityFeature](../com.google.adk.kt.annotations/-experimental-resumability-feature/index.html) constructor(val isResumable: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Configuration for resumability in ADK.

[RunConfig](-run-config/index.html)

Link copied to clipboard

data class [RunConfig](-run-config/index.html)(val streamingMode: [StreamingMode](-streaming-mode/index.html) = StreamingMode.NONE, val customMetadata: [Map](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-map/index.html)<[String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), [Any](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-any/index.html)>? = null)

Configs for runtime behavior of agents.

[SequentialAgent](-sequential-agent/index.html)

Link copied to clipboard

class [SequentialAgent](-sequential-agent/index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](-base-agent/index.html)> = emptyList(), val beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), val afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList()) : [BaseAgent](-base-agent/index.html)

A shell agent that runs its sub-agents in sequence.

[SequentialAgentState](-sequential-agent-state/index.html)

Link copied to clipboard

data class [SequentialAgentState](-sequential-agent-state/index.html)(val currentSubAgent: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)) : [AgentState](-agent-state/index.html)

Persistent state of a [SequentialAgent](-sequential-agent/index.html).

[StreamingMode](-streaming-mode/index.html)

Link copied to clipboard

enum [StreamingMode](-streaming-mode/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[StreamingMode](-streaming-mode/index.html)>

Streaming modes for agent execution.

[TypedData](-typed-data/index.html)

Link copied to clipboard

sealed class [TypedData](-typed-data/index.html)

A type-safe hierarchy for agent state variables, ensuring primitives don't collapse.

## Functions

[findAgent](find-agent.html)

Link copied to clipboard

fun [BaseAgent](-base-agent/index.html).[findAgent](find-agent.html)(targetName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)): [BaseAgent](-base-agent/index.html)?

Finds an agent with the given name in this agent's subtree (including itself).

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
