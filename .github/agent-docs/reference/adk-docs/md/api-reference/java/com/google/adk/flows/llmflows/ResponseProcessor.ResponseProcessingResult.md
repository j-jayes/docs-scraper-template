JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ResponseProcessor.ResponseProcessingResult.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.flows.llmflows](package-summary.html)
  2. [ResponseProcessor](ResponseProcessor.html)
  3. [ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ResponseProcessingResult()
  5. Method Details
     1. updatedResponse()
     2. events()
     3. transferToAgent()
     4. create(LlmResponse, Iterable, String)
     5. create(LlmResponse, Iterable)

Hide sidebar  Show sidebar

# Class ResponseProcessor.ResponseProcessingResult

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.flows.llmflows.ResponseProcessor.ResponseProcessingResult

Enclosing interface:
    `[ResponseProcessor](ResponseProcessor.html "interface in com.google.adk.flows.llmflows")`

* * *

public abstract static class ResponseProcessor.ResponseProcessingResult extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Result of response processing.

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

`create([LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events)`

 

`static [ResponseProcessor.ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows")`

`create([LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") transferToAgent)`

 

`abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")>`

`events()`

Events generated during processing.

`abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`transferToAgent()`

The agent to transfer to.

`abstract [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models")`

`updatedResponse()`

Updated LLM response.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### ResponseProcessingResult

public ResponseProcessingResult()

  * ## Method Details

    * ### updatedResponse

public abstract [LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse()

Updated LLM response. 

This is the LLM response that will be returned to the client.

    * ### events

public abstract [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events()

Events generated during processing. 

These events are not necessarily part of the LLM response.

    * ### transferToAgent

public abstract [Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> transferToAgent()

The agent to transfer to. 

If present, the invocation will be transferred to the specified agent.

    * ### create

public static [ResponseProcessor.ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows") create([LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") transferToAgent)

    * ### create

public static [ResponseProcessor.ResponseProcessingResult](ResponseProcessor.ResponseProcessingResult.html "class in com.google.adk.flows.llmflows") create([LlmResponse](../../models/LlmResponse.html "class in com.google.adk.models") updatedResponse, [Iterable](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Iterable.html "interface in java.lang")<[Event](../../events/Event.html "class in com.google.adk.events")> events)




* * *

Copyright (C) 1980\. All rights reserved.
