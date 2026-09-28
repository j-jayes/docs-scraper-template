[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [VertexAiSearchTool]()



# Class VertexAiSearchTool

A built-in tool using Vertex AI Search.

#### Hierarchy ([View Summary](../hierarchy.html#VertexAiSearchTool))

  * [BaseTool](BaseTool.html)
    * VertexAiSearchTool



  * Defined in [core/src/tools/vertex_ai_search_tool.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L54)



## Constructors

### constructor

  * new VertexAiSearchTool(params: [VertexAiSearchToolParams](../types/VertexAiSearchToolParams.html)): [VertexAiSearchTool]()

#### Parameters

    * params: [VertexAiSearchToolParams](../types/VertexAiSearchToolParams.html)

#### Returns [VertexAiSearchTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/tools/vertex_ai_search_tool.ts:62](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L62)




## Properties

### `Readonly`[BASE_TOOL_SIGNATURE_SYMBOL]

"[BASE_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base tool class.

Inherited from [BaseTool](BaseTool.html).[[BASE_TOOL_SIGNATURE_SYMBOL]](BaseTool.html#base_tool_signature_symbol)

  * Defined in [core/src/tools/base_tool.ts:64](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L64)



### `Readonly`bypassMultiToolsLimit

bypassMultiToolsLimit: boolean

  * Defined in [core/src/tools/vertex_ai_search_tool.ts:60](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L60)



### `Optional` `Readonly`dataStoreId

dataStoreId?: string

  * Defined in [core/src/tools/vertex_ai_search_tool.ts:55](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L55)



### `Optional` `Readonly`dataStoreSpecs

dataStoreSpecs?: [VertexAISearchDataStoreSpec](../interfaces/VertexAISearchDataStoreSpec.html)[]

  * Defined in [core/src/tools/vertex_ai_search_tool.ts:56](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L56)



### `Readonly`description

description: string

Inherited from [BaseTool](BaseTool.html).[description](BaseTool.html#description)

  * Defined in [core/src/tools/base_tool.ts:67](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L67)



### `Optional` `Readonly`filter

filter?: string

  * Defined in [core/src/tools/vertex_ai_search_tool.ts:58](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L58)



### `Readonly`isLongRunning

isLongRunning: boolean

Inherited from [BaseTool](BaseTool.html).[isLongRunning](BaseTool.html#islongrunning)

  * Defined in [core/src/tools/base_tool.ts:68](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L68)



### `Optional` `Readonly`maxResults

maxResults?: number

  * Defined in [core/src/tools/vertex_ai_search_tool.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L59)



### `Readonly`name

name: string

Inherited from [BaseTool](BaseTool.html).[name](BaseTool.html#name)

  * Defined in [core/src/tools/base_tool.ts:66](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_tool.ts#L66)



### `Optional` `Readonly`searchEngineId

searchEngineId?: string

  * Defined in [core/src/tools/vertex_ai_search_tool.ts:57](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L57)



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




### `Protected`buildVertexAiSearchConfig

  * buildVertexAiSearchConfig(  
_readonlyContext: [ReadonlyContext](ReadonlyContext.html),  
): [VertexAISearchConfig](../interfaces/VertexAISearchConfig.html)

Builds the VertexAISearch configuration.

Override this method in a subclass to dynamically customize the search configuration based on the context (e.g., set filter based on session state).

#### Parameters

    * _readonlyContext: [ReadonlyContext](ReadonlyContext.html)

#### Returns [VertexAISearchConfig](../interfaces/VertexAISearchConfig.html)

    * Defined in [core/src/tools/vertex_ai_search_tool.ts:111](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L111)




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

    * Defined in [core/src/tools/vertex_ai_search_tool.ts:123](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L123)




### runAsync

  * runAsync(): Promise<unknown>

Runs the tool with the given arguments and context.

NOTE

    * Required if this tool needs to run at the client side.
    * Otherwise, can be skipped, e.g. for a built-in GoogleSearch tool for Gemini.

#### Returns Promise<unknown>

A promise that resolves to the tool response.

Overrides [BaseTool](BaseTool.html).[runAsync](BaseTool.html#runasync)

    * Defined in [core/src/tools/vertex_ai_search_tool.ts:98](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_ai_search_tool.ts#L98)




Constructors

constructor

Properties

[BASE_TOOL_SIGNATURE_SYMBOL]bypassMultiToolsLimitdataStoreIddataStoreSpecsdescriptionfilterisLongRunningmaxResultsnamesearchEngineId

Accessors

apiVariant

Methods

_getDeclarationbuildVertexAiSearchConfigprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


