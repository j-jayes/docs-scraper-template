JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ResponseProcessor.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [ResponseProcessor](ResponseProcessor.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. processResponse(InvocationContext, LlmResponse)



# Interface ResponseProcessor

* * *

public interface ResponseProcessor

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

`static class `

`[ResponseProcessor.ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

 

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

`processResponse([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") response)`

Process the LLM response as part of the post-processing stage.




  * ## Method Details

    * ### processResponse

io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")> processResponse([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") response)

Process the LLM response as part of the post-processing stage.

Parameters:
    `context` \- the invocation context.
    `response` \- the LLM response to process.
Returns:
    a list of events generated during processing (if any).




* * *

Copyright (C) 2025\. All rights reserved.
