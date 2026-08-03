[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LlmRequest]()



# Interface LlmRequest

LLM request class that allows passing in tools, output schema and system instructions to the model.

interface LlmRequest {  
allowedTools?: string[];  
config?: GenerateContentConfig;  
contents: Content[];  
liveConnectConfig: LiveConnectConfig;  
model?: string;  
previousInteractionId?: string;  
toolsDict: { [key: string]: [BaseTool](../classes/BaseTool.html) };  
}

  * Defined in [core/src/models/llm_request.ts:21](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_request.ts#L21)



## Properties

### `Optional`allowedTools

allowedTools?: string[]

The set of allowed tools, populated by request processors.

  * Defined in [core/src/models/llm_request.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_request.ts#L48)



### `Optional`config

config?: GenerateContentConfig

Additional config for the generate content request. Tools in generateContentConfig should not be set directly; use appendTools.

  * Defined in [core/src/models/llm_request.ts:36](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_request.ts#L36)



### contents

contents: Content[]

The contents to send to the model.

  * Defined in [core/src/models/llm_request.ts:30](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_request.ts#L30)



### liveConnectConfig

liveConnectConfig: LiveConnectConfig

  * Defined in [core/src/models/llm_request.ts:38](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_request.ts#L38)



### `Optional`model

model?: string

The model name.

  * Defined in [core/src/models/llm_request.ts:25](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_request.ts#L25)



### `Optional`previousInteractionId

previousInteractionId?: string

The interaction ID from the previous turn, if any.

  * Defined in [core/src/models/llm_request.ts:53](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_request.ts#L53)



### toolsDict

toolsDict: { [key: string]: [BaseTool](../classes/BaseTool.html) }

The tools dictionary. Excluded from JSON serialization.

  * Defined in [core/src/models/llm_request.ts:43](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/llm_request.ts#L43)



Properties

allowedToolsconfigcontentsliveConnectConfigmodelpreviousInteractionIdtoolsDict

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


