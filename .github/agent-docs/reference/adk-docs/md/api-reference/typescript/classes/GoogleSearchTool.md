[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [GoogleSearchTool]()



# Class GoogleSearchTool

A built-in tool that is automatically invoked by Gemini 2 models to retrieve search results from Google Search.

This tool operates internally within the model and does not require or perform local code execution.

#### Hierarchy ([View Summary](../hierarchy.html#GoogleSearchTool))

  * [BaseTool](BaseTool.html)
    * GoogleSearchTool



  * Defined in [tools/google_search_tool.ts:19](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/google_search_tool.ts#L19)



## Constructors

### constructor

  * new GoogleSearchTool(): [GoogleSearchTool]()

#### Returns [GoogleSearchTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [tools/google_search_tool.ts:20](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/google_search_tool.ts#L20)




## Properties

### `Readonly`[BASE_TOOL_SIGNATURE_SYMBOL]

"[BASE_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base tool class.

Inherited from [BaseTool](BaseTool.html).[[BASE_TOOL_SIGNATURE_SYMBOL]](BaseTool.html#base_tool_signature_symbol)

  * Defined in [tools/base_tool.ts:64](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L64)



### `Readonly`description

description: string

Inherited from [BaseTool](BaseTool.html).[description](BaseTool.html#description)

  * Defined in [tools/base_tool.ts:67](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L67)



### `Readonly`isLongRunning

isLongRunning: boolean

Inherited from [BaseTool](BaseTool.html).[isLongRunning](BaseTool.html#islongrunning)

  * Defined in [tools/base_tool.ts:68](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L68)



### `Readonly`name

name: string

Inherited from [BaseTool](BaseTool.html).[name](BaseTool.html#name)

  * Defined in [tools/base_tool.ts:66](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L66)



## Accessors

### apiVariant

  * get apiVariant(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

The Google API LLM variant to use.

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

Inherited from BaseTool.apiVariant

    * Defined in [tools/base_tool.ts:151](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L151)




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

    * Defined in [tools/base_tool.ts:94](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L94)




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

    * Defined in [tools/google_search_tool.ts:30](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/google_search_tool.ts#L30)




### runAsync

  * runAsync(): Promise<unknown>

Runs the tool with the given arguments and context.

NOTE

    * Required if this tool needs to run at the client side.
    * Otherwise, can be skipped, e.g. for a built-in GoogleSearch tool for Gemini.

#### Returns Promise<unknown>

A promise that resolves to the tool response.

Overrides [BaseTool](BaseTool.html).[runAsync](BaseTool.html#runasync)

    * Defined in [tools/google_search_tool.ts:24](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/google_search_tool.ts#L24)




Constructors

constructor

Properties

[BASE_TOOL_SIGNATURE_SYMBOL]descriptionisLongRunningname

Accessors

apiVariant

Methods

_getDeclarationprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


