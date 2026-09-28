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
useInteractionsApi?: boolean;  
vertexai?: boolean;  
}

#### Hierarchy ([View Summary](../hierarchy.html#GeminiParams))

  * GeminiParams
    * [ApigeeLlmParams](ApigeeLlmParams.html)



  * Defined in [core/src/models/google_llm.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L32)



## Properties

### `Optional`apiKey

apiKey?: string

The API key to use for the Gemini API. If not provided, it will look for the GOOGLE_GENAI_API_KEY or GEMINI_API_KEY environment variable.

  * Defined in [core/src/models/google_llm.ts:41](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L41)



### `Optional`headers

headers?: Record<string, string>

Headers to merge with internally crafted headers.

  * Defined in [core/src/models/google_llm.ts:58](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L58)



### `Optional`location

location?: string

The Vertex AI location. Required if `vertexai` is true.

  * Defined in [core/src/models/google_llm.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L54)



### `Optional`model

model?: string

The name of the model to use. Defaults to 'gemini-2.5-flash'.

  * Defined in [core/src/models/google_llm.ts:36](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L36)



### `Optional`project

project?: string

The Vertex AI project ID. Required if `vertexai` is true.

  * Defined in [core/src/models/google_llm.ts:50](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L50)



### `Optional`useInteractionsApi

useInteractionsApi?: boolean

Whether to use the Interactions API for stateful conversations.

  * Defined in [core/src/models/google_llm.ts:62](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L62)



### `Optional`vertexai

vertexai?: boolean

Whether to use Vertex AI. If true, `project`, `location` should be provided.

  * Defined in [core/src/models/google_llm.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L46)



Properties

apiKeyheaderslocationmodelprojectuseInteractionsApivertexai

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


