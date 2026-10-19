JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../BaseNode.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](../package-summary.html)
  2. [BaseNode](../BaseNode.html)



# Uses of Class  
com.google.adk.workflow.BaseNode

Packages that use [BaseNode](../BaseNode.html "class in com.google.adk.workflow")

Package

Description

com.google.adk.a2a.agent

 

com.google.adk.agents

 

com.google.adk.workflow

 

  * ## Uses of [BaseNode](../BaseNode.html "class in com.google.adk.workflow") in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html)

Subclasses of [BaseNode](../BaseNode.html "class in com.google.adk.workflow") in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html)

Modifier and Type

Class

Description

`class `

`[RemoteA2AAgent](../../a2a/agent/RemoteA2AAgent.html "class in com.google.adk.a2a.agent")`

Agent that communicates with a remote A2A agent via an A2A client.

  * ## Uses of [BaseNode](../BaseNode.html "class in com.google.adk.workflow") in [com.google.adk.agents](../../agents/package-summary.html)

Subclasses of [BaseNode](../BaseNode.html "class in com.google.adk.workflow") in [com.google.adk.agents](../../agents/package-summary.html)

Modifier and Type

Class

Description

`class `

`[BaseAgent](../../agents/BaseAgent.html "class in com.google.adk.agents")`

Base class for all agents.

`class `

`[LlmAgent](../../agents/LlmAgent.html "class in com.google.adk.agents")`

The LLM-based agent.

`class `

`[LoopAgent](../../agents/LoopAgent.html "class in com.google.adk.agents")`

An agent that runs its sub-agents sequentially in a loop.

`class `

`[ParallelAgent](../../agents/ParallelAgent.html "class in com.google.adk.agents")`

A shell agent that runs its sub-agents in parallel in isolated manner.

`class `

`[PlannerAgent](../../agents/PlannerAgent.html "class in com.google.adk.agents")`

An agent that delegates execution planning to a [`Planner`](../../agents/Planner.html "interface in com.google.adk.agents") strategy.

`class `

`[SequentialAgent](../../agents/SequentialAgent.html "class in com.google.adk.agents")`

An agent that runs its sub-agents sequentially.

  * ## Uses of [BaseNode](../BaseNode.html "class in com.google.adk.workflow") in [com.google.adk.workflow](../package-summary.html)

Subclasses of [BaseNode](../BaseNode.html "class in com.google.adk.workflow") in [com.google.adk.workflow](../package-summary.html)

Modifier and Type

Class

Description

`final class `

`[JoinNode](../JoinNode.html "class in com.google.adk.workflow")`

A node that waits for every predecessor to complete, then outputs their outputs keyed by predecessor name.

`final class `

`[Workflow](../Workflow.html "class in com.google.adk.workflow")`

A graph of nodes that is itself a node, so a workflow can go wherever a node can, including in another workflow.




* * *

Copyright (C) 1980\. All rights reserved.
