[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [MCPToolset]()



# Class MCPToolset

A toolset that dynamically discovers and provides tools from a Model Context Protocol (MCP) server.

This class connects to an MCP server, retrieves the list of available tools, and wraps each of them in an [MCPTool](MCPTool.html) instance. This allows the agent to seamlessly use tools from an external MCP-compliant service.

The toolset can be configured with a filter to selectively expose a subset of the tools provided by the MCP server.

It can also be configured with a prefix. If provided, all tools discovered from the MCP server will have their names prefixed with `${prefix}_`. When the LLM invokes the prefixed tool, this toolset transparently strips the prefix before sending the request to the underlying MCP server.

Usage: import { MCPToolset } from '@google/adk'; import { StreamableHTTPConnectionParamsSchema } from '@google/adk';

const connectionParams = StreamableHTTPConnectionParamsSchema.parse({ type: "StreamableHTTPConnectionParams", url: "<http://localhost:8788/mcp>" });

const mcpToolset = new MCPToolset(connectionParams); const tools = await mcpToolset.getTools();

#### Hierarchy ([View Summary](../hierarchy.html#MCPToolset))

  * [BaseToolset](BaseToolset.html)
    * MCPToolset



  * Defined in [core/src/tools/mcp/mcp_toolset.ts:53](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_toolset.ts#L53)



## Constructors

### constructor

  * new MCPToolset(  
connectionParams: [MCPConnectionParams](../types/MCPConnectionParams.html),  
toolFilter?: string[] | [ToolPredicate](../types/ToolPredicate.html),  
prefix?: string,  
): [MCPToolset]()

#### Parameters

    * connectionParams: [MCPConnectionParams](../types/MCPConnectionParams.html)
    * toolFilter: string[] | [ToolPredicate](../types/ToolPredicate.html) = []
    * `Optional`prefix: string

#### Returns [MCPToolset]()

Overrides [BaseToolset](BaseToolset.html).[constructor](BaseToolset.html#constructor)

    * Defined in [core/src/tools/mcp/mcp_toolset.ts:56](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_toolset.ts#L56)




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

    * Defined in [core/src/tools/mcp/mcp_toolset.ts:184](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_toolset.ts#L184)




### getResourceInfo

  * getResourceInfo(name: string): Promise<{}>

Returns metadata for the resource whose name matches `name`.

#### Parameters

    * name: string

The advertised name of the resource.

#### Returns Promise<{}>

The matching MCP `Resource`.

#### Throws

If no resource with the given name is advertised by the server.

    * Defined in [core/src/tools/mcp/mcp_toolset.ts:136](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_toolset.ts#L136)




### getTools

  * getTools(context?: [ReadonlyContext](ReadonlyContext.html)): Promise<[BaseTool](BaseTool.html)[]>

Returns the tools that should be exposed to LLM.

#### Parameters

    * `Optional`context: [ReadonlyContext](ReadonlyContext.html)

Context used to filter tools available to the agent. If not defined, all tools in the toolset are returned.

#### Returns Promise<[BaseTool](BaseTool.html)[]>

A Promise that resolves to the list of tools.

Overrides [BaseToolset](BaseToolset.html).[getTools](BaseToolset.html#gettools)

    * Defined in [core/src/tools/mcp/mcp_toolset.ts:65](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_toolset.ts#L65)




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




### listResources

  * listResources(): Promise<string[]>

Lists the names of the resources advertised by the MCP server.

#### Returns Promise<string[]>

The resource names available on the server.

    * Defined in [core/src/tools/mcp/mcp_toolset.ts:119](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_toolset.ts#L119)




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




### readResource

  * readResource(name: string): Promise<({} | {})[]>

Reads the contents of the named resource from the MCP server.

The resource name is resolved to a URI via getResourceInfo before reading. Binary contents are returned base64-encoded, exactly as provided by the server (never decoded and re-encoded).

#### Parameters

    * name: string

The advertised name of the resource to read.

#### Returns Promise<({} | {})[]>

The resource contents (text and/or base64-encoded binary).

#### Throws

If the resource is unknown or has no URI.

    * Defined in [core/src/tools/mcp/mcp_toolset.ts:165](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_toolset.ts#L165)




Constructors

constructor

Properties

[BASE_TOOLSET_SIGNATURE_SYMBOL]prefixtoolFilter

Methods

closegetResourceInfogetToolsisToolSelectedlistResourcesprocessLlmRequestreadResource

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


