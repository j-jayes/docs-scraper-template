[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ChromeBuiltInDiagnostic]()



# Interface ChromeBuiltInDiagnostic

Timing and context signals emitted while the adapter runs.

interface ChromeBuiltInDiagnostic {  
contextUsage?: number;  
contextWindow?: number;  
ms?: number;  
note?: string;  
phase: "prompt" | "create" | "parse-fallback" | "context-overflow";  
}

  * Defined in [core/src/models/chrome_prompt_llm.ts:176](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L176)



## Properties

### `Optional`contextUsage

contextUsage?: number

  * Defined in [core/src/models/chrome_prompt_llm.ts:179](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L179)



### `Optional`contextWindow

contextWindow?: number

  * Defined in [core/src/models/chrome_prompt_llm.ts:180](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L180)



### `Optional`ms

ms?: number

  * Defined in [core/src/models/chrome_prompt_llm.ts:178](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L178)



### `Optional`note

note?: string

  * Defined in [core/src/models/chrome_prompt_llm.ts:181](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L181)



### phase

phase: "prompt" | "create" | "parse-fallback" | "context-overflow"

  * Defined in [core/src/models/chrome_prompt_llm.ts:177](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L177)



Properties

contextUsagecontextWindowmsnotephase

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


