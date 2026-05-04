JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/ParallelPlanner.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner](package-summary.html)
  2. [ParallelPlanner](ParallelPlanner.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. ParallelPlanner()
  5. Method Details
     1. firstAction(PlanningContext)
     2. nextAction(PlanningContext)

Hide sidebar  Show sidebar

# Class ParallelPlanner

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.planner.ParallelPlanner

All Implemented Interfaces:
    `[Planner](../agents/Planner.html "interface in com.google.adk.agents")`

* * *

public final class ParallelPlanner extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [Planner](../agents/Planner.html "interface in com.google.adk.agents")

A planner that runs all sub-agents in parallel, then completes.

  * ## Constructor Summary

Constructors

Constructor

Description

`ParallelPlanner()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[PlannerAction](../agents/PlannerAction.html "interface in com.google.adk.agents")>`

`firstAction([PlanningContext](../agents/PlanningContext.html "class in com.google.adk.agents") context)`

Select the first action to execute.

`io.reactivex.rxjava3.core.Single<[PlannerAction](../agents/PlannerAction.html "interface in com.google.adk.agents")>`

`nextAction([PlanningContext](../agents/PlanningContext.html "class in com.google.adk.agents") context)`

Select the next action based on updated state and events.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`

### Methods inherited from interface [Planner](../agents/Planner.html#method-summary "interface in com.google.adk.agents")

`[init](../agents/Planner.html#init\(com.google.adk.agents.PlanningContext\) "init\(PlanningContext\)")`

Modifier and Type

Method

Description

`default void`

`[init](../agents/Planner.html#init\(com.google.adk.agents.PlanningContext\))([PlanningContext](../agents/PlanningContext.html "class in com.google.adk.agents") context)`

Initialize the planner with context and available agents.




  * ## Constructor Details

    * ### ParallelPlanner

public ParallelPlanner()

  * ## Method Details

    * ### firstAction

public io.reactivex.rxjava3.core.Single<[PlannerAction](../agents/PlannerAction.html "interface in com.google.adk.agents")> firstAction([PlanningContext](../agents/PlanningContext.html "class in com.google.adk.agents") context)

Description copied from interface: `[Planner](../agents/Planner.html#firstAction\(com.google.adk.agents.PlanningContext\))`

Select the first action to execute.

Specified by:
    `[firstAction](../agents/Planner.html#firstAction\(com.google.adk.agents.PlanningContext\))` in interface `[Planner](../agents/Planner.html "interface in com.google.adk.agents")`

    * ### nextAction

public io.reactivex.rxjava3.core.Single<[PlannerAction](../agents/PlannerAction.html "interface in com.google.adk.agents")> nextAction([PlanningContext](../agents/PlanningContext.html "class in com.google.adk.agents") context)

Description copied from interface: `[Planner](../agents/Planner.html#nextAction\(com.google.adk.agents.PlanningContext\))`

Select the next action based on updated state and events.

Specified by:
    `[nextAction](../agents/Planner.html#nextAction\(com.google.adk.agents.PlanningContext\))` in interface `[Planner](../agents/Planner.html "interface in com.google.adk.agents")`




* * *

Copyright (C) 1980\. All rights reserved.
