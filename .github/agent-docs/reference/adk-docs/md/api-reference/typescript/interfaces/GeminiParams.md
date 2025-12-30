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

  * Defined in [core/src/models/google_llm.ts:26](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L26)



## Properties

### `Optional`apiKey

apiKey?: string

The API key to use for the Gemini API. If not provided, it will look for the GOOGLE_GENAI_API_KEY or GEMINI_API_KEY environment variable.

  * Defined in [core/src/models/google_llm.ts:35](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L35)



### `Optional`headers

headers?: Record<string, string>

Headers to merge with internally crafted headers.

  * Defined in [core/src/models/google_llm.ts:52](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L52)



### `Optional`location

location?: string

The Vertex AI location. Required if `vertexai` is true.

  * Defined in [core/src/models/google_llm.ts:48](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L48)



### `Optional`model

model?: string

The name of the model to use. Defaults to 'gemini-2.5-flash'.

  * Defined in [core/src/models/google_llm.ts:30](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L30)



### `Optional`project

project?: string

The Vertex AI project ID. Required if `vertexai` is true.

  * Defined in [core/src/models/google_llm.ts:44](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L44)



### `Optional`vertexai

vertexai?: boolean

Whether to use Vertex AI. If true, `project`, `location` should be provided.

  * Defined in [core/src/models/google_llm.ts:40](https://github.com/google/adk-js/blob/6d1a56a15e0864ce1e83b259bc9964333503ff5a/core/src/models/google_llm.ts#L40)



Properties

apiKeyheaderslocationmodelprojectvertexai

[ADK for TypeScript: API Reference](../index.html)

  * Loading...


