JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/Callbacks.AfterExecuteCallback.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.a2a.executor](package-summary.html)
  2. [Callbacks](Callbacks.html)
  3. [AfterExecuteCallback](Callbacks.AfterExecuteCallback.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. call(RequestContext, TaskStatusUpdateEvent)

Hide sidebar  Show sidebar

# Interface Callbacks.AfterExecuteCallback

Enclosing class:
    `[Callbacks](Callbacks.html "class in com.google.adk.a2a.executor")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "class or interface in java.lang") public static interface Callbacks.AfterExecuteCallback

Async callback interface for actions to be performed after an execution is completed or failed.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<io.a2a.spec.TaskStatusUpdateEvent>`

`call(io.a2a.server.agentexecution.RequestContext ctx, io.a2a.spec.TaskStatusUpdateEvent finalUpdateEvent)`

Callback which will be called after an execution resolved into a completed or failed task.




  * ## Method Details

    * ### call

io.reactivex.rxjava3.core.Maybe<io.a2a.spec.TaskStatusUpdateEvent> call(io.a2a.server.agentexecution.RequestContext ctx, io.a2a.spec.TaskStatusUpdateEvent finalUpdateEvent)

Callback which will be called after an execution resolved into a completed or failed task. This gives an opportunity to enrich the event with additional metadata or log it.

Parameters:
    `ctx` \- the request context
    `finalUpdateEvent` \- the final update event
Returns:
    a `Maybe` that completes when the callback is done




* * *

Copyright (C) 1980\. All rights reserved.
