[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LlmRequest]()



# Interface LlmRequest

LLM request class that allows passing in tools, output schema and system instructions to the model.

interface LlmRequest {  
config?: GenerateContentConfig;  
contents: Content[];  
liveConnectConfig: LiveConnectConfig;  
model?: string;  
toolsDict: { [key: string]: [BaseTool](../classes/BaseTool.html) };  
}

  * Defined in [core/src/models/llm_request.ts:15](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_request.ts#L15)



## Properties

### `Optional`config

config?: GenerateContentConfig

Additional config for the generate content request. Tools in generateContentConfig should not be set directly; use appendTools.

  * Defined in [core/src/models/llm_request.ts:30](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_request.ts#L30)



### contents

contents: Content[]

The contents to send to the model.

  * Defined in [core/src/models/llm_request.ts:24](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_request.ts#L24)



### liveConnectConfig

liveConnectConfig: LiveConnectConfig

  * Defined in [core/src/models/llm_request.ts:32](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_request.ts#L32)



### `Optional`model

model?: string

The model name.

  * Defined in [core/src/models/llm_request.ts:19](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_request.ts#L19)



### toolsDict

toolsDict: { [key: string]: [BaseTool](../classes/BaseTool.html) }

The tools dictionary. Excluded from JSON serialization.

  * Defined in [core/src/models/llm_request.ts:37](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/llm_request.ts#L37)



Properties

configcontentsliveConnectConfigmodeltoolsDict

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


