JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/Callbacks.BeforeExecuteCallback.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.a2a.executor](package-summary.html)
  2. [Callbacks](Callbacks.html)
  3. [BeforeExecuteCallback](Callbacks.BeforeExecuteCallback.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. call(RequestContext)

Hide sidebar  Show sidebar

# Interface Callbacks.BeforeExecuteCallback

Enclosing class:
    `[Callbacks](Callbacks.html "class in com.google.adk.a2a.executor")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "annotation interface in java.lang") public static interface Callbacks.BeforeExecuteCallback

Async callback interface for actions to be performed before an execution is started.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")>`

`call(io.a2a.server.agentexecution.RequestContext ctx)`

Callback which will be called before an execution is started.




  * ## Method Details

    * ### call

io.reactivex.rxjava3.core.Single<[Boolean](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Boolean.html "class in java.lang")> call(io.a2a.server.agentexecution.RequestContext ctx)

Callback which will be called before an execution is started. It can be used to instrument a context or prevent the execution by returning an error.

Parameters:
    `ctx` \- the request context
Returns:
    a `Single` that completes with a boolean indicating whether the execution should be prevented




* * *

Copyright (C) 1980\. All rights reserved.
