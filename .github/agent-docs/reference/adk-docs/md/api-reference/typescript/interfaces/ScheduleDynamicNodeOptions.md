[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ScheduleDynamicNodeOptions]()



# Interface ScheduleDynamicNodeOptions

Options for scheduling a dynamic node via [ScheduleDynamicNode](ScheduleDynamicNode.html).

interface ScheduleDynamicNodeOptions {  
nodeName?: string;  
overrideBranch?: string;  
overrideIsolationScope?: string;  
runId: string;  
useAsOutput?: boolean;  
useSubBranch?: boolean;  
}

  * Defined in [core/src/workflow/schedule_dynamic_node.ts:14](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/schedule_dynamic_node.ts#L14)



## Properties

### `Optional`nodeName

nodeName?: string

Deterministic tracking name; defaults to `node.name`.

  * Defined in [core/src/workflow/schedule_dynamic_node.ts:16](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/schedule_dynamic_node.ts#L16)



### `Optional`overrideBranch

overrideBranch?: string

Explicit branch override.

  * Defined in [core/src/workflow/schedule_dynamic_node.ts:24](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/schedule_dynamic_node.ts#L24)



### `Optional`overrideIsolationScope

overrideIsolationScope?: string

Explicit isolation-scope override.

  * Defined in [core/src/workflow/schedule_dynamic_node.ts:26](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/schedule_dynamic_node.ts#L26)



### runId

runId: string

Unique id for this specific execution (used for path/dedup keys).

  * Defined in [core/src/workflow/schedule_dynamic_node.ts:18](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/schedule_dynamic_node.ts#L18)



### `Optional`useAsOutput

useAsOutput?: boolean

If true, the child's output replaces the caller's output.

  * Defined in [core/src/workflow/schedule_dynamic_node.ts:20](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/schedule_dynamic_node.ts#L20)



### `Optional`useSubBranch

useSubBranch?: boolean

If true, run the child in an isolated sub-branch.

  * Defined in [core/src/workflow/schedule_dynamic_node.ts:22](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/schedule_dynamic_node.ts#L22)



Properties

nodeNameoverrideBranchoverrideIsolationScoperunIduseAsOutputuseSubBranch

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


