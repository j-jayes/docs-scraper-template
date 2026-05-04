JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/DependencyGraphSearch.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](package-summary.html)
  2. [DependencyGraphSearch](DependencyGraphSearch.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. search(GoalOrientedSearchGraph, Collection, String)
     2. searchGrouped(GoalOrientedSearchGraph, List, Collection, String)

Hide sidebar  Show sidebar

# Class DependencyGraphSearch

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.planner.goap.DependencyGraphSearch

* * *

public final class DependencyGraphSearch extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Performs a topological search on the dependency graph to find the ordered list of agents that must execute to produce a goal output, given a set of initial preconditions (state keys already available). 

The search works backward from the goal: for each unsatisfied dependency, it finds the agent that produces it and recursively resolves that agent's dependencies. Uses recursive DFS to ensure correct topological ordering.

  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

`search([GoalOrientedSearchGraph](GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)`

Finds the ordered list of agent names that must execute to produce the goal.

`static com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

`searchGrouped([GoalOrientedSearchGraph](GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)`

Groups agents into parallelizable execution levels.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### search

public static com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> search([GoalOrientedSearchGraph](GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)

Finds the ordered list of agent names that must execute to produce the goal.

Parameters:
    `graph` \- the dependency graph built from agent metadata
    `preconditions` \- state keys already available (no agent needed to produce them)
    `goal` \- the target output key to produce
Returns:
    ordered list of agent names, from first to execute to last
Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class in java.lang")` \- if a dependency cannot be resolved or a cycle is detected

    * ### searchGrouped

public static com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>> searchGrouped([GoalOrientedSearchGraph](GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)

Groups agents into parallelizable execution levels. 

Each group contains agents whose dependencies are all satisfied by agents in earlier groups or by initial preconditions. Agents within the same group are independent and can run in parallel.

Parameters:
    `graph` \- the dependency graph
    `metadata` \- agent metadata used to compute dependency levels
    `preconditions` \- state keys already available
    `goal` \- the target output key
Returns:
    ordered list of agent groups; agents within each group can run in parallel
Throws:
    `[IllegalStateException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalStateException.html "class in java.lang")` \- if a dependency cannot be resolved or a cycle is detected




* * *

Copyright (C) 1980\. All rights reserved.
