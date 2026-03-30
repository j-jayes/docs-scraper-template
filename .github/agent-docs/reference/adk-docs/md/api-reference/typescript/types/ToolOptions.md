[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToolOptions]()



# Type Alias ToolOptions<TParameters>

The configuration options for creating a function-based tool. The `name`, `description` and `parameters` fields are used to generate the tool definition that is passed to the LLM prompt.

Note: Unlike Python's ADK, JSDoc on the `execute` function is ignored for tool definition generation.

type ToolOptions<TParameters extends [ToolInputParameters](ToolInputParameters.html)> = {  
description: string;  
execute: [ToolExecuteFunction](ToolExecuteFunction.html)<TParameters>;  
isLongRunning?: boolean;  
name?: string;  
parameters?: TParameters;  
}

#### Type Parameters

  * TParameters extends [ToolInputParameters](ToolInputParameters.html)



  * Defined in [tools/function_tool.ts:53](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/function_tool.ts#L53)



## Properties

### description

description: string

  * Defined in [tools/function_tool.ts:55](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/function_tool.ts#L55)



### execute

execute: [ToolExecuteFunction](ToolExecuteFunction.html)<TParameters>

  * Defined in [tools/function_tool.ts:57](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/function_tool.ts#L57)



### `Optional`isLongRunning

isLongRunning?: boolean

  * Defined in [tools/function_tool.ts:58](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/function_tool.ts#L58)



### `Optional`name

name?: string

  * Defined in [tools/function_tool.ts:54](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/function_tool.ts#L54)



### `Optional`parameters

parameters?: TParameters

  * Defined in [tools/function_tool.ts:56](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/function_tool.ts#L56)



Properties

descriptionexecuteisLongRunningnameparameters

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


