[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [WebMCPToolsetOptions]()



# Interface WebMCPToolsetOptions

Options for [WebMCPToolset](../classes/WebMCPToolset.html).

interface WebMCPToolsetOptions {  
document?: [WebMCPDocument](WebMCPDocument.html);  
fromOrigins?: string[];  
prefix?: string;  
toolFilter?: string[] | [ToolPredicate](../types/ToolPredicate.html);  
}

  * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:16](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L16)



## Properties

### `Optional`document

document?: [WebMCPDocument](WebMCPDocument.html)

Document to read `modelContext` from. Defaults to the global document.

  * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:28](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L28)



### `Optional`fromOrigins

fromOrigins?: string[]

Secure origins to also collect tools from, for cross-origin iframes. A cross-origin tool is only returned if its page also exposed it to this origin via `exposedTo`.

  * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:26](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L26)



### `Optional`prefix

prefix?: string

Prefixes every discovered tool name with `${prefix}_`.

  * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:20](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L20)



### `Optional`toolFilter

toolFilter?: string[] | [ToolPredicate](../types/ToolPredicate.html)

Restricts which tools reach the model, by name or predicate.

  * Defined in [core/src/tools/webmcp/webmcp_toolset.ts:18](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_toolset.ts#L18)



Properties

documentfromOriginsprefixtoolFilter

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


