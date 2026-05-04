JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/Callbacks.AfterEventCallback.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.a2a.executor](package-summary.html)
  2. [Callbacks](Callbacks.html)
  3. [AfterEventCallback](Callbacks.AfterEventCallback.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. call(RequestContext, TaskArtifactUpdateEvent, Event)

Hide sidebar  Show sidebar

# Interface Callbacks.AfterEventCallback

Enclosing class:
    `[Callbacks](Callbacks.html "class in com.google.adk.a2a.executor")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "annotation interface in java.lang") public static interface Callbacks.AfterEventCallback

Async callback interface for actions to be performed after an event is processed.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Maybe<io.a2a.spec.TaskArtifactUpdateEvent>`

`call(io.a2a.server.agentexecution.RequestContext ctx, io.a2a.spec.TaskArtifactUpdateEvent processedEvent, [Event](../../events/Event.html "class in com.google.adk.events") event)`

Callback which will be called after an ADK event is successfully converted to an A2A event.




  * ## Method Details

    * ### call

io.reactivex.rxjava3.core.Maybe<io.a2a.spec.TaskArtifactUpdateEvent> call(io.a2a.server.agentexecution.RequestContext ctx, io.a2a.spec.TaskArtifactUpdateEvent processedEvent, [Event](../../events/Event.html "class in com.google.adk.events") event)

Callback which will be called after an ADK event is successfully converted to an A2A event. This gives an opportunity to enrich the event with additional metadata or abort the execution by returning an error. The callback is not invoked for errors originating from ADK or event processing.

Parameters:
    `ctx` \- the request context
    `processedEvent` \- the processed task artifact update event
    `event` \- the ADK event
Returns:
    a `Maybe` that completes when the callback is done




* * *

Copyright (C) 1980\. All rights reserved.
