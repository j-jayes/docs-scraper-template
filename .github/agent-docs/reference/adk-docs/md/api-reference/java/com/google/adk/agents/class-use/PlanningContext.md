JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../PlanningContext.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](../package-summary.html)
  2. [PlanningContext](../PlanningContext.html)



# Uses of Class  
com.google.adk.agents.PlanningContext

Packages that use [PlanningContext](../PlanningContext.html "class in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.planner

 

com.google.adk.planner.goap

 

com.google.adk.planner.p2p

 

  * ## Uses of [PlanningContext](../PlanningContext.html "class in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [PlanningContext](../PlanningContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

Planner.`[firstAction](../Planner.html#firstAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

Select the first action to execute.

`default void`

Planner.`[init](../Planner.html#init\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

Initialize the planner with context and available agents.

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

Planner.`[nextAction](../Planner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

Select the next action based on updated state and events.

  * ## Uses of [PlanningContext](../PlanningContext.html "class in com.google.adk.agents") in [com.google.adk.planner](../../planner/package-summary.html)

Methods in [com.google.adk.planner](../../planner/package-summary.html) with parameters of type [PlanningContext](../PlanningContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

LoopPlanner.`[firstAction](../../planner/LoopPlanner.html#firstAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

ParallelPlanner.`[firstAction](../../planner/ParallelPlanner.html#firstAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

SequentialPlanner.`[firstAction](../../planner/SequentialPlanner.html#firstAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

SupervisorPlanner.`[firstAction](../../planner/SupervisorPlanner.html#firstAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`void`

LoopPlanner.`[init](../../planner/LoopPlanner.html#init\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`void`

SequentialPlanner.`[init](../../planner/SequentialPlanner.html#init\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

LoopPlanner.`[nextAction](../../planner/LoopPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

ParallelPlanner.`[nextAction](../../planner/ParallelPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

SequentialPlanner.`[nextAction](../../planner/SequentialPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

SupervisorPlanner.`[nextAction](../../planner/SupervisorPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

  * ## Uses of [PlanningContext](../PlanningContext.html "class in com.google.adk.agents") in [com.google.adk.planner.goap](../../planner/goap/package-summary.html)

Methods in [com.google.adk.planner.goap](../../planner/goap/package-summary.html) with parameters of type [PlanningContext](../PlanningContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

GoalOrientedPlanner.`[firstAction](../../planner/goap/GoalOrientedPlanner.html#firstAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`void`

GoalOrientedPlanner.`[init](../../planner/goap/GoalOrientedPlanner.html#init\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

GoalOrientedPlanner.`[nextAction](../../planner/goap/GoalOrientedPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

  * ## Uses of [PlanningContext](../PlanningContext.html "class in com.google.adk.agents") in [com.google.adk.planner.p2p](../../planner/p2p/package-summary.html)

Methods in [com.google.adk.planner.p2p](../../planner/p2p/package-summary.html) with parameters of type [PlanningContext](../PlanningContext.html "class in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

P2PPlanner.`[firstAction](../../planner/p2p/P2PPlanner.html#firstAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`void`

P2PPlanner.`[init](../../planner/p2p/P2PPlanner.html#init\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

P2PPlanner.`[nextAction](../../planner/p2p/P2PPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 




* * *

Copyright (C) 1980\. All rights reserved.
