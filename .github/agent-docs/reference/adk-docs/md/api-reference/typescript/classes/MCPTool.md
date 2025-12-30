[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [MCPTool]()



# Class MCPTool

Represents a tool exposed via the Model Context Protocol (MCP).

This class acts as a wrapper around a tool definition received from an MCP server. It translates the MCP tool's schema into a format compatible with the Gemini AI platform (FunctionDeclaration) and handles the remote execution of the tool by communicating with the MCP server through an [MCPSessionManager](MCPSessionManager.html).

When an LLM decides to call this tool, the `runAsync` method will be invoked, which in turn establishes an MCP session, sends a `callTool` request with the provided arguments, and returns the result from the remote tool.

#### Hierarchy ([View Summary](../hierarchy.html#MCPTool))

  * [BaseTool](BaseTool.html)
    * MCPTool



  * Defined in [core/src/tools/mcp/mcp_tool.ts:29](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_tool.ts#L29)



## Constructors

### constructor

  * new MCPTool(  
mcpTool: { [key: string]: unknown },  
mcpSessionManager: [MCPSessionManager](MCPSessionManager.html),  
): [MCPTool]()

#### Parameters

    * mcpTool: { [key: string]: unknown }
    * mcpSessionManager: [MCPSessionManager](MCPSessionManager.html)

#### Returns [MCPTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/tools/mcp/mcp_tool.ts:33](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_tool.ts#L33)




## Properties

### `Readonly`description

description: string

Inherited from [BaseTool](BaseTool.html).[description](BaseTool.html#description)

  * Defined in [core/src/tools/base_tool.ts:44](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L44)



### `Readonly`isLongRunning

isLongRunning: boolean

Inherited from [BaseTool](BaseTool.html).[isLongRunning](BaseTool.html#islongrunning)

  * Defined in [core/src/tools/base_tool.ts:45](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L45)



### `Readonly`name

name: string

Inherited from [BaseTool](BaseTool.html).[name](BaseTool.html#name)

  * Defined in [core/src/tools/base_tool.ts:43](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L43)



## Accessors

### apiVariant

  * get apiVariant(): GoogleLLMVariant

The Google API LLM variant to use.

#### Returns GoogleLLMVariant

Inherited from BaseTool.apiVariant

    * Defined in [core/src/tools/base_tool.ts:125](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L125)




## Methods

### _getDeclaration

  * _getDeclaration(): FunctionDeclaration

Gets the OpenAPI specification of this tool in the form of a FunctionDeclaration.

NOTE

    * Required if subclass uses the default implementation of `processLlmRequest` to add function declaration to LLM request.
    * Otherwise, can be skipped, e.g. for a built-in GoogleSearch tool for Gemini.

#### Returns FunctionDeclaration

The FunctionDeclaration of this tool, or undefined if it doesn't need to be added to LlmRequest.config.

Overrides [BaseTool](BaseTool.html).[_getDeclaration](BaseTool.html#_getdeclaration)

    * Defined in [core/src/tools/mcp/mcp_tool.ts:39](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_tool.ts#L39)




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

Inherited from [BaseTool](BaseTool.html).[processLlmRequest](BaseTool.html#processllmrequest)

    * Defined in [core/src/tools/base_tool.ts:97](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_tool.ts#L97)




### runAsync

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

Overrides [BaseTool](BaseTool.html).[runAsync](BaseTool.html#runasync)

    * Defined in [core/src/tools/mcp/mcp_tool.ts:52](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_tool.ts#L52)




Constructors

constructor

Properties

descriptionisLongRunningname

Accessors

apiVariant

Methods

_getDeclarationprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


