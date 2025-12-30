[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseTool]()



# Class BaseTool`Abstract`

The base class for all tools.

#### Hierarchy ([View Summary](../hierarchy.html#BaseTool))

  * BaseTool
    * [MCPTool](MCPTool.html)
    * [AgentTool](AgentTool.html)
    * [FunctionTool](FunctionTool.html)



  * Defined in [core/src/tools/base_tool.ts:42](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L42)



## Constructors

### constructor

  * new BaseTool(params: [BaseToolParams](../interfaces/BaseToolParams.html)): [BaseTool]()

Base constructor for a tool.

#### Parameters

    * params: [BaseToolParams](../interfaces/BaseToolParams.html)

The parameters for `BaseTool`.

#### Returns [BaseTool]()

    * Defined in [core/src/tools/base_tool.ts:52](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L52)




## Properties

### `Readonly`description

description: string

  * Defined in [core/src/tools/base_tool.ts:44](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L44)



### `Readonly`isLongRunning

isLongRunning: boolean

  * Defined in [core/src/tools/base_tool.ts:45](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L45)



### `Readonly`name

name: string

  * Defined in [core/src/tools/base_tool.ts:43](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L43)



## Accessors

### apiVariant

  * get apiVariant(): GoogleLLMVariant

The Google API LLM variant to use.

#### Returns GoogleLLMVariant

    * Defined in [core/src/tools/base_tool.ts:125](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L125)




## Methods

### _getDeclaration

  * _getDeclaration(): FunctionDeclaration | undefined

Gets the OpenAPI specification of this tool in the form of a FunctionDeclaration.

NOTE

    * Required if subclass uses the default implementation of `processLlmRequest` to add function declaration to LLM request.
    * Otherwise, can be skipped, e.g. for a built-in GoogleSearch tool for Gemini.

#### Returns FunctionDeclaration | undefined

The FunctionDeclaration of this tool, or undefined if it doesn't need to be added to LlmRequest.config.

    * Defined in [core/src/tools/base_tool.ts:71](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L71)




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

    * Defined in [core/src/tools/base_tool.ts:97](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L97)




### `Abstract`runAsync

  * runAsync(request: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)): Promise<unknown>

Runs the tool with the given arguments and context.

NOTE

    * Required if this tool needs to run at the client side.
    * Otherwise, can be skipped, e.g. for a built-in GoogleSearch tool for Gemini.

#### Parameters

    * request: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)

The request to run the tool.

#### Returns Promise<unknown>

A promise that resolves to the tool response.

    * Defined in [core/src/tools/base_tool.ts:86](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L86)




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


