[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [NodeContextOptions]()



# Interface NodeContextOptions

Options for constructing a [NodeContext](../classes/NodeContext.html).

interface NodeContextOptions {  
actions?: [EventActions](EventActions.html);  
channel: [AsyncQueue](../classes/AsyncQueue.html)<[Event](Event.html)>;  
invocationContext: [InvocationContext](../classes/InvocationContext.html);  
isolationScope?: string;  
nodePath: string;  
resumeInputs?: Record<string, unknown>;  
runId: string;  
stateSchema?: [SchemaLike](../types/SchemaLike.html);  
}

  * Defined in [core/src/workflow/node_context.ts:48](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L48)



## Properties

### `Optional`actions

actions?: [EventActions](EventActions.html)

Accumulator for event actions (state delta, etc).

  * Defined in [core/src/workflow/node_context.ts:60](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L60)



### channel

channel: [AsyncQueue](../classes/AsyncQueue.html)<[Event](Event.html)>

  * Defined in [core/src/workflow/node_context.ts:50](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L50)



### invocationContext

invocationContext: [InvocationContext](../classes/InvocationContext.html)

  * Defined in [core/src/workflow/node_context.ts:49](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L49)



### `Optional`isolationScope

isolationScope?: string

Scope tag isolating this node's events from peer scopes.

  * Defined in [core/src/workflow/node_context.ts:58](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L58)



### nodePath

nodePath: string

Dotted node path of the owning node (empty string for the root).

  * Defined in [core/src/workflow/node_context.ts:52](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L52)



### `Optional`resumeInputs

resumeInputs?: Record<string, unknown>

Responses for resuming interrupted child nodes, keyed by interrupt id.

  * Defined in [core/src/workflow/node_context.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L56)



### runId

runId: string

Deterministic run id of the owning node.

  * Defined in [core/src/workflow/node_context.ts:54](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L54)



### `Optional`stateSchema

stateSchema?: [SchemaLike](../types/SchemaLike.html)

Declares the keys this node may write to `ctx.state` and their types. Resolved by the runner: the node's own schema, or the parent's.

  * Defined in [core/src/workflow/node_context.ts:65](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L65)



Properties

actionschannelinvocationContextisolationScopenodePathresumeInputsrunIdstateSchema

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


