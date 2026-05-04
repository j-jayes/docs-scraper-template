JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../AgentMetadata.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](../package-summary.html)
  2. [AgentMetadata](../AgentMetadata.html)



# Uses of Record Class  
com.google.adk.planner.goap.AgentMetadata

Packages that use [AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")

Package

Description

com.google.adk.planner.goap

 

com.google.adk.planner.p2p

 

  * ## Uses of [AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap") in [com.google.adk.planner.goap](../package-summary.html)

Method parameters in [com.google.adk.planner.goap](../package-summary.html) with type arguments of type [AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")

Modifier and Type

Method

Description

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

Constructor parameters in [com.google.adk.planner.goap](../package-summary.html) with type arguments of type [AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")

Modifier

Constructor

Description

` `

`[GoalOrientedPlanner](../GoalOrientedPlanner.html#%3Cinit%3E\(java.lang.String,java.util.List\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata)`

 

` `

`[GoalOrientedPlanner](../GoalOrientedPlanner.html#%3Cinit%3E\(java.lang.String,java.util.List,boolean\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, boolean validateOutputs)`

 

` `

`[GoalOrientedPlanner](../GoalOrientedPlanner.html#%3Cinit%3E\(java.lang.String,java.util.List,com.google.adk.planner.goap.SearchStrategy,com.google.adk.planner.goap.ReplanPolicy\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [SearchStrategy](../SearchStrategy.html "interface in com.google.adk.planner.goap") searchStrategy, [ReplanPolicy](../ReplanPolicy.html "interface in com.google.adk.planner.goap") replanPolicy)`

 

` `

`[GoalOrientedSearchGraph](../GoalOrientedSearchGraph.html#%3Cinit%3E\(java.util.List\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata)`

 

  * ## Uses of [AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap") in [com.google.adk.planner.p2p](../../p2p/package-summary.html)

Constructor parameters in [com.google.adk.planner.p2p](../../p2p/package-summary.html) with type arguments of type [AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")

Modifier

Constructor

Description

` `

`[P2PPlanner](../../p2p/P2PPlanner.html#%3Cinit%3E\(java.util.List,int\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, int maxInvocations)`

Creates a P2P planner that exits only on maxInvocations.

` `

`[P2PPlanner](../../p2p/P2PPlanner.html#%3Cinit%3E\(java.util.List,int,java.util.function.BiPredicate\))([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, int maxInvocations, [BiPredicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html "interface in java.util.function")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>, [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> exitCondition)`

Creates a P2P planner with a custom exit condition.




* * *

Copyright (C) 1980\. All rights reserved.
