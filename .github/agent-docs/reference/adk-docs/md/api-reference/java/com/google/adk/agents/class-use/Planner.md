JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Planner.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](../package-summary.html)
  2. [Planner](../Planner.html)



# Uses of Interface  
com.google.adk.agents.Planner

Packages that use [Planner](../Planner.html "interface in com.google.adk.agents")

Package

Description

com.google.adk.agents

 

com.google.adk.planner

 

com.google.adk.planner.goap

 

com.google.adk.planner.p2p

 

  * ## Uses of [Planner](../Planner.html "interface in com.google.adk.agents") in [com.google.adk.agents](../package-summary.html)

Methods in [com.google.adk.agents](../package-summary.html) that return [Planner](../Planner.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[Planner](../Planner.html "interface in com.google.adk.agents")`

PlannerAgent.`[planner](../PlannerAgent.html#planner\(\))()`

Returns the planner strategy used by this agent.

Methods in [com.google.adk.agents](../package-summary.html) with parameters of type [Planner](../Planner.html "interface in com.google.adk.agents")

Modifier and Type

Method

Description

`[PlannerAgent.Builder](../PlannerAgent.Builder.html "class in com.google.adk.agents")`

PlannerAgent.Builder.`[planner](../PlannerAgent.Builder.html#planner\(com.google.adk.agents.Planner\))([Planner](../Planner.html "interface in com.google.adk.agents") planner)`

 

  * ## Uses of [Planner](../Planner.html "interface in com.google.adk.agents") in [com.google.adk.planner](../../planner/package-summary.html)

Classes in [com.google.adk.planner](../../planner/package-summary.html) that implement [Planner](../Planner.html "interface in com.google.adk.agents")

Modifier and Type

Class

Description

`final class `

`[LoopPlanner](../../planner/LoopPlanner.html "class in com.google.adk.planner")`

A planner that cycles through sub-agents repeatedly, stopping when an escalate event is detected or the maximum number of cycles is reached.

`final class `

`[ParallelPlanner](../../planner/ParallelPlanner.html "class in com.google.adk.planner")`

A planner that runs all sub-agents in parallel, then completes.

`final class `

`[SequentialPlanner](../../planner/SequentialPlanner.html "class in com.google.adk.planner")`

A planner that runs sub-agents one at a time in order.

`final class `

`[SupervisorPlanner](../../planner/SupervisorPlanner.html "class in com.google.adk.planner")`

A planner that uses an LLM to dynamically decide which sub-agent(s) to run next.

  * ## Uses of [Planner](../Planner.html "interface in com.google.adk.agents") in [com.google.adk.planner.goap](../../planner/goap/package-summary.html)

Classes in [com.google.adk.planner.goap](../../planner/goap/package-summary.html) that implement [Planner](../Planner.html "interface in com.google.adk.agents")

Modifier and Type

Class

Description

`final class `

`[GoalOrientedPlanner](../../planner/goap/GoalOrientedPlanner.html "class in com.google.adk.planner.goap")`

A planner that resolves agent execution order based on input/output dependencies and a target goal (output key).

  * ## Uses of [Planner](../Planner.html "interface in com.google.adk.agents") in [com.google.adk.planner.p2p](../../planner/p2p/package-summary.html)

Classes in [com.google.adk.planner.p2p](../../planner/p2p/package-summary.html) that implement [Planner](../Planner.html "interface in com.google.adk.agents")

Modifier and Type

Class

Description

`final class `

`[P2PPlanner](../../planner/p2p/P2PPlanner.html "class in com.google.adk.planner.p2p")`

A peer-to-peer planner where agents activate dynamically as their input dependencies become available in session state.




* * *

Copyright (C) 1980\. All rights reserved.
