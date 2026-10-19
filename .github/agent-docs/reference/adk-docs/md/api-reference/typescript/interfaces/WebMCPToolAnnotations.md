[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [WebMCPToolAnnotations]()



# Interface WebMCPToolAnnotations

Metadata a page may attach to a registered tool.

interface WebMCPToolAnnotations {  
consequentialHint?: boolean;  
readOnlyHint?: boolean;  
untrustedContentHint?: boolean;  
}

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:18](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L18)



## Properties

### `Optional`consequentialHint

consequentialHint?: boolean

The tool performs a significant or non-reversible real-world action.

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:24](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L24)



### `Optional`readOnlyHint

readOnlyHint?: boolean

The tool only reads state.

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:20](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L20)



### `Optional`untrustedContentHint

untrustedContentHint?: boolean

The tool's output may contain untrusted content.

  * Defined in [core/src/tools/webmcp/webmcp_types.ts:22](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/webmcp/webmcp_types.ts#L22)



Properties

consequentialHintreadOnlyHintuntrustedContentHint

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


