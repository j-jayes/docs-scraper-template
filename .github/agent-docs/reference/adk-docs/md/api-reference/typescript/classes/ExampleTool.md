[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ExampleTool]()



# Class ExampleTool

A tool that adds (few-shot) examples to the LLM request.

This tool is executed for each LLM request and is never called by the model; it only mutates the outgoing request by appending few-shot instructions built from the latest user query.

#### Hierarchy ([View Summary](../hierarchy.html#ExampleTool))

  * [BaseTool](BaseTool.html)
    * ExampleTool



  * Defined in [core/src/tools/example_tool.ts:25](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/example_tool.ts#L25)



## Constructors

### constructor

  * new ExampleTool(examples: [BaseExampleProvider](BaseExampleProvider.html) | [Example](../interfaces/Example.html)[]): [ExampleTool]()

#### Parameters

    * examples: [BaseExampleProvider](BaseExampleProvider.html) | [Example](../interfaces/Example.html)[]

#### Returns [ExampleTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/tools/example_tool.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/example_tool.ts#L26)




## Properties

### `Readonly`[BASE_TOOL_SIGNATURE_SYMBOL]

"[BASE_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base tool class.

Inherited from [BaseTool](BaseTool.html).[[BASE_TOOL_SIGNATURE_SYMBOL]](BaseTool.html#base_tool_signature_symbol)

  * Defined in [core/src/tools/base_tool.ts:64](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L64)



### `Readonly`description

description: string

Inherited from [BaseTool](BaseTool.html).[description](BaseTool.html#description)

  * Defined in [core/src/tools/base_tool.ts:67](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L67)



### `Readonly`examples

examples: [BaseExampleProvider](BaseExampleProvider.html) | [Example](../interfaces/Example.html)[]

  * Defined in [core/src/tools/example_tool.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/example_tool.ts#L26)



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

  * _getDeclaration(): FunctionDeclaration | undefined

Gets the OpenAPI specification of this tool in the form of a FunctionDeclaration.

NOTE

    * Required if subclass uses the default implementation of `processLlmRequest` to add function declaration to LLM request.
    * Otherwise, can be skipped, e.g. for a built-in GoogleSearch tool for Gemini.

#### Returns FunctionDeclaration | undefined

The FunctionDeclaration of this tool, or undefined if it doesn't need to be added to LlmRequest.config.

Inherited from [BaseTool](BaseTool.html).[_getDeclaration](BaseTool.html#_getdeclaration)

    * Defined in [core/src/tools/base_tool.ts:94](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L94)




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

Overrides [BaseTool](BaseTool.html).[processLlmRequest](BaseTool.html#processllmrequest)

    * Defined in [core/src/tools/example_tool.ts:40](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/example_tool.ts#L40)




### runAsync

  * runAsync(_request: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)): Promise<unknown>

Runs the tool with the given arguments and context.

NOTE

    * Required if this tool needs to run at the client side.
    * Otherwise, can be skipped, e.g. for a built-in GoogleSearch tool for Gemini.

#### Parameters

    * _request: [RunAsyncToolRequest](../interfaces/RunAsyncToolRequest.html)

#### Returns Promise<unknown>

A promise that resolves to the tool response.

Overrides [BaseTool](BaseTool.html).[runAsync](BaseTool.html#runasync)

    * Defined in [core/src/tools/example_tool.ts:35](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/example_tool.ts#L35)




Constructors

constructor

Properties

[BASE_TOOL_SIGNATURE_SYMBOL]descriptionexamplesisLongRunningname

Accessors

apiVariant

Methods

_getDeclarationprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


