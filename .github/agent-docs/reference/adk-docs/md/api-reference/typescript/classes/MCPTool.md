[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [MCPTool]()



# Class MCPTool

Represents a tool exposed via the Model Context Protocol (MCP).

This class acts as a wrapper around a tool definition received from an MCP server. It translates the MCP tool's schema into a format compatible with the Gemini AI platform (FunctionDeclaration) and handles the remote execution of the tool by communicating with the MCP server through an [MCPSessionManager](MCPSessionManager.html).

When an LLM decides to call this tool, the `runAsync` method will be invoked, which in turn establishes an MCP session, sends a `callTool` request with the provided arguments, and returns the result from the remote tool.

The originalName parameter allows the tool to track the native tool name exposed by the MCP server. This is critical when the toolset applies a prefix to tool names (e.g., for LLM namespace disambiguation), ensuring the correct original name is used when executing on the server.

#### Hierarchy ([View Summary](../hierarchy.html#MCPTool))

  * [BaseTool](BaseTool.html)
    * MCPTool



  * Defined in [core/src/tools/mcp/mcp_tool.ts:38](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_tool.ts#L38)



## Constructors

### constructor

  * new MCPTool(  
mcpTool: {},  
mcpSessionManager: [MCPSessionManager](MCPSessionManager.html),  
originalName?: string,  
): [MCPTool]()

#### Parameters

    * mcpTool: {}
    * mcpSessionManager: [MCPSessionManager](MCPSessionManager.html)
    * `Optional`originalName: string

#### Returns [MCPTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/tools/mcp/mcp_tool.ts:43](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_tool.ts#L43)




## Properties

### `Readonly`[BASE_TOOL_SIGNATURE_SYMBOL]

"[BASE_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base tool class.

Inherited from [BaseTool](BaseTool.html).[[BASE_TOOL_SIGNATURE_SYMBOL]](BaseTool.html#base_tool_signature_symbol)

  * Defined in [core/src/tools/base_tool.ts:83](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_tool.ts#L83)



### `Readonly`description

description: string

Inherited from [BaseTool](BaseTool.html).[description](BaseTool.html#description)

  * Defined in [core/src/tools/base_tool.ts:86](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_tool.ts#L86)



### `Readonly`isLongRunning

isLongRunning: boolean

Inherited from [BaseTool](BaseTool.html).[isLongRunning](BaseTool.html#islongrunning)

  * Defined in [core/src/tools/base_tool.ts:87](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_tool.ts#L87)



### `Readonly`name

name: string

Inherited from [BaseTool](BaseTool.html).[name](BaseTool.html#name)

  * Defined in [core/src/tools/base_tool.ts:85](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_tool.ts#L85)



## Accessors

### apiVariant

  * get apiVariant(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

The Google API LLM variant to use.

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

Inherited from BaseTool.apiVariant

    * Defined in [core/src/tools/base_tool.ts:198](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_tool.ts#L198)




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

    * Defined in [core/src/tools/mcp/mcp_tool.ts:54](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_tool.ts#L54)




### checkRequireConfirmation

  * checkRequireConfirmation(  
_args: Record<string, unknown>,  
_toolContext?: [Context](Context.html),  
): Promise<boolean>

Whether this tool needs a human to approve `args` before it runs.

The gate itself lives in the tool that owns it (see `FunctionTool`), but the resume path has to ask the same question a turn later, to check that an approval it is about to honour belongs to a tool that gates at all. A tool that never gates returns false here, which is the safe default: an approval naming it is meaningless and gets rejected rather than executed. Mirrors Python's `BaseTool.check_require_confirmation`.

#### Parameters

    * _args: Record<string, unknown>

The arguments the tool would run with.

    * `Optional`_toolContext: [Context](Context.html)

The context of the call, when there is one.

#### Returns Promise<boolean>

Whether the call requires confirmation.

Inherited from [BaseTool](BaseTool.html).[checkRequireConfirmation](BaseTool.html#checkrequireconfirmation)

    * Defined in [core/src/tools/base_tool.ts:144](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_tool.ts#L144)




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

    * Defined in [core/src/tools/base_tool.ts:160](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_tool.ts#L160)




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

    * Defined in [core/src/tools/mcp/mcp_tool.ts:65](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_tool.ts#L65)




Constructors

constructor

Properties

[BASE_TOOL_SIGNATURE_SYMBOL]descriptionisLongRunningname

Accessors

apiVariant

Methods

_getDeclarationcheckRequireConfirmationprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


