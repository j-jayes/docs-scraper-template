JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../CallbackContext.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.agents](../package-summary.html)
  2. [CallbackContext](../CallbackContext.html)



# Uses of Class  
com.google.adk.agents.CallbackContext

Packages that use [CallbackContext](../CallbackContext.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.tools

 

  * ## Uses of [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [CallbackContext](../CallbackContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

Callbacks.AfterAgentCallback.`[call](../Callbacks.AfterAgentCallback.html#call\(com.google.adk.agents.CallbackContext\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Async callback after agent runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

Callbacks.AfterAgentCallbackSync.`[call](../Callbacks.AfterAgentCallbackSync.html#call\(com.google.adk.agents.CallbackContext\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallback.`[call](../Callbacks.AfterModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Async callback after LLM response.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Callbacks.AfterModelCallbackSync.`[call](../Callbacks.AfterModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmResponse\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

 

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

Callbacks.BeforeAgentCallback.`[call](../Callbacks.BeforeAgentCallback.html#call\(com.google.adk.agents.CallbackContext\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Async callback before agent runs.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<com.google.genai.types.Content>`

Callbacks.BeforeAgentCallbackSync.`[call](../Callbacks.BeforeAgentCallbackSync.html#call\(com.google.adk.agents.CallbackContext\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext)`

 

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallback.`[call](../Callbacks.BeforeModelCallback.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest)`

Async callback before LLM invocation.

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")>`

Callbacks.BeforeModelCallbackSync.`[call](../Callbacks.BeforeModelCallbackSync.html#call\(com.google.adk.agents.CallbackContext,com.google.adk.models.LlmRequest\))([CallbackContext](../CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest)`

 

  * ## Uses of [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Subclasses of [CallbackContext](../CallbackContext.html "class in com.google.adk.agents") in [com.google.adk.tools](../../tools/package-summary.html)

Modifier and Type

Class

Description

`class `

`[ToolContext](../../tools/ToolContext.html "class in com.google.adk.tools")`

ToolContext object provides a structured context for executing tools or functions.




* * *

Copyright (C) 2025\. All rights reserved.
