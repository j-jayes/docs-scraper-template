JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/Identity.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [Identity](Identity.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. Identity()
  6. Method Details
     1. processRequest(InvocationContext, LlmRequest)

Hide sidebar  Show sidebar

# Class Identity

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.flows.llmflows.Identity

All Implemented Interfaces:
    `[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")`

* * *

public final class Identity extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")

[`RequestProcessor`](RequestProcessor.html "interface in com.google.adk.flows.llmflows") that gives the agent identity from the framework

  * ## Nested Class Summary

### Nested classes/interfaces inherited from interface [RequestProcessor](RequestProcessor.html#nested-class-summary "interface in com.google.adk.flows.llmflows")

`[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

Modifier and Type

Interface

Description

`static class `

`[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

Result of request processing.

  * ## Constructor Summary

Constructors

Constructor

Description

`Identity()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")>`

`processRequest([InvocationContext](../../agents/InvocationContext.html "class in com.google.adk.agents") context, [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") request)`

Process the LLM request as part of the pre-processing stage.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### Identity

public Identity()

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

Copyright (C) 1980\. All rights reserved.
