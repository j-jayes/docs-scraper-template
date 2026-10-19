[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [RunNodeOptions]()



# Interface RunNodeOptions

Options controlling a single `ctx.runNode(...)` execution.

interface RunNodeOptions {  
nodeName?: string;  
overrideBranch?: string;  
overrideIsolationScope?: string;  
overrideNodePath?: string;  
runId?: string;  
useAsOutput?: boolean;  
useSubBranch?: boolean;  
}

  * Defined in [core/src/workflow/node_runner.ts:31](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_runner.ts#L31)



## Properties

### `Optional`nodeName

nodeName?: string

Deterministic tracking name; defaults to `node.name`.

  * Defined in [core/src/workflow/node_runner.ts:33](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_runner.ts#L33)



### `Optional`overrideBranch

overrideBranch?: string

Explicit branch, overriding the default/sub-branch computation.

  * Defined in [core/src/workflow/node_runner.ts:50](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_runner.ts#L50)



### `Optional`overrideIsolationScope

overrideIsolationScope?: string

Explicit isolation scope, overriding inheritance from the parent.

  * Defined in [core/src/workflow/node_runner.ts:52](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_runner.ts#L52)



### `Optional`overrideNodePath

overrideNodePath?: string

Explicit node path for the child (used by the dynamic scheduler to embed the run id, e.g. `wf.node@1`, so distinct runs are distinguishable on resume). Defaults to `${parent.nodePath}.${nodeName}`.

  * Defined in [core/src/workflow/node_runner.ts:58](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_runner.ts#L58)



### `Optional`runId

runId?: string

Unique id for this specific run. Defaults to a per-node sequence — "1", "2", "3" in call order — which is what a resume matches checkpoints on.

Supply one only when position is not stable but identity is (a reorderable collection: key it off the item's own id). Give it a non-numeric character so it cannot collide with the automatic sequence: an all-digit id is refused for any node ADK also numbers automatically in the same context, whichever call comes first.

  * Defined in [core/src/workflow/node_runner.ts:44](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_runner.ts#L44)



### `Optional`useAsOutput

useAsOutput?: boolean

If true, the child's output replaces the caller's output.

  * Defined in [core/src/workflow/node_runner.ts:46](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_runner.ts#L46)



### `Optional`useSubBranch

useSubBranch?: boolean

If true, run the child in an isolated sub-branch.

  * Defined in [core/src/workflow/node_runner.ts:48](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/node_runner.ts#L48)



Properties

nodeNameoverrideBranchoverrideIsolationScopeoverrideNodePathrunIduseAsOutputuseSubBranch

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


