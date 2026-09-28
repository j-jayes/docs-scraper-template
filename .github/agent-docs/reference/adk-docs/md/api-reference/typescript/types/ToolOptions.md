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



  * Defined in [core/src/tools/function_tool.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L54)



## Properties

### description

description: string

  * Defined in [core/src/tools/function_tool.ts:56](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L56)



### execute

execute: [ToolExecuteFunction](ToolExecuteFunction.html)<TParameters>

  * Defined in [core/src/tools/function_tool.ts:58](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L58)



### `Optional`isLongRunning

isLongRunning?: boolean

  * Defined in [core/src/tools/function_tool.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L59)



### `Optional`name

name?: string

  * Defined in [core/src/tools/function_tool.ts:55](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L55)



### `Optional`parameters

parameters?: TParameters

  * Defined in [core/src/tools/function_tool.ts:57](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L57)



Properties

descriptionexecuteisLongRunningnameparameters

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


