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



  * Defined in [core/src/models/google_llm.ts:32](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L32)



## Properties

### `Optional`apiKey

apiKey?: string

The API key to use for the Gemini API. If not provided, it will look for the GOOGLE_GENAI_API_KEY, GOOGLE_API_KEY or GEMINI_API_KEY environment variable, in that order.

  * Defined in [core/src/models/google_llm.ts:42](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L42)



### `Optional`headers

headers?: Record<string, string>

Headers to merge with internally crafted headers.

  * Defined in [core/src/models/google_llm.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L59)



### `Optional`location

location?: string

The Vertex AI location. Required if `vertexai` is true.

  * Defined in [core/src/models/google_llm.ts:55](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L55)



### `Optional`model

model?: string

The name of the model to use. Defaults to 'gemini-2.5-flash'.

  * Defined in [core/src/models/google_llm.ts:36](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L36)



### `Optional`project

project?: string

The Vertex AI project ID. Required if `vertexai` is true.

  * Defined in [core/src/models/google_llm.ts:51](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L51)



### `Optional`useInteractionsApi

useInteractionsApi?: boolean

Whether to use the Interactions API for stateful conversations.

  * Defined in [core/src/models/google_llm.ts:63](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L63)



### `Optional`vertexai

vertexai?: boolean

Whether to use Vertex AI. If true, `project`, `location` should be provided.

  * Defined in [core/src/models/google_llm.ts:47](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/google_llm.ts#L47)



Properties

apiKeyheaderslocationmodelprojectuseInteractionsApivertexai

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


