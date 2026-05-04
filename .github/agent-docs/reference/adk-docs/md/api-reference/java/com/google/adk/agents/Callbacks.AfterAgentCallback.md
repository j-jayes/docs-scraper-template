JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Callbacks.AfterAgentCallback.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [Callbacks](Callbacks.html)
  3. [AfterAgentCallback](Callbacks.AfterAgentCallback.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. call(CallbackContext)

Hide sidebar  Show sidebar

# Interface Callbacks.AfterAgentCallback

Enclosing class:
    `[Callbacks](Callbacks.html "class in com.google.adk.agents")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "annotation interface in java.lang") public static interface Callbacks.AfterAgentCallback

Async callback interface for actions to be performed after an agent has finished running.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content>`

`call([CallbackContext](CallbackContext.html "class in com.google.adk.agents") callbackContext)`

Async callback after agent runs.




  * ## Method Details

    * ### call

io.reactivex.rxjava3.core.Maybe<com.google.genai.types.Content> call([CallbackContext](CallbackContext.html "class in com.google.adk.agents") callbackContext)

Async callback after agent runs.

Parameters:
    `callbackContext` \- Callback context.
Returns:
    modified content, or empty to keep original.




* * *

Copyright (C) 1980\. All rights reserved.
