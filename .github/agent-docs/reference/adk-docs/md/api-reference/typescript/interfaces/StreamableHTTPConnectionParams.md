[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [StreamableHTTPConnectionParams]()



# Interface StreamableHTTPConnectionParams

Defines the parameters for establishing a connection to an MCP server over HTTP using Server-Sent Events (SSE) for streaming.

Usage: const connectionParams: StreamableHTTPConnectionParams = { type: 'StreamableHTTPConnectionParams', url: '<http://localhost:8788/mcp>' };

interface StreamableHTTPConnectionParams {  
header?: Record<string, unknown>;  
sseReadTimeout?: number;  
terminateOnClose?: boolean;  
timeout?: number;  
transportOptions?: StreamableHTTPClientTransportOptions;  
type: "StreamableHTTPConnectionParams";  
url: string;  
}

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:54](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L54)



## Properties

### `Optional`header

header?: Record<string, unknown>

#### Deprecated

Use transportOptions.requestInit.headers instead. This field will be ignored if transportOptions is provided even if no headers are specified in transportOptions.

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:62](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L62)



### `Optional`sseReadTimeout

sseReadTimeout?: number

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:64](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L64)



### `Optional`terminateOnClose

terminateOnClose?: boolean

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:65](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L65)



### `Optional`timeout

timeout?: number

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:63](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L63)



### `Optional`transportOptions

transportOptions?: StreamableHTTPClientTransportOptions

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:66](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L66)



### type

type: "StreamableHTTPConnectionParams"

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:55](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L55)



### url

url: string

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:56](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L56)



Properties

headersseReadTimeoutterminateOnClosetimeouttransportOptionstypeurl

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


