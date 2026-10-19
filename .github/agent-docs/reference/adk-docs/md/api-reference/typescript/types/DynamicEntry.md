[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [DynamicEntry]()



# Type Alias DynamicEntry

DynamicEntry: (ctx: [NodeContext](../classes/NodeContext.html), input: unknown) => unknown | Promise<unknown>

An imperative workflow entry point. Receives the workflow's node context and input, drives execution via `ctx.runNode(...)`, and returns the workflow output. Mutually exclusive with `edges`.

#### Type Declaration

  *     * (ctx: [NodeContext](../classes/NodeContext.html), input: unknown): unknown | Promise<unknown>
    * #### Parameters

      * ctx: [NodeContext](../classes/NodeContext.html)
      * input: unknown

#### Returns unknown | Promise<unknown>




  * Defined in [core/src/workflow/workflow.ts:54](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/workflow.ts#L54)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


