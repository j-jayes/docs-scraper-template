[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [GeminiParams]()



# Interface GeminiParams

The parameters for creating a Gemini instance.

interface GeminiParams {  
apiKey?: string;  
headers?: Record<string, string>;  
location?: string;  
model?: string;  
project?: string;  
vertexai?: boolean;  
}

#### Hierarchy ([View Summary](../hierarchy.html#GeminiParams))

  * GeminiParams
    * [ApigeeLlmParams](ApigeeLlmParams.html)



  * Defined in [models/google_llm.ts:31](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L31)



## Properties

### `Optional`apiKey

apiKey?: string

The API key to use for the Gemini API. If not provided, it will look for the GOOGLE_GENAI_API_KEY or GEMINI_API_KEY environment variable.

  * Defined in [models/google_llm.ts:40](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L40)



### `Optional`headers

headers?: Record<string, string>

Headers to merge with internally crafted headers.

  * Defined in [models/google_llm.ts:57](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L57)



### `Optional`location

location?: string

The Vertex AI location. Required if `vertexai` is true.

  * Defined in [models/google_llm.ts:53](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L53)



### `Optional`model

model?: string

The name of the model to use. Defaults to 'gemini-2.5-flash'.

  * Defined in [models/google_llm.ts:35](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L35)



### `Optional`project

project?: string

The Vertex AI project ID. Required if `vertexai` is true.

  * Defined in [models/google_llm.ts:49](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L49)



### `Optional`vertexai

vertexai?: boolean

Whether to use Vertex AI. If true, `project`, `location` should be provided.

  * Defined in [models/google_llm.ts:45](https://github.com/google/adk-js/blob/1a012d266d3a60055efc59d994f42dce293500af/core/src/models/google_llm.ts#L45)



Properties

apiKeyheaderslocationmodelprojectvertexai

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


