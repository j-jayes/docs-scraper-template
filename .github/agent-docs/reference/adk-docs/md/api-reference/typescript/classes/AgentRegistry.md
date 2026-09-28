[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AgentRegistry]()



# Class AgentRegistry

Client for interacting with the Google Cloud Agent Registry service.

Unlike a standard REST client library, this class provides higher-level abstractions for ADK integration. It surfaces the agent registry service methods along with helper methods like `getMcpToolset` and `getRemoteA2AAgent` that automatically resolve connection details, manage OAuth authentication schemes, and handle GCP credentials to produce ready-to-use ADK components.

  * Defined in [core/src/integrations/agent_registry/agent_registry.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L59)



## Constructors

### constructor

  * new AgentRegistry(  
options: {  
headerProvider?: (context: [ReadonlyContext](ReadonlyContext.html)) => Record<string, string>;  
location?: string | null;  
projectId?: string | null;  
},  
): [AgentRegistry]()

#### Parameters

    * options: {  
headerProvider?: (context: [ReadonlyContext](ReadonlyContext.html)) => Record<string, string>;  
location?: string | null;  
projectId?: string | null;  
}

#### Returns [AgentRegistry]()

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:68](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L68)




## Properties

### `Readonly`location

location: string

  * Defined in [core/src/integrations/agent_registry/agent_registry.ts:61](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L61)



### `Readonly`projectId

projectId: string

  * Defined in [core/src/integrations/agent_registry/agent_registry.ts:60](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L60)



## Methods

### getAgentInfo

  * getAgentInfo(name: string): Promise<[AgentInfo](../interfaces/AgentInfo.html)>

#### Parameters

    * name: string

#### Returns Promise<[AgentInfo](../interfaces/AgentInfo.html)>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:402](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L402)




### getAuthHeaders

  * getAuthHeaders(): Promise<Record<string, string>>

Resolves default Google Cloud credentials and returns standard headers. Automatically caches, fetches, and handles refreshing expired OAuth tokens. Injects the billing/quota project identifier `x-goog-user-project` if present.

#### Returns Promise<Record<string, string>>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:92](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L92)




### getConnectionUri

  * getConnectionUri(  
resourceDetails: {  
interfaces?: { protocolBinding?: string; url?: string }[];  
protocols?: {  
interfaces?: { protocolBinding?: string; url?: string }[];  
protocolVersion?: string;  
type?: [ProtocolType](../enums/ProtocolType.html);  
}[];  
},  
filters?: [ConnectionUriFilter](../interfaces/ConnectionUriFilter.html),  
): [ConnectionUriResult](../interfaces/ConnectionUriResult.html)

Parses connection interfaces list from registry metadata and returns the first match corresponding to requested protocol types and binding options.

#### Parameters

    * resourceDetails: {  
interfaces?: { protocolBinding?: string; url?: string }[];  
protocols?: {  
interfaces?: { protocolBinding?: string; url?: string }[];  
protocolVersion?: string;  
type?: [ProtocolType](../enums/ProtocolType.html);  
}[];  
}
    * `Optional`filters: [ConnectionUriFilter](../interfaces/ConnectionUriFilter.html)

#### Returns [ConnectionUriResult](../interfaces/ConnectionUriResult.html)

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:180](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L180)




### getEndpoint

  * getEndpoint(name: string): Promise<[Endpoint](../interfaces/Endpoint.html)>

#### Parameters

    * name: string

#### Returns Promise<[Endpoint](../interfaces/Endpoint.html)>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:359](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L359)




### getMcpServer

  * getMcpServer(name: string): Promise<[McpServer](../interfaces/McpServer.html)>

#### Parameters

    * name: string

#### Returns Promise<[McpServer](../interfaces/McpServer.html)>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:248](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L248)




### getMcpToolset

  * getMcpToolset(  
mcpServerName: string,  
options?: {  
authCredential?: [AuthCredential](../interfaces/AuthCredential.html);  
authScheme?: [AuthScheme](../types/AuthScheme.html);  
continueUri?: string;  
},  
): Promise<[AgentRegistrySingleMCPToolset](AgentRegistrySingleMCPToolset.html)>

#### Parameters

    * mcpServerName: string
    * `Optional`options: {  
authCredential?: [AuthCredential](../interfaces/AuthCredential.html);  
authScheme?: [AuthScheme](../types/AuthScheme.html);  
continueUri?: string;  
}

#### Returns Promise<[AgentRegistrySingleMCPToolset](AgentRegistrySingleMCPToolset.html)>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:252](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L252)




### getModelName

  * getModelName(endpointName: string): Promise<string>

#### Parameters

    * endpointName: string

#### Returns Promise<string>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:363](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L363)




### getRemoteA2AAgent

  * getRemoteA2AAgent(  
agentName: string,  
options?: { client?: Client; clientFactory?: ClientFactory },  
): Promise<[RemoteA2AAgent](RemoteA2AAgent.html)>

#### Parameters

    * agentName: string
    * `Optional`options: { client?: Client; clientFactory?: ClientFactory }

#### Returns Promise<[RemoteA2AAgent](RemoteA2AAgent.html)>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:406](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L406)




### listAgents

  * listAgents(  
options?: { filterStr?: string; pageSize?: number; pageToken?: string },  
): Promise<[ListAgentsResponse](../interfaces/ListAgentsResponse.html)>

#### Parameters

    * `Optional`options: { filterStr?: string; pageSize?: number; pageToken?: string }

#### Returns Promise<[ListAgentsResponse](../interfaces/ListAgentsResponse.html)>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:384](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L384)




### listEndpoints

  * listEndpoints(  
options?: { filterStr?: string; pageSize?: number; pageToken?: string },  
): Promise<[ListEndpointsResponse](../interfaces/ListEndpointsResponse.html)>

#### Parameters

    * `Optional`options: { filterStr?: string; pageSize?: number; pageToken?: string }

#### Returns Promise<[ListEndpointsResponse](../interfaces/ListEndpointsResponse.html)>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:341](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L341)




### listMcpServers

  * listMcpServers(  
options?: { filterStr?: string; pageSize?: number; pageToken?: string },  
): Promise<[ListMcpServersResponse](../interfaces/ListMcpServersResponse.html)>

#### Parameters

    * `Optional`options: { filterStr?: string; pageSize?: number; pageToken?: string }

#### Returns Promise<[ListMcpServersResponse](../interfaces/ListMcpServersResponse.html)>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:230](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L230)




### makeRequest

  * makeRequest<T = unknown>(  
path: string,  
params?: Record<string, string>,  
): Promise<T>

Helper function to execute HTTP GET requests against the Agent Registry API. Handles path resolution, search query params compilation, and auth headers fetching.

#### Type Parameters

    * T = unknown

#### Parameters

    * path: string
    * `Optional`params: Record<string, string>

#### Returns Promise<T>

    * Defined in [core/src/integrations/agent_registry/agent_registry.ts:137](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/agent_registry.ts#L137)




Constructors

constructor

Properties

locationprojectId

Methods

getAgentInfogetAuthHeadersgetConnectionUrigetEndpointgetMcpServergetMcpToolsetgetModelNamegetRemoteA2AAgentlistAgentslistEndpointslistMcpServersmakeRequest

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


