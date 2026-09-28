[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [MCPSessionManager]()



# Class MCPSessionManager

Manages Model Context Protocol (MCP) client sessions.

This class is responsible for establishing and managing connections to MCP servers. It supports different transport protocols like Standard I/O (Stdio) and Server-Sent Events (SSE) over HTTP, determined by the provided connection parameters.

The primary purpose of this manager is to abstract away the details of session creation and connection handling, providing a simple interface for creating new MCP client instances that can be used to interact with remote tools.

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:73](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_session_manager.ts#L73)



## Constructors

### constructor

  * new MCPSessionManager(connectionParams: [MCPConnectionParams](../types/MCPConnectionParams.html)): [MCPSessionManager]()

#### Parameters

    * connectionParams: [MCPConnectionParams](../types/MCPConnectionParams.html)

#### Returns [MCPSessionManager]()

    * Defined in [core/src/tools/mcp/mcp_session_manager.ts:77](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_session_manager.ts#L77)




## Methods

### closeSession

  * closeSession(client: Client): Promise<void>

#### Parameters

    * client: Client

#### Returns Promise<void>

    * Defined in [core/src/tools/mcp/mcp_session_manager.ts:121](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_session_manager.ts#L121)




### createSession

  * createSession(): Promise<Client<{}, {}, { [key: string]: unknown }>>

#### Returns Promise<Client<{}, {}, { [key: string]: unknown }>>

    * Defined in [core/src/tools/mcp/mcp_session_manager.ts:81](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_session_manager.ts#L81)




### getActiveSessions

  * getActiveSessions(): Client<{}, {}, { [key: string]: unknown }>[]

#### Returns Client<{}, {}, { [key: string]: unknown }>[]

    * Defined in [core/src/tools/mcp/mcp_session_manager.ts:128](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/tools/mcp/mcp_session_manager.ts#L128)




Constructors

constructor

Methods

closeSessioncreateSessiongetActiveSessions

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


