JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/SingleFlow.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [SingleFlow](SingleFlow.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Field Summary
  3. Constructor Summary
  4. Method Summary
  5. Field Details
     1. REQUEST_PROCESSORS
     2. RESPONSE_PROCESSORS
  6. Constructor Details
     1. SingleFlow()
     2. SingleFlow(Optional)
     3. SingleFlow(List, List, Optional)



# Class SingleFlow

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

[com.google.adk.flows.llmflows.BaseLlmFlow](BaseLlmFlow.html "class in com.google.adk.flows.llmflows")

com.google.adk.flows.llmflows.SingleFlow

All Implemented Interfaces:
    `[BaseFlow](../BaseFlow.html "interface in com.google.adk.flows")`

Direct Known Subclasses:
    `[AutoFlow](AutoFlow.html "class in com.google.adk.flows.llmflows")`

* * *

public class SingleFlow extends [BaseLlmFlow](BaseLlmFlow.html "class in com.google.adk.flows.llmflows")

Basic LLM flow with fixed request processors and no response post-processing.

  * ## Field Summary

Fields

Modifier and Type

Field

Description

`protected static final com.google.common.collect.ImmutableList<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")>`

`REQUEST_PROCESSORS`

 

`protected static final com.google.common.collect.ImmutableList<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")>`

`RESPONSE_PROCESSORS`

 

### Fields inherited from class com.google.adk.flows.llmflows.[BaseLlmFlow](BaseLlmFlow.html "class in com.google.adk.flows.llmflows")

`[maxSteps](BaseLlmFlow.html#maxSteps), [requestProcessors](BaseLlmFlow.html#requestProcessors), [responseProcessors](BaseLlmFlow.html#responseProcessors), [stepsCompleted](BaseLlmFlow.html#stepsCompleted)`

  * ## Constructor Summary

Constructors

Modifier

Constructor

Description

` `

`SingleFlow()`

 

`protected `

`SingleFlow([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")> requestProcessors, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> responseProcessors, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxSteps)`

 

` `

`SingleFlow([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxSteps)`

 

  * ## Method Summary

### Methods inherited from class com.google.adk.flows.llmflows.[BaseLlmFlow](BaseLlmFlow.html "class in com.google.adk.flows.llmflows")

`[postprocess](BaseLlmFlow.html#postprocess\(com.google.adk.agents.InvocationContext,com.google.adk.events.Event,com.google.adk.models.LlmRequest,com.google.adk.models.LlmResponse\)), [preprocess](BaseLlmFlow.html#preprocess\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\)), [run](BaseLlmFlow.html#run\(com.google.adk.agents.InvocationContext\)), [runLive](BaseLlmFlow.html#runLive\(com.google.adk.agents.InvocationContext\))`

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Field Details

    * ### REQUEST_PROCESSORS

protected static final com.google.common.collect.ImmutableList<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")> REQUEST_PROCESSORS

    * ### RESPONSE_PROCESSORS

protected static final com.google.common.collect.ImmutableList<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> RESPONSE_PROCESSORS

  * ## Constructor Details

    * ### SingleFlow

public SingleFlow()

    * ### SingleFlow

public SingleFlow([Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxSteps)

    * ### SingleFlow

protected SingleFlow([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")> requestProcessors, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "class or interface in java.util")<[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")> responseProcessors, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class or interface in java.lang")> maxSteps)




* * *

Copyright (C) 2025\. All rights reserved.
