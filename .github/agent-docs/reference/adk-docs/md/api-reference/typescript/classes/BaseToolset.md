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
    * [MCPToolset](MCPToolset.html)



  * Defined in [core/src/tools/base_toolset.ts:26](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_toolset.ts#L26)



## Constructors

### constructor

  * new BaseToolset(toolFilter: string[] | ToolPredicate): [BaseToolset]()

#### Parameters

    * toolFilter: string[] | ToolPredicate

#### Returns [BaseToolset]()

    * Defined in [core/src/tools/base_toolset.ts:27](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_toolset.ts#L27)




## Properties

### `Readonly`toolFilter

toolFilter: string[] | ToolPredicate

  * Defined in [core/src/tools/base_toolset.ts:27](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_toolset.ts#L27)



## Methods

### `Abstract`close

  * close(): Promise<void>

Closes the toolset.

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

#### Returns Promise<void>

A Promise that resolves when the toolset is closed.

    * Defined in [core/src/tools/base_toolset.ts:48](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_toolset.ts#L48)




### `Abstract`getTools

  * getTools(context?: ReadonlyContext): Promise<[BaseTool](BaseTool.html)[]>

Returns the tools that should be exposed to LLM.

#### Parameters

    * `Optional`context: ReadonlyContext

Context used to filter tools available to the agent. If not defined, all tools in the toolset are returned.

#### Returns Promise<[BaseTool](BaseTool.html)[]>

A Promise that resolves to the list of tools.

    * Defined in [core/src/tools/base_toolset.ts:36](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_toolset.ts#L36)




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

    * Defined in [core/src/tools/base_toolset.ts:85](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/base_toolset.ts#L85)




Constructors

constructor

Properties

toolFilter

Methods

closegetToolsisToolSelectedprocessLlmRequest

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


