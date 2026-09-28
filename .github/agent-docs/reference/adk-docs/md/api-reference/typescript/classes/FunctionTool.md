[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [FunctionTool]()



# Class FunctionTool<TParameters>

A tool that wraps a user-defined function, making it callable by an LLM.

The function's name, description, and parameter schema are exposed to the model as a function declaration. When the model requests a call, the framework validates the arguments and invokes the user-provided `execute` callback.

#### Type Parameters

  * TParameters extends [ToolInputParameters](../types/ToolInputParameters.html) = undefined



#### Hierarchy ([View Summary](../hierarchy.html#FunctionTool))

  * [BaseTool](BaseTool.html)
    * FunctionTool
      * [LongRunningFunctionTool](LongRunningFunctionTool.html)



  * Defined in [core/src/tools/function_tool.ts:104](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L104)



## Constructors

### constructor

  * new FunctionTool<TParameters extends [ToolInputParameters](../types/ToolInputParameters.html) = undefined>(  
options: [ToolOptions](../types/ToolOptions.html)<TParameters>,  
): [FunctionTool]()<TParameters>

The constructor acts as the user-friendly factory.

#### Type Parameters

    * TParameters extends [ToolInputParameters](../types/ToolInputParameters.html) = undefined

#### Parameters

    * options: [ToolOptions](../types/ToolOptions.html)<TParameters>

The configuration for the tool.

#### Returns [FunctionTool]()<TParameters>

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/tools/function_tool.ts:119](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L119)




## Properties

### `Readonly`[BASE_TOOL_SIGNATURE_SYMBOL]

"[BASE_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base tool class.

Inherited from [BaseTool](BaseTool.html).[[BASE_TOOL_SIGNATURE_SYMBOL]](BaseTool.html#base_tool_signature_symbol)

  * Defined in [core/src/tools/base_tool.ts:64](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L64)



### `Readonly`[FUNCTION_TOOL_SIGNATURE_SYMBOL]

"[FUNCTION_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK function tool class.

  * Defined in [core/src/tools/function_tool.ts:108](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L108)



### `Readonly`description

description: string

Inherited from [BaseTool](BaseTool.html).[description](BaseTool.html#description)

  * Defined in [core/src/tools/base_tool.ts:67](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L67)



### `Readonly`isLongRunning

isLongRunning: boolean

Inherited from [BaseTool](BaseTool.html).[isLongRunning](BaseTool.html#islongrunning)

  * Defined in [core/src/tools/base_tool.ts:68](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L68)



### `Readonly`name

name: string

Inherited from [BaseTool](BaseTool.html).[name](BaseTool.html#name)

  * Defined in [core/src/tools/base_tool.ts:66](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L66)



## Accessors

### apiVariant

  * get apiVariant(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

The Google API LLM variant to use.

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

Inherited from BaseTool.apiVariant

    * Defined in [core/src/tools/base_tool.ts:151](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L151)




## Methods

### _getDeclaration

  * _getDeclaration(): FunctionDeclaration

Returns the function declaration derived from the tool's name, description, and parameter schema.

#### Returns FunctionDeclaration

Overrides [BaseTool](BaseTool.html).[_getDeclaration](BaseTool.html#_getdeclaration)

    * Defined in [core/src/tools/function_tool.ts:139](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L139)




### processLlmRequest

  * processLlmRequest(request: [ToolProcessLlmRequest](../interfaces/ToolProcessLlmRequest.html)): Promise<void>

Processes the outgoing LLM request for this tool.

Use cases:

    * Most common use case is adding this tool to the LLM request.
    * Some tools may just preprocess the LLM request before it's sent out.

#### Parameters

    * request: [ToolProcessLlmRequest](../interfaces/ToolProcessLlmRequest.html)

The request to process the LLM request.

#### Returns Promise<void>

Inherited from [BaseTool](BaseTool.html).[processLlmRequest](BaseTool.html#processllmrequest)

    * Defined in [core/src/tools/base_tool.ts:120](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L120)




### runAsync

  * runAsync(req: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)): Promise<unknown>

Validates the model-provided arguments against the parameter schema and invokes the user-defined `execute` function.

#### Parameters

    * req: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)

The tool request containing arguments and tool context.

#### Returns Promise<unknown>

A promise resolving to the function's return value.

Overrides [BaseTool](BaseTool.html).[runAsync](BaseTool.html#runasync)

    * Defined in [core/src/tools/function_tool.ts:154](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L154)




Constructors

constructor

Properties

[BASE_TOOL_SIGNATURE_SYMBOL][FUNCTION_TOOL_SIGNATURE_SYMBOL]descriptionisLongRunningname

Accessors

apiVariant

Methods

_getDeclarationprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


