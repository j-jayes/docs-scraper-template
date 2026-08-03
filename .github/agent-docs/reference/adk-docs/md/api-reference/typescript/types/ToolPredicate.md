[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolPredicate]()



# Type Alias ToolPredicate

ToolPredicate: (tool: [BaseTool](../classes/BaseTool.html), readonlyContext: [ReadonlyContext](../classes/ReadonlyContext.html)) => boolean

Function to decide whether a tool should be exposed to LLM. Toolset implementer could consider whether to accept such instance in the toolset's constructor and apply the predicate in getTools method.

#### Type Declaration

  *     * (tool: [BaseTool](../classes/BaseTool.html), readonlyContext: [ReadonlyContext](../classes/ReadonlyContext.html)): boolean
    * #### Parameters

      * tool: [BaseTool](../classes/BaseTool.html)
      * readonlyContext: [ReadonlyContext](../classes/ReadonlyContext.html)

#### Returns boolean




  * Defined in [core/src/tools/base_toolset.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L18)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


