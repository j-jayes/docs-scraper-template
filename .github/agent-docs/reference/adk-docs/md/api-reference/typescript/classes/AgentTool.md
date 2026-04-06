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



  * Defined in [tools/agent_tool.ts:64](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/agent_tool.ts#L64)



## Constructors

### constructor

  * new AgentTool(config: [AgentToolConfig](../interfaces/AgentToolConfig.html)): [AgentTool]()

#### Parameters

    * config: [AgentToolConfig](../interfaces/AgentToolConfig.html)

#### Returns [AgentTool]()

Overrides [BaseTool](BaseTool.html).[constructor](BaseTool.html#constructor)

    * Defined in [tools/agent_tool.ts:72](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/agent_tool.ts#L72)




## Properties

### `Readonly`[AGENT_TOOL_SIGNATURE_SYMBOL]

"[AGENT_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK agent tool class.

  * Defined in [tools/agent_tool.ts:66](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/agent_tool.ts#L66)



### `Readonly`[BASE_TOOL_SIGNATURE_SYMBOL]

"[BASE_TOOL_SIGNATURE_SYMBOL]": true

A unique symbol to identify ADK base tool class.

Inherited from [BaseTool](BaseTool.html).[[BASE_TOOL_SIGNATURE_SYMBOL]](BaseTool.html#base_tool_signature_symbol)

  * Defined in [tools/base_tool.ts:64](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L64)



### `Readonly`description

description: string

Inherited from [BaseTool](BaseTool.html).[description](BaseTool.html#description)

  * Defined in [tools/base_tool.ts:67](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L67)



### `Readonly`isLongRunning

isLongRunning: boolean

Inherited from [BaseTool](BaseTool.html).[isLongRunning](BaseTool.html#islongrunning)

  * Defined in [tools/base_tool.ts:68](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L68)



### `Readonly`name

name: string

Inherited from [BaseTool](BaseTool.html).[name](BaseTool.html#name)

  * Defined in [tools/base_tool.ts:66](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L66)



## Accessors

### apiVariant

  * get apiVariant(): [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

The Google API LLM variant to use.

#### Returns [GoogleLLMVariant](../enums/GoogleLLMVariant.html)

Inherited from BaseTool.apiVariant

    * Defined in [tools/base_tool.ts:151](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L151)




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

    * Defined in [tools/agent_tool.ts:81](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/agent_tool.ts#L81)




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

    * Defined in [tools/base_tool.ts:120](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/base_tool.ts#L120)




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

    * Defined in [tools/agent_tool.ts:119](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/agent_tool.ts#L119)




Constructors

constructor

Properties

[AGENT_TOOL_SIGNATURE_SYMBOL][BASE_TOOL_SIGNATURE_SYMBOL]descriptionisLongRunningname

Accessors

apiVariant

Methods

_getDeclarationprocessLlmRequestrunAsync

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


