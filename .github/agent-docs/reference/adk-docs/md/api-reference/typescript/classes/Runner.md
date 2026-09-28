[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [Runner]()



# Class Runner

Orchestrates agent execution for a given application.

The Runner manages the full lifecycle of an agent invocation: it loads the session, invokes plugin callbacks, runs the root agent, and yields the resulting events. Use [InMemoryRunner](InMemoryRunner.html) for quick prototyping without external services.

Example:
    
    
    const runner = new Runner({  
      appName: 'my_app',  
      agent: myAgent,  
      sessionService: new InMemorySessionService(),  
    });  
      
    for await (const event of runner.runAsync({  
      userId: 'user1',  
      sessionId: 'session1',  
      newMessage: {parts: [{text: 'Hello'}]},  
    })) {  
      console.log(event);  
    }
    Copy

#### Hierarchy ([View Summary](../hierarchy.html#Runner))

  * Runner
    * [InMemoryRunner](InMemoryRunner.html)



  * Defined in [core/src/runner/runner.ts:138](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L138)



## Constructors

### constructor

  * new Runner(input: [RunnerConfig](../interfaces/RunnerConfig.html)): [Runner]()

Creates a new Runner instance.

#### Parameters

    * input: [RunnerConfig](../interfaces/RunnerConfig.html)

The configuration for the runner.

#### Returns [Runner]()

    * Defined in [core/src/runner/runner.ts:154](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L154)




## Properties

### `Readonly`[RUNNER_SIGNATURE_SYMBOL]

"[RUNNER_SIGNATURE_SYMBOL]": true

  * Defined in [core/src/runner/runner.ts:139](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L139)



### `Readonly`agent

agent: [BaseAgent](BaseAgent.html)

  * Defined in [core/src/runner/runner.ts:141](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L141)



### `Readonly`appName

appName: string

  * Defined in [core/src/runner/runner.ts:140](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L140)



### `Optional` `Readonly`artifactService

artifactService?: [BaseArtifactService](../interfaces/BaseArtifactService.html)

  * Defined in [core/src/runner/runner.ts:143](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L143)



### `Optional` `Readonly`credentialService

credentialService?: [BaseCredentialService](../interfaces/BaseCredentialService.html)

  * Defined in [core/src/runner/runner.ts:146](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L146)



### `Optional` `Readonly`memoryService

memoryService?: [BaseMemoryService](../interfaces/BaseMemoryService.html)

  * Defined in [core/src/runner/runner.ts:145](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L145)



### `Readonly`pluginManager

pluginManager: [PluginManager](PluginManager.html)

  * Defined in [core/src/runner/runner.ts:142](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L142)



### `Optional` `Readonly`resumabilityConfig

resumabilityConfig?: [ResumabilityConfig](../interfaces/ResumabilityConfig.html)

  * Defined in [core/src/runner/runner.ts:147](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L147)



### `Readonly`sessionService

sessionService: [BaseSessionService](BaseSessionService.html)

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

    * Defined in [core/src/runner/runner.ts:184](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/runner/runner.ts#L184)




Constructors

constructor

Properties

[RUNNER_SIGNATURE_SYMBOL]agentappNameartifactServicecredentialServicememoryServicepluginManagerresumabilityConfigsessionService

Methods

runAsyncrunEphemeral

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


