[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AgentTool]()



# Class AgentTool

A tool that wraps an agent.

This tool allows an agent to be called as a tool within a larger application. The agent's input schema is used to define the tool's input parameters, and the agent's output is returned as the tool's result.

#### Param: config:

The configuration of the agent tool.

#### Hierarchy ([View Summary](../hierarchy.html#AgentTool))

  * [BaseTool](BaseTool.html)
    * AgentTool



  * Defined in [core/src/tools/agent_tool.ts:45](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/agent_tool.ts#L45)



## Constructors

### constructor

  * new AgentTool(config: AgentToolConfig): [AgentTool]()

#### Parameters

    * config: AgentToolConfig

#### Returns [AgentTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [core/src/tools/agent_tool.ts:50](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/agent_tool.ts#L50)




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

    * Defined in [core/src/tools/agent_tool.ts:57](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/agent_tool.ts#L57)




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

    * Defined in [core/src/tools/agent_tool.ts:95](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/agent_tool.ts#L95)




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


