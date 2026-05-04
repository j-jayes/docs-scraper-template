JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/GoalOrientedPlanner.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.goap](package-summary.html)
  2. [GoalOrientedPlanner](GoalOrientedPlanner.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. GoalOrientedPlanner(String, List)
     2. GoalOrientedPlanner(String, List, boolean)
     3. GoalOrientedPlanner(String, List, SearchStrategy, ReplanPolicy)
  5. Method Details
     1. init(PlanningContext)
     2. firstAction(PlanningContext)
     3. nextAction(PlanningContext)

Hide sidebar  Show sidebar

# Class GoalOrientedPlanner

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.planner.goap.GoalOrientedPlanner

All Implemented Interfaces:
    `[Planner](../../agents/Planner.html "interface in com.google.adk.agents")`

* * *

public final class GoalOrientedPlanner extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [Planner](../../agents/Planner.html "interface in com.google.adk.agents")

A planner that resolves agent execution order based on input/output dependencies and a target goal (output key). 

Given agent metadata declaring what each agent reads (inputKeys) and writes (outputKey), this planner uses backward-chaining dependency resolution to compute the execution path from initial preconditions to the goal. 

Example: 
    
    
      Agent A: inputs=[], output="person"
      Agent B: inputs=[], output="sign"
      Agent C: inputs=["person", "sign"], output="horoscope"
      Agent D: inputs=["person", "horoscope"], output="writeup"
      Goal: "writeup"
    
      Resolved groups: [A, B] → [C] → [D]
      (A and B are independent and run in parallel)
    

Supports configurable failure handling via [`ReplanPolicy`](ReplanPolicy.html "interface in com.google.adk.planner.goap"): 

  * [`ReplanPolicy.Ignore`](ReplanPolicy.Ignore.html "class in com.google.adk.planner.goap") — proceed regardless of missing outputs (default) 
  * [`ReplanPolicy.FailStop`](ReplanPolicy.FailStop.html "class in com.google.adk.planner.goap") — halt on first missing output 
  * [`ReplanPolicy.Replan`](ReplanPolicy.Replan.html "class in com.google.adk.planner.goap") — recompute the remaining plan from current world state 


Supports pluggable search strategies via [`SearchStrategy`](SearchStrategy.html "interface in com.google.adk.planner.goap"): backward-chaining DFS ([`DfsSearchStrategy`](DfsSearchStrategy.html "class in com.google.adk.planner.goap")) or forward A* ([`AStarSearchStrategy`](AStarSearchStrategy.html "class in com.google.adk.planner.goap")).

  * ## Constructor Summary

Constructors

Constructor

Description

`GoalOrientedPlanner([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata)`

 

`GoalOrientedPlanner([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, boolean validateOutputs)`

 

`GoalOrientedPlanner([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [SearchStrategy](SearchStrategy.html "interface in com.google.adk.planner.goap") searchStrategy, [ReplanPolicy](ReplanPolicy.html "interface in com.google.adk.planner.goap") replanPolicy)`

 

  * ## Method Summary

All MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`io.reactivex.rxjava3.core.Single<[PlannerAction](../../agents/PlannerAction.html "interface in com.google.adk.agents")>`

`firstAction([PlanningContext](../../agents/PlanningContext.html "class in com.google.adk.agents") context)`

Select the first action to execute.

`void`

`init([PlanningContext](../../agents/PlanningContext.html "class in com.google.adk.agents") context)`

Initialize the planner with context and available agents.

`io.reactivex.rxjava3.core.Single<[PlannerAction](../../agents/PlannerAction.html "interface in com.google.adk.agents")>`

`nextAction([PlanningContext](../../agents/PlanningContext.html "class in com.google.adk.agents") context)`

Select the next action based on updated state and events.

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Constructor Details

    * ### GoalOrientedPlanner

public GoalOrientedPlanner([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata)

    * ### GoalOrientedPlanner

public GoalOrientedPlanner([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, boolean validateOutputs)

    * ### GoalOrientedPlanner

public GoalOrientedPlanner([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") goal, [List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, [SearchStrategy](SearchStrategy.html "interface in com.google.adk.planner.goap") searchStrategy, [ReplanPolicy](ReplanPolicy.html "interface in com.google.adk.planner.goap") replanPolicy)

  * ## Method Details

    * ### init

public void init([PlanningContext](../../agents/PlanningContext.html "class in com.google.adk.agents") context)

Description copied from interface: `[Planner](../../agents/Planner.html#init\(com.google.adk.agents.PlanningContext\))`

Initialize the planner with context and available agents. Called once before the planning loop starts. 

Default implementation is a no-op. Override to perform setup like building dependency graphs.

Specified by:
    `[init](../../agents/Planner.html#init\(com.google.adk.agents.PlanningContext\))` in interface `[Planner](../../agents/Planner.html "interface in com.google.adk.agents")`

    * ### firstAction

public io.reactivex.rxjava3.core.Single<[PlannerAction](../../agents/PlannerAction.html "interface in com.google.adk.agents")> firstAction([PlanningContext](../../agents/PlanningContext.html "class in com.google.adk.agents") context)

Description copied from interface: `[Planner](../../agents/Planner.html#firstAction\(com.google.adk.agents.PlanningContext\))`

Select the first action to execute.

Specified by:
    `[firstAction](../../agents/Planner.html#firstAction\(com.google.adk.agents.PlanningContext\))` in interface `[Planner](../../agents/Planner.html "interface in com.google.adk.agents")`

    * ### nextAction

public io.reactivex.rxjava3.core.Single<[PlannerAction](../../agents/PlannerAction.html "interface in com.google.adk.agents")> nextAction([PlanningContext](../../agents/PlanningContext.html "class in com.google.adk.agents") context)

Description copied from interface: `[Planner](../../agents/Planner.html#nextAction\(com.google.adk.agents.PlanningContext\))`

Select the next action based on updated state and events.

Specified by:
    `[nextAction](../../agents/Planner.html#nextAction\(com.google.adk.agents.PlanningContext\))` in interface `[Planner](../../agents/Planner.html "interface in com.google.adk.agents")`




* * *

Copyright (C) 1980\. All rights reserved.
