JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AgentExecutor.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.a2a.executor](package-summary.html)
  2. [AgentExecutor](AgentExecutor.html)



Contents  

  1. Description
  2. Nested Class Summary
  3. Method Summary
  4. Method Details
     1. cancel(RequestContext, EventQueue)
     2. execute(RequestContext, EventQueue)

Hide sidebar  Show sidebar

# Class AgentExecutor

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.a2a.executor.AgentExecutor

All Implemented Interfaces:
    `io.a2a.server.agentexecution.AgentExecutor`

* * *

public class AgentExecutor extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements io.a2a.server.agentexecution.AgentExecutor

Implementation of the A2A AgentExecutor interface that uses ADK to execute agent tasks.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[AgentExecutor.Builder](AgentExecutor.Builder.html "class in com.google.adk.a2a.executor")`

Builder for [`AgentExecutor`](AgentExecutor.html "class in com.google.adk.a2a.executor").

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`void`

`cancel(io.a2a.server.agentexecution.RequestContext ctx, io.a2a.server.events.EventQueue eventQueue)`

 

`void`

`execute(io.a2a.server.agentexecution.RequestContext ctx, io.a2a.server.events.EventQueue eventQueue)`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### cancel

public void cancel(io.a2a.server.agentexecution.RequestContext ctx, io.a2a.server.events.EventQueue eventQueue)

Specified by:
    `cancel` in interface `io.a2a.server.agentexecution.AgentExecutor`

    * ### execute

public void execute(io.a2a.server.agentexecution.RequestContext ctx, io.a2a.server.events.EventQueue eventQueue)

Specified by:
    `execute` in interface `io.a2a.server.agentexecution.AgentExecutor`




* * *

Copyright (C) 1980\. All rights reserved.
