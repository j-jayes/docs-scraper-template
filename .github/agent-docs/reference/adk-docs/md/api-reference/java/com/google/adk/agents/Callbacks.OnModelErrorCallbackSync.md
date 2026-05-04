JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Callbacks.OnModelErrorCallbackSync.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [Callbacks](Callbacks.html)
  3. [OnModelErrorCallbackSync](Callbacks.OnModelErrorCallbackSync.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. call(CallbackContext, LlmRequest, Exception)

Hide sidebar  Show sidebar

# Interface Callbacks.OnModelErrorCallbackSync

Enclosing class:
    `[Callbacks](Callbacks.html "class in com.google.adk.agents")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "annotation interface in java.lang") public static interface Callbacks.OnModelErrorCallbackSync

Helper interface to allow for sync onModelErrorCallback. The function is wrapped into an async one before being processed further.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")>`

`call([CallbackContext](CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)`

 




  * ## Method Details

    * ### call

[Optional](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Optional.html "class in java.util")<[LlmResponse](../models/LlmResponse.html "class in com.google.adk.models")> call([CallbackContext](CallbackContext.html "class in com.google.adk.agents") callbackContext, [LlmRequest](../models/LlmRequest.html "class in com.google.adk.models") llmRequest, [Exception](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Exception.html "class in java.lang") error)




* * *

Copyright (C) 1980\. All rights reserved.
