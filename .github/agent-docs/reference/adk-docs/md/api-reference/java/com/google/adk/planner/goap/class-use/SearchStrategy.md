JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../SearchStrategy.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](../package-summary.html)
  2. [SearchStrategy](../SearchStrategy.html)



# Uses of Interface  
com.google.adk.planner.goap.SearchStrategy

Packages that use [SearchStrategy](../SearchStrategy.html "interface in com.google.adk.planner.goap")

Package

Description

com.google.adk.planner.goap

 

  * ## Uses of [SearchStrategy](../SearchStrategy.html "interface in com.google.adk.planner.goap") in [com.google.adk.planner.goap](../package-summary.html)

Classes in [com.google.adk.planner.goap](../package-summary.html) that implement [SearchStrategy](../SearchStrategy.html "interface in com.google.adk.planner.goap")

Modifier and Type

Class

Description

`final class `

`[AStarSearchStrategy](../AStarSearchStrategy.html "class in com.google.adk.planner.goap")`

A* forward search strategy that explores from preconditions toward the goal, activating agents whose inputs are all satisfied.

`final class `

`[DfsSearchStrategy](../DfsSearchStrategy.html "class in com.google.adk.planner.goap")`

Backward-chaining DFS search strategy with parallel grouping.

Constructors in [com.google.adk.planner.goap](../package-summary.html) with parameters of type [SearchStrategy](../SearchStrategy.html "interface in com.google.adk.planner.goap")

Modifier

Constructor

Description

` `

`[GoalOrientedPlanner](../GoalOrientedPlanner.html#%3Cinit%3E\(java.lang.String,java.util.List,com.google.adk.planner.goap.SearchStrategy,com.google.adk.planner.goap.ReplanPolicy\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [SearchStrategy](../SearchStrategy.html "interface in com.google.adk.planner.goap") searchStrategy, [ReplanPolicy](../ReplanPolicy.html "interface in com.google.adk.planner.goap") replanPolicy)`

 




* * *

Copyright (C) 1980\. All rights reserved.
