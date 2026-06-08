toggle menu

[ google-adk-kotlin ](../../../index.html)

0.2.0 

common

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.agents](../index.html)/LlmAgent

# LlmAgent

class [LlmAgent](index.html)(val name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), val model: [Model](../../com.google.adk.kt.models/-model/index.html), val description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", val subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](../-base-agent/index.html)> = emptyList(), val beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), val afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList(), val disallowTransferToParent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val disallowTransferToPeers: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, val tools: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)> = emptyList(), val toolsets: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Toolset](../../com.google.adk.kt.tools/-toolset/index.html)> = emptyList(), val generateContentConfig: [GenerateContentConfig](../../com.google.adk.kt.types/-generate-content-config/index.html)? = null, val instruction: [Instruction](../-instruction/index.html)? = null, val staticInstruction: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, val beforeModelCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeModelCallback](../../com.google.adk.kt.callbacks/-before-model-callback/index.html)> = emptyList(), val afterModelCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterModelCallback](../../com.google.adk.kt.callbacks/-after-model-callback/index.html)> = emptyList(), val beforeToolCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeToolCallback](../../com.google.adk.kt.callbacks/-before-tool-callback/index.html)> = emptyList(), val afterToolCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterToolCallback](../../com.google.adk.kt.callbacks/-after-tool-callback/index.html)> = emptyList(), val inputSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null, val onModelErrorCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnModelErrorCallback](../../com.google.adk.kt.callbacks/-on-model-error-callback/index.html)> = emptyList(), val onToolErrorCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnToolErrorCallback](../../com.google.adk.kt.callbacks/-on-tool-error-callback/index.html)> = emptyList(), val includeContents: [LlmAgent.IncludeContents](-include-contents/index.html) = IncludeContents.DEFAULT) : [BaseAgent](../-base-agent/index.html)

LLM-based Agent.

When this agent is a sub-agent and the parent transfers control to it via `transfer_to_agent`, the runner decides who handles the _next_ user turn based on the [disallowTransferToParent](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-llm-agent/disallow-transfer-to-parent.html) / [disallowTransferToPeers](../../../google-adk-kotlin-core/com.google.adk.kt.agents/-llm-agent/disallow-transfer-to-peers.html) flags inherited from `BaseAgent` \- see those flags for the full dispatch rules.

MembersMembers & Extensions

## Constructors

[LlmAgent](-llm-agent.html)

Link copied to clipboard

constructor(name: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), model: [Model](../../com.google.adk.kt.models/-model/index.html), description: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html) = "", subAgents: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](../-base-agent/index.html)> = emptyList(), beforeAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../../com.google.adk.kt.callbacks/-before-agent-callback/index.html)> = emptyList(), afterAgentCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../../com.google.adk.kt.callbacks/-after-agent-callback/index.html)> = emptyList(), disallowTransferToParent: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, disallowTransferToPeers: [Boolean](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-boolean/index.html) = false, tools: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)> = emptyList(), toolsets: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Toolset](../../com.google.adk.kt.tools/-toolset/index.html)> = emptyList(), generateContentConfig: [GenerateContentConfig](../../com.google.adk.kt.types/-generate-content-config/index.html)? = null, instruction: [Instruction](../-instruction/index.html)? = null, staticInstruction: [Content](../../com.google.adk.kt.types/-content/index.html)? = null, beforeModelCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeModelCallback](../../com.google.adk.kt.callbacks/-before-model-callback/index.html)> = emptyList(), afterModelCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterModelCallback](../../com.google.adk.kt.callbacks/-after-model-callback/index.html)> = emptyList(), beforeToolCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeToolCallback](../../com.google.adk.kt.callbacks/-before-tool-callback/index.html)> = emptyList(), afterToolCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterToolCallback](../../com.google.adk.kt.callbacks/-after-tool-callback/index.html)> = emptyList(), inputSchema: [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null, onModelErrorCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnModelErrorCallback](../../com.google.adk.kt.callbacks/-on-model-error-callback/index.html)> = emptyList(), onToolErrorCallbacks: [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnToolErrorCallback](../../com.google.adk.kt.callbacks/-on-tool-error-callback/index.html)> = emptyList(), includeContents: [LlmAgent.IncludeContents](-include-contents/index.html) = IncludeContents.DEFAULT)

## Types

[IncludeContents](-include-contents/index.html)

Link copied to clipboard

enum [IncludeContents](-include-contents/index.html) : [Enum](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-enum/index.html)<[LlmAgent.IncludeContents](-include-contents/index.html)>

Controls how prior conversation history is included in this agent's model request.

## Properties

[afterAgentCallbacks](../-base-agent/after-agent-callbacks.html)

Link copied to clipboard

val [afterAgentCallbacks](../-base-agent/after-agent-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterAgentCallback](../../com.google.adk.kt.callbacks/-after-agent-callback/index.html)>

List of callbacks to run after the agent executes.

[afterModelCallbacks](after-model-callbacks.html)

Link copied to clipboard

val [afterModelCallbacks](after-model-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterModelCallback](../../com.google.adk.kt.callbacks/-after-model-callback/index.html)>

List of callbacks to run after each model call.

[afterToolCallbacks](after-tool-callbacks.html)

Link copied to clipboard

val [afterToolCallbacks](after-tool-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[AfterToolCallback](../../com.google.adk.kt.callbacks/-after-tool-callback/index.html)>

List of callbacks to run after each tool call.

[beforeAgentCallbacks](../-base-agent/before-agent-callbacks.html)

Link copied to clipboard

val [beforeAgentCallbacks](../-base-agent/before-agent-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeAgentCallback](../../com.google.adk.kt.callbacks/-before-agent-callback/index.html)>

List of callbacks to run before the agent executes.

[beforeModelCallbacks](before-model-callbacks.html)

Link copied to clipboard

val [beforeModelCallbacks](before-model-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeModelCallback](../../com.google.adk.kt.callbacks/-before-model-callback/index.html)>

List of callbacks to run before each model call.

[beforeToolCallbacks](before-tool-callbacks.html)

Link copied to clipboard

val [beforeToolCallbacks](before-tool-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BeforeToolCallback](../../com.google.adk.kt.callbacks/-before-tool-callback/index.html)>

List of callbacks to run before each tool call.

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

[generateContentConfig](generate-content-config.html)

Link copied to clipboard

val [generateContentConfig](generate-content-config.html): [GenerateContentConfig](../../com.google.adk.kt.types/-generate-content-config/index.html)? = null

The additional content generation configurations.

[includeContents](include-contents.html)

Link copied to clipboard

val [includeContents](include-contents.html): [LlmAgent.IncludeContents](-include-contents/index.html)

Controls how prior conversation history is included in the model request. Defaults to [IncludeContents.DEFAULT](-include-contents/-d-e-f-a-u-l-t/index.html), which includes the relevant conversation history. Set to [IncludeContents.NONE](-include-contents/-n-o-n-e/index.html) to exclude prior history; the model then receives only the current turn (the most recent user input or other-agent reply, plus any tool calls/responses produced within that turn). The system instruction and tools are preserved in both modes.

[inputSchema](input-schema.html)

Link copied to clipboard

val [inputSchema](input-schema.html): [Schema](../../com.google.adk.kt.types/-schema/index.html)? = null

The input schema of the agent.

[instruction](instruction.html)

Link copied to clipboard

val [instruction](instruction.html): [Instruction](../-instruction/index.html)? = null

Instruction guiding the agent's behavior. Use one of: - `Instruction("text")` for a literal string (the most common case), - `Instruction(content)` for a pre-built, possibly multimodal [Content](../../com.google.adk.kt.types/-content/index.html), or - `Instruction { ctx -> ... }` for a [Instruction.Provider](../-instruction/-provider/index.html) resolved per turn.

[model](model.html)

Link copied to clipboard

val [model](model.html): [Model](../../com.google.adk.kt.models/-model/index.html)

The model to use for the agent.

[name](../-base-agent/name.html)

Link copied to clipboard

val [name](../-base-agent/name.html): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

The name of the agent.

[onModelErrorCallbacks](on-model-error-callbacks.html)

Link copied to clipboard

val [onModelErrorCallbacks](on-model-error-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnModelErrorCallback](../../com.google.adk.kt.callbacks/-on-model-error-callback/index.html)>

List of callbacks to run when a model call fails.

[onToolErrorCallbacks](on-tool-error-callbacks.html)

Link copied to clipboard

val [onToolErrorCallbacks](on-tool-error-callbacks.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[OnToolErrorCallback](../../com.google.adk.kt.callbacks/-on-tool-error-callback/index.html)>

List of callbacks to run when a tool call fails.

[staticInstruction](static-instruction.html)

Link copied to clipboard

val [staticInstruction](static-instruction.html): [Content](../../com.google.adk.kt.types/-content/index.html)? = null

Static instruction content sent literally as system instruction at the beginning. This field is for content that never changes. It's sent directly to the model without any processing or variable substitution.

[subAgents](../-base-agent/sub-agents.html)

Link copied to clipboard

val [subAgents](../-base-agent/sub-agents.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseAgent](../-base-agent/index.html)>

List of sub-agents.

[tools](tools.html)

Link copied to clipboard

val [tools](tools.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[BaseTool](../../com.google.adk.kt.tools/-base-tool/index.html)>

Tools available to this agent.

[toolsets](toolsets.html)

Link copied to clipboard

val [toolsets](toolsets.html): [List](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin.collections/-list/index.html)<[Toolset](../../com.google.adk.kt.tools/-toolset/index.html)>

Toolsets available to this agent.

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
