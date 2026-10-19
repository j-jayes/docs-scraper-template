[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ChromeCreateMonitor]()



# Interface ChromeCreateMonitor

Emits `downloadprogress` while the model is fetched on first use.

interface ChromeCreateMonitor {  
addEventListener(  
type: "downloadprogress",  
listener: (event: { loaded: number }) => void,  
): void;  
}

  * Defined in [core/src/models/chrome_prompt_llm.ts:117](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L117)



## Methods

### addEventListener

  * addEventListener(  
type: "downloadprogress",  
listener: (event: { loaded: number }) => void,  
): void

#### Parameters

    * type: "downloadprogress"
    * listener: (event: { loaded: number }) => void

#### Returns void

    * Defined in [core/src/models/chrome_prompt_llm.ts:118](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_llm.ts#L118)




Methods

addEventListener

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


