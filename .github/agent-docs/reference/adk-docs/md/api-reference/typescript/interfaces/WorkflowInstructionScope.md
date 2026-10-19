[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [WorkflowInstructionScope]()



# Interface WorkflowInstructionScope

Workflow: data exposed to `{Class.field}` and `<Class.field from source_node>` instruction placeholders when an LlmAgent runs as a workflow node. Populated by `LLMAgentWrapper`; absent for ordinary (non-workflow) agent runs, in which case those placeholders are left untouched.

interface WorkflowInstructionScope {  
input?: unknown;  
outputsByNode?: Record<string, unknown>;  
}

  * Defined in [core/src/agents/invocation_context.ts:31](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L31)



## Properties

### `Optional`input

input?: unknown

The current node's input, exposing fields for `{Class.field}`.

  * Defined in [core/src/agents/invocation_context.ts:33](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L33)



### `Optional`outputsByNode

outputsByNode?: Record<string, unknown>

Predecessor node outputs keyed by node name, for `<Class.field from node>`.

  * Defined in [core/src/agents/invocation_context.ts:35](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/agents/invocation_context.ts#L35)



Properties

inputoutputsByNode

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


