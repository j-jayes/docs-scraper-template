[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LongRunningFunctionTool]()



# Class LongRunningFunctionTool<TParameters>

A [FunctionTool](FunctionTool.html) for long-running operations whose result is returned asynchronously.

The framework invokes the user-provided function and delivers the response back to the model once it completes, identified by the `function_call_id`. The model is also instructed not to re-invoke the tool while a call is already in flight.

#### Type Parameters

  * TParameters extends [ToolInputParameters](../types/ToolInputParameters.html) = undefined



#### Hierarchy ([View Summary](../hierarchy.html#LongRunningFunctionTool))

  * [FunctionTool](FunctionTool.html)<TParameters>
    * LongRunningFunctionTool



  * Defined in [core/src/tools/long_running_tool.ts:28](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/long_running_tool.ts#L28)



## Constructors

### constructor

  * new LongRunningFunctionTool<TParameters extends [ToolInputParameters](../types/ToolInputParameters.html) = undefined>(  
options: [ToolOptions](../types/ToolOptions.html)<TParameters>,  
): [LongRunningFunctionTool]()<TParameters>

The constructor acts as the user-friendly factory.

#### Type Parameters

    * TParameters extends [ToolInputParameters](../types/ToolInputParameters.html) = undefined

#### Parameters

    * options: [ToolOptions](../types/ToolOptions.html)<TParameters>

The configuration for the tool.

#### Returns [LongRunningFunctionTool]()<TParameters>

Overrides [FunctionTool](FunctionTool.html).[constructor](FunctionTool.html#constructor)

    * Defined in [core/src/tools/long_running_tool.ts:35](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/long_running_tool.ts#L35)




## Properties

### `Readonly`[BASE_TOOL_SIGNATURE_SYMBOL]

"[BASE_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base tool class.

Inherited from [FunctionTool](FunctionTool.html).[[BASE_TOOL_SIGNATURE_SYMBOL]](FunctionTool.html#base_tool_signature_symbol)

  * Defined in [core/src/tools/base_tool.ts:64](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L64)



### `Readonly`[FUNCTION_TOOL_SIGNATURE_SYMBOL]

"[FUNCTION_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK function tool class.

Inherited from [FunctionTool](FunctionTool.html).[[FUNCTION_TOOL_SIGNATURE_SYMBOL]](FunctionTool.html#function_tool_signature_symbol)

  * Defined in [core/src/tools/function_tool.ts:108](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/function_tool.ts#L108)



### `Readonly`description

description: string

Inherited from [FunctionTool](FunctionTool.html).[description](FunctionTool.html#description)

  * Defined in [core/src/tools/base_tool.ts:67](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L67)



### `Readonly`isLongRunning

isLongRunning: boolean

Inherited from [FunctionTool](FunctionTool.html).[isLongRunning](FunctionTool.html#islongrunning)

  * Defined in [core/src/tools/base_tool.ts:68](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L68)



### `Readonly`name

name: string

Inherited from [FunctionTool](FunctionTool.html).[name](FunctionTool.html#name)

  * Defined in [core/src/tools/base_tool.ts:66](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L66)



## Accessors

### apiVariant

  * get apiVariant(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

The Google API LLM variant to use.

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

Inherited from FunctionTool.apiVariant

    * Defined in [core/src/tools/base_tool.ts:151](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L151)




## Methods

### _getDeclaration

  * _getDeclaration(): FunctionDeclaration

Returns the function declaration with an appended instruction warning the model not to re-invoke the tool while it is still running.

#### Returns FunctionDeclaration

Overrides [FunctionTool](FunctionTool.html).[_getDeclaration](FunctionTool.html#_getdeclaration)

    * Defined in [core/src/tools/long_running_tool.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/long_running_tool.ts#L43)




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

Inherited from [FunctionTool](FunctionTool.html).[processLlmRequest](FunctionTool.html#processllmrequest)

    * Defined in [core/src/tools/base_tool.ts:120](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L120)




### runAsync

  * runAsync(req: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)): Promise<unknown>

Validates the model-provided arguments against the parameter schema and invokes the user-defined `execute` function.

#### Parameters

    * req: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)

The tool request containing arguments and tool context.

#### Returns Promise<unknown>

A promise resolving to the function's return value.

Inherited from [FunctionTool](FunctionTool.html).[runAsync](FunctionTool.html#runasync)

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


