JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/SearchStrategy.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](package-summary.html)
  2. [SearchStrategy](SearchStrategy.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. searchGrouped(GoalOrientedSearchGraph, List, Collection, String)

Hide sidebar  Show sidebar

# Interface SearchStrategy

All Known Implementing Classes:
    `[AStarSearchStrategy](AStarSearchStrategy.html "class in com.google.adk.planner.goap"), [DfsSearchStrategy](DfsSearchStrategy.html "class in com.google.adk.planner.goap")`

* * *

public interface SearchStrategy

Strategy for searching a dependency graph to find ordered agent execution groups. 

Given a graph, agent metadata, available preconditions, and a goal output key, produces an ordered list of agent groups where agents within each group are independent and can run in parallel.

  * ## Method Summary

All MethodsInstance MethodsAbstract Methods

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`searchGrouped([GoalOrientedSearchGraph](GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)`

Searches for agent execution groups that produce the goal.




  * ## Method Details

    * ### searchGrouped

com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> searchGrouped([GoalOrientedSearchGraph](GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)

Searches for agent execution groups that produce the goal.

Parameters:
    `graph` \- the dependency graph
    `metadata` \- agent metadata
    `preconditions` \- state keys already available
    `goal` \- the target output key
Returns:
    ordered list of agent groups for parallel execution
Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class in java.lang")` \- if the goal cannot be reached




* * *

Copyright (C) 1980\. All rights reserved.
