JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../index.html)
  * [Package](package-summary.html)
  * Use
  * [Tree](package-tree.html)
  * [Deprecated](../../../../deprecated-list.html)
  * [Index](../../../../index-all.html)
  * [Search](../../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.google.adk.workflow](package-summary.html)



# Uses of Package  
com.google.adk.workflow

Packages that use [com.google.adk.workflow](package-summary.html)

Package

Description

com.google.adk.a2a.agent

 

com.google.adk.agents

 

com.google.adk.events

 

com.google.adk.workflow

 

  * Classes in [com.google.adk.workflow](package-summary.html) used by [com.google.adk.a2a.agent](../a2a/agent/package-summary.html)

Class

Description

[BaseNode](class-use/BaseNode.html#com.google.adk.a2a.agent)

Base class for nodes in a workflow graph.

[Node](class-use/Node.html#com.google.adk.a2a.agent)

A unit of work in a workflow graph.

  * Classes in [com.google.adk.workflow](package-summary.html) used by [com.google.adk.agents](../agents/package-summary.html)

Class

Description

[BaseNode](class-use/BaseNode.html#com.google.adk.agents)

Base class for nodes in a workflow graph.

[Node](class-use/Node.html#com.google.adk.agents)

A unit of work in a workflow graph.

  * Classes in [com.google.adk.workflow](package-summary.html) used by [com.google.adk.events](../events/package-summary.html)

Class

Description

[NodeInfo](class-use/NodeInfo.html#com.google.adk.events)

The identity of the workflow-node activation that emitted an [`Event`](../events/Event.html "class in com.google.adk.events").

[Route](class-use/Route.html#com.google.adk.events)

A value on a workflow edge, and the value a node emits to select which of its outgoing edges are followed.

  * Classes in [com.google.adk.workflow](package-summary.html) used by [com.google.adk.workflow](package-summary.html)

Class

Description

[BaseNode](class-use/BaseNode.html#com.google.adk.workflow)

Base class for nodes in a workflow graph.

[Edge](class-use/Edge.html#com.google.adk.workflow)

A connection between two nodes in a workflow graph.

[JoinNode](class-use/JoinNode.html#com.google.adk.workflow)

A node that waits for every predecessor to complete, then outputs their outputs keyed by predecessor name.

[JoinNode.Builder](class-use/JoinNode.Builder.html#com.google.adk.workflow)

Builder for [`JoinNode`](JoinNode.html "class in com.google.adk.workflow").

[Node](class-use/Node.html#com.google.adk.workflow)

A unit of work in a workflow graph.

[NodeConfig](class-use/NodeConfig.html#com.google.adk.workflow)

A node's retry policy and execution timeout.

[NodeConfig.Builder](class-use/NodeConfig.Builder.html#com.google.adk.workflow)

Builder for [`NodeConfig`](NodeConfig.html "class in com.google.adk.workflow").

[NodeInfo](class-use/NodeInfo.html#com.google.adk.workflow)

The identity of the workflow-node activation that emitted an [`Event`](../events/Event.html "class in com.google.adk.events").

[NodeInfo.Builder](class-use/NodeInfo.Builder.html#com.google.adk.workflow)

Builder for [`NodeInfo`](NodeInfo.html "class in com.google.adk.workflow").

[RetryConfig](class-use/RetryConfig.html#com.google.adk.workflow)

How a node is retried when it fails.

[RetryConfig.Builder](class-use/RetryConfig.Builder.html#com.google.adk.workflow)

Builder for [`RetryConfig`](RetryConfig.html "class in com.google.adk.workflow").

[Route](class-use/Route.html#com.google.adk.workflow)

A value on a workflow edge, and the value a node emits to select which of its outgoing edges are followed.

[Route.Default](class-use/Route.Default.html#com.google.adk.workflow)

The fallback edge, followed when no other routed edge of the node matches what it emitted, including when it emitted no route.

[Start](class-use/Start.html#com.google.adk.workflow)

The node that marks where a workflow graph starts.

[Workflow](class-use/Workflow.html#com.google.adk.workflow)

A graph of nodes that is itself a node, so a workflow can go wherever a node can, including in another workflow.

[Workflow.Builder](class-use/Workflow.Builder.html#com.google.adk.workflow)

Builder for [`Workflow`](Workflow.html "class in com.google.adk.workflow").




* * *

Copyright (C) 1980\. All rights reserved.
