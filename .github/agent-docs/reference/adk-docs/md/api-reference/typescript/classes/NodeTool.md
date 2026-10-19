[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [NodeTool]()



# Class NodeTool

A tool that executes a [BaseNode](BaseNode.html) (e.g. a `Workflow` or a function node) on behalf of an `LlmAgent`. This is the inverse of [ToolNode](ToolNode.html) (which exposes a tool as a workflow node): here a node/workflow is exposed to a model as a callable tool.

The wrapped node MUST declare an `inputSchema` (the tool's parameter schema is derived from it). When the model calls the tool, the node runs with a [NodeContext](NodeContext.html) bridged from the tool's agent context (sharing the invocation, session, and state); the node's structured output becomes the tool result.

Ported from `google/adk-python` `tools/_node_tool.py::NodeTool`.

The tool is marked long-running so a node that pauses for input (`RequestInput`) does not force a synthetic empty response.

#### Hierarchy ([View Summary](../hierarchy.html#NodeTool))

  * [BaseTool](BaseTool.html)
    * NodeTool



  * Defined in [core/src/workflow/nodes/node_tool.ts:48](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/node_tool.ts#L48)



## Constructors

### constructor

  * new NodeTool(node: [BaseNode](BaseNode.html), name?: string, description?: string): [NodeTool]()

#### Parameters

    * node: [BaseNode](BaseNode.html)
    * `Optional`name: string
    * `Optional`description: string

#### Returns [NodeTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/workflow/nodes/node_tool.ts:54](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/node_tool.ts#L54)




## Properties

### `Readonly`[BASE_TOOL_SIGNATURE_SYMBOL]

"[BASE_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base tool class.

Inherited from [BaseTool](BaseTool.html).[[BASE_TOOL_SIGNATURE_SYMBOL]](BaseTool.html#base_tool_signature_symbol)

  * Defined in [core/src/tools/base_tool.ts:83](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_tool.ts#L83)



### `Readonly`[NODE_TOOL_SIGNATURE_SYMBOL]

"[NODE_TOOL_SIGNATURE_SYMBOL]": true

Brand identifying this object as a NodeTool (see `isNodeTool`).

  * Defined in [core/src/workflow/nodes/node_tool.ts:50](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/node_tool.ts#L50)



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



### `Readonly`node

node: [BaseNode](BaseNode.html)

  * Defined in [core/src/workflow/nodes/node_tool.ts:52](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/node_tool.ts#L52)



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

    * Defined in [core/src/workflow/nodes/node_tool.ts:70](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/node_tool.ts#L70)




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

    * Defined in [core/src/workflow/nodes/node_tool.ts:93](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/workflow/nodes/node_tool.ts#L93)




Constructors

constructor

Properties

[BASE_TOOL_SIGNATURE_SYMBOL][NODE_TOOL_SIGNATURE_SYMBOL]descriptionisLongRunningnamenode

Accessors

apiVariant

Methods

_getDeclarationcheckRequireConfirmationprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


