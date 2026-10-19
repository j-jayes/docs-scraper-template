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




  * Defined in [core/src/tools/base_toolset.ts:18](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_toolset.ts#L18)



[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


