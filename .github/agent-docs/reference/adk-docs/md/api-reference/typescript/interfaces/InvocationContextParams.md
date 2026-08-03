[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InvocationContextParams]()



# Interface InvocationContextParams

The parameters for creating an invocation context.

interface InvocationContextParams {  
abortSignal?: AbortSignal;  
activeStreamingTools?: Record<string, [ActiveStreamingTool](../classes/ActiveStreamingTool.html)>;  
agent: [BaseAgent](../classes/BaseAgent.html);  
artifactService?: [SessionArtifactService](SessionArtifactService.html);  
branch?: string;  
credentialService?: [BaseCredentialService](BaseCredentialService.html);  
endInvocation?: boolean;  
invocationId: string;  
memoryService?: [BaseMemoryService](BaseMemoryService.html);  
pluginManager: [PluginManager](../classes/PluginManager.html);  
runConfig?: [RunConfig](RunConfig.html);  
session: [Session](Session.html);  
sessionService?: [BaseSessionService](../classes/BaseSessionService.html);  
transcriptionCache?: [TranscriptionEntry](TranscriptionEntry.html)[];  
userContent?: Content;  
}

  * Defined in [core/src/agents/invocation_context.ts:25](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L25)



## Properties

### `Optional`abortSignal

abortSignal?: AbortSignal

  * Defined in [core/src/agents/invocation_context.ts:40](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L40)



### `Optional`activeStreamingTools

activeStreamingTools?: Record<string, [ActiveStreamingTool](../classes/ActiveStreamingTool.html)>

  * Defined in [core/src/agents/invocation_context.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L38)



### agent

agent: [BaseAgent](../classes/BaseAgent.html)

  * Defined in [core/src/agents/invocation_context.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L32)



### `Optional`artifactService

artifactService?: [SessionArtifactService](SessionArtifactService.html)

  * Defined in [core/src/agents/invocation_context.ts:26](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L26)



### `Optional`branch

branch?: string

  * Defined in [core/src/agents/invocation_context.ts:31](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L31)



### `Optional`credentialService

credentialService?: [BaseCredentialService](BaseCredentialService.html)

  * Defined in [core/src/agents/invocation_context.ts:29](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L29)



### `Optional`endInvocation

endInvocation?: boolean

  * Defined in [core/src/agents/invocation_context.ts:35](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L35)



### invocationId

invocationId: string

  * Defined in [core/src/agents/invocation_context.ts:30](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L30)



### `Optional`memoryService

memoryService?: [BaseMemoryService](BaseMemoryService.html)

  * Defined in [core/src/agents/invocation_context.ts:28](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L28)



### pluginManager

pluginManager: [PluginManager](../classes/PluginManager.html)

  * Defined in [core/src/agents/invocation_context.ts:39](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L39)



### `Optional`runConfig

runConfig?: [RunConfig](RunConfig.html)

  * Defined in [core/src/agents/invocation_context.ts:37](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L37)



### session

session: [Session](Session.html)

  * Defined in [core/src/agents/invocation_context.ts:34](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L34)



### `Optional`sessionService

sessionService?: [BaseSessionService](../classes/BaseSessionService.html)

  * Defined in [core/src/agents/invocation_context.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L27)



### `Optional`transcriptionCache

transcriptionCache?: [TranscriptionEntry](TranscriptionEntry.html)[]

  * Defined in [core/src/agents/invocation_context.ts:36](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L36)



### `Optional`userContent

userContent?: Content

  * Defined in [core/src/agents/invocation_context.ts:33](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/agents/invocation_context.ts#L33)



Properties

abortSignalactiveStreamingToolsagentartifactServicebranchcredentialServiceendInvocationinvocationIdmemoryServicepluginManagerrunConfigsessionsessionServicetranscriptionCacheuserContent

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


