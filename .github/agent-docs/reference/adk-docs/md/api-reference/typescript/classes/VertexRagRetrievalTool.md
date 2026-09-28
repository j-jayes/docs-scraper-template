[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [VertexRagRetrievalTool]()



# Class VertexRagRetrievalTool

A tool that retrieves relevant content from a Vertex AI RAG corpus to ground model responses.

This tool operates server-side; it modifies the LLM request config to enable RAG retrieval via the `retrieval.vertexRagStore` field and does not perform local code execution.

**Note:** The Vertex AI RAG Engine only supports one corpus per `ragResources` array. Create one `VertexRagRetrievalTool` instance per corpus.

#### Example
    
    
    import { VertexRagRetrievalTool } from '@google/adk';  
    import { VertexRagStore } from '@google/genai';  
      
    const ragTool = new VertexRagRetrievalTool({  
      ragResources: [{ragCorpus: 'projects/my-project/locations/us-central1/ragCorpora/my-corpus'}],  
      similarityTopK: 5,  
    });  
      
    const agent = new LlmAgent({ tools: [ragTool], ... });
    Copy

#### Hierarchy ([View Summary](../hierarchy.html#VertexRagRetrievalTool))

  * [BaseTool](BaseTool.html)
    * VertexRagRetrievalTool



  * Defined in [core/src/tools/vertex_rag_retrieval_tool.ts:36](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_rag_retrieval_tool.ts#L36)



## Constructors

### constructor

  * new VertexRagRetrievalTool(config: VertexRagStore): [VertexRagRetrievalTool]()

#### Parameters

    * config: VertexRagStore

#### Returns [VertexRagRetrievalTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/tools/vertex_rag_retrieval_tool.ts:39](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_rag_retrieval_tool.ts#L39)




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

    * Defined in [core/src/tools/vertex_rag_retrieval_tool.ts:55](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_rag_retrieval_tool.ts#L55)




### runAsync

  * runAsync(): Promise<unknown>

This tool is executed server-side by the Vertex AI RAG Engine. Local execution is not required.

#### Returns Promise<unknown>

Overrides [BaseTool](BaseTool.html).[runAsync](BaseTool.html#runasync)

    * Defined in [core/src/tools/vertex_rag_retrieval_tool.ts:51](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/vertex_rag_retrieval_tool.ts#L51)




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


