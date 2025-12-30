JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Callbacks.BeforeAgentCallback.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.agents](package-summary.html)
  2. [Callbacks](Callbacks.html)
  3. [BeforeAgentCallback](Callbacks.BeforeAgentCallback.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. call(CallbackContext)



# Interface Callbacks.BeforeAgentCallback

Enclosing class:
    `[Callbacks](Callbacks.html "class in com.google.adk.agents")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "class or interface in java.lang") public static interface Callbacks.BeforeAgentCallback

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`call([CallbackContext](CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Async callback before agent runs.




  * ## Method Details

    * ### call

io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> call([CallbackContext](CallbackContext.html "class in com.google.adk.agents") callbackContext)

Async callback before agent runs.

Parameters:
    `callbackContext` \- Callback context.
Returns:
    content override, or empty to continue.




* * *

Copyright (C) 2025\. All rights reserved.
