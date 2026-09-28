[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InMemoryRunner]()



# Class InMemoryRunner

A [Runner](Runner.html) pre-configured with in-memory services.

Suitable for local development, testing, and prototyping. All session, artifact, and memory data is stored in-process and is not persisted between runs.

Example:
    
    
    const runner = new InMemoryRunner({agent: myAgent});  
      
    for await (const event of runner.runEphemeral({  
      userId: 'user1',  
      newMessage: {parts: [{text: 'Hello'}]},  
    })) {  
      console.log(event);  
    }
    Copy

#### Hierarchy ([View Summary](../hierarchy.html#InMemoryRunner))

  * [Runner](Runner.html)
    * InMemoryRunner



  * Defined in [core/src/runner/in_memory_runner.ts:36](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/in_memory_runner.ts#L36)



## Constructors

### constructor

  * new InMemoryRunner(  
params: {  
agent?: [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)>;  
app?: [App](App.html);  
appName?: string;  
plugins?: [BasePlugin](BasePlugin.html)[];  
resumabilityConfig?: [ResumabilityConfig](../interfaces/ResumabilityConfig.html);  
},  
): [InMemoryRunner]()

Creates a new InMemoryRunner instance.

#### Parameters

    * params: {  
agent?: [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)>;  
app?: [App](App.html);  
appName?: string;  
plugins?: [BasePlugin](BasePlugin.html)[];  
resumabilityConfig?: [ResumabilityConfig](../interfaces/ResumabilityConfig.html);  
}

The configuration for the runner.

      * ##### `Optional`agent?: [BaseAgent](BaseAgent.html)<[BaseAgentConfig](../interfaces/BaseAgentConfig.html)>

The root agent to run.

      * ##### `Optional`app?: [App](App.html)

An optional application instance to run.

      * ##### `Optional`appName?: string

The application name. Defaults to `'InMemoryRunner'`.

      * ##### `Optional`plugins?: [BasePlugin](BasePlugin.html)[]

An optional list of plugins.

      * ##### `Optional`resumabilityConfig?: [ResumabilityConfig](../interfaces/ResumabilityConfig.html)

An optional resumability configuration.

#### Returns [InMemoryRunner]()

Overrides [Runner](Runner.html).[constructor](Runner.html#constructor)

    * Defined in [core/src/runner/in_memory_runner.ts:47](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/in_memory_runner.ts#L47)




## Properties

### `Readonly`[RUNNER_SIGNATURE_SYMBOL]

"[RUNNER_SIGNATURE_SYMBOL]": true

Inherited from [Runner](Runner.html).[[RUNNER_SIGNATURE_SYMBOL]](Runner.html#runner_signature_symbol)

  * Defined in [core/src/runner/runner.ts:139](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L139)



### `Readonly`agent

agent: [BaseAgent](BaseAgent.html)

Inherited from [Runner](Runner.html).[agent](Runner.html#agent)

  * Defined in [core/src/runner/runner.ts:141](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L141)



### `Readonly`appName

appName: string

Inherited from [Runner](Runner.html).[appName](Runner.html#appname)

  * Defined in [core/src/runner/runner.ts:140](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L140)



### `Optional` `Readonly`artifactService

artifactService?: [BaseArtifactService](../interfaces/BaseArtifactService.html)

Inherited from [Runner](Runner.html).[artifactService](Runner.html#artifactservice)

  * Defined in [core/src/runner/runner.ts:143](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L143)



### `Optional` `Readonly`credentialService

credentialService?: [BaseCredentialService](../interfaces/BaseCredentialService.html)

Inherited from [Runner](Runner.html).[credentialService](Runner.html#credentialservice)

  * Defined in [core/src/runner/runner.ts:146](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L146)



### `Optional` `Readonly`memoryService

memoryService?: [BaseMemoryService](../interfaces/BaseMemoryService.html)

Inherited from [Runner](Runner.html).[memoryService](Runner.html#memoryservice)

  * Defined in [core/src/runner/runner.ts:145](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L145)



### `Readonly`pluginManager

pluginManager: [PluginManager](PluginManager.html)

Inherited from [Runner](Runner.html).[pluginManager](Runner.html#pluginmanager)

  * Defined in [core/src/runner/runner.ts:142](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L142)



### `Optional` `Readonly`resumabilityConfig

resumabilityConfig?: [ResumabilityConfig](../interfaces/ResumabilityConfig.html)

Inherited from [Runner](Runner.html).[resumabilityConfig](Runner.html#resumabilityconfig)

  * Defined in [core/src/runner/runner.ts:147](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L147)



### `Readonly`sessionService

sessionService: [BaseSessionService](BaseSessionService.html)

Inherited from [Runner](Runner.html).[sessionService](Runner.html#sessionservice)

  * Defined in [core/src/runner/runner.ts:144](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L144)



## Methods

### runAsync

  * runAsync(  
params: {  
abortSignal?: AbortSignal;  
customMetadata?: Record<string, unknown>;  
newMessage: Content;  
runConfig?: [RunConfig](../interfaces/RunConfig.html);  
sessionId: string;  
stateDelta?: Record<string, unknown>;  
userId: string;  
},  
): AsyncGenerator<[Event](../interfaces/Event.html), void, undefined>

Runs the agent with the given message, and returns an async generator of events.

#### Parameters

    * params: {  
abortSignal?: AbortSignal;  
customMetadata?: Record<string, unknown>;  
newMessage: Content;  
runConfig?: [RunConfig](../interfaces/RunConfig.html);  
sessionId: string;  
stateDelta?: Record<string, unknown>;  
userId: string;  
}
      * ##### `Optional`abortSignal?: AbortSignal

      * ##### `Optional`customMetadata?: Record<string, unknown>

      * ##### newMessage: Content

A new message to append to the session.

      * ##### `Optional`runConfig?: [RunConfig](../interfaces/RunConfig.html)

The run config for the agent.

      * ##### sessionId: string

The session ID of the session.

      * ##### `Optional`stateDelta?: Record<string, unknown>

An optional state delta to apply to the session.

      * ##### userId: string

The user ID of the session.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, undefined>

#### Yields

The events generated by the agent.

Inherited from [Runner](Runner.html).[runAsync](Runner.html#runasync)

    * Defined in [core/src/runner/runner.ts:227](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L227)




### runEphemeral

  * runEphemeral(  
params: {  
customMetadata?: Record<string, unknown>;  
newMessage: Content;  
runConfig?: [RunConfig](../interfaces/RunConfig.html);  
stateDelta?: Record<string, unknown>;  
userId: string;  
},  
): AsyncGenerator<[Event](../interfaces/Event.html), void, undefined>

Runs the agent with a new, ephemeral session.

#### Parameters

    * params: {  
customMetadata?: Record<string, unknown>;  
newMessage: Content;  
runConfig?: [RunConfig](../interfaces/RunConfig.html);  
stateDelta?: Record<string, unknown>;  
userId: string;  
}
      * ##### `Optional`customMetadata?: Record<string, unknown>

      * ##### newMessage: Content

A new message to append to the session.

      * ##### `Optional`runConfig?: [RunConfig](../interfaces/RunConfig.html)

The run config for the agent.

      * ##### `Optional`stateDelta?: Record<string, unknown>

An optional state delta to apply to the session.

      * ##### userId: string

The user ID of the session.

#### Returns AsyncGenerator<[Event](../interfaces/Event.html), void, undefined>

#### Yields

The Events generated by the agent.

Inherited from [Runner](Runner.html).[runEphemeral](Runner.html#runephemeral)

    * Defined in [core/src/runner/runner.ts:184](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L184)




Constructors

constructor

Properties

[RUNNER_SIGNATURE_SYMBOL]agentappNameartifactServicecredentialServicememoryServicepluginManagerresumabilityConfigsessionService

Methods

runAsyncrunEphemeral

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


