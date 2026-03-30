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

#### Type Parameters

  * TParameters extends [ToolInputParameters](ToolInputParameters.html)



  * Defined in [tools/function_tool.ts:28](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/function_tool.ts#L28)



[ADK for TypeScript: API Reference](../index.html)

  * Loading...


