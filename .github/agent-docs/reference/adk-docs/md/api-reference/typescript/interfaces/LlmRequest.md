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

  * Defined in [models/llm_request.ts:21](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_request.ts#L21)



## Properties

### `Optional`config

config?: GenerateContentConfig

Additional config for the generate content request. Tools in generateContentConfig should not be set directly; use appendTools.

  * Defined in [models/llm_request.ts:36](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_request.ts#L36)



### contents

contents: Content[]

The contents to send to the model.

  * Defined in [models/llm_request.ts:30](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_request.ts#L30)



### liveConnectConfig

liveConnectConfig: LiveConnectConfig

  * Defined in [models/llm_request.ts:38](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_request.ts#L38)



### `Optional`model

model?: string

The model name.

  * Defined in [models/llm_request.ts:25](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_request.ts#L25)



### toolsDict

toolsDict: { [key: string]: [BaseTool](../classes/BaseTool.html) }

The tools dictionary. Excluded from JSON serialization.

  * Defined in [models/llm_request.ts:43](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/llm_request.ts#L43)



Properties

configcontentsliveConnectConfigmodeltoolsDict

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


