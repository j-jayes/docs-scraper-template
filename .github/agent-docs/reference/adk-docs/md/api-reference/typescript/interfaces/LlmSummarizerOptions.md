[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [LlmSummarizerOptions]()



# Interface LlmSummarizerOptions

Options for constructing an [LlmSummarizer](../classes/LlmSummarizer.html).

interface LlmSummarizerOptions {  
llm: [BaseLlm](../classes/BaseLlm.html);  
prompt?: string;  
}

  * Defined in [core/src/context/summarizers/llm_summarizer.ts:17](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/summarizers/llm_summarizer.ts#L17)



## Properties

### llm

llm: [BaseLlm](../classes/BaseLlm.html)

The LLM instance used to generate the summary.

  * Defined in [core/src/context/summarizers/llm_summarizer.ts:19](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/summarizers/llm_summarizer.ts#L19)



### `Optional`prompt

prompt?: string

Optional system prompt prepended to the formatted events. Defaults to a built-in summarization prompt when omitted.

  * Defined in [core/src/context/summarizers/llm_summarizer.ts:24](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/context/summarizers/llm_summarizer.ts#L24)



Properties

llmprompt

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


