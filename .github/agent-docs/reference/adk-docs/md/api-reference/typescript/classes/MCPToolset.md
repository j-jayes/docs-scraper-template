[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [MCPToolset]()



# Class MCPToolset

A toolset that dynamically discovers and provides tools from a Model Context Protocol (MCP) server.

This class connects to an MCP server, retrieves the list of available tools, and wraps each of them in an [MCPTool](MCPTool.html) instance. This allows the agent to seamlessly use tools from an external MCP-compliant service.

The toolset can be configured with a filter to selectively expose a subset of the tools provided by the MCP server.

Usage: import { MCPToolset } from '@google/adk'; import { StreamableHTTPConnectionParamsSchema } from '@google/adk';

const connectionParams = StreamableHTTPConnectionParamsSchema.parse({ type: "StreamableHTTPConnectionParams", url: "<http://localhost:8788/mcp>" });

const mcpToolset = new MCPToolset(connectionParams); const tools = await mcpToolset.getTools();

#### Hierarchy ([View Summary](../hierarchy.html#MCPToolset))

  * [BaseToolset](BaseToolset.html)
    * MCPToolset



  * Defined in [tools/mcp/mcp_toolset.ts:40](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_toolset.ts#L40)



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

    * Defined in [tools/mcp/mcp_toolset.ts:43](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_toolset.ts#L43)




## Properties

### `Readonly`[BASE_TOOLSET_SIGNATURE_SYMBOL]

"[BASE_TOOLSET_SIGNATURE_SYMBOL]": true

Inherited from [BaseToolset](BaseToolset.html).[[BASE_TOOLSET_SIGNATURE_SYMBOL]](BaseToolset.html#base_toolset_signature_symbol)

  * Defined in [tools/base_toolset.ts:44](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_toolset.ts#L44)



### `Optional` `Readonly`prefix

prefix?: string

Inherited from [BaseToolset](BaseToolset.html).[prefix](BaseToolset.html#prefix)

  * Defined in [tools/base_toolset.ts:48](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_toolset.ts#L48)



### `Readonly`toolFilter

toolFilter: string[] | [ToolPredicate](../types/ToolPredicate.html)

Inherited from [BaseToolset](BaseToolset.html).[toolFilter](BaseToolset.html#toolfilter)

  * Defined in [tools/base_toolset.ts:47](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_toolset.ts#L47)



## Methods

### close

  * close(): Promise<void>

Closes the toolset.

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

#### Returns Promise<void>

A Promise that resolves when the toolset is closed.

Overrides [BaseToolset](BaseToolset.html).[close](BaseToolset.html#close)

    * Defined in [tools/mcp/mcp_toolset.ts:72](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_toolset.ts#L72)




### getTools

  * getTools(): Promise<[BaseTool](BaseTool.html)[]>

Returns the tools that should be exposed to LLM.

#### Returns Promise<[BaseTool](BaseTool.html)[]>

A Promise that resolves to the list of tools.

Overrides [BaseToolset](BaseToolset.html).[getTools](BaseToolset.html#gettools)

    * Defined in [tools/mcp/mcp_toolset.ts:52](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_toolset.ts#L52)




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

    * Defined in [tools/base_toolset.ts:79](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_toolset.ts#L79)




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

    * Defined in [tools/base_toolset.ts:107](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_toolset.ts#L107)




Constructors

constructor

Properties

[BASE_TOOLSET_SIGNATURE_SYMBOL]prefixtoolFilter

Methods

closegetToolsisToolSelectedprocessLlmRequest

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


