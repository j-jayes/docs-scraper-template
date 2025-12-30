JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/BaseLlmFlow.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [BaseLlmFlow](BaseLlmFlow.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. requestProcessors
     2. responseProcessors
     3. stepsCompleted
     4. maxSteps
  6. Constructor Details
     1. BaseLlmFlow(List, List)
     2. BaseLlmFlow(List, List, Optional)
  7. Method Details
     1. preprocess(InvocationContext, LlmRequest)
     2. postprocess(InvocationContext, Event, LlmRequest, LlmResponse)
     3. run(InvocationContext)
     4. runLive(InvocationContext)



# Class BaseLlmFlow

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.flows.llmflows.BaseLlmFlow

All Implemented Interfaces:
    `[BaseFlow](../BaseFlow.html "interface in com.google.adk.flows")`

Direct Known Subclasses:
    `[SingleFlow](SingleFlow.html "class in com.google.adk.flows.llmflows")`

* * *

public abstract class BaseLlmFlow extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [BaseFlow](../BaseFlow.html "interface in com.google.adk.flows")

A basic flow that calls the LLM in a loop until a final response is generated.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`protected final int`

`maxSteps`

 

`protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")>`

`requestProcessors`

 

`protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")>`

`responseProcessors`

 

`protected int`

`stepsCompleted`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`BaseLlmFlow([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")> requestProcessors, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> responseProcessors)`

 

`BaseLlmFlow([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")> requestProcessors, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> responseProcessors, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxSteps)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`protected io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")>`

`postprocess([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../../events/Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)`

Post-processes the LLM response after receiving it from the LLM.

`protected io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

`preprocess([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest)`

Pre-processes the LLM request before sending it to the LLM.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

`run([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the full LLM flow by repeatedly calling `runOneStep(com.google.adk.agents.InvocationContext)` until a final response is produced.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

`runLive([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the LLM flow in streaming mode.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### requestProcessors

protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")> requestProcessors

    * ### responseProcessors

protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> responseProcessors

    * ### stepsCompleted

protected int stepsCompleted

    * ### maxSteps

protected final int maxSteps

  * ## Constructor Details

    * ### BaseLlmFlow

public BaseLlmFlow([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")> requestProcessors, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> responseProcessors)

    * ### BaseLlmFlow

public BaseLlmFlow([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")> requestProcessors, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> responseProcessors, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxSteps)

  * ## Method Details

    * ### preprocess

protected io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")> preprocess([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest)

Pre-processes the LLM request before sending it to the LLM. Executes all registered [`RequestProcessor`](RequestProcessor.html "interface in com.google.adk.flows.llmflows").

    * ### postprocess

protected io.reactivex.rxjava3.core.Single<[ResponseProcessor.ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")> postprocess([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../../events/Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse)

Post-processes the LLM response after receiving it from the LLM. Executes all registered [`ResponseProcessor`](ResponseProcessor.html "interface in com.google.adk.flows.llmflows") instances. Handles function calls if present in the response.

    * ### run

public io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")> run([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Executes the full LLM flow by repeatedly calling `runOneStep(com.google.adk.agents.InvocationContext)` until a final response is produced.

Specified by:
    `[run](../BaseFlow.html#run\(com.google.adk.agents.InvocationContext\))` in interface `[BaseFlow](../BaseFlow.html "interface in com.google.adk.flows")`
Returns:
    A `Flowable` of all [`Event`](../../events/Event.html "class in com.google.adk.events")s generated during the flow.

    * ### runLive

public io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")> runLive([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Executes the LLM flow in streaming mode. 

Handles sending history and live requests to the LLM, receiving responses, processing them, and managing agent transfers.

Specified by:
    `[runLive](../BaseFlow.html#runLive\(com.google.adk.agents.InvocationContext\))` in interface `[BaseFlow](../BaseFlow.html "interface in com.google.adk.flows")`
Returns:
    A `Flowable` of [`Event`](../../events/Event.html "class in com.google.adk.events")s streamed in real-time.




* * *

Copyright (C) 2025\. All rights reserved.
