[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [RunConfig]()



# Interface RunConfig

Configs for runtime behavior of agents.

interface RunConfig {  
enableAffectiveDialog?: boolean;  
inputAudioTranscription?: AudioTranscriptionConfig;  
maxLlmCalls?: number;  
outputAudioTranscription?: AudioTranscriptionConfig;  
pauseOnToolCalls?: boolean;  
proactivity?: ProactivityConfig;  
realtimeInputConfig?: RealtimeInputConfig;  
responseModalities?: Modality[];  
saveInputBlobsAsArtifacts?: boolean;  
speechConfig?: SpeechConfig;  
streamingMode?: [StreamingMode](../enums/StreamingMode.html);  
supportCfc?: boolean;  
}

  * Defined in [agents/run_config.ts:29](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L29)



## Properties

### `Optional`enableAffectiveDialog

enableAffectiveDialog?: boolean

If enabled, the model will detect emotions and adapt its responses accordingly.

  * Defined in [agents/run_config.ts:74](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L74)



### `Optional`inputAudioTranscription

inputAudioTranscription?: AudioTranscriptionConfig

Input transcription for live agents with audio input from user.

  * Defined in [agents/run_config.ts:68](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L68)



### `Optional`maxLlmCalls

maxLlmCalls?: number

A limit on the total number of llm calls for a given run.

Valid Values:

  * More than 0 and less than sys.maxsize: The bound on the number of llm calls is enforced, if the value is set in this range.
  * Less than or equal to 0: This allows for unbounded number of llm calls.



  * Defined in [agents/run_config.ts:95](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L95)



### `Optional`outputAudioTranscription

outputAudioTranscription?: AudioTranscriptionConfig

Output audio transcription config.

  * Defined in [agents/run_config.ts:63](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L63)



### `Optional`pauseOnToolCalls

pauseOnToolCalls?: boolean

If true, the agent loop will suspend on ANY tool call, allowing the client to intercept and execute tools (Client-Side Tool Execution).

  * Defined in [agents/run_config.ts:101](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L101)



### `Optional`proactivity

proactivity?: ProactivityConfig

Configures the proactivity of the model. This allows the model to respond proactively to the input and to ignore irrelevant input.

  * Defined in [agents/run_config.ts:80](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L80)



### `Optional`realtimeInputConfig

realtimeInputConfig?: RealtimeInputConfig

Realtime input config for live agents with audio input from user.

  * Defined in [agents/run_config.ts:85](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L85)



### `Optional`responseModalities

responseModalities?: Modality[]

The output modalities. If not set, it's default to AUDIO.

  * Defined in [agents/run_config.ts:38](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L38)



### `Optional`saveInputBlobsAsArtifacts

saveInputBlobsAsArtifacts?: boolean

Whether or not to save the input blobs as artifacts.

  * Defined in [agents/run_config.ts:43](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L43)



### `Optional`speechConfig

speechConfig?: SpeechConfig

Speech configuration for the live agent.

  * Defined in [agents/run_config.ts:33](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L33)



### `Optional`streamingMode

streamingMode?: [StreamingMode](../enums/StreamingMode.html)

Streaming mode, None or StreamingMode.SSE or StreamingMode.BIDI.

  * Defined in [agents/run_config.ts:58](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L58)



### `Optional`supportCfc

supportCfc?: boolean

Whether to support CFC (Compositional Function Calling). Only applicable for StreamingMode.SSE. If it's true. the LIVE API will be invoked. Since only LIVE API supports CFC

WARNING: This feature is **experimental** and its API or behavior may change in future releases.

  * Defined in [agents/run_config.ts:53](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/agents/run_config.ts#L53)



Properties

enableAffectiveDialoginputAudioTranscriptionmaxLlmCallsoutputAudioTranscriptionpauseOnToolCallsproactivityrealtimeInputConfigresponseModalitiessaveInputBlobsAsArtifactsspeechConfigstreamingModesupportCfc

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


