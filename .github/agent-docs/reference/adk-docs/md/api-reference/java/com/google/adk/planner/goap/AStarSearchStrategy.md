JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/AStarSearchStrategy.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](package-summary.html)
  2. [AStarSearchStrategy](AStarSearchStrategy.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. AStarSearchStrategy()
  5. Method Details
     1. searchGrouped(GoalOrientedSearchGraph, List, Collection, String)

Hide sidebar  Show sidebar

# Class AStarSearchStrategy

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.planner.goap.AStarSearchStrategy

All Implemented Interfaces:
    `[SearchStrategy](SearchStrategy.html "interface in com.google.adk.planner.goap")`

* * *

public final class AStarSearchStrategy extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [SearchStrategy](SearchStrategy.html "interface in com.google.adk.planner.goap")

A* forward search strategy that explores from preconditions toward the goal, activating agents whose inputs are all satisfied. 

Uses a priority queue ordered by f-score (g + h) where: 

  * g = number of agents activated so far (uniform cost) 
  * h = admissible heuristic counting unsatisfied dependencies reachable backward from goal 


After finding the goal, reconstructs the agent path and delegates to `DependencyGraphSearch.assignParallelLevels(ImmutableList, List, Collection, GoalOrientedSearchGraph)` for parallel grouping.

  * ## Constructor Summary

Constructors

Constructor

Description

`AStarSearchStrategy()`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`searchGrouped([GoalOrientedSearchGraph](GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)`

Searches for agent execution groups that produce the goal.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### AStarSearchStrategy

public AStarSearchStrategy()

  * ## Method Details

    * ### searchGrouped

public com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> searchGrouped([GoalOrientedSearchGraph](GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)

Description copied from interface: `[SearchStrategy](SearchStrategy.html#searchGrouped\(com.google.adk.planner.goap.GoalOrientedSearchGraph,java.util.List,java.util.Collection,java.lang.String\))`

Searches for agent execution groups that produce the goal.

Specified by:
    `[searchGrouped](SearchStrategy.html#searchGrouped\(com.google.adk.planner.goap.GoalOrientedSearchGraph,java.util.List,java.util.Collection,java.lang.String\))` in interface `[SearchStrategy](SearchStrategy.html "interface in com.google.adk.planner.goap")`
Parameters:
    `graph` \- the dependency graph
    `metadata` \- agent metadata
    `preconditions` \- state keys already available
    `goal` \- the target output key
Returns:
    ordered list of agent groups for parallel execution




* * *

Copyright (C) 1980\. All rights reserved.
