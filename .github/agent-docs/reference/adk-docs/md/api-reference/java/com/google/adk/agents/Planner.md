JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/Planner.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [Planner](Planner.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. init(PlanningContext)
     2. firstAction(PlanningContext)
     3. nextAction(PlanningContext)

Hide sidebar  Show sidebar

# Interface Planner

All Known Implementing Classes:
    `[GoalOrientedPlanner](../planner/goap/GoalOrientedPlanner.html "class in com.google.adk.planner.goap"), [LoopPlanner](../planner/LoopPlanner.html "class in com.google.adk.planner"), [P2PPlanner](../planner/p2p/P2PPlanner.html "class in com.google.adk.planner.p2p"), [ParallelPlanner](../planner/ParallelPlanner.html "class in com.google.adk.planner"), [SequentialPlanner](../planner/SequentialPlanner.html "class in com.google.adk.planner"), [SupervisorPlanner](../planner/SupervisorPlanner.html "class in com.google.adk.planner")`

* * *

public interface Planner

Strategy interface for planning which sub-agent(s) to execute next. 

A `Planner` is used by [`PlannerAgent`](PlannerAgent.html "class in com.google.adk.agents") to dynamically determine execution order at runtime. The planning loop works as follows: 

  1. `init(PlanningContext)` is called once before the loop starts 
  2. `firstAction(PlanningContext)` returns the first action to execute 
  3. The selected agent(s) execute, producing events and updating session state 
  4. `nextAction(PlanningContext)` is called with updated context to decide what to do next 
  5. Steps 3-4 repeat until [`PlannerAction.Done`](PlannerAction.Done.html "class in com.google.adk.agents") or max iterations 


Returns `Single``<PlannerAction>` to support both synchronous planners (wrap in `Single.just()`) and asynchronous planners that call an LLM.

  * ## Method Summary

All MethodsInstance MethodsAbstract MethodsDefault Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[PlannerAction](PlannerAction.html "interface in com.google.adk.agents")>`

`firstAction([PlanningContext](PlanningContext.html "class in com.google.adk.agents") context)`

Select the first action to execute.

`default void`

`init([PlanningContext](PlanningContext.html "class in com.google.adk.agents") context)`

Initialize the planner with context and available agents.

`io.reactivex.rxjava3.core.Single<[PlannerAction](PlannerAction.html "interface in com.google.adk.agents")>`

`nextAction([PlanningContext](PlanningContext.html "class in com.google.adk.agents") context)`

Select the next action based on updated state and events.




  * ## Method Details

    * ### init

default void init([PlanningContext](PlanningContext.html "class in com.google.adk.agents") context)

Initialize the planner with context and available agents. Called once before the planning loop starts. 

Default implementation is a no-op. Override to perform setup like building dependency graphs.

    * ### firstAction

io.reactivex.rxjava3.core.Single<[PlannerAction](PlannerAction.html "interface in com.google.adk.agents")> firstAction([PlanningContext](PlanningContext.html "class in com.google.adk.agents") context)

Select the first action to execute.

    * ### nextAction

io.reactivex.rxjava3.core.Single<[PlannerAction](PlannerAction.html "interface in com.google.adk.agents")> nextAction([PlanningContext](PlanningContext.html "class in com.google.adk.agents") context)

Select the next action based on updated state and events.




* * *

Copyright (C) 1980\. All rights reserved.
