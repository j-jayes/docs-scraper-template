JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/RequestProcessor.RequestProcessingResult.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [RequestProcessor](RequestProcessor.html)
  3. [RequestProcessingResult](RequestProcessor.RequestProcessingResult.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. RequestProcessingResult()
  5. Method Details
     1. updatedRequest()
     2. events()
     3. create(LlmRequest, Iterable)



# Class RequestProcessor.RequestProcessingResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.flows.llmflows.RequestProcessor.RequestProcessingResult

Enclosing interface:
    `[RequestProcessor](RequestProcessor.html "interface in com.google.adk.flows.llmflows")`

* * *

public abstract static class RequestProcessor.RequestProcessingResult extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

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

`create([LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") updatedRequest, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events)`

 

`abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")>`

`events()`

 

`abstract [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models")`

`updatedRequest()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### RequestProcessingResult

public RequestProcessingResult()

  * ## Method Details

    * ### updatedRequest

public abstract [LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") updatedRequest()

    * ### events

public abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events()

    * ### create

public static [RequestProcessor.RequestProcessingResult](RequestProcessor.RequestProcessingResult.html "class in com.google.adk.flows.llmflows") create([LlmRequest](../../models/LlmRequest.html "class in com.google.adk.models") updatedRequest, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events)




* * *

Copyright (C) 2025\. All rights reserved.
