JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/RequestProcessor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [RequestProcessor](RequestProcessor.html)



Contents 

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. processRequest(InvocationContext, LlmRequest)

Hide sidebar  Show sidebar

# Interface RequestProcessor

All Known Implementing Classes:
    `[AgentTransfer](AgentTransfer.html "class in com.google.adk.flows.llmflows"), [Basic](Basic.html "class in com.google.adk.flows.llmflows"), [Compaction](Compaction.html "class in com.google.adk.flows.llmflows"), [Contents](Contents.html "class in com.google.adk.flows.llmflows"), [Identity](Identity.html "class in com.google.adk.flows.llmflows"), [Instructions](Instructions.html "class in com.google.adk.flows.llmflows"), [RequestConfirmationLlmRequestProcessor](RequestConfirmationLlmRequestProcessor.html "class in com.google.adk.flows.llmflows")`

* * *

public interface RequestProcessor

Interface for processing LLM requests.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

`static class `

`[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

Result of request processing.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

`processRequest([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

Process the LLM request as part of the pre-processing stage.




  * ## Method Details

    * ### processRequest

io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")> processRequest([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)

Process the LLM request as part of the pre-processing stage.

Parameters:
    `context` \- the invocation context.
    `request` \- the LLM request to process.
Returns:
    a list of events generated during processing (if any).




* * *

Copyright (C) 1980\. All rights reserved.
