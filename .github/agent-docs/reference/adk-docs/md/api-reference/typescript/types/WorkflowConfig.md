[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [WorkflowConfig]()



# Type Alias WorkflowConfig

WorkflowConfig: [BaseNodeConfig](../interfaces/BaseNodeConfig.html) & { maxConcurrency?: number } & (  
| { dynamicEntry?: never; edges: [EdgeItem](EdgeItem.html)[] }  
| { dynamicEntry: [DynamicEntry](DynamicEntry.html); edges?: never }  
)

Configuration for a [Workflow](../classes/Workflow.html).

A workflow is driven either by a static `edges` graph or by an imperative `dynamicEntry` function — exactly one is required, and the two are mutually exclusive. The type is a discriminated union so that constraint is enforced at compile time (the runtime constructor keeps the equivalent throws for JS callers).

#### Type Declaration

  * ##### `Optional`maxConcurrency?: number

Maximum number of graph-scheduled nodes running in parallel. `undefined` means unlimited; must be a positive integer otherwise. Does not throttle dynamic (`ctx.runNode`) children.



  * { dynamicEntry?: never; edges: [EdgeItem](EdgeItem.html)[] }
    * ##### `Optional`dynamicEntry?: never

    * ##### edges: [EdgeItem](EdgeItem.html)[]

Edge definitions used to build the workflow graph.

  * { dynamicEntry: [DynamicEntry](DynamicEntry.html); edges?: never }
    * ##### dynamicEntry: [DynamicEntry](DynamicEntry.html)

An imperative entry function driving execution via `ctx.runNode(...)`. Mutually exclusive with `edges`.

    * ##### `Optional`edges?: never




  * Defined in [core/src/workflow/workflow.ts:68](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/workflow.ts#L68)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


