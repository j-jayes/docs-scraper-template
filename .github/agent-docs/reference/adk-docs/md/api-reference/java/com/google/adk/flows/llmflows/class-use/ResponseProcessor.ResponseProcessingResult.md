JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../ResponseProcessor.ResponseProcessingResult.html)
  * Use
  * [Tree](../package-tree.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)



  1. [com.google.adk.flows.llmflows](../package-summary.html)
  2. [ResponseProcessor](../ResponseProcessor.html)
  3. [ResponseProcessingResult](../ResponseProcessor.ResponseProcessingResult.html)



# Uses of Class  
com.google.adk.flows.llmflows.ResponseProcessor.ResponseProcessingResult

Packages that use [ResponseProcessor.ResponseProcessingResult](../ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")

Package

Description

com.google.adk.flows.llmflows

 

  * ## Uses of [ResponseProcessor.ResponseProcessingResult](../ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows") in [com.google.adk.flows.llmflows](../package-summary.html)

Methods in [com.google.adk.flows.llmflows](../package-summary.html) that return [ResponseProcessor.ResponseProcessingResult](../ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")

Modifier and Type

Method

Description

`static [ResponseProcessor.ResponseProcessingResult](../ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

ResponseProcessor.ResponseProcessingResult.`[create](../ResponseProcessor.ResponseProcessingResult.html#create\(com.google.adk.models.LlmResponse,java.lang.Iterable,java.util.Optional\))([LlmResponse](../../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../../events/Event.html "class in com.google.adk.events")> events, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> transferToAgent)`

 

Methods in [com.google.adk.flows.llmflows](../package-summary.html) that return types with arguments of type [ResponseProcessor.ResponseProcessingResult](../ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")

Modifier and Type

Method

Description

`protected io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](../ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

BaseLlmFlow.`[postprocess](../BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\))([InvocationContext](../../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../../../events/Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Post-processes the LLM response after receiving it from the LLM.

`io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](../ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

ResponseProcessor.`[processResponse](../ResponseProcessor.html#processResponse\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmResponse\))([InvocationContext](../../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmResponse](../../../models/LlmResponse.html "class in com.google.adk.models") response)`

Process the LLM response as part of the post-processing stage.




* * *

Copyright (C) 2025\. All rights reserved.
