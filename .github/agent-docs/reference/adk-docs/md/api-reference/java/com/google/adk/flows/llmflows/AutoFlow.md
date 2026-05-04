JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AutoFlow.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [AutoFlow](AutoFlow.html)



Contents  

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. AutoFlow()
     2. AutoFlow(Optional)

Hide sidebar  Show sidebar

# Class AutoFlow

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

[com.google.adk.flows.llmflows.BaseLlmFlow](BaseLlmFlow.html "class in com.google.adk.flows.llmflows")

[com.google.adk.flows.llmflows.SingleFlow](SingleFlow.html "class in com.google.adk.flows.llmflows")

com.google.adk.flows.llmflows.AutoFlow

All Implemented Interfaces:
    `[BaseFlow](../BaseFlow.html "interface in com.google.adk.flows")`

* * *

public class AutoFlow extends [SingleFlow](SingleFlow.html "class in com.google.adk.flows.llmflows")

LLM flow with automatic agent transfer support.

  * ## Field Summary

### Fields inherited from class [BaseLlmFlow](BaseLlmFlow.html#field-summary "class in com.google.adk.flows.llmflows")

`[maxSteps](BaseLlmFlow.html#maxSteps), [requestProcessors](BaseLlmFlow.html#requestProcessors), [responseProcessors](BaseLlmFlow.html#responseProcessors)`

Modifier and Type

Field

Description

`protected final int`

`[maxSteps](BaseLlmFlow.html#maxSteps)`

 

`protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")>`

`[requestProcessors](BaseLlmFlow.html#requestProcessors)`

 

`protected final [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")>`

`[responseProcessors](BaseLlmFlow.html#responseProcessors)`

 

  * ## Constructor Summary

Constructors

Constructor

Description

`AutoFlow()`

 

`AutoFlow([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> maxSteps)`

 

  * ## Method Summary

### Methods inherited from class [BaseLlmFlow](BaseLlmFlow.html#method-summary "class in com.google.adk.flows.llmflows")

`[postprocess](BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse,io.opentelemetry.context.Context\) "postprocess\(InvocationContext, Event, LlmRequest, LlmResponse, Context\)"), [run](BaseLlmFlow.html#run\(com.google.adk.agents.InvocationContext\) "run\(InvocationContext\)"), [runLive](BaseLlmFlow.html#runLive\(com.google.adk.agents.InvocationContext\) "runLive\(InvocationContext\)")`

Modifier and Type

Method

Description

`protected io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

`[postprocess](BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse,io.opentelemetry.context.Context\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [Event](../../events/Event.html "class in com.google.adk.events") baseEventForLlmResponse, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") llmResponse, io.opentelemetry.context.Context parentContext)`

Post-processes the LLM response after receiving it from the LLM.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

`[run](BaseLlmFlow.html#run\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the full LLM flow by repeatedly calling `BaseLlmFlow.runOneStep(Context, InvocationContext)` until a final response is produced.

`io.reactivex.rxjava3.core.Flowable<[Event](../../events/Event.html "class in com.google.adk.events")>`

`[runLive](BaseLlmFlow.html#runLive\(com.google.adk.agents.InvocationContext\))([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Executes the LLM flow in streaming mode.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### AutoFlow

public AutoFlow()

    * ### AutoFlow

public AutoFlow([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> maxSteps)




* * *

Copyright (C) 1980\. All rights reserved.
