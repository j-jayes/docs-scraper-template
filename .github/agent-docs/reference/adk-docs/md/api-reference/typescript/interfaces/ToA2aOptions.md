[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ToA2aOptions]()



# Interface ToA2aOptions

Options for the `toA2a` function.

interface ToA2aOptions {  
agentCard?: string | AgentCard;  
allowUnauthenticated?: boolean;  
app?: Application;  
artifactService?: [BaseArtifactService](BaseArtifactService.html);  
authentication?: UserBuilder;  
basePath?: string;  
host?: string;  
memoryService?: [BaseMemoryService](BaseMemoryService.html);  
port?: number;  
protocol?: string;  
runner?: [Runner](../classes/Runner.html);  
sessionService?: [BaseSessionService](../classes/BaseSessionService.html);  
}

  * Defined in [core/src/a2a/agent_to_a2a.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L43)



## Properties

### `Optional`agentCard

agentCard?: string | AgentCard

Optional pre-built AgentCard object or path to agent card JSON

  * Defined in [core/src/a2a/agent_to_a2a.ts:53](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L53)



### `Optional`allowUnauthenticated

allowUnauthenticated?: boolean

Explicit escape hatch to mount the A2A surface WITHOUT authentication.

This is intentionally insecure and must only be used for local, trusted development where the surface is not network reachable. When set to `true` (and no ToA2aOptions.authentication is provided), a loud warning is logged and the handlers are mounted with no authentication.

Defaults to `false`, which makes `toA2a` fail closed.

  * Defined in [core/src/a2a/agent_to_a2a.ts:88](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L88)



### `Optional`app

app?: Application

Optional existing express application

  * Defined in [core/src/a2a/agent_to_a2a.ts:63](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L63)



### `Optional`artifactService

artifactService?: [BaseArtifactService](BaseArtifactService.html)

Optional artifact service

  * Defined in [core/src/a2a/agent_to_a2a.ts:61](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L61)



### `Optional`authentication

authentication?: UserBuilder

Authenticator used to validate incoming A2A requests.

A2A is the production-intended inter-agent surface: any network-reachable caller that can reach it can invoke the agent and its tools with arbitrary input and read the output. Provide a `UserBuilder` (from `@a2a-js/sdk/server/express`) that validates the request's credentials — for example a bearer token or an OIDC ID token — and it will be wired into both the REST and JSON-RPC handlers.

When omitted, `toA2a` fails closed and throws unless ToA2aOptions.allowUnauthenticated is explicitly set to `true`.

  * Defined in [core/src/a2a/agent_to_a2a.ts:77](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L77)



### `Optional`basePath

basePath?: string

The base path for the A2A RPC URL (default: "a2a")

  * Defined in [core/src/a2a/agent_to_a2a.ts:51](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L51)



### `Optional`host

host?: string

The host for the A2A RPC URL (default: "localhost")

  * Defined in [core/src/a2a/agent_to_a2a.ts:45](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L45)



### `Optional`memoryService

memoryService?: [BaseMemoryService](BaseMemoryService.html)

Optional memory service

  * Defined in [core/src/a2a/agent_to_a2a.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L59)



### `Optional`port

port?: number

The port for the A2A RPC URL (default: 8000)

  * Defined in [core/src/a2a/agent_to_a2a.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L47)



### `Optional`protocol

protocol?: string

The protocol for the A2A RPC URL (default: "http")

  * Defined in [core/src/a2a/agent_to_a2a.ts:49](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L49)



### `Optional`runner

runner?: [Runner](../classes/Runner.html)

Optional pre-built Runner object

  * Defined in [core/src/a2a/agent_to_a2a.ts:55](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L55)



### `Optional`sessionService

sessionService?: [BaseSessionService](../classes/BaseSessionService.html)

Optional session service

  * Defined in [core/src/a2a/agent_to_a2a.ts:57](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/a2a/agent_to_a2a.ts#L57)



Properties

agentCardallowUnauthenticatedappartifactServiceauthenticationbasePathhostmemoryServiceportprotocolrunnersessionService

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


