[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [OpenAPIToolset]()



# Class OpenAPIToolset

Base class for toolset.

A toolset is a collection of tools that can be used by an agent.

#### Hierarchy ([View Summary](../hierarchy.html#OpenAPIToolset))

  * [BaseToolset](BaseToolset.html)
    * OpenAPIToolset



  * Defined in [core/src/tools/openapi_tool/openapi_toolset.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_toolset.ts#L18)



## Constructors

### constructor

  * new OpenAPIToolset(  
options?: {  
authCredential?: [AuthCredential](../interfaces/AuthCredential.html);  
authScheme?: SecuritySchemeObject;  
credentialKey?: string;  
headerProvider?: (context: [ReadonlyContext](ReadonlyContext.html)) => Record<string, string>;  
prefix?: string;  
preservePropertyNames?: boolean;  
specDict?: Document<{}>;  
specStr?: string;  
specType?: "json" | "yaml";  
toolFilter?: string[] | [ToolPredicate](../types/ToolPredicate.html);  
},  
): [OpenAPIToolset]()

#### Parameters

    * options: {  
authCredential?: [AuthCredential](../interfaces/AuthCredential.html);  
authScheme?: SecuritySchemeObject;  
credentialKey?: string;  
headerProvider?: (context: [ReadonlyContext](ReadonlyContext.html)) => Record<string, string>;  
prefix?: string;  
preservePropertyNames?: boolean;  
specDict?: Document<{}>;  
specStr?: string;  
specType?: "json" | "yaml";  
toolFilter?: string[] | [ToolPredicate](../types/ToolPredicate.html);  
} = {}

#### Returns [OpenAPIToolset]()

Overrides [BaseToolset](BaseToolset.html).[constructor](BaseToolset.html#constructor)

    * Defined in [core/src/tools/openapi_tool/openapi_toolset.ts:21](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_toolset.ts#L21)




## Properties

### `Readonly`[BASE_TOOLSET_SIGNATURE_SYMBOL]

"[BASE_TOOLSET_SIGNATURE_SYMBOL]": true

Inherited from [BaseToolset](BaseToolset.html).[[BASE_TOOLSET_SIGNATURE_SYMBOL]](BaseToolset.html#base_toolset_signature_symbol)

  * Defined in [core/src/tools/base_toolset.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L44)



### `Optional` `Readonly`prefix

prefix?: string

Inherited from [BaseToolset](BaseToolset.html).[prefix](BaseToolset.html#prefix)

  * Defined in [core/src/tools/base_toolset.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L48)



### `Readonly`toolFilter

toolFilter: string[] | [ToolPredicate](../types/ToolPredicate.html)

Inherited from [BaseToolset](BaseToolset.html).[toolFilter](BaseToolset.html#toolfilter)

  * Defined in [core/src/tools/base_toolset.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L47)



## Methods

### close

  * close(): Promise<void>

Closes the toolset.

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

#### Returns Promise<void>

A Promise that resolves when the toolset is closed.

Overrides [BaseToolset](BaseToolset.html).[close](BaseToolset.html#close)

    * Defined in [core/src/tools/openapi_tool/openapi_toolset.ts:106](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_toolset.ts#L106)




### getTools

  * getTools(context?: [ReadonlyContext](ReadonlyContext.html)): Promise<[BaseTool](BaseTool.html)[]>

Returns the tools that should be exposed to LLM.

#### Parameters

    * `Optional`context: [ReadonlyContext](ReadonlyContext.html)

Context used to filter tools available to the agent. If not defined, all tools in the toolset are returned.

#### Returns Promise<[BaseTool](BaseTool.html)[]>

A Promise that resolves to the list of tools.

Overrides [BaseToolset](BaseToolset.html).[getTools](BaseToolset.html#gettools)

    * Defined in [core/src/tools/openapi_tool/openapi_toolset.ts:93](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/openapi_tool/openapi_toolset.ts#L93)




### `Protected`isToolSelected

  * isToolSelected(tool: [BaseTool](BaseTool.html), context: [ReadonlyContext](ReadonlyContext.html)): boolean

Returns whether the tool should be exposed to LLM.

#### Parameters

    * tool: [BaseTool](BaseTool.html)

The tool to check.

    * context: [ReadonlyContext](ReadonlyContext.html)

Context used to filter tools available to the agent.

#### Returns boolean

Whether the tool should be exposed to LLM.

Inherited from [BaseToolset](BaseToolset.html).[isToolSelected](BaseToolset.html#istoolselected)

    * Defined in [core/src/tools/base_toolset.ts:79](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L79)




### processLlmRequest

  * processLlmRequest(toolContext: [Context](Context.html), llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): Promise<void>

Processes the outgoing LLM request for this toolset. This method will be called before each tool processes the llm request.

Use cases:

    * Instead of let each tool process the llm request, we can let the toolset process the llm request. e.g. ComputerUseToolset can add computer use tool to the llm request.

#### Parameters

    * toolContext: [Context](Context.html)

The context of the tool.

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The outgoing LLM request, mutable this method.

#### Returns Promise<void>

Inherited from [BaseToolset](BaseToolset.html).[processLlmRequest](BaseToolset.html#processllmrequest)

    * Defined in [core/src/tools/base_toolset.ts:111](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L111)




Constructors

constructor

Properties

[BASE_TOOLSET_SIGNATURE_SYMBOL]prefixtoolFilter

Methods

closegetToolsisToolSelectedprocessLlmRequest

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


