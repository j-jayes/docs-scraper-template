[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseTool]()



# Class BaseTool`Abstract`

The base class for all tools.

#### Hierarchy ([View Summary](../hierarchy.html#BaseTool))

  * BaseTool
    * [LoadMcpResourceTool](LoadMcpResourceTool.html)
    * [MCPTool](MCPTool.html)
    * [RunSkillInlineScriptTool](RunSkillInlineScriptTool.html)
    * [RunSkillScriptTool](RunSkillScriptTool.html)
    * [AgentTool](AgentTool.html)
    * [ConsolidateContextTool](ConsolidateContextTool.html)
    * [EnterpriseWebSearchTool](EnterpriseWebSearchTool.html)
    * [ExampleTool](ExampleTool.html)
    * [ExitLoopTool](ExitLoopTool.html)
    * [FunctionTool](FunctionTool.html)
    * [GoogleMapsGroundingTool](GoogleMapsGroundingTool.html)
    * [GoogleSearchTool](GoogleSearchTool.html)
    * [LoadArtifactsTool](LoadArtifactsTool.html)
    * [LoadMemoryTool](LoadMemoryTool.html)
    * [PreloadMemoryTool](PreloadMemoryTool.html)
    * [UrlContextTool](UrlContextTool.html)
    * [VertexAiSearchTool](VertexAiSearchTool.html)
    * [VertexRagRetrievalTool](VertexRagRetrievalTool.html)
    * [ListSkillsTool](ListSkillsTool.html)
    * [LoadSkillResourceTool](LoadSkillResourceTool.html)
    * [LoadSkillTool](LoadSkillTool.html)
    * [SearchSkillsTool](SearchSkillsTool.html)
    * [RestApiTool](RestApiTool.html)



  * Defined in [core/src/tools/base_tool.ts:62](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L62)



## Constructors

### constructor

  * new BaseTool(params: [BaseToolParams](../interfaces/BaseToolParams.html)): [BaseTool]()

Base constructor for a tool.

#### Parameters

    * params: [BaseToolParams](../interfaces/BaseToolParams.html)

The parameters for `BaseTool`.

#### Returns [BaseTool]()

    * Defined in [core/src/tools/base_tool.ts:75](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L75)




## Properties

### `Readonly`[BASE_TOOL_SIGNATURE_SYMBOL]

"[BASE_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base tool class.

  * Defined in [core/src/tools/base_tool.ts:64](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L64)



### `Readonly`description

description: string

  * Defined in [core/src/tools/base_tool.ts:67](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L67)



### `Readonly`isLongRunning

isLongRunning: boolean

  * Defined in [core/src/tools/base_tool.ts:68](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L68)



### `Readonly`name

name: string

  * Defined in [core/src/tools/base_tool.ts:66](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L66)



## Accessors

### apiVariant

  * get apiVariant(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

The Google API LLM variant to use.

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

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

    * Defined in [core/src/tools/base_tool.ts:120](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L120)




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

    * Defined in [core/src/tools/base_tool.ts:109](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L109)




Constructors

constructor

Properties

[BASE_TOOL_SIGNATURE_SYMBOL]descriptionisLongRunningname

Accessors

apiVariant

Methods

_getDeclarationprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


