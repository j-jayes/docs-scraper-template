[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AgentEngineSandboxCodeExecutorOptions]()



# Interface AgentEngineSandboxCodeExecutorOptions

Options for AgentEngineSandboxCodeExecutor.

interface AgentEngineSandboxCodeExecutorOptions {  
agentEngineResourceName?: string;  
client?: Client;  
location?: string;  
projectId?: string;  
sandboxResourceName?: string;  
}

  * Defined in [core/src/code_executors/agent_engine_sandbox_code_executor.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/agent_engine_sandbox_code_executor.ts#L43)



## Properties

### `Optional`agentEngineResourceName

agentEngineResourceName?: string

The resource name of the agent engine to use to create the code execution sandbox. Format: projects/123/locations/us-central1/reasoningEngines/456

  * Defined in [core/src/code_executors/agent_engine_sandbox_code_executor.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/agent_engine_sandbox_code_executor.ts#L54)



### `Optional`client

client?: Client

Optional client instance to use. If not provided, a new one will be created. Primarily for testing.

  * Defined in [core/src/code_executors/agent_engine_sandbox_code_executor.ts:70](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/agent_engine_sandbox_code_executor.ts#L70)



### `Optional`location

location?: string

Location to use. If not provided, read from GOOGLE_CLOUD_LOCATION env var or default to 'us-central1'.

  * Defined in [core/src/code_executors/agent_engine_sandbox_code_executor.ts:64](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/agent_engine_sandbox_code_executor.ts#L64)



### `Optional`projectId

projectId?: string

Project ID to use. If not provided, read from GOOGLE_CLOUD_PROJECT env var.

  * Defined in [core/src/code_executors/agent_engine_sandbox_code_executor.ts:59](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/agent_engine_sandbox_code_executor.ts#L59)



### `Optional`sandboxResourceName

sandboxResourceName?: string

If set, load the existing resource name of the code execution sandbox. Format: projects/123/locations/us-central1/reasoningEngines/456/sandboxEnvironments/789

  * Defined in [core/src/code_executors/agent_engine_sandbox_code_executor.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/code_executors/agent_engine_sandbox_code_executor.ts#L48)



Properties

agentEngineResourceNameclientlocationprojectIdsandboxResourceName

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


