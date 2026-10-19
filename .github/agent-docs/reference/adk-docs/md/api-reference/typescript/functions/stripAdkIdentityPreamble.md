[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [stripAdkIdentityPreamble]()



# Function stripAdkIdentityPreamble

  * stripAdkIdentityPreamble(systemPrompt: string): string

Removes ADK's per-agent identity preamble from a system prompt.

Turns:
        
        You are an agent. Your internal name is "rerank_11".
        The description about you is "..."
        
        <the actual instruction>
        

into just the instruction, so that sibling agents sharing one instruction also share one cached session. See [ChromeBuiltInLlmParams.normalizeSystemPrompt](../interfaces/ChromeBuiltInLlmParams.html#normalizesystemprompt).

#### Parameters

    * systemPrompt: string

#### Returns string

    * Defined in [core/src/models/chrome_prompt_utils.ts:249](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/models/chrome_prompt_utils.ts#L249)




[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


