[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [BaseToolset]()



# Class BaseToolset`Abstract`

Base class for toolset.

A toolset is a collection of tools that can be used by an agent.

#### Hierarchy ([View Summary](../hierarchy.html#BaseToolset))

  * BaseToolset
    * [AgentRegistrySingleMCPToolset](AgentRegistrySingleMCPToolset.html)
    * [MCPToolset](MCPToolset.html)
    * [SkillToolset](SkillToolset.html)
    * [OpenAPIToolset](OpenAPIToolset.html)



  * Defined in [core/src/tools/base_toolset.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L43)



## Constructors

### constructor

  * new BaseToolset(  
toolFilter: string[] | [ToolPredicate](../types/ToolPredicate.html),  
prefix?: string,  
): [BaseToolset]()

#### Parameters

    * toolFilter: string[] | [ToolPredicate](../types/ToolPredicate.html)
    * `Optional`prefix: string

#### Returns [BaseToolset]()

    * Defined in [core/src/tools/base_toolset.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L46)




## Properties

### `Readonly`[BASE_TOOLSET_SIGNATURE_SYMBOL]

"[BASE_TOOLSET_SIGNATURE_SYMBOL]": true

  * Defined in [core/src/tools/base_toolset.ts:44](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L44)



### `Optional` `Readonly`prefix

prefix?: string

  * Defined in [core/src/tools/base_toolset.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L48)



### `Readonly`toolFilter

toolFilter: string[] | [ToolPredicate](../types/ToolPredicate.html)

  * Defined in [core/src/tools/base_toolset.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L47)



## Methods

### `Abstract`close

  * close(): Promise<void>

Closes the toolset.

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

#### Returns Promise<void>

A Promise that resolves when the toolset is closed.

    * Defined in [core/src/tools/base_toolset.ts:70](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L70)




### `Abstract`getTools

  * getTools(context?: [ReadonlyContext](ReadonlyContext.html)): Promise<[BaseTool](BaseTool.html)[]>

Returns the tools that should be exposed to LLM.

#### Parameters

    * `Optional`context: [ReadonlyContext](ReadonlyContext.html)

Context used to filter tools available to the agent. If not defined, all tools in the toolset are returned.

#### Returns Promise<[BaseTool](BaseTool.html)[]>

A Promise that resolves to the list of tools.

    * Defined in [core/src/tools/base_toolset.ts:58](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L58)




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

    * Defined in [core/src/tools/base_toolset.ts:111](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/base_toolset.ts#L111)




Constructors

constructor

Properties

[BASE_TOOLSET_SIGNATURE_SYMBOL]prefixtoolFilter

Methods

closegetToolsisToolSelectedprocessLlmRequest

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


