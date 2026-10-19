[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ChromeCreateOptions]()



# Interface ChromeCreateOptions

Options accepted by `LanguageModel.create()`.

interface ChromeCreateOptions {  
expectedInputs?: [ChromeExpectedModality](ChromeExpectedModality.html)[];  
expectedOutputs?: [ChromeExpectedModality](ChromeExpectedModality.html)[];  
initialPrompts?: [ChromeMessage](ChromeMessage.html)[];  
monitor?: (monitor: [ChromeCreateMonitor](ChromeCreateMonitor.html)) => void;  
signal?: AbortSignal;  
temperature?: number;  
topK?: number;  
}

#### Hierarchy ([View Summary](../hierarchy.html#ChromeCreateOptions))

  * [ChromeCreateCoreOptions](ChromeCreateCoreOptions.html)
    * ChromeCreateOptions



  * Defined in [core/src/models/chrome_prompt_llm.ts:131](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L131)



## Properties

### `Optional`expectedInputs

expectedInputs?: [ChromeExpectedModality](ChromeExpectedModality.html)[]

Inherited from [ChromeCreateCoreOptions](ChromeCreateCoreOptions.html).[expectedInputs](ChromeCreateCoreOptions.html#expectedinputs)

  * Defined in [core/src/models/chrome_prompt_llm.ts:126](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L126)



### `Optional`expectedOutputs

expectedOutputs?: [ChromeExpectedModality](ChromeExpectedModality.html)[]

Inherited from [ChromeCreateCoreOptions](ChromeCreateCoreOptions.html).[expectedOutputs](ChromeCreateCoreOptions.html#expectedoutputs)

  * Defined in [core/src/models/chrome_prompt_llm.ts:127](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L127)



### `Optional`initialPrompts

initialPrompts?: [ChromeMessage](ChromeMessage.html)[]

  * Defined in [core/src/models/chrome_prompt_llm.ts:133](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L133)



### `Optional`monitor

monitor?: (monitor: [ChromeCreateMonitor](ChromeCreateMonitor.html)) => void

  * Defined in [core/src/models/chrome_prompt_llm.ts:134](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L134)



### `Optional`signal

signal?: AbortSignal

  * Defined in [core/src/models/chrome_prompt_llm.ts:132](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L132)



### `Optional`temperature

temperature?: number

  * Defined in [core/src/models/chrome_prompt_llm.ts:135](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L135)



### `Optional`topK

topK?: number

  * Defined in [core/src/models/chrome_prompt_llm.ts:136](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L136)



Properties

expectedInputsexpectedOutputsinitialPromptsmonitorsignaltemperaturetopK

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


