JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../GoalOrientedSearchGraph.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](../package-summary.html)
  2. [GoalOrientedSearchGraph](../GoalOrientedSearchGraph.html)



# Uses of Class  
com.google.adk.planner.goap.GoalOrientedSearchGraph

Packages that use [GoalOrientedSearchGraph](../GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap")

Package

Description

com.google.adk.planner.goap

 

  * ## Uses of [GoalOrientedSearchGraph](../GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") in [com.google.adk.planner.goap](../package-summary.html)

Methods in [com.google.adk.planner.goap](../package-summary.html) with parameters of type [GoalOrientedSearchGraph](../GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap")

Modifier and Type

Method

Description

`static com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>`

DependencyGraphSearch.`[search](../DependencyGraphSearch.html#search\(com.google.adk.planner.goap.GoalOrientedSearchGraph,java.util.Collection,java.lang.String\))([GoalOrientedSearchGraph](../GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)`

Finds the ordered list of agent names that must execute to produce the goal.

`com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

AStarSearchStrategy.`[searchGrouped](../AStarSearchStrategy.html#searchGrouped\(com.google.adk.planner.goap.GoalOrientedSearchGraph,java.util.List,java.util.Collection,java.lang.String\))([GoalOrientedSearchGraph](../GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)`

 

`static com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

DependencyGraphSearch.`[searchGrouped](../DependencyGraphSearch.html#searchGrouped\(com.google.adk.planner.goap.GoalOrientedSearchGraph,java.util.List,java.util.Collection,java.lang.String\))([GoalOrientedSearchGraph](../GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)`

Groups agents into parallelizable execution levels.

`com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

DfsSearchStrategy.`[searchGrouped](../DfsSearchStrategy.html#searchGrouped\(com.google.adk.planner.goap.GoalOrientedSearchGraph,java.util.List,java.util.Collection,java.lang.String\))([GoalOrientedSearchGraph](../GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)`

 

`com.google.common.collect.ImmutableList<com.google.common.collect.ImmutableList<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")>>`

SearchStrategy.`[searchGrouped](../SearchStrategy.html#searchGrouped\(com.google.adk.planner.goap.GoalOrientedSearchGraph,java.util.List,java.util.Collection,java.lang.String\))([GoalOrientedSearchGraph](../GoalOrientedSearchGraph.html "class in com.google.adk.planner.goap") graph, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [Collection](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Collection.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")> preconditions, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal)`

Searches for agent execution groups that produce the goal.




* * *

Copyright (C) 1980\. All rights reserved.
