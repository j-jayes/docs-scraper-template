[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LongRunningFunctionTool]()



# Class LongRunningFunctionTool<TParameters>

The base class for all tools.

#### Type Parameters

  * TParameters extends ToolInputParameters = undefined



#### Hierarchy ([View Summary](../hierarchy.html#LongRunningFunctionTool))

  * [FunctionTool](FunctionTool.html)<TParameters>
    * LongRunningFunctionTool



  * Defined in [core/src/tools/long_running_tool.ts:24](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/long_running_tool.ts#L24)



## Constructors

### constructor

  * new LongRunningFunctionTool<TParameters extends ToolInputParameters = undefined>(  
options: ToolOptions<TParameters>,  
): [LongRunningFunctionTool]()<TParameters>

The constructor acts as the user-friendly factory.

#### Type Parameters

    * TParameters extends ToolInputParameters = undefined

#### Parameters

    * options: ToolOptions<TParameters>

The configuration for the tool.

#### Returns [LongRunningFunctionTool]()<TParameters>

Overrides [FunctionTool](FunctionTool.html).[constructor](FunctionTool.html#constructor)

    * Defined in [core/src/tools/long_running_tool.ts:31](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/long_running_tool.ts#L31)




## Properties

### `Readonly`description

description: string

Inherited from [FunctionTool](FunctionTool.html).[description](FunctionTool.html#description)

  * Defined in [core/src/tools/base_tool.ts:44](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L44)



### `Readonly`isLongRunning

isLongRunning: boolean

Inherited from [FunctionTool](FunctionTool.html).[isLongRunning](FunctionTool.html#islongrunning)

  * Defined in [core/src/tools/base_tool.ts:45](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L45)



### `Readonly`name

name: string

Inherited from [FunctionTool](FunctionTool.html).[name](FunctionTool.html#name)

  * Defined in [core/src/tools/base_tool.ts:43](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L43)



## Accessors

### apiVariant

  * get apiVariant(): GoogleLLMVariant

The Google API LLM variant to use.

#### Returns GoogleLLMVariant

Inherited from FunctionTool.apiVariant

    * Defined in [core/src/tools/base_tool.ts:125](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L125)




## Methods

### _getDeclaration

  * _getDeclaration(): FunctionDeclaration

Provide a schema for the function.

#### Returns FunctionDeclaration

Overrides [FunctionTool](FunctionTool.html).[_getDeclaration](FunctionTool.html#_getdeclaration)

    * Defined in [core/src/tools/long_running_tool.ts:38](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/long_running_tool.ts#L38)




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

    * Defined in [core/src/tools/base_tool.ts:97](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L97)




### runAsync

  * runAsync(req: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)): Promise<unknown>

Logic for running the tool.

#### Parameters

    * req: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)

#### Returns Promise<unknown>

Inherited from [FunctionTool](FunctionTool.html).[runAsync](FunctionTool.html#runasync)

    * Defined in [core/src/tools/function_tool.ts:111](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/function_tool.ts#L111)




Constructors

constructor

Properties

descriptionisLongRunningname

Accessors

apiVariant

Methods

_getDeclarationprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


