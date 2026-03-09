JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/A2ASendMessageExecutor.AgentExecutionStrategy.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.a2a](package-summary.html)
  2. [A2ASendMessageExecutor](A2ASendMessageExecutor.html)
  3. [AgentExecutionStrategy](A2ASendMessageExecutor.AgentExecutionStrategy.html)



Contents 

  1. Description
  2. Method Summary
  3. Method Details
     1. execute(String, String, Content, RunConfig, String)

Hide sidebar  Show sidebar

# Interface A2ASendMessageExecutor.AgentExecutionStrategy

Enclosing class:
    `[A2ASendMessageExecutor](A2ASendMessageExecutor.html "class in com.google.adk.a2a")`

Functional Interface:
    This is a functional interface and can therefore be used as the assignment target for a lambda expression or method reference.

* * *

[@FunctionalInterface](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html "class or interface in java.lang") public static interface A2ASendMessageExecutor.AgentExecutionStrategy

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Event](../events/Event.html "class in com.google.adk.events")>>`

`execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content userContent, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)`

 




  * ## Method Details

    * ### execute

io.reactivex.rxjava3.core.Single<com.google.common.collect.ImmutableList<[Event](../events/Event.html "class in com.google.adk.events")>> execute([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") userId, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") sessionId, com.google.genai.types.Content userContent, [RunConfig](../agents/RunConfig.html "class in com.google.adk.agents") runConfig, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") invocationId)




* * *

Copyright (C) 1980\. All rights reserved.
