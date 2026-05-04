JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Package
  * [Use](package-use.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](package-summary.html)



Contents

  1. Description
  2. Related Packages
  3. Classes and Interfaces

Hide sidebar  Show sidebar

# Package com.google.adk.planner.goap

* * *

package com.google.adk.planner.goap

  * Related Packages

Package

Description

[com.google.adk.planner](../package-summary.html)

 

[com.google.adk.planner.p2p](../p2p/package-summary.html)

 

  * All Classes and InterfacesInterfacesClassesRecord Classes

Class

Description

[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")

Declares what state keys an agent reads (inputs) and writes (output).

[AStarSearchStrategy](AStarSearchStrategy.html "class in com.google.adk.planner.goap")

A* forward search strategy that explores from preconditions toward the goal, activating agents whose inputs are all satisfied.

[DependencyGraphSearch](DependencyGraphSearch.html "class in com.google.adk.planner.goap")

Performs a topological search on the dependency graph to find the ordered list of agents that must execute to produce a goal output, given a set of initial preconditions (state keys already available).

[DfsSearchStrategy](DfsSearchStrategy.html "class in com.google.adk.planner.goap")

Backward-chaining DFS search strategy with parallel grouping.

[GoalOrientedPlanner](GoalOrientedPlanner.html "class in com.google.adk.planner.goap")

A planner that resolves agent execution order based on input/output dependencies and a target goal (output key).

[GoalOrientedSearchGraph](GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap")

Transforms [`AgentMetadata`](AgentMetadata.html "class in com.google.adk.planner.goap") into a dependency graph where: Each output key maps to the agent that produces it Each output key maps to the input keys (dependencies) required to produce it 

[ReplanPolicy](ReplanPolicy.html "interface in com.google.adk.planner.goap")

Policy governing how the planner reacts to missing expected outputs after an agent group executes.

[ReplanPolicy.FailStop](ReplanPolicy.FailStop.html "class in com.google.adk.planner.goap")

Stop immediately on failure with an error message.

[ReplanPolicy.Ignore](ReplanPolicy.Ignore.html "class in com.google.adk.planner.goap")

Ignore failures and proceed with the remaining plan as-is.

[ReplanPolicy.Replan](ReplanPolicy.Replan.html "class in com.google.adk.planner.goap")

Attempt to recompute the remaining plan from current world state.

[SearchStrategy](SearchStrategy.html "interface in com.google.adk.planner.goap")

Strategy for searching a dependency graph to find ordered agent execution groups.




* * *

Copyright (C) 1980\. All rights reserved.
