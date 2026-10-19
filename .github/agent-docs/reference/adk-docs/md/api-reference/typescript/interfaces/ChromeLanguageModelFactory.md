[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ChromeLanguageModelFactory]()



# Interface ChromeLanguageModelFactory

The `LanguageModel` global itself.

interface ChromeLanguageModelFactory {  
availability(  
options?: [ChromeCreateCoreOptions](ChromeCreateCoreOptions.html),  
): Promise<[ChromeModelAvailability](../types/ChromeModelAvailability.html)>;  
create(options?: [ChromeCreateOptions](ChromeCreateOptions.html)): Promise<[ChromeLanguageModelSession](ChromeLanguageModelSession.html)>;  
}

  * Defined in [core/src/models/chrome_prompt_llm.ts:164](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L164)



## Methods

### availability

  * availability(  
options?: [ChromeCreateCoreOptions](ChromeCreateCoreOptions.html),  
): Promise<[ChromeModelAvailability](../types/ChromeModelAvailability.html)>

#### Parameters

    * `Optional`options: [ChromeCreateCoreOptions](ChromeCreateCoreOptions.html)

#### Returns Promise<[ChromeModelAvailability](../types/ChromeModelAvailability.html)>

    * Defined in [core/src/models/chrome_prompt_llm.ts:165](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L165)




### create

  * create(options?: [ChromeCreateOptions](ChromeCreateOptions.html)): Promise<[ChromeLanguageModelSession](ChromeLanguageModelSession.html)>

#### Parameters

    * `Optional`options: [ChromeCreateOptions](ChromeCreateOptions.html)

#### Returns Promise<[ChromeLanguageModelSession](ChromeLanguageModelSession.html)>

    * Defined in [core/src/models/chrome_prompt_llm.ts:168](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L168)




Methods

availabilitycreate

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


