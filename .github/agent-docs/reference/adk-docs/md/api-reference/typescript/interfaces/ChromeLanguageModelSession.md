[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ChromeLanguageModelSession]()



# Interface ChromeLanguageModelSession

A live Prompt API session.

interface ChromeLanguageModelSession {  
contextUsage?: number;  
contextWindow?: number;  
addEventListener?(type: "contextoverflow", listener: () => void): void;  
clone(  
options?: { signal?: AbortSignal },  
): Promise<[ChromeLanguageModelSession]()>;  
destroy?(): void;  
prompt(  
input: string | [ChromeMessage](ChromeMessage.html)[],  
options?: [ChromePromptOptions](ChromePromptOptions.html),  
): Promise<string>;  
promptStreaming(  
input: string | [ChromeMessage](ChromeMessage.html)[],  
options?: [ChromePromptOptions](ChromePromptOptions.html),  
): ReadableStream<string>;  
}

  * Defined in [core/src/models/chrome_prompt_llm.ts:147](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L147)



## Properties

### `Optional` `Readonly`contextUsage

contextUsage?: number

  * Defined in [core/src/models/chrome_prompt_llm.ts:159](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L159)



### `Optional` `Readonly`contextWindow

contextWindow?: number

  * Defined in [core/src/models/chrome_prompt_llm.ts:160](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L160)



## Methods

### `Optional`addEventListener

  * addEventListener?(type: "contextoverflow", listener: () => void): void

#### Parameters

    * type: "contextoverflow"
    * listener: () => void

#### Returns void

    * Defined in [core/src/models/chrome_prompt_llm.ts:158](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L158)




### clone

  * clone(options?: { signal?: AbortSignal }): Promise<[ChromeLanguageModelSession]()>

#### Parameters

    * `Optional`options: { signal?: AbortSignal }

#### Returns Promise<[ChromeLanguageModelSession]()>

    * Defined in [core/src/models/chrome_prompt_llm.ts:156](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L156)




### `Optional`destroy

  * destroy?(): void

#### Returns void

    * Defined in [core/src/models/chrome_prompt_llm.ts:157](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L157)




### prompt

  * prompt(  
input: string | [ChromeMessage](ChromeMessage.html)[],  
options?: [ChromePromptOptions](ChromePromptOptions.html),  
): Promise<string>

#### Parameters

    * input: string | [ChromeMessage](ChromeMessage.html)[]
    * `Optional`options: [ChromePromptOptions](ChromePromptOptions.html)

#### Returns Promise<string>

    * Defined in [core/src/models/chrome_prompt_llm.ts:148](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L148)




### promptStreaming

  * promptStreaming(  
input: string | [ChromeMessage](ChromeMessage.html)[],  
options?: [ChromePromptOptions](ChromePromptOptions.html),  
): ReadableStream<string>

#### Parameters

    * input: string | [ChromeMessage](ChromeMessage.html)[]
    * `Optional`options: [ChromePromptOptions](ChromePromptOptions.html)

#### Returns ReadableStream<string>

    * Defined in [core/src/models/chrome_prompt_llm.ts:152](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L152)




Properties

contextUsagecontextWindow

Methods

addEventListenerclonedestroypromptpromptStreaming

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


