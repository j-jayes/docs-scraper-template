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
proactivity?: ProactivityConfig;  
realtimeInputConfig?: RealtimeInputConfig;  
responseModalities?: Modality[];  
saveInputBlobsAsArtifacts?: boolean;  
speechConfig?: SpeechConfig;  
streamingMode?: [StreamingMode](../enums/StreamingMode.html);  
supportCfc?: boolean;  
}

  * Defined in [core/src/agents/run_config.ts:23](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L23)



## Properties

### `Optional`enableAffectiveDialog

enableAffectiveDialog?: boolean

If enabled, the model will detect emotions and adapt its responses accordingly.

  * Defined in [core/src/agents/run_config.ts:68](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L68)



### `Optional`inputAudioTranscription

inputAudioTranscription?: AudioTranscriptionConfig

Input transcription for live agents with audio input from user.

  * Defined in [core/src/agents/run_config.ts:62](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L62)



### `Optional`maxLlmCalls

maxLlmCalls?: number

A limit on the total number of llm calls for a given run.

Valid Values:

  * More than 0 and less than sys.maxsize: The bound on the number of llm calls is enforced, if the value is set in this range.
  * Less than or equal to 0: This allows for unbounded number of llm calls.



  * Defined in [core/src/agents/run_config.ts:89](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L89)



### `Optional`outputAudioTranscription

outputAudioTranscription?: AudioTranscriptionConfig

Output audio transcription config.

  * Defined in [core/src/agents/run_config.ts:57](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L57)



### `Optional`proactivity

proactivity?: ProactivityConfig

Configures the proactivity of the model. This allows the model to respond proactively to the input and to ignore irrelevant input.

  * Defined in [core/src/agents/run_config.ts:74](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L74)



### `Optional`realtimeInputConfig

realtimeInputConfig?: RealtimeInputConfig

Realtime input config for live agents with audio input from user.

  * Defined in [core/src/agents/run_config.ts:79](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L79)



### `Optional`responseModalities

responseModalities?: Modality[]

The output modalities. If not set, it's default to AUDIO.

  * Defined in [core/src/agents/run_config.ts:32](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L32)



### `Optional`saveInputBlobsAsArtifacts

saveInputBlobsAsArtifacts?: boolean

Whether or not to save the input blobs as artifacts.

  * Defined in [core/src/agents/run_config.ts:37](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L37)



### `Optional`speechConfig

speechConfig?: SpeechConfig

Speech configuration for the live agent.

  * Defined in [core/src/agents/run_config.ts:27](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L27)



### `Optional`streamingMode

streamingMode?: [StreamingMode](../enums/StreamingMode.html)

Streaming mode, None or StreamingMode.SSE or StreamingMode.BIDI.

  * Defined in [core/src/agents/run_config.ts:52](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L52)



### `Optional`supportCfc

supportCfc?: boolean

Whether to support CFC (Compositional Function Calling). Only applicable for StreamingMode.SSE. If it's true. the LIVE API will be invoked. Since only LIVE API supports CFC

WARNING: This feature is **experimental** and its API or behavior may change in future releases.

  * Defined in [core/src/agents/run_config.ts:47](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/agents/run_config.ts#L47)



Properties

enableAffectiveDialoginputAudioTranscriptionmaxLlmCallsoutputAudioTranscriptionproactivityrealtimeInputConfigresponseModalitiessaveInputBlobsAsArtifactsspeechConfigstreamingModesupportCfc

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


