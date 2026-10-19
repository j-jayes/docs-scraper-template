[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [WebMCPModelContext]()



# Interface WebMCPModelContext

The `document.modelContext` object.

interface WebMCPModelContext {  
executeTool(  
tool: [WebMCPRegisteredTool](WebMCPRegisteredTool.html),  
args?: unknown,  
options?: [WebMCPExecuteToolOptions](WebMCPExecuteToolOptions.html),  
): Promise<unknown>;  
getTools(options?: [WebMCPGetToolsOptions](WebMCPGetToolsOptions.html)): Promise<[WebMCPRegisteredTool](WebMCPRegisteredTool.html)[]>;  
}

#### Hierarchy

  * EventTarget
    * WebMCPModelContext



  * Defined in [core/src/tools/webmcp/webmcp_types.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L56)



## Methods

### executeTool

  * executeTool(  
tool: [WebMCPRegisteredTool](WebMCPRegisteredTool.html),  
args?: unknown,  
options?: [WebMCPExecuteToolOptions](WebMCPExecuteToolOptions.html),  
): Promise<unknown>

#### Parameters

    * tool: [WebMCPRegisteredTool](WebMCPRegisteredTool.html)
    * `Optional`args: unknown
    * `Optional`options: [WebMCPExecuteToolOptions](WebMCPExecuteToolOptions.html)

#### Returns Promise<unknown>

    * Defined in [core/src/tools/webmcp/webmcp_types.ts:58](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L58)




### getTools

  * getTools(options?: [WebMCPGetToolsOptions](WebMCPGetToolsOptions.html)): Promise<[WebMCPRegisteredTool](WebMCPRegisteredTool.html)[]>

#### Parameters

    * `Optional`options: [WebMCPGetToolsOptions](WebMCPGetToolsOptions.html)

#### Returns Promise<[WebMCPRegisteredTool](WebMCPRegisteredTool.html)[]>

    * Defined in [core/src/tools/webmcp/webmcp_types.ts:57](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L57)




Methods

executeToolgetTools

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


