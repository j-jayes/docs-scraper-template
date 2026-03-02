JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Callbacks.OnModelErrorCallback.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [Callbacks](Callbacks.html)
  3. [OnModelErrorCallback](Callbacks.OnModelErrorCallback.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. call(CallbackContext, LlmRequest, Exception)

Hide sidebar  Show sidebar

# Interface Callbacks.OnModelErrorCallback

Enclosing class:
    `[Callbacks](Callbacks.html "class in com.google.adk.agents")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "class or interface in java.lang") public static interface Callbacks.OnModelErrorCallback

Async callback interface for handling errors that occur during an LLM model call.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`call([CallbackContext](CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang") error)`

Async callback when model call fails.




  * ## Method Details

    * ### call

io.reactivex.rxjava3.core.Maybe<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> call([CallbackContext](CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class or interface in java.lang") error)

Async callback when model call fails.

Parameters:
    `callbackContext` \- Callback context.
    `llmRequest` \- LLM request.
    `error` \- The exception that occurred.
Returns:
    response override, or empty to continue with error.




* * *

Copyright (C) 1980\. All rights reserved.
