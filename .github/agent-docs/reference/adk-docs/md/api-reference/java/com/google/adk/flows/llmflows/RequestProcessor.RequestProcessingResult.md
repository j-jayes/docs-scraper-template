JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/RequestProcessor.RequestProcessingResult.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [RequestProcessor](RequestProcessor.html)
  3. [RequestProcessingResult](RequestProcessor.RequestProcessingResult.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. RequestProcessingResult()
  5. Method Details
     1. updatedRequest()
     2. events()
     3. create(LlmRequest, Iterable)

Hide sidebar  Show sidebar

# Class RequestProcessor.RequestProcessingResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.flows.llmflows.RequestProcessor.RequestProcessingResult

Enclosing interface:
    `[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")`

* * *

public abstract static class RequestProcessor.RequestProcessingResult extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Result of request processing.

  * ## Constructor Summary

Constructors

Constructor

Description

`RequestProcessingResult()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows")`

`create([LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") updatedRequest, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events)`

Creates a new [`RequestProcessor.RequestProcessingResult`](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows").

`abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")>`

`events()`

Events generated during processing.

`abstract [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models")`

`updatedRequest()`

Updated LLM request.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### RequestProcessingResult

public RequestProcessingResult()

  * ## Method Details

    * ### updatedRequest

public abstract [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") updatedRequest()

Updated LLM request. 

This is the LLM request that will be used to generate the LLM response.

    * ### events

public abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events()

Events generated during processing. 

These events are not necessarily part of the LLM request.

    * ### create

public static [RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows") create([LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") updatedRequest, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events)

Creates a new [`RequestProcessor.RequestProcessingResult`](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows").




* * *

Copyright (C) 1980\. All rights reserved.
