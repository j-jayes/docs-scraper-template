[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [RunnerConfig]()



# Interface RunnerConfig

The configuration parameters for the Runner.

interface RunnerConfig {  
agent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>;  
app?: [App](../classes/App.html);  
appName?: string;  
artifactService?: [BaseArtifactService](BaseArtifactService.html);  
credentialService?: [BaseCredentialService](BaseCredentialService.html);  
memoryService?: [BaseMemoryService](BaseMemoryService.html);  
plugins?: [BasePlugin](../classes/BasePlugin.html)[];  
resumabilityConfig?: [ResumabilityConfig](ResumabilityConfig.html);  
sessionService: [BaseSessionService](../classes/BaseSessionService.html);  
}

  * Defined in [core/src/runner/runner.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L46)



## Properties

### `Optional`agent

agent?: [BaseAgent](../classes/BaseAgent.html)<[BaseAgentConfig](BaseAgentConfig.html)>

The agent to run. Required if `app` is not provided.

  * Defined in [core/src/runner/runner.ts:60](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L60)



### `Optional`app

app?: [App](../classes/App.html)

The application object. If provided, `appName`, `agent`, and `plugins` will default from this app.

  * Defined in [core/src/runner/runner.ts:50](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L50)



### `Optional`appName

appName?: string

The application name. Required if `app` is not provided.

  * Defined in [core/src/runner/runner.ts:55](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L55)



### `Optional`artifactService

artifactService?: [BaseArtifactService](BaseArtifactService.html)

An optional service for storing and retrieving artifacts.

  * Defined in [core/src/runner/runner.ts:70](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L70)



### `Optional`credentialService

credentialService?: [BaseCredentialService](BaseCredentialService.html)

An optional service for managing authentication credentials.

  * Defined in [core/src/runner/runner.ts:85](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L85)



### `Optional`memoryService

memoryService?: [BaseMemoryService](BaseMemoryService.html)

An optional service for storing and querying agent memory.

  * Defined in [core/src/runner/runner.ts:80](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L80)



### `Optional`plugins

plugins?: [BasePlugin](../classes/BasePlugin.html)[]

An optional list of plugins to apply globally across all agents.

  * Defined in [core/src/runner/runner.ts:65](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L65)



### `Optional`resumabilityConfig

resumabilityConfig?: [ResumabilityConfig](ResumabilityConfig.html)

An optional resumability configuration applied to the runner.

  * Defined in [core/src/runner/runner.ts:90](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L90)



### sessionService

sessionService: [BaseSessionService](../classes/BaseSessionService.html)

The service for managing sessions.

  * Defined in [core/src/runner/runner.ts:75](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L75)



Properties

agentappappNameartifactServicecredentialServicememoryServicepluginsresumabilityConfigsessionService

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


