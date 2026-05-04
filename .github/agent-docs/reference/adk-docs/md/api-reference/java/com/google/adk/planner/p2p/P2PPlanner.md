JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/P2PPlanner.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.planner.p2p](package-summary.html)
  2. [P2PPlanner](P2PPlanner.html)



Contents  

  1. Description
  2. Constructor Summary
  3. Method Summary
  4. Constructor Details
     1. P2PPlanner(List, int, BiPredicate)
     2. P2PPlanner(List, int)
  5. Method Details
     1. init(PlanningContext)
     2. firstAction(PlanningContext)
     3. nextAction(PlanningContext)

Hide sidebar  Show sidebar

# Class P2PPlanner

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.google.adk.planner.p2p.P2PPlanner

All Implemented Interfaces:
    `[Planner](../../agents/Planner.html "interface in com.google.adk.agents")`

* * *

public final class P2PPlanner extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang") implements [Planner](../../agents/Planner.html "interface in com.google.adk.agents")

A peer-to-peer planner where agents activate dynamically as their input dependencies become available in session state. 

Key behaviors: 

  * Multiple agents can activate in parallel when their inputs are satisfied 
  * When an agent produces output, other agents whose inputs are now satisfied activate 
  * Agents can re-execute when their inputs change (iterative refinement) 
  * Terminates on maxInvocations or a custom exit condition 


Example: Research collaboration where a critic's feedback causes hypothesis refinement: 
    
    
      LiteratureAgent (needs: topic) → researchFindings
      HypothesisAgent (needs: topic, researchFindings) → hypothesis
      CriticAgent (needs: topic, hypothesis) → critique
      ScorerAgent (needs: topic, hypothesis, critique) → score
      Exit when: score >= 0.85
    

  * ## Constructor Summary

Constructors

Constructor

Description

`P2PPlanner([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../goap/AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, int maxInvocations)`

Creates a P2P planner that exits only on maxInvocations.

`P2PPlanner([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../goap/AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, int maxInvocations, [BiPredicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html "interface in java.util.function")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>, [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> exitCondition)`

Creates a P2P planner with a custom exit condition.

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

    * ### P2PPlanner

public P2PPlanner([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../goap/AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, int maxInvocations, [BiPredicate](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/function/BiPredicate.html "interface in java.util.function")<[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")>, [Integer](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Integer.html "class in java.lang")> exitCondition)

Creates a P2P planner with a custom exit condition.

Parameters:
    `metadata` \- agent input/output declarations
    `maxInvocations` \- maximum total agent invocations before termination
    `exitCondition` \- predicate tested on (state, invocationCount); returns true to stop

    * ### P2PPlanner

public P2PPlanner([List](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html "interface in java.util")<[AgentMetadata](../goap/AgentMetadata.html "class in com.google.adk.planner.goap")> metadata, int maxInvocations)

Creates a P2P planner that exits only on maxInvocations.

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
