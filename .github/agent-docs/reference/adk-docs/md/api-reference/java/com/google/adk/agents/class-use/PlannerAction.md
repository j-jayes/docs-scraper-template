JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../PlannerAction.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](../package-summary.html)
  2. [PlannerAction](../PlannerAction.html)



# Uses of Interface  
com.google.adk.agents.PlannerAction

Packages that use [PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.planner

 

com.google.adk.planner.goap

 

com.google.adk.planner.p2p

 

  * ## Uses of [PlannerAction](../PlannerAction.html "interface in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Classes in [com.google.adk.agents](../package-summary.html) that implement [PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")

Modifier and Type

Class

Description

`static final record `

`[PlannerAction.Done](../PlannerAction.Done.html "class in com.google.adk.agents")`

Plan is complete, no result to emit.

`static final record `

`[PlannerAction.DoneWithResult](../PlannerAction.DoneWithResult.html "class in com.google.adk.agents")`

Plan is complete with a final text result.

`static final record `

`[PlannerAction.NoOp](../PlannerAction.NoOp.html "class in com.google.adk.agents")`

Skip this iteration (no-op).

`static final record `

`[PlannerAction.RunAgents](../PlannerAction.RunAgents.html "class in com.google.adk.agents")`

Run the specified sub-agent(s).

Methods in [com.google.adk.agents](../package-summary.html) that return types with arguments of type [PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

Planner.`[firstAction](../Planner.html#firstAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

Select the first action to execute.

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

Planner.`[nextAction](../Planner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

Select the next action based on updated state and events.

  * ## Uses of [PlannerAction](../PlannerAction.html "interface in com.google.adk.agents") in [com.google.adk.planner](../../planner/package-summary.html)

Methods in [com.google.adk.planner](../../planner/package-summary.html) that return types with arguments of type [PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")

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

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

LoopPlanner.`[nextAction](../../planner/LoopPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

ParallelPlanner.`[nextAction](../../planner/ParallelPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

SequentialPlanner.`[nextAction](../../planner/SequentialPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

SupervisorPlanner.`[nextAction](../../planner/SupervisorPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

  * ## Uses of [PlannerAction](../PlannerAction.html "interface in com.google.adk.agents") in [com.google.adk.planner.goap](../../planner/goap/package-summary.html)

Methods in [com.google.adk.planner.goap](../../planner/goap/package-summary.html) that return types with arguments of type [PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

GoalOrientedPlanner.`[firstAction](../../planner/goap/GoalOrientedPlanner.html#firstAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

GoalOrientedPlanner.`[nextAction](../../planner/goap/GoalOrientedPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

  * ## Uses of [PlannerAction](../PlannerAction.html "interface in com.google.adk.agents") in [com.google.adk.planner.p2p](../../planner/p2p/package-summary.html)

Methods in [com.google.adk.planner.p2p](../../planner/p2p/package-summary.html) that return types with arguments of type [PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

P2PPlanner.`[firstAction](../../planner/p2p/P2PPlanner.html#firstAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 

`io.reactivex.rxjava3.core.Single<[PlannerAction](../PlannerAction.html "interface in com.google.adk.agents")>`

P2PPlanner.`[nextAction](../../planner/p2p/P2PPlanner.html#nextAction\(com.google.adk.agents.PlanningContext\))([PlanningContext](../PlanningContext.html "class in com.google.adk.agents") context)`

 




* * *

Copyright (C) 1980\. All rights reserved.
