[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [FinishTaskTool]()



# Class FinishTaskTool

Tool for signaling that a task-mode [LlmAgent](Agent.html) has completed its task.

The tool's parameters mirror the agent's `outputSchema` (or a default single `result` string). The task-mode wrapper sniffs the `finish_task` function call and, on a successful function response, promotes the call's arguments to the node's output.

Ported from `google/adk-python` `agents/llm/task/_finish_task_tool.py::FinishTaskTool`.

#### Hierarchy ([View Summary](../hierarchy.html#FinishTaskTool))

  * [BaseTool](BaseTool.html)
    * FinishTaskTool



  * Defined in [core/src/tools/finish_task_tool.ts:49](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/finish_task_tool.ts#L49)



## Constructors

### constructor

  * new FinishTaskTool(outputSchema?: Schema): [FinishTaskTool]()

#### Parameters

    * `Optional`outputSchema: Schema

#### Returns [FinishTaskTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/tools/finish_task_tool.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/finish_task_tool.ts#L59)




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



### `Optional` `Readonly`wrapperKey

wrapperKey?: string

When the output schema is a non-object (primitive/array), the value is wrapped under this key (the GenAI API requires object-typed parameters). `undefined` for object schemas (the value lives at the top level of args).

  * Defined in [core/src/tools/finish_task_tool.ts:57](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/finish_task_tool.ts#L57)



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

    * Defined in [core/src/tools/finish_task_tool.ts:72](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/finish_task_tool.ts#L72)




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




### extractOutput

  * extractOutput(args: Record<string, unknown>): unknown

Extracts the task output from a `finish_task` call's arguments, applying the wrapper-key unwrapping when the schema is a non-object.

#### Parameters

    * args: Record<string, unknown>

#### Returns unknown

    * Defined in [core/src/tools/finish_task_tool.ts:102](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/finish_task_tool.ts#L102)




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

    * Defined in [core/src/tools/finish_task_tool.ts:83](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/finish_task_tool.ts#L83)




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

    * Defined in [core/src/tools/finish_task_tool.ts:109](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/finish_task_tool.ts#L109)




Constructors

constructor

Properties

[BASE_TOOL_SIGNATURE_SYMBOL]descriptionisLongRunningnamewrapperKey

Accessors

apiVariant

Methods

_getDeclarationcheckRequireConfirmationextractOutputprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


