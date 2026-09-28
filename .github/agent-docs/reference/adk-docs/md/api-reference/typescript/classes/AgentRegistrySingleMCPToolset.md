[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AgentRegistrySingleMCPToolset]()



# Class AgentRegistrySingleMCPToolset

A specialized BaseToolset subclass designed to represent a single registered MCP server.

Unlike a standard MCPToolset, this class:

  1. Supports a dynamic `headerProvider` to fetch/refresh authorization and custom headers immediately before establishing the MCP connection session.
  2. Automatically injects the special `gcp.mcp.server.destination.id` telemetry metadata identifier into all resolved tools' custom metadata, allowing downstream execute_tool traces to be correctly attributed.



#### Hierarchy ([View Summary](../hierarchy.html#AgentRegistrySingleMCPToolset))

  * [BaseToolset](BaseToolset.html)
    * AgentRegistrySingleMCPToolset



  * Defined in [core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts:31](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts#L31)



## Constructors

### constructor

  * new AgentRegistrySingleMCPToolset(  
options: {  
authCredential?: [AuthCredential](../interfaces/AuthCredential.html);  
authScheme?: [AuthScheme](../types/AuthScheme.html);  
connectionParams: [StreamableHTTPConnectionParams](../interfaces/StreamableHTTPConnectionParams.html);  
destinationResourceId?: string;  
headerProvider?: (  
context?: [ReadonlyContext](ReadonlyContext.html),  
) => Record<string, string> | Promise<Record<string, string>>;  
prefix?: string;  
toolFilter?: string[] | [ToolPredicate](../types/ToolPredicate.html);  
},  
): [AgentRegistrySingleMCPToolset]()

#### Parameters

    * options: {  
authCredential?: [AuthCredential](../interfaces/AuthCredential.html);  
authScheme?: [AuthScheme](../types/AuthScheme.html);  
connectionParams: [StreamableHTTPConnectionParams](../interfaces/StreamableHTTPConnectionParams.html);  
destinationResourceId?: string;  
headerProvider?: (  
context?: [ReadonlyContext](ReadonlyContext.html),  
) => Record<string, string> | Promise<Record<string, string>>;  
prefix?: string;  
toolFilter?: string[] | [ToolPredicate](../types/ToolPredicate.html);  
}

Configuration for the MCP toolset.

      * ##### `Optional`authCredential?: [AuthCredential](../interfaces/AuthCredential.html)

Optional credential forwarded to each resolved tool.

      * ##### `Optional`authScheme?: [AuthScheme](../types/AuthScheme.html)

Optional auth scheme forwarded to each resolved tool.

      * ##### connectionParams: [StreamableHTTPConnectionParams](../interfaces/StreamableHTTPConnectionParams.html)

HTTP connection parameters for the MCP server.

      * ##### `Optional`destinationResourceId?: string

Telemetry identifier injected as `gcp.mcp.server.destination.id` into each resolved tool's custom metadata.

      * ##### `Optional`headerProvider?: (  
context?: [ReadonlyContext](ReadonlyContext.html),  
) => Record<string, string> | Promise<Record<string, string>>

Optional async function called immediately before each getTools invocation to supply or refresh request headers (e.g. GCP auth tokens).

      * ##### `Optional`prefix?: string

Optional prefix prepended to each tool name (e.g. `myServer_toolName`).

      * ##### `Optional`toolFilter?: string[] | [ToolPredicate](../types/ToolPredicate.html)

Optional predicate or list of tool names to include. When omitted, all tools from the server are returned.

#### Returns [AgentRegistrySingleMCPToolset]()

Overrides [BaseToolset](BaseToolset.html).[constructor](BaseToolset.html#constructor)

    * Defined in [core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts:53](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts#L53)




## Properties

### `Readonly`[BASE_TOOLSET_SIGNATURE_SYMBOL]

"[BASE_TOOLSET_SIGNATURE_SYMBOL]": true

Inherited from [BaseToolset](BaseToolset.html).[[BASE_TOOLSET_SIGNATURE_SYMBOL]](BaseToolset.html#base_toolset_signature_symbol)

  * Defined in [core/src/tools/base_toolset.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L44)



### `Optional` `Readonly`authCredential

authCredential?: [AuthCredential](../interfaces/AuthCredential.html)

  * Defined in [core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts#L38)



### `Optional` `Readonly`authScheme

authScheme?: [AuthScheme](../types/AuthScheme.html)

  * Defined in [core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts:37](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts#L37)



### `Readonly`connectionParams

connectionParams: [StreamableHTTPConnectionParams](../interfaces/StreamableHTTPConnectionParams.html)

  * Defined in [core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts:33](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts#L33)



### `Optional` `Readonly`destinationResourceId

destinationResourceId?: string

  * Defined in [core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts#L32)



### `Optional` `Readonly`headerProvider

headerProvider?: (  
context?: [ReadonlyContext](ReadonlyContext.html),  
) => Record<string, string> | Promise<Record<string, string>>

  * Defined in [core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts:34](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts#L34)



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

    * Defined in [core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts:154](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts#L154)




### getTools

  * getTools(context?: [ReadonlyContext](ReadonlyContext.html)): Promise<[BaseTool](BaseTool.html)[]>

Connects to the underlying MCP server, retrieves tool definitions, prefixes tool names, and injects destination telemetry metadata into each tool.

The `headerProvider`, if configured, is invoked immediately before the connection is established so that tokens are always fresh.

#### Parameters

    * `Optional`context: [ReadonlyContext](ReadonlyContext.html)

Optional readonly agent context passed to the header provider.

#### Returns Promise<[BaseTool](BaseTool.html)[]>

The resolved and optionally filtered list of [MCPTool](MCPTool.html) instances.

Overrides [BaseToolset](BaseToolset.html).[getTools](BaseToolset.html#gettools)

    * Defined in [core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts:82](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry_mcp_toolset.ts#L82)




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

[BASE_TOOLSET_SIGNATURE_SYMBOL]authCredentialauthSchemeconnectionParamsdestinationResourceIdheaderProviderprefixtoolFilter

Methods

closegetToolsisToolSelectedprocessLlmRequest

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


