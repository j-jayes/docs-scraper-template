JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ResponseProcessor.ResponseProcessingResult.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [ResponseProcessor](ResponseProcessor.html)
  3. [ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ResponseProcessingResult()
  5. Method Details
     1. updatedResponse()
     2. events()
     3. transferToAgent()
     4. create(LlmResponse, Iterable, Optional)



# Class ResponseProcessor.ResponseProcessingResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.flows.llmflows.ResponseProcessor.ResponseProcessingResult

Enclosing interface:
    `[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")`

* * *

public abstract static class ResponseProcessor.ResponseProcessingResult extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

  * ## Constructor Summary

Constructors

Constructor

Description

`ResponseProcessingResult()`

 

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsAbstract MethodsConcrete Methods

Modifier and Type

Method

Description

`static [ResponseProcessor.ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

`create([LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> transferToAgent)`

 

`abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")>`

`events()`

 

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")>`

`transferToAgent()`

 

`abstract [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")`

`updatedResponse()`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### ResponseProcessingResult

public ResponseProcessingResult()

  * ## Method Details

    * ### updatedResponse

public abstract [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse()

    * ### events

public abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events()

    * ### transferToAgent

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> transferToAgent()

    * ### create

public static [ResponseProcessor.ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows") create([LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "class or interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events, [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang")> transferToAgent)




* * *

Copyright (C) 2025\. All rights reserved.
