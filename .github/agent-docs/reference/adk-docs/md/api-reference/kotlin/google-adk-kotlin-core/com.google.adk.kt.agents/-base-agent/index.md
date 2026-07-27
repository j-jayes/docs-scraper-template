toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/BaseAgent

# BaseAgent

abstract class [BaseAgent](index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](index.html)> = emptyList(), val beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), val afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList(), val disallowTransferToParent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val disallowTransferToPeers: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

Base class for all agents.

Implements the Template Method pattern to handle the agent execution lifecycle, including context creation, tracing, and callbacks. Subclasses must implement [runAsyncImpl](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-base-agent/run-async-impl.html) to define specific behavior.

#### Inheritors

[LlmAgent](../-llm-agent/index.html)

[LoopAgent](../-loop-agent/index.html)

[ParallelAgent](../-parallel-agent/index.html)

[SequentialAgent](../-sequential-agent/index.html)

MembersMembers & Extensions

## Constructors

[BaseAgent](-base-agent.html)

Link copied to clipboard

constructor(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](index.html)> = emptyList(), beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList(), disallowTransferToParent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, disallowTransferToPeers: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false)

## Properties

[afterAgentCallbacks](after-agent-callbacks.html)

Link copied to clipboard

val [afterAgentCallbacks](after-agent-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../../com.google.adk.kt.callbacks/-after-agent-callback/index.html)>

List of callbacks to run after the agent executes.

[beforeAgentCallbacks](before-agent-callbacks.html)

Link copied to clipboard

val [beforeAgentCallbacks](before-agent-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../../com.google.adk.kt.callbacks/-before-agent-callback/index.html)>

List of callbacks to run before the agent executes.

[description](description.html)

Link copied to clipboard

open val [description](description.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The description of the agent.

[disallowTransferToParent](disallow-transfer-to-parent.html)

Link copied to clipboard

val [disallowTransferToParent](disallow-transfer-to-parent.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

When `true`, the framework will not route the next user turn back to this agent after the parent transfers control to it; instead the next turn falls back to the root agent. Set this on utility sub-agents the parent calls and returns from (translators, summarizers, classifiers). Leave at the default `false` for sub-agents that should keep handling follow-up turns directly (e.g. billing, support).

[disallowTransferToPeers](disallow-transfer-to-peers.html)

Link copied to clipboard

val [disallowTransferToPeers](disallow-transfer-to-peers.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

When `true`, prevents this agent from transferring sideways to a peer agent under the same parent. Typically set together with [disallowTransferToParent](disallow-transfer-to-parent.html) on one-shot utility agents. Violations are surfaced by the runner as `IllegalArgumentException`.

[name](name.html)

Link copied to clipboard

val [name](name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The name of the agent.

[subAgents](sub-agents.html)

Link copied to clipboard

val [subAgents](sub-agents.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](index.html)>

List of sub-agents.

## Functions

[findAgent](../find-agent.html)

Link copied to clipboard

fun [BaseAgent](index.html).[findAgent](../find-agent.html)(targetName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)): [BaseAgent](index.html)?

Finds an agent with the given name in this agent's subtree (including itself).

[runAsync](run-async.html)

Link copied to clipboard

fun [runAsync](run-async.html)(parentContext: [InvocationContext](../-invocation-context/index.html)): Flow<[Event](../../com.google.adk.kt.events/-event/index.html)>

Public entry point for executing the agent asynchronously (text-based).

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
