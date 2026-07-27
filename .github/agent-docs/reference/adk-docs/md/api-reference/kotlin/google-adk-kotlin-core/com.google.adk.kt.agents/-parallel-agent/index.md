toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/ParallelAgent

# ParallelAgent

class [ParallelAgent](index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](../-base-agent/index.html)> = emptyList(), val beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), val afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList()) : [BaseAgent](../-base-agent/index.html)

A shell agent that runs its sub-agents in parallel in an isolated manner.

This approach is beneficial for scenarios requiring multiple perspectives or attempts on a single task, such as:

  * Running different algorithms simultaneously.

  * Generating multiple responses for review by a subsequent evaluation agent.




MembersMembers & Extensions

## Constructors

[ParallelAgent](-parallel-agent.html)

Link copied to clipboard

constructor(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](../-base-agent/index.html)> = emptyList(), beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList())

## Properties

[afterAgentCallbacks](../-base-agent/after-agent-callbacks.html)

Link copied to clipboard

val [afterAgentCallbacks](../-base-agent/after-agent-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../../com.google.adk.kt.callbacks/-after-agent-callback/index.html)>

List of callbacks to run after the agent executes.

[beforeAgentCallbacks](../-base-agent/before-agent-callbacks.html)

Link copied to clipboard

val [beforeAgentCallbacks](../-base-agent/before-agent-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../../com.google.adk.kt.callbacks/-before-agent-callback/index.html)>

List of callbacks to run before the agent executes.

[description](../-base-agent/description.html)

Link copied to clipboard

open val [description](../-base-agent/description.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The description of the agent.

[disallowTransferToParent](../-base-agent/disallow-transfer-to-parent.html)

Link copied to clipboard

val [disallowTransferToParent](../-base-agent/disallow-transfer-to-parent.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

When `true`, the framework will not route the next user turn back to this agent after the parent transfers control to it; instead the next turn falls back to the root agent. Set this on utility sub-agents the parent calls and returns from (translators, summarizers, classifiers). Leave at the default `false` for sub-agents that should keep handling follow-up turns directly (e.g. billing, support).

[disallowTransferToPeers](../-base-agent/disallow-transfer-to-peers.html)

Link copied to clipboard

val [disallowTransferToPeers](../-base-agent/disallow-transfer-to-peers.html): [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false

When `true`, prevents this agent from transferring sideways to a peer agent under the same parent. Typically set together with [disallowTransferToParent](../-base-agent/disallow-transfer-to-parent.html) on one-shot utility agents. Violations are surfaced by the runner as `IllegalArgumentException`.

[name](../-base-agent/name.html)

Link copied to clipboard

val [name](../-base-agent/name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The name of the agent.

[subAgents](../-base-agent/sub-agents.html)

Link copied to clipboard

val [subAgents](../-base-agent/sub-agents.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](../-base-agent/index.html)>

List of sub-agents.

## Functions

[findAgent](../find-agent.html)

Link copied to clipboard

fun [BaseAgent](../-base-agent/index.html).[findAgent](../find-agent.html)(targetName: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)): [BaseAgent](../-base-agent/index.html)?

Finds an agent with the given name in this agent's subtree (including itself).

[runAsync](../-base-agent/run-async.html)

Link copied to clipboard

fun [runAsync](../-base-agent/run-async.html)(parentContext: [InvocationContext](../-invocation-context/index.html)): Flow<[Event](../../com.google.adk.kt.events/-event/index.html)>

Public entry point for executing the agent asynchronously (text-based).

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
