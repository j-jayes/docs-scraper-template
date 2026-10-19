[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [NodeResult]()



# Interface NodeResult

The result of running a node: the fields a caller (and the engine's completion handling) reads off a finished run — its `output`, emitted `route`, the `branch` it ran on, and any raised interrupt ids.

A node that actually executes returns its full [NodeContext](../classes/NodeContext.html) (which satisfies this shape). A node that is _fast-forwarded_ on resume (its output was cached in a prior turn, so its body is not re-run) returns a bare `NodeResult` with no live context behaviour — so callers of `ctx.runNode()` should treat the result as a `NodeResult` and read only these fields.

interface NodeResult {  
branch?: string;  
interruptIds: string[];  
output: unknown;  
route?: [RouteValue](../types/RouteValue.html) | [RouteValue](../types/RouteValue.html)[];  
}

  * Defined in [core/src/workflow/node_context.ts:34](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L34)



## Properties

### `Optional`branch

branch?: string

The branch the node ran on.

  * Defined in [core/src/workflow/node_context.ts:40](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L40)



### interruptIds

interruptIds: string[]

Interrupt ids the node is blocked on (empty when it completed).

  * Defined in [core/src/workflow/node_context.ts:42](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L42)



### output

output: unknown

The structured output the node produced (if any).

  * Defined in [core/src/workflow/node_context.ts:36](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L36)



### `Optional`route

route?: [RouteValue](../types/RouteValue.html) | [RouteValue](../types/RouteValue.html)[]

The route key(s) the node emitted, if any (array = multi-route).

  * Defined in [core/src/workflow/node_context.ts:38](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_context.ts#L38)



Properties

branchinterruptIdsoutputroute

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


