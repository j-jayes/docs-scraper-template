[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ChromeBuiltInLlmParams]()



# Interface ChromeBuiltInLlmParams

Constructor options for [ChromeBuiltInLlm](../classes/ChromeBuiltInLlm.html).

interface ChromeBuiltInLlmParams {  
expectedInputs?: [ChromeExpectedModality](ChromeExpectedModality.html)[];  
expectedOutputs?: [ChromeExpectedModality](ChromeExpectedModality.html)[];  
languageModel?: [ChromeLanguageModelFactory](ChromeLanguageModelFactory.html);  
model?: string;  
normalizeSystemPrompt?: (systemPrompt: string) => string;  
onDiagnostic?: (diagnostic: [ChromeBuiltInDiagnostic](ChromeBuiltInDiagnostic.html)) => void;  
onDownloadProgress?: (loaded: number) => void;  
temperature?: number;  
topK?: number;  
}

  * Defined in [core/src/models/chrome_prompt_llm.ts:185](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L185)



## Properties

### `Optional`expectedInputs

expectedInputs?: [ChromeExpectedModality](ChromeExpectedModality.html)[]

Modalities to declare at session creation.

  * Defined in [core/src/models/chrome_prompt_llm.ts:202](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L202)



### `Optional`expectedOutputs

expectedOutputs?: [ChromeExpectedModality](ChromeExpectedModality.html)[]

  * Defined in [core/src/models/chrome_prompt_llm.ts:203](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L203)



### `Optional`languageModel

languageModel?: [ChromeLanguageModelFactory](ChromeLanguageModelFactory.html)

Injects an alternative implementation of the `LanguageModel` global, for tests and for embedding a stand-in. Defaults to `globalThis.LanguageModel`.

  * Defined in [core/src/models/chrome_prompt_llm.ts:193](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L193)



### `Optional`model

model?: string

Model id used for registry matching. Defaults to `chrome-on-device`.

  * Defined in [core/src/models/chrome_prompt_llm.ts:187](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L187)



### `Optional`normalizeSystemPrompt

normalizeSystemPrompt?: (systemPrompt: string) => string

Rewrites the system prompt before a session is created.

This exists because of a specific and costly interaction with ADK. Every request is prefixed by ADK's identity processor with:
    
    
    You are an agent. Your internal name is "<agent name>".
    

Under a `ParallelAgent` fan-out each child has a different name, so every child produces a _different_ system prompt, so the warm base session never hits and each child pays a full `create()` — the most expensive call available — precisely when the most calls are in flight.

Pass [stripAdkIdentityPreamble](../functions/stripAdkIdentityPreamble.html) to drop it. That is safe whenever agent transfer is disabled, because the identity line exists to support transfer. Leave it unset for multi-agent setups that route by name.

  * Defined in [core/src/models/chrome_prompt_llm.ts:223](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L223)



### `Optional`onDiagnostic

onDiagnostic?: (diagnostic: [ChromeBuiltInDiagnostic](ChromeBuiltInDiagnostic.html)) => void

Receives timing and context diagnostics.

  * Defined in [core/src/models/chrome_prompt_llm.ts:225](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L225)



### `Optional`onDownloadProgress

onDownloadProgress?: (loaded: number) => void

Receives bytes-loaded progress while the model downloads on first use.

  * Defined in [core/src/models/chrome_prompt_llm.ts:205](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L205)



### `Optional`temperature

temperature?: number

Sampling temperature. Accepted only in extension contexts; on a plain web page `create()` rejects it and the adapter retries without it.

  * Defined in [core/src/models/chrome_prompt_llm.ts:198](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L198)



### `Optional`topK

topK?: number

Sampling top-K. Subject to the same restriction as `temperature`.

  * Defined in [core/src/models/chrome_prompt_llm.ts:200](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L200)



Properties

expectedInputsexpectedOutputslanguageModelmodelnormalizeSystemPromptonDiagnosticonDownloadProgresstemperaturetopK

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


