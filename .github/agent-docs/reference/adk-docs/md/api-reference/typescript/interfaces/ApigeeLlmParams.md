[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ApigeeLlmParams]()



# Interface ApigeeLlmParams

The parameters for creating a Gemini instance.

interface ApigeeLlmParams {  
apiKey?: string;  
headers?: Record<string, string>;  
location?: string;  
model: string;  
project?: string;  
proxyUrl?: string;  
useInteractionsApi?: boolean;  
vertexai?: boolean;  
}

#### Hierarchy ([View Summary](../hierarchy.html#ApigeeLlmParams))

  * [GeminiParams](GeminiParams.html)
    * ApigeeLlmParams



  * Defined in [core/src/models/apigee_llm.ts:18](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/apigee_llm.ts#L18)



## Properties

### `Optional`apiKey

apiKey?: string

API key to use. If not provided, it will look for the GOOGLE_GENAI_API_KEY or GEMINI_API_KEY environment variable. If gemini provider is selected and no key is provided, the fake key "-" will be used for the "x-goog-api-key" header.

Overrides [GeminiParams](GeminiParams.html).[apiKey](GeminiParams.html#apikey)

  * Defined in [core/src/models/apigee_llm.ts:48](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/apigee_llm.ts#L48)



### `Optional`headers

headers?: Record<string, string>

Headers to merge with internally crafted headers.

Inherited from [GeminiParams](GeminiParams.html).[headers](GeminiParams.html#headers)

  * Defined in [core/src/models/google_llm.ts:58](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L58)



### `Optional`location

location?: string

The Vertex AI location. Required if `vertexai` is true.

Inherited from [GeminiParams](GeminiParams.html).[location](GeminiParams.html#location)

  * Defined in [core/src/models/google_llm.ts:54](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L54)



### model

model: string

The name of the model to use. The model string specifies the LLM provider (e.g., Vertex AI, Gemini), API version, and the model ID. Supported format: `apigee/[<provider>/][<version>/]<model_id>` Components: `provider` (optional): `vertex_ai` or `gemini`. `version` (optional): The API version (e.g., `v1`, `v1beta`). If not provided, a default version will selected based on the provider. `model_id` (required): The model identifier (e.g., `gemini-2.5-flash`). Examples: \- `apigee/gemini-2.5-flash` \- `apigee/v1/gemini-2.5-flash` \- `apigee/vertex_ai/gemini-2.5-flash` \- `apigee/gemini/v1/gemini-2.5-flash` \- `apigee/vertex_ai/v1beta/gemini-2.5-flash`

Overrides [GeminiParams](GeminiParams.html).[model](GeminiParams.html#model)

  * Defined in [core/src/models/apigee_llm.ts:36](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/apigee_llm.ts#L36)



### `Optional`project

project?: string

The Vertex AI project ID. Required if `vertexai` is true.

Inherited from [GeminiParams](GeminiParams.html).[project](GeminiParams.html#project)

  * Defined in [core/src/models/google_llm.ts:50](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L50)



### `Optional`proxyUrl

proxyUrl?: string

The proxy URL for the provider API. If not provided, it will look for the APIGEE_PROXY_URL environment variable.

  * Defined in [core/src/models/apigee_llm.ts:41](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/apigee_llm.ts#L41)



### `Optional`useInteractionsApi

useInteractionsApi?: boolean

Whether to use the Interactions API for stateful conversations.

Inherited from [GeminiParams](GeminiParams.html).[useInteractionsApi](GeminiParams.html#useinteractionsapi)

  * Defined in [core/src/models/google_llm.ts:62](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L62)



### `Optional`vertexai

vertexai?: boolean

Whether to use Vertex AI. If true, `project`, `location` should be provided.

Inherited from [GeminiParams](GeminiParams.html).[vertexai](GeminiParams.html#vertexai)

  * Defined in [core/src/models/google_llm.ts:46](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/models/google_llm.ts#L46)



Properties

apiKeyheaderslocationmodelprojectproxyUrluseInteractionsApivertexai

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


