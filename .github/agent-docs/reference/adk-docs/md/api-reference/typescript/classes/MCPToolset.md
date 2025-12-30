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



  * Defined in [core/src/tools/mcp/mcp_toolset.ts:41](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_toolset.ts#L41)



## Constructors

### constructor

  * new MCPToolset(  
connectionParams: [MCPConnectionParams](../types/MCPConnectionParams.html),  
toolFilter?: string[] | ToolPredicate,  
): [MCPToolset]()

#### Parameters

    * connectionParams: [MCPConnectionParams](../types/MCPConnectionParams.html)
    * toolFilter: string[] | ToolPredicate = []

#### Returns [MCPToolset]()

Overrides [BaseToolset](BaseToolset.html).[constructor](BaseToolset.html#constructor)

    * Defined in [core/src/tools/mcp/mcp_toolset.ts:44](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_toolset.ts#L44)




## Properties

### `Readonly`toolFilter

toolFilter: string[] | ToolPredicate

Inherited from [BaseToolset](BaseToolset.html).[toolFilter](BaseToolset.html#toolfilter)

  * Defined in [core/src/tools/base_toolset.ts:27](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_toolset.ts#L27)



## Methods

### close

  * close(): Promise<void>

Closes the toolset.

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

#### Returns Promise<void>

A Promise that resolves when the toolset is closed.

Overrides [BaseToolset](BaseToolset.html).[close](BaseToolset.html#close)

    * Defined in [core/src/tools/mcp/mcp_toolset.ts:65](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_toolset.ts#L65)




### getTools

  * getTools(context?: ReadonlyContext): Promise<[BaseTool](BaseTool.html)[]>

Returns the tools that should be exposed to LLM.

#### Parameters

    * `Optional`context: ReadonlyContext

Context used to filter tools available to the agent. If not defined, all tools in the toolset are returned.

#### Returns Promise<[BaseTool](BaseTool.html)[]>

A Promise that resolves to the list of tools.

Overrides [BaseToolset](BaseToolset.html).[getTools](BaseToolset.html#gettools)

    * Defined in [core/src/tools/mcp/mcp_toolset.ts:51](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_toolset.ts#L51)




### `Protected`isToolSelected

  * isToolSelected(tool: [BaseTool](BaseTool.html), context: ReadonlyContext): boolean

Returns whether the tool should be exposed to LLM.

#### Parameters

    * tool: [BaseTool](BaseTool.html)

The tool to check.

    * context: ReadonlyContext

Context used to filter tools available to the agent.

#### Returns boolean

Whether the tool should be exposed to LLM.

Inherited from [BaseToolset](BaseToolset.html).[isToolSelected](BaseToolset.html#istoolselected)

    * Defined in [core/src/tools/base_toolset.ts:57](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_toolset.ts#L57)




### processLlmRequest

  * processLlmRequest(  
toolContext: [ToolContext](ToolContext.html),  
llmRequest: [LlmRequest](../interfaces/LlmRequest.html),  
): Promise<void>

Processes the outgoing LLM request for this toolset. This method will be called before each tool processes the llm request.

Use cases:

    * Instead of let each tool process the llm request, we can let the toolset process the llm request. e.g. ComputerUseToolset can add computer use tool to the llm request.

#### Parameters

    * toolContext: [ToolContext](ToolContext.html)

The context of the tool.

    * llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The outgoing LLM request, mutable this method.

#### Returns Promise<void>

Inherited from [BaseToolset](BaseToolset.html).[processLlmRequest](BaseToolset.html#processllmrequest)

    * Defined in [core/src/tools/base_toolset.ts:85](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_toolset.ts#L85)




Constructors

constructor

Properties

toolFilter

Methods

closegetToolsisToolSelectedprocessLlmRequest

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


