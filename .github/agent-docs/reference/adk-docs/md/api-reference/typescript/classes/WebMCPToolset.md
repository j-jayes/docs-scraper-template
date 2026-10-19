[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [WebMCPToolset]()



# Class WebMCPToolset

A toolset backed by the tools a web page registers with WebMCP.

WebMCP lets a page declare typed, callable tools on `document.modelContext`. This toolset surfaces them to an in-browser agent, so the agent drives the page through the handlers it published instead of scraping the DOM. Each tool's own `execute` runs in the page, so its UI updates as a side effect.

Unlike [MCPToolset](MCPToolset.html), nothing is transported anywhere: discovery and execution are same-document browser calls.

Outside a browser, or in a browser without WebMCP, `getTools()` returns an empty array rather than throwing, so this is safe to construct anywhere.

#### Example
    
    
    import {LlmAgent} from '@google/adk';  
    import {WebMCPToolset} from '@google/adk/tools/webmcp';  
      
    const agent = new LlmAgent({  
      name: 'page_agent',  
      model: 'gemini-3.8-live',  
      tools: [new WebMCPToolset()],  
    });
    Copy

#### See

<https://developer.chrome.com/docs/ai/webmcp>

#### Hierarchy ([View Summary](../hierarchy.html#WebMCPToolset))

  * [BaseToolset](BaseToolset.html)
    * WebMCPToolset



  * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L59)



## Constructors

### constructor

  * new WebMCPToolset(options?: [WebMCPToolsetOptions](../interfaces/WebMCPToolsetOptions.html)): [WebMCPToolset]()

#### Parameters

    * options: [WebMCPToolsetOptions](../interfaces/WebMCPToolsetOptions.html) = {}

#### Returns [WebMCPToolset]()

Overrides [BaseToolset](BaseToolset.html).[constructor](BaseToolset.html#constructor)

    * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:64](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L64)




## Properties

### `Readonly`[BASE_TOOLSET_SIGNATURE_SYMBOL]

"[BASE_TOOLSET_SIGNATURE_SYMBOL]": true

Inherited from [BaseToolset](BaseToolset.html).[[BASE_TOOLSET_SIGNATURE_SYMBOL]](BaseToolset.html#base_toolset_signature_symbol)

  * Defined in [core/src/tools/base_toolset.ts:44](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_toolset.ts#L44)



### `Optional` `Readonly`prefix

prefix?: string

Inherited from [BaseToolset](BaseToolset.html).[prefix](BaseToolset.html#prefix)

  * Defined in [core/src/tools/base_toolset.ts:48](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_toolset.ts#L48)



### `Readonly`toolFilter

toolFilter: string[] | [ToolPredicate](../types/ToolPredicate.html)

Inherited from [BaseToolset](BaseToolset.html).[toolFilter](BaseToolset.html#toolfilter)

  * Defined in [core/src/tools/base_toolset.ts:47](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_toolset.ts#L47)



## Methods

### close

  * close(): Promise<void>

Closes the toolset.

NOTE: This method is invoked, for example, at the end of an agent server's lifecycle or when the toolset is no longer needed. Implementations should ensure that any open connections, files, or other managed resources are properly released to prevent leaks.

#### Returns Promise<void>

A Promise that resolves when the toolset is closed.

Overrides [BaseToolset](BaseToolset.html).[close](BaseToolset.html#close)

    * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:131](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L131)




### getTools

  * getTools(context?: [ReadonlyContext](ReadonlyContext.html)): Promise<[BaseTool](BaseTool.html)[]>

Returns the tools that should be exposed to LLM.

#### Parameters

    * `Optional`context: [ReadonlyContext](ReadonlyContext.html)

Context used to filter tools available to the agent. If not defined, all tools in the toolset are returned.

#### Returns Promise<[BaseTool](BaseTool.html)[]>

A Promise that resolves to the list of tools.

Overrides [BaseToolset](BaseToolset.html).[getTools](BaseToolset.html#gettools)

    * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:75](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L75)




### isSupported

  * isSupported(): boolean

Whether this document exposes WebMCP.

#### Returns boolean

    * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:71](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L71)




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

    * Defined in [core/src/tools/base_toolset.ts:79](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_toolset.ts#L79)




### onToolChange

  * onToolChange(listener: () => void): () => void

Subscribes to the WebMCP `toolchange` event, which fires when the page registers or removes tools. Returns an unsubscribe function.

#### Parameters

    * listener: () => void

#### Returns () => void

    * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:117](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L117)




### processLlmRequest

  * processLlmRequest(_toolContext: [Context](Context.html), _llmRequest: [LlmRequest](../interfaces/LlmRequest.html)): Promise<void>

Processes the outgoing LLM request for this toolset. This method will be called before each tool processes the llm request.

Use cases:

    * Instead of let each tool process the llm request, we can let the toolset process the llm request. e.g. ComputerUseToolset can add computer use tool to the llm request.

#### Parameters

    * _toolContext: [Context](Context.html)

The context of the tool.

    * _llmRequest: [LlmRequest](../interfaces/LlmRequest.html)

The outgoing LLM request, mutable this method.

#### Returns Promise<void>

Inherited from [BaseToolset](BaseToolset.html).[processLlmRequest](BaseToolset.html#processllmrequest)

    * Defined in [core/src/tools/base_toolset.ts:111](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/base_toolset.ts#L111)




Constructors

constructor

Properties

[BASE_TOOLSET_SIGNATURE_SYMBOL]prefixtoolFilter

Methods

closegetToolsisSupportedisToolSelectedonToolChangeprocessLlmRequest

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


