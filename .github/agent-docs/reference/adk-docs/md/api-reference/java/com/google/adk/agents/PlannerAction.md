JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * Class
  * [Use](class-use/PlannerAction.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.agents](package-summary.html)
  2. [PlannerAction](PlannerAction.html)



Contents  

  1. Description
  2. Nested Class Summary

Hide sidebar  Show sidebar

# Interface PlannerAction

All Known Implementing Classes:
    `[PlannerAction.Done](PlannerAction.Done.html "class in com.google.adk.agents"), [PlannerAction.DoneWithResult](PlannerAction.DoneWithResult.html "class in com.google.adk.agents"), [PlannerAction.NoOp](PlannerAction.NoOp.html "class in com.google.adk.agents"), [PlannerAction.RunAgents](PlannerAction.RunAgents.html "class in com.google.adk.agents")`

* * *

public sealed interface PlannerAction permits [PlannerAction.RunAgents](PlannerAction.RunAgents.html "class in com.google.adk.agents"), [PlannerAction.Done](PlannerAction.Done.html "class in com.google.adk.agents"), [PlannerAction.DoneWithResult](PlannerAction.DoneWithResult.html "class in com.google.adk.agents"), [PlannerAction.NoOp](PlannerAction.NoOp.html "class in com.google.adk.agents")

Represents the next action a [`Planner`](Planner.html "interface in com.google.adk.agents") wants the [`PlannerAgent`](PlannerAgent.html "class in com.google.adk.agents") to take. 

This is a sealed interface with four variants: 

  * [`PlannerAction.RunAgents`](PlannerAction.RunAgents.html "class in com.google.adk.agents") — execute one or more sub-agents (multiple agents run in parallel) 
  * [`PlannerAction.Done`](PlannerAction.Done.html "class in com.google.adk.agents") — planning is complete, no result to emit 
  * [`PlannerAction.DoneWithResult`](PlannerAction.DoneWithResult.html "class in com.google.adk.agents") — planning is complete with a final text result 
  * [`PlannerAction.NoOp`](PlannerAction.NoOp.html "class in com.google.adk.agents") — skip this iteration (no-op), then ask the planner for the next action 


  * ## Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

`static final record `

`[PlannerAction.Done](PlannerAction.Done.html "class in com.google.adk.agents")`

Plan is complete, no result to emit.

`static final record `

`[PlannerAction.DoneWithResult](PlannerAction.DoneWithResult.html "class in com.google.adk.agents")`

Plan is complete with a final text result.

`static final record `

`[PlannerAction.NoOp](PlannerAction.NoOp.html "class in com.google.adk.agents")`

Skip this iteration (no-op).

`static final record `

`[PlannerAction.RunAgents](PlannerAction.RunAgents.html "class in com.google.adk.agents")`

Run the specified sub-agent(s).




* * *

Copyright (C) 1980\. All rights reserved.
