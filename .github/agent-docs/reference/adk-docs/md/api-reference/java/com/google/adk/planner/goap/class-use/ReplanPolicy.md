JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../../index.html)
  * [Class](../ReplanPolicy.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../../deprecated-list.html)
  * [Index](../../../../../../index-all.html)
  * [Search](../../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](../package-summary.html)
  2. [ReplanPolicy](../ReplanPolicy.html)



# Uses of Interface  
com.google.adk.planner.goap.ReplanPolicy

Packages that use [ReplanPolicy](../ReplanPolicy.html "interface in com.google.adk.planner.goap")

Package

Description

com.google.adk.planner.goap

 

  * ## Uses of [ReplanPolicy](../ReplanPolicy.html "interface in com.google.adk.planner.goap") in [com.google.adk.planner.goap](../package-summary.html)

Classes in [com.google.adk.planner.goap](../package-summary.html) that implement [ReplanPolicy](../ReplanPolicy.html "interface in com.google.adk.planner.goap")

Modifier and Type

Class

Description

`static final record `

`[ReplanPolicy.FailStop](../ReplanPolicy.FailStop.html "class in com.google.adk.planner.goap")`

Stop immediately on failure with an error message.

`static final record `

`[ReplanPolicy.Ignore](../ReplanPolicy.Ignore.html "class in com.google.adk.planner.goap")`

Ignore failures and proceed with the remaining plan as-is.

`static final record `

`[ReplanPolicy.Replan](../ReplanPolicy.Replan.html "class in com.google.adk.planner.goap")`

Attempt to recompute the remaining plan from current world state.

Constructors in [com.google.adk.planner.goap](../package-summary.html) with parameters of type [ReplanPolicy](../ReplanPolicy.html "interface in com.google.adk.planner.goap")

Modifier

Constructor

Description

` `

`[GoalOrientedPlanner](../GoalOrientedPlanner.html#%3Cinit%3E\(java.lang.String,java.util.List,com.google.adk.planner.goap.SearchStrategy,com.google.adk.planner.goap.ReplanPolicy\))([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [SearchStrategy](../SearchStrategy.html "interface in com.google.adk.planner.goap") searchStrategy, [ReplanPolicy](../ReplanPolicy.html "interface in com.google.adk.planner.goap") replanPolicy)`

 




* * *

Copyright (C) 1980\. All rights reserved.
