JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/Basic.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [Basic](Basic.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Basic()
  6. Method Details
     1. processRequest(InvocationContext, LlmRequest)



# Class Basic

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.flows.llmflows.Basic

All Implemented Interfaces:
    `[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")`

* * *

public final class Basic extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang") implements [RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")

[`RequestProcessor`](RequestProcessor.html "interface in com.google.adk.flows.llmflows") that handles basic information to build the LLM request.

  * ## Nested Class Summary

### Nested classes/interfaces inherited from interface com.google.adk.flows.llmflows.[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")

`[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

  * ## Constructor Summary

Constructors

Constructor

Description

`Basic()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

`processRequest([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

Process the LLM request as part of the pre-processing stage.

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### Basic

public Basic()

  * ## Method Details

    * ### processRequest

public io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")> processRequest([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)

Description copied from interface: `[RequestProcessor](RequestProcessor.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))`

Process the LLM request as part of the pre-processing stage.

Specified by:
    `[processRequest](RequestProcessor.html#processRequest\(com.google.adk.agents.InvocationContext,com.google.adk.models.LlmRequest\))` in interface `[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")`
Parameters:
    `context` \- the invocation context.
    `request` \- the LLM request to process.
Returns:
    a list of events generated during processing (if any).




* * *

Copyright (C) 2025\. All rights reserved.
