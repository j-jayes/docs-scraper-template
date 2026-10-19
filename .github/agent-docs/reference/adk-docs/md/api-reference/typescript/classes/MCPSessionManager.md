[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [MCPSessionManager]()



# Class MCPSessionManager

Manages Model Context Protocol (MCP) client sessions.

This class is responsible for establishing and managing connections to MCP servers. It supports different transport protocols like Standard I/O (Stdio) and Server-Sent Events (SSE) over HTTP, determined by the provided connection parameters.

The primary purpose of this manager is to abstract away the details of session creation and connection handling, providing a simple interface for creating new MCP client instances that can be used to interact with remote tools.

  * Defined in [core/src/tools/mcp/mcp_session_manager.ts:114](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L114)



## Constructors

### constructor

  * new MCPSessionManager(connectionParams: [MCPConnectionParams](../types/MCPConnectionParams.html)): [MCPSessionManager]()

#### Parameters

    * connectionParams: [MCPConnectionParams](../types/MCPConnectionParams.html)

#### Returns [MCPSessionManager]()

    * Defined in [core/src/tools/mcp/mcp_session_manager.ts:118](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L118)




## Methods

### closeSession

  * closeSession(client: Client): Promise<void>

#### Parameters

    * client: Client

#### Returns Promise<void>

    * Defined in [core/src/tools/mcp/mcp_session_manager.ts:172](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L172)




### createSession

  * createSession(): Promise<Client<{}, {}, { [key: string]: unknown }>>

#### Returns Promise<Client<{}, {}, { [key: string]: unknown }>>

    * Defined in [core/src/tools/mcp/mcp_session_manager.ts:122](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L122)




### getActiveSessions

  * getActiveSessions(): Client<{}, {}, { [key: string]: unknown }>[]

#### Returns Client<{}, {}, { [key: string]: unknown }>[]

    * Defined in [core/src/tools/mcp/mcp_session_manager.ts:179](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/tools/mcp/mcp_session_manager.ts#L179)




Constructors

constructor

Methods

closeSessioncreateSessiongetActiveSessions

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


