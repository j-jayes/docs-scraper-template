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

  * Defined in [tools/mcp/mcp_session_manager.ts:38](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_session_manager.ts#L38)



## Properties

### `Optional`header

header?: Record<string, unknown>

#### Deprecated

Use transportOptions.requestInit.headers instead. This field will be ignored if transportOptions is provided even if no headers are specified in transportOptions.

  * Defined in [tools/mcp/mcp_session_manager.ts:46](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_session_manager.ts#L46)



### `Optional`sseReadTimeout

sseReadTimeout?: number

  * Defined in [tools/mcp/mcp_session_manager.ts:48](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_session_manager.ts#L48)



### `Optional`terminateOnClose

terminateOnClose?: boolean

  * Defined in [tools/mcp/mcp_session_manager.ts:49](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_session_manager.ts#L49)



### `Optional`timeout

timeout?: number

  * Defined in [tools/mcp/mcp_session_manager.ts:47](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_session_manager.ts#L47)



### `Optional`transportOptions

transportOptions?: StreamableHTTPClientTransportOptions

  * Defined in [tools/mcp/mcp_session_manager.ts:50](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_session_manager.ts#L50)



### type

type: "StreamableHTTPConnectionParams"

  * Defined in [tools/mcp/mcp_session_manager.ts:39](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_session_manager.ts#L39)



### url

url: string

  * Defined in [tools/mcp/mcp_session_manager.ts:40](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/tools/mcp/mcp_session_manager.ts#L40)



Properties

headersseReadTimeoutterminateOnClosetimeouttransportOptionstypeurl

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


