[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [MCPSessionManager]()



# Class MCPSessionManager

Manages Model Context Protocol (MCP) client sessions.

This class is responsible for establishing and managing connections to MCP servers. It supports different transport protocols like Standard I/O (Stdio) and Server-Sent Events (SSE) over HTTP, determined by the provided connection parameters.

The primary purpose of this manager is to abstract away the details of session creation and connection handling, providing a simple interface for creating new MCP client instances that can be used to interact with remote tools.

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:60](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_session_manager.ts#L60)



## Constructors

### constructor

  * new MCPSessionManager(connectionParams: [MCPConnectionParams](../types/MCPConnectionParams.html)): [MCPSessionManager]()

#### Parameters

    * connectionParams: [MCPConnectionParams](../types/MCPConnectionParams.html)

#### Returns [MCPSessionManager]()

    * Defined in [core/src/tools/mcp/mcp_session_manager.ts:63](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_session_manager.ts#L63)




## Methods

### createSession

  * createSession(): Promise<Client<{}, {}, { [key: string]: unknown }>>

#### Returns Promise<Client<{}, {}, { [key: string]: unknown }>>

    * Defined in [core/src/tools/mcp/mcp_session_manager.ts:67](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/tools/mcp/mcp_session_manager.ts#L67)




Constructors

constructor

Methods

createSession

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


