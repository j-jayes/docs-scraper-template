JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * [Class](../Node.html)
  * Use
  * [Tree](../package-tree.html)
  * [Deprecated](../../../../../deprecated-list.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](../package-summary.html)
  2. [Node](../Node.html)



# Uses of Interface  
com.google.adk.workflow.Node

Packages that use [Node](../Node.html "interface in com.google.adk.workflow")

Package

Description

com.google.adk.a2a.agent

 

com.google.adk.agents

 

com.google.adk.workflow

 

  * ## Uses of [Node](../Node.html "interface in com.google.adk.workflow") in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html)

Classes in [com.google.adk.a2a.agent](../../a2a/agent/package-summary.html) that implement [Node](../Node.html "interface in com.google.adk.workflow")

Modifier and Type

Class

Description

`class `

`[RemoteA2AAgent](../../a2a/agent/RemoteA2AAgent.html "class in com.google.adk.a2a.agent")`

Agent that communicates with a remote A2A agent via an A2A client.

  * ## Uses of [Node](../Node.html "interface in com.google.adk.workflow") in [com.google.adk.agents](../../agents/package-summary.html)

Classes in [com.google.adk.agents](../../agents/package-summary.html) that implement [Node](../Node.html "interface in com.google.adk.workflow")

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

  * ## Uses of [Node](../Node.html "interface in com.google.adk.workflow") in [com.google.adk.workflow](../package-summary.html)

Classes in [com.google.adk.workflow](../package-summary.html) that implement [Node](../Node.html "interface in com.google.adk.workflow")

Modifier and Type

Class

Description

`class `

`[BaseNode](../BaseNode.html "class in com.google.adk.workflow")`

Base class for nodes in a workflow graph.

`final class `

`[JoinNode](../JoinNode.html "class in com.google.adk.workflow")`

A node that waits for every predecessor to complete, then outputs their outputs keyed by predecessor name.

`final class `

`[Start](../Start.html "class in com.google.adk.workflow")`

The node that marks where a workflow graph starts.

`final class `

`[Workflow](../Workflow.html "class in com.google.adk.workflow")`

A graph of nodes that is itself a node, so a workflow can go wherever a node can, including in another workflow.

Methods in [com.google.adk.workflow](../package-summary.html) that return [Node](../Node.html "interface in com.google.adk.workflow")

Modifier and Type

Method

Description

`[Node](../Node.html "interface in com.google.adk.workflow")`

Edge.`[from](../Edge.html#from\(\))()`

Returns the value of the [`from`](../../../../../com/google/adk/workflow/Edge.html#param-from) record component.

`[Node](../Node.html "interface in com.google.adk.workflow")`

Edge.`[to](../Edge.html#to\(\))()`

Returns the value of the [`to`](../../../../../com/google/adk/workflow/Edge.html#param-to) record component.

Constructors in [com.google.adk.workflow](../package-summary.html) with parameters of type [Node](../Node.html "interface in com.google.adk.workflow")

Modifier

Constructor

Description

` `

`[Edge](../Edge.html#%3Cinit%3E\(com.google.adk.workflow.Node,com.google.adk.workflow.Node\))([Node](../Node.html "interface in com.google.adk.workflow") from, [Node](../Node.html "interface in com.google.adk.workflow") to)`

Creates an unconditional edge.

` `

`[Edge](../Edge.html#%3Cinit%3E\(com.google.adk.workflow.Node,com.google.adk.workflow.Node,com.google.adk.workflow.Route\))([Node](../Node.html "interface in com.google.adk.workflow") from, [Node](../Node.html "interface in com.google.adk.workflow") to, [Route](../Route.html "interface in com.google.adk.workflow") route)`

Creates an edge selected by a single route.

` `

`[Edge](../Edge.html#%3Cinit%3E\(com.google.adk.workflow.Node,com.google.adk.workflow.Node,com.google.common.collect.ImmutableList\))([Node](../Node.html "interface in com.google.adk.workflow") from, [Node](../Node.html "interface in com.google.adk.workflow") to, com.google.common.collect.ImmutableList<[Route](../Route.html "interface in com.google.adk.workflow")> routes)`

Creates an instance of a `Edge` record class.




* * *

Copyright (C) 1980\. All rights reserved.
