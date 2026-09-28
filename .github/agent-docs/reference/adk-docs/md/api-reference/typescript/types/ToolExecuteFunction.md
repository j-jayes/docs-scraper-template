[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolExecuteFunction]()



# Type Alias ToolExecuteFunction<TParameters>

ToolExecuteFunction: (  
input: [ToolExecuteArgument](ToolExecuteArgument.html)<TParameters>,  
tool_context?: [Context](../classes/Context.html),  
) => Promise<unknown> | unknown

The signature of the user-provided function executed by a [FunctionTool](../classes/FunctionTool.html).

#### Type Parameters

  * TParameters extends [ToolInputParameters](ToolInputParameters.html)



#### Type Declaration

  *     * (  
input: [ToolExecuteArgument](ToolExecuteArgument.html)<TParameters>,  
tool_context?: [Context](../classes/Context.html),  
): Promise<unknown> | unknown
    * #### Parameters

      * input: [ToolExecuteArgument](ToolExecuteArgument.html)<TParameters>
      * `Optional`tool_context: [Context](../classes/Context.html)

#### Returns Promise<unknown> | unknown




  * Defined in [core/src/tools/function_tool.ts:41](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L41)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


