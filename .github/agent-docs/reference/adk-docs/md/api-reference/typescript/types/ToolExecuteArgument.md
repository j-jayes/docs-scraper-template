[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolExecuteArgument]()



# Type Alias ToolExecuteArgument<TParameters>

ToolExecuteArgument: TParameters extends z3.ZodObject<infer T, infer U, infer V>  
? z3.infer<z3.ZodObject<T, U, V>>  
: TParameters extends z4.ZodObject<infer T>  
? z4.infer<z4.ZodObject<T>>  
: TParameters extends Schema ? unknown : string

The arguments passed to the function tool's `execute` callback, inferred from the `parameters` schema type.

#### Type Parameters

  * TParameters extends [ToolInputParameters](ToolInputParameters.html)



  * Defined in [core/src/tools/function_tool.ts:29](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L29)



[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


