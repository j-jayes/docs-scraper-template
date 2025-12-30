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
sseReadTimeout?: Number;  
terminateOnClose?: boolean;  
timeout?: Number;  
type: "StreamableHTTPConnectionParams";  
url: string;  
}

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:32](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_session_manager.ts#L32)



## Properties

### `Optional`header

header?: Record<string, unknown>

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:35](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_session_manager.ts#L35)



### `Optional`sseReadTimeout

sseReadTimeout?: Number

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:37](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_session_manager.ts#L37)



### `Optional`terminateOnClose

terminateOnClose?: boolean

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:38](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_session_manager.ts#L38)



### `Optional`timeout

timeout?: Number

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:36](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_session_manager.ts#L36)



### type

type: "StreamableHTTPConnectionParams"

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:33](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_session_manager.ts#L33)



### url

url: string

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:34](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_session_manager.ts#L34)



Properties

headersseReadTimeoutterminateOnClosetimeouttypeurl

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


