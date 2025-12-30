JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/BaseFlow.html)
  * [Tree](package-tree.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)



  1. [com.google.adk.flows](package-summary.html)
  2. [BaseFlow](BaseFlow.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Method Summary
  3. Method Details
     1. run(InvocationContext)
     2. runLive(InvocationContext)



# Interface BaseFlow

All Known Implementing Classes:
    `[AutoFlow](llmflows/AutoFlow.html "class in com.google.adk.flows.llmflows")`, `[BaseLlmFlow](llmflows/BaseLlmFlow.html "class in com.google.adk.flows.llmflows")`, `[SingleFlow](llmflows/SingleFlow.html "class in com.google.adk.flows.llmflows")`

* * *

public interface BaseFlow

Interface for the execution flows to run a group of agents.

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsDefault Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`run([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

Run this flow.

`default io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")>`

`runLive([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)`

 




  * ## Method Details

    * ### run

io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> run([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)

Run this flow. 

To implement this method, the flow should follow the below requirements: 
      1. 1\. `session` should be treated as immutable, DO NOT change it. 
      2. 2\. The caller who trigger the flow is responsible for updating the session as the events being generated. The subclass implementation will assume session is updated after each yield event statement. 
      3. 3\. A flow may spawn sub-agent flows depending on the agent definition. 

    * ### runLive

default io.reactivex.rxjava3.core.Flowable<[Event](../events/Event.html "class in com.google.adk.events")> runLive([InvocationContext](../agents/InvocationContext.html "class in com.google.adk.agents") invocationContext)




* * *

Copyright (C) 2025\. All rights reserved.
