[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [InvocationContextParams]()



# Interface InvocationContextParams

The parameters for creating an invocation context.

interface InvocationContextParams {  
activeStreamingTools?: Record<string, [ActiveStreamingTool](../classes/ActiveStreamingTool.html)>;  
agent: [BaseAgent](../classes/BaseAgent.html);  
artifactService?: [BaseArtifactService](BaseArtifactService.html);  
branch?: string;  
credentialService?: [BaseCredentialService](BaseCredentialService.html);  
endInvocation?: boolean;  
invocationId: string;  
liveRequestQueue?: [LiveRequestQueue](../classes/LiveRequestQueue.html);  
memoryService?: [BaseMemoryService](BaseMemoryService.html);  
pluginManager: [PluginManager](../classes/PluginManager.html);  
runConfig?: [RunConfig](RunConfig.html);  
session: [Session](Session.html);  
sessionService?: [BaseSessionService](../classes/BaseSessionService.html);  
transcriptionCache?: [TranscriptionEntry](TranscriptionEntry.html)[];  
userContent?: Content;  
}

  * Defined in [agents/invocation_context.ts:26](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L26)



## Properties

### `Optional`activeStreamingTools

activeStreamingTools?: Record<string, [ActiveStreamingTool](../classes/ActiveStreamingTool.html)>

  * Defined in [agents/invocation_context.ts:40](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L40)



### agent

agent: [BaseAgent](../classes/BaseAgent.html)

  * Defined in [agents/invocation_context.ts:33](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L33)



### `Optional`artifactService

artifactService?: [BaseArtifactService](BaseArtifactService.html)

  * Defined in [agents/invocation_context.ts:27](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L27)



### `Optional`branch

branch?: string

  * Defined in [agents/invocation_context.ts:32](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L32)



### `Optional`credentialService

credentialService?: [BaseCredentialService](BaseCredentialService.html)

  * Defined in [agents/invocation_context.ts:30](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L30)



### `Optional`endInvocation

endInvocation?: boolean

  * Defined in [agents/invocation_context.ts:36](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L36)



### invocationId

invocationId: string

  * Defined in [agents/invocation_context.ts:31](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L31)



### `Optional`liveRequestQueue

liveRequestQueue?: [LiveRequestQueue](../classes/LiveRequestQueue.html)

  * Defined in [agents/invocation_context.ts:39](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L39)



### `Optional`memoryService

memoryService?: [BaseMemoryService](BaseMemoryService.html)

  * Defined in [agents/invocation_context.ts:29](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L29)



### pluginManager

pluginManager: [PluginManager](../classes/PluginManager.html)

  * Defined in [agents/invocation_context.ts:41](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L41)



### `Optional`runConfig

runConfig?: [RunConfig](RunConfig.html)

  * Defined in [agents/invocation_context.ts:38](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L38)



### session

session: [Session](Session.html)

  * Defined in [agents/invocation_context.ts:35](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L35)



### `Optional`sessionService

sessionService?: [BaseSessionService](../classes/BaseSessionService.html)

  * Defined in [agents/invocation_context.ts:28](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L28)



### `Optional`transcriptionCache

transcriptionCache?: [TranscriptionEntry](TranscriptionEntry.html)[]

  * Defined in [agents/invocation_context.ts:37](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L37)



### `Optional`userContent

userContent?: Content

  * Defined in [agents/invocation_context.ts:34](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/invocation_context.ts#L34)



Properties

activeStreamingToolsagentartifactServicebranchcredentialServiceendInvocationinvocationIdliveRequestQueuememoryServicepluginManagerrunConfigsessionsessionServicetranscriptionCacheuserContent

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


