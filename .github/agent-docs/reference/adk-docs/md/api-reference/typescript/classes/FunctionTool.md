[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [FunctionTool]()



# Class FunctionTool<TParameters>

The base class for all tools.

#### Type Parameters

  * TParameters extends ToolInputParameters = undefined



#### Hierarchy ([View Summary](../hierarchy.html#FunctionTool))

  * [BaseTool](BaseTool.html)
    * FunctionTool
      * [LongRunningFunctionTool](LongRunningFunctionTool.html)



  * Defined in [core/src/tools/function_tool.ts:69](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/function_tool.ts#L69)



## Constructors

### constructor

  * new FunctionTool<TParameters extends ToolInputParameters = undefined>(  
options: ToolOptions<TParameters>,  
): [FunctionTool]()<TParameters>

The constructor acts as the user-friendly factory.

#### Type Parameters

    * TParameters extends ToolInputParameters = undefined

#### Parameters

    * options: ToolOptions<TParameters>

The configuration for the tool.

#### Returns [FunctionTool]()<TParameters>

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/tools/function_tool.ts:81](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/function_tool.ts#L81)




## Properties

### `Readonly`description

description: string

Inherited from [BaseTool](BaseTool.html).[description](BaseTool.html#description)

  * Defined in [core/src/tools/base_tool.ts:44](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L44)



### `Readonly`isLongRunning

isLongRunning: boolean

Inherited from [BaseTool](BaseTool.html).[isLongRunning](BaseTool.html#islongrunning)

  * Defined in [core/src/tools/base_tool.ts:45](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L45)



### `Readonly`name

name: string

Inherited from [BaseTool](BaseTool.html).[name](BaseTool.html#name)

  * Defined in [core/src/tools/base_tool.ts:43](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L43)



## Accessors

### apiVariant

  * get apiVariant(): GoogleLLMVariant

The Google API LLM variant to use.

#### Returns GoogleLLMVariant

Inherited from BaseTool.apiVariant

    * Defined in [core/src/tools/base_tool.ts:125](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L125)




## Methods

### _getDeclaration

  * _getDeclaration(): FunctionDeclaration

Provide a schema for the function.

#### Returns FunctionDeclaration

Overrides [BaseTool](BaseTool.html).[_getDeclaration](BaseTool.html#_getdeclaration)

    * Defined in [core/src/tools/function_tool.ts:100](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/function_tool.ts#L100)




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

    * Defined in [core/src/tools/base_tool.ts:97](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L97)




### runAsync

  * runAsync(req: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)): Promise<unknown>

Logic for running the tool.

#### Parameters

    * req: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)

#### Returns Promise<unknown>

Overrides [BaseTool](BaseTool.html).[runAsync](BaseTool.html#runasync)

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


